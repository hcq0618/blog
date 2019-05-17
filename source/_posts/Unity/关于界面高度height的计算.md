---
title: 关于界面高度height的计算
thumbnail: http://upload-images.jianshu.io/upload_images/17266280-a61dd914895a4b69.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240
categories: Unity
tags: [Unity]
---

首先看一个例子，新建一个Panel，在下面添加两个Button，分别命名为Button、Button2。

1、给Panel添加一个VerticalLayoutGroup组件，ChildForceExpand属性中勾上Width。

2、给Button、Button2添加LayoutElement组件，其中Button的FlexibleHeight设置为0.3，Button2的FlexibleHeight设置为0.1

3、将Panel的高度设置为100

  

![](http://upload-images.jianshu.io/upload_images/17266280-a61dd914895a4b69.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

  

![](http://upload-images.jianshu.io/upload_images/17266280-c74d44cba15dfecb.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

这时我们发现，Button的高度是70，Button2的高度是30。奇怪，这个高度是怎么算出来的呢？

网上搜索一番，竟然很少有人讨论uGUI的AutoLayout，尤其是flexibleWidth/Height属性的意义，官方文档也语焉不详。这时只能放大招了，uGUI已经开源，索性把代码拉下来看看到底怎么实现的。下面是托管代码的地址：

<https://bitbucket.org/Unity-Technologies/ui>

uGUI的AutoLayout有三个核心接口，定义在ILayoutElement.cs文件中：

ILayoutElement

ILayoutController

ILayoutIgnorer

结构很清晰，由ILayoutElement提供布局信息，ILayoutController来控制布局，ILayoutIgnore提供给UI忽略AutoLayout的能力。

例子中使用的VerticalLayoutGroup继承自HorizontalOrVerticalLayoutGroup，这个类实现了布局的核心逻辑，代码量不多，我就直接贴上来了


其中SetChildrenAlongAxis方法清晰地阐释了minHeight,preferredHeight,flexibleHeight的涵义。

为了帮助理解，我们先定义几个概念。我们把当前UI所有同级并参与自动布局的组件的preferredHeight总和称为totalPreferredHeight，minHeight的总和称为totalMinHeight，父UI的真实高度称为realHeight。总结如下：

1、 **minHeight**

在自动布局中，此UI最小高度不会小于minHeight。这个参数定义了realHeight <
totalMinHeight时，当前子UI的height为minHeight。

2、 **preferredHeight**

可以理解为，UI自身希望的高度。

当totalMinHeight < realHeight <
totalPreferredHeight时，realHeight处于totalMinHeight和totalPreferredHeight之间一定百分比，把这个比例应用到每一个接受自动布局的子UI上，即是我们最终得到的效果

![](http://upload-images.jianshu.io/upload_images/17266280-1240ece0245c46cd.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

3、 **flexibleHeight**

当realHeight >
totalPreferredHeight时，父UI会剩下一部分高度。flexibleHeight就是告诉AutoLayout系统，应该怎么瓜分剩下的高度，使子UI填充满父UI。flexibleHeight默认是-1，不会进行扩充。当flexibleHeight
> 0时，flexibleHeight值作为权重来计算当前子UI最终的高度，公式如下：

height = preferredHeight + (flexibleHeight / totalFlexibleHeight) *
(realHeight - totalPreferredHeight)

![](http://upload-images.jianshu.io/upload_images/17266280-7dd199a2b1bbe3d0.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

flexibleHeight示意图

弄清楚这些概念后，我们再看一下文章开头的例子。

button1的flexibleHeight=0.3，button2的flexibleHeight=0.1，minHeight和preferredHeight都没有设置，按道理高度应该分别是75、25。为什么会出现70、30？

查一下ILayoutElement的实现类

![](http://upload-images.jianshu.io/upload_images/17266280-4d6556ae3f039540.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

ILayoutElement实现类

发现Image和Text实现了ILayoutElement，而我们的按钮中默认是有一个Image组件的，用脚本获取这个Image然后打印它的preferredHeight，发现等于10

再套用flexibleHeight的计算公式：

这里有个问题，一个GameObject上挂载两个ILayoutElement组件，是怎么决定用哪个的？这个可以在LayoutUtility.cs中找到答案：


原来LayoutElement有一个layoutPriority属性用来决定优先级，这个属性暂时还没有在编辑器中暴露，也许后续版本会加强这方面的能力。

AutoLayout系统会选用优先级最高的ILayoutElement里相应属性返回。Image和Text的优先级默认是0，LayoutElement默认优先级是1。所以正常情况会使用LayoutElement中的设置，但我们的例子中，LayoutElement没有设置preferredHeight，LayoutElement里布局相关的初始值都是-1，所以还是使用了Image的preferredHeight:10。

【结语】

其实，只要官方文档描述详细一些，根本没必要浪费时间去查这个来龙去脉。这几天在学习[Swift](http://lib.csdn.net/base/1)，苹果人性化的Programming
Guide加上iBooks的配合，使得学习这门语言真是件轻松愉快的事情。相比之下，Unity简直是在虐待开发者。Unity、Unreal、Cryengine等最近也为争市场弄得头破血流，除了降价开源提供新特性之外，完善文档也是不容忽视的工作，毕竟开发者才是这些厂商真正的衣食父母。

