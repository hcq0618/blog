---
title: Strumpy-Shader-Editor入门教程
thumbnail: http://upload-images.jianshu.io/upload_images/17266280-a68abfd8e88342bb.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240
categories: Unity插件
tags: [Unity插件]
---

对于3D游戏来说，有很多绚丽的效果，都是靠shader（着色器）来实现的。不过很多朋友估计都不会编写shader，阿赵我自己也只是看了个入门，明白了它的原理，很多具体的效果都写不出来的。这次来介绍一个Unity3D的第三方shader编辑器：Strumpy。这个编辑器是完全可视化编辑，使用起来相对简单一点。

先来看看我们这次需要做的例子：

  

![](http://upload-images.jianshu.io/upload_images/17266280-a68abfd8e88342bb.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

我们需要使用Strumpy，编辑出这样一个shader：包括了漫反射通道、法线通道、高光通道，以及在模型的边缘运动的光效。

很显然，Unity3D自带的shader没有能直接实现这样的功能的，最多也只能使用法线和高光通道而已。

      由于这个例子稍微复杂，所以我们先来做一个更简单的例子，来熟悉一下strumpy的界面和基本操作。

首先肯定是要先下载Strumpy插件了。在Asset Store里面有，免费下载的。我这里使用的是4.0a版本。

下载完之后导入，会看到多了一个选项：

  

![](http://upload-images.jianshu.io/upload_images/17266280-b0ca2dd525a05043.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

选择之后打开了Strumpy的编辑窗口：

  

![](http://upload-images.jianshu.io/upload_images/17266280-5a08cfb866179d29.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

  

![](http://upload-images.jianshu.io/upload_images/17266280-98dfba326ba5eeb4.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

Flie的功能很直观，新建，读取，保存和导出的功能，我们可以先看看读取功能

  

![](http://upload-images.jianshu.io/upload_images/17266280-ff237f8eeba1a64a.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

插件自带了一些已经编辑好的范例，有兴趣的朋友可以逐个看看，会有很大的收益。

  

![](http://upload-images.jianshu.io/upload_images/17266280-c5c3f36c56204c65.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

然后我们来正式开始做这个简单的例子，我们准备了一张带有透明通道的贴图（拿斩首大刀的阿赵），接下来我们做一个shader，把这张贴图显示在一个面片上面，使它实现漫反射通道和透明通道的显示。

我们新建一个着色器编辑：

  

![](http://upload-images.jianshu.io/upload_images/17266280-6f7b5bdc47c1234c.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

 注意看，新建时，在Settings的标签是红色的，然后Shader
Name也是红色的，这是提醒我们，每一个shader必须要先有一个名称，而这个名称就是以后你在材质栏里面选择的材质名称了。比如你可以用“myshader/test”，这样test材质会出现在myshader下面。

输入材质名词之后，我们先来Inputs里面，新建一个输入。这个输入，就是我们平常在Unity自带的材质球里面看到的输入通道了。假如我们需要它能调节颜色，那么就要新建一个颜色的输入，假如需要调用贴图，就要新建一个贴图的输入。这里我们新建一个Unity预设的MainTexture。熟悉用脚本替换材质贴图的朋友估计很熟悉这个标签的含义了。

  

![](http://upload-images.jianshu.io/upload_images/17266280-11496dbb1c0dc1e3.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

  

![](http://upload-images.jianshu.io/upload_images/17266280-af76026aea9c1182.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

新建之后，我们可以看到，出现了一个贴图选择的通道，就像我们平常操作的自带材质球一样。

接下来我们会新建一些节点，然后对他们进行编辑。

创建节点的方式有两种：

第一种是在Nodes里面选择相应的节点：

  

![](http://upload-images.jianshu.io/upload_images/17266280-41356f3dbb427707.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

第二种是在节点编辑的窗口鼠标右键单击，选择相应的节点。

  

![](http://upload-images.jianshu.io/upload_images/17266280-7288f066e2956ae8.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

我个人比较习惯第二种方法。

我们选择了一个Sampler2D的输入

  

![](http://upload-images.jianshu.io/upload_images/17266280-a65e9ac8bedd33f6.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

刚生成的时候，这个节点是红色的，因为我们没有指定输入的来源。想起刚才我们新建的Input了吧？那个MainTexture指定在这里。

  

![](http://upload-images.jianshu.io/upload_images/17266280-d0d29147dc6b8496.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

在选中该节点的情况下，来到Node的标签，会看到提示错误了

  

![](http://upload-images.jianshu.io/upload_images/17266280-297c148f7408a062.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

我们选择_MainTex

  

![](http://upload-images.jianshu.io/upload_images/17266280-09168c299b5ea973.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

这时候，节点就不再是红色了，而是出现了两项输出，分别是2D采样和UV信息。节点名称里面，也会相应的显示出_MainTex，也就是我们刚才新建的Input的名称。

  

![](http://upload-images.jianshu.io/upload_images/17266280-a2eea10fcb7cc15a.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

接下来我们新建一个Tex2D方法节点。

  

![](http://upload-images.jianshu.io/upload_images/17266280-5890bc05786aea9f.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

然后像上图一样，用鼠标把他们之间连起来。

这时候，把我们预先准备好的贴图指定在贴图通道里面

  

![](http://upload-images.jianshu.io/upload_images/17266280-3112708d85300c07.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

  

![](http://upload-images.jianshu.io/upload_images/17266280-320be879b54686fd.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

点击预览窗口的Update Preview，会看到预览的物体上面出现了我们的贴图

  

![](http://upload-images.jianshu.io/upload_images/17266280-2c1679eaf2d4f416.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

为了便于观察，我们选择一个片面模型。这时候，漫反射通道已经完成了，接下来我们继续做透明通道。

  

![](http://upload-images.jianshu.io/upload_images/17266280-a0b91d3b6f1db10b.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

如上图一样，把A连接到Alpha通道。

  

![](http://upload-images.jianshu.io/upload_images/17266280-d9bb45c23495d433.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

然后来到Settings，按上图设置一下。

  

![](http://upload-images.jianshu.io/upload_images/17266280-7bc2218d713e7c8b.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

打开背景显示，会看到透明通道已经生效了。

在完成了以上的小例子之后，我们正式来解释一下Strumpy各个部分的意思吧。

  

![](http://upload-images.jianshu.io/upload_images/17266280-6bce62b455c5c4c7.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

在master里面，分别是各个通道的最终输出。

  

![](http://upload-images.jianshu.io/upload_images/17266280-b513255d2b62b748.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

节点是通过有方向性的线条来连接的，分为输入端和输出端，上图是一个单向输入输出的例子。

  

![](http://upload-images.jianshu.io/upload_images/17266280-c2ce88dbd4a38e8a.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

再来是一个运算的例子，Add是相加的操作，这里是两个输入端进入了相加，然后输出一个结果。

在这里要说明一下的是，这些操作很大一部分都是数学运算的方法，比如加减乘除、sin、cos之类，各位在学习之前最好要先理解他们的意思。比如相加就是互相叠加，两张图相加会整张图都变得更亮。相乘是波峰波谷的叠加，两张图相乘，会使亮的地方更亮，暗的地方更暗。其他的方法请各位自行百度去查阅了，就不一一说明。

再来看看设置的选项

  

![](http://upload-images.jianshu.io/upload_images/17266280-93eb7277d6f6b1be.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

如果曾经自己写过shader的朋友，对于这些选项应该是很熟悉的。比如很多朋友问的双面显示，其实就是把CullMode选择为Off就行。

介绍完基本功能，我们正式的来做这次的目标例子了。

  

![](http://upload-images.jianshu.io/upload_images/17266280-95f6dad75a2f1dae.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

这里我们准备了一个模型。

  

![](http://upload-images.jianshu.io/upload_images/17266280-715290413e9180f3.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

模型带有了漫反射贴图和法线贴图。

  

![](http://upload-images.jianshu.io/upload_images/17266280-82a587c2a4f68de0.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

首先新建一个着色器编辑，然后给shader起名为：myShader

  

![](http://upload-images.jianshu.io/upload_images/17266280-07468e6b2d136bc9.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

按照第一个例子的操作，我们完成了漫反射通道。

  

![](http://upload-images.jianshu.io/upload_images/17266280-6d1b37e0db1c6106.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

为了应用在我们的模型上，我们需要先生成一个shader。选择导出（Export As）

  

![](http://upload-images.jianshu.io/upload_images/17266280-eb46664af6561331.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

给shader起一个文件名。这个名称没有太大的意义。

  

![](http://upload-images.jianshu.io/upload_images/17266280-7afb457949f1a224.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

导出之后，我们来到材质球选择的地方，会看到了我们新建的myShader，选择它。

  

![](http://upload-images.jianshu.io/upload_images/17266280-75a2603a238cdf50.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

然后指定漫反射贴图，我们的模型变成了上图的效果。

  

![](http://upload-images.jianshu.io/upload_images/17266280-b185837cf2198810.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

接下来，我们在Inputs里面新建一个凹凸贴图的输入

  

![](http://upload-images.jianshu.io/upload_images/17266280-7f3d3c51fad4da49.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

然后完成法线通道节点的编辑。由于需要使用法线贴图，所以需要加入一个UnPackNormal的节点。

  

![](http://upload-images.jianshu.io/upload_images/17266280-f3e6cdd38af0b619.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

这时候，我们会发现输入通道处多了Normalmap通道，我们把法线贴图赋予上去。模型变成上图的效果。

  

![](http://upload-images.jianshu.io/upload_images/17266280-b4c9e4fa184558bb.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

我们再新建一个颜色输入，作为高光的颜色。

  

![](http://upload-images.jianshu.io/upload_images/17266280-ca35f62ab7b3e356.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

完成高光通道和光泽强度的节点编辑。

这里我用了一个Multiply（相乘），目的是让光泽强度范围的对比度更大，显得高光会更尖锐一点。高光颜色直接连接到Specular通道。

  

![](http://upload-images.jianshu.io/upload_images/17266280-ad3eab3b1a68f64f.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

现在我们的模型已经拥有了一定的质感了。由于模型原来是没有法线贴图的，我拿了漫反射贴图来直接转换，所以效果差了点，有兴趣的朋友可以自己做法线贴图增强效果。

接下来做有动画效果的光。

  

![](http://upload-images.jianshu.io/upload_images/17266280-21d5315bcb24b121.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

我们新建了几个输入：发光颜色（_LightColor），一个发光颜色的遮罩贴图（_Light），一个浮点（_dir）作为光运动的方向，一个范围选择（_RimPow）作为发光强度的控制。

  

![](http://upload-images.jianshu.io/upload_images/17266280-c3100934cd06ffe7.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

这张是发光遮罩贴图，是一张黑白的梯度图。

  

![](http://upload-images.jianshu.io/upload_images/17266280-2f7dbc1523463f2a.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

这一个步骤的节点编辑有点复杂，基本的思路是将颜色和遮罩贴图混合在一起，并用时间控制UV动画：

1、遮罩贴图我用了ViewDirection和Fresnel结合控制显示方向，并用_RimPow作为显示方向的次幂控制显示强度。

2、为了让光会随着时间自己做动画，我是用来Time和_dir相乘，这样可以控制动画的速度和方向。

3、为了让UV移动做动画，我用了UV_Pan。记得UV_Pan需要选择输入的轴，这里我选择了Y轴。

  

![](http://upload-images.jianshu.io/upload_images/17266280-cdf50a94cfb8bc56.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

4、最后，我把发光颜色和遮罩运算的结果相乘，达到叠加波峰改变颜色的目的。

  

![](http://upload-images.jianshu.io/upload_images/17266280-b898f38de3f313d9.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

最后，发布shader，根据需要选择相应的遮罩贴图，指定发光的颜色、强度和方向，我们的例子就完成了。

补充说明几点：

1、可能很多功能自带的shader都有，不过有时候你就是会需要一些功能特殊一点的shader，具体需要什么输入通道，和怎样的操作，请根据实际情况考虑。

2、关于即时镜面反射的shader，估计很多朋友都很感兴趣。不过我这里不打算详细介绍，因为unity没有直接即时反射运算的shader。

简单说明一下其原理：

在自带的水面和愤怒机器人场景里面，我们都看到了类似镜面反射的效果，其实这都是一种欺骗。做法不算复杂，其实是根据了当前摄像机的位置，新建了一个相对角度的反射摄像机，并把反射摄像机看到的内容渲染成RenderTexture。最后把RenderTexture和位置矩阵输入到普通材质的贴图通道，达到好像即时反射的效果。水面的例子做法会傻一点，因为它是针对水面物体自己生成了一个反射摄像机，所以的反射效果只会对水面本身有效果，每个可以反射的面，都要单独生成。而愤怒机器人里面的例子会聪明很多，它会在摄像机的脚本里面根据预先选择的可反射的图层，统一生成了一张RenderTexture，并让所有可以反射的shader使用。

结合着即时反射这个例子，可以看出实际上很多特殊的效果，都不是单独的shader能直接实现的，还需要到其他的脚本去配合。

