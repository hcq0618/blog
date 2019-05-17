---
title: 插件改造Unity为建模利器
thumbnail: http://upload-images.jianshu.io/upload_images/17266280-0d0452efdcd994ce.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240
categories: Unity插件
tags: [Unity插件]
---

随着许多优秀开发者的大力支持，积极地将优质内容发布到Unity资源商店上，Asset
Store俨然已经成为一座宝库。我们前面已经为大家分享多种类型的插件资源以及编辑器扩展工具，包括脚本编程工具等。今天继续为大家介绍三款建模工具，通过它们，您可以直接把Unity当作Maya或3D
Max来用了。

# Realtime CSG

  

![](http://upload-images.jianshu.io/upload_images/17266280-0d0452efdcd994ce.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

Realtime
CSG用于在Unity中快速创建3D环境。由于是在Unity编辑器下直接进行的操作，所以可以很方便的进行迭代调整。通过它能够进行基本3D建模工具的大部分操作，例如创建及编辑几何体、自动为几何体添加碰撞体、网格对齐及旋转、导出为FBX等等。

将Realtime CSG插件导入Unity中，即可看到Scene视图变为下图的样子：

  

![](http://upload-images.jianshu.io/upload_images/17266280-e35730f092aae4f8.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

这就是Realtime CSG的操作界面了。Edit Modes包含了Realtime
CSG提供的5种编辑模式，每一种模式都有单独的操作，显示在左下角。界面下方的工具栏按钮用来控制Unity网格是否显示，网格是否按X、Y、Z轴对齐，对齐的方式与角度，是否以线框模式渲染场景，是否显示辅助面以及最后的重做场景按钮。

为了更符合建模师的操作习惯，可以首先将Unity编辑器视图切换为4 Split模式，同时显示4个窗口：

  

![](http://upload-images.jianshu.io/upload_images/17266280-14357db5e83051c0.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

然后您可以按照自己的操作习惯，分别设置四个视图的视角与渲染模式。对于正交模式的2D视图，可以关闭一些特效渲染：

  

![](http://upload-images.jianshu.io/upload_images/17266280-d2933ec592742bab.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

使用Realtime CSG自带的线框模式，可以将场景切换为如下显示效果：

  

![](http://upload-images.jianshu.io/upload_images/17266280-4d281e55a68d5e75.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

基本操作就是这些了，下面来看看实际建模的效果：

  

![](http://upload-images.jianshu.io/upload_images/17266280-ef151bd44cab4baa.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

下载地址：https://www.assetstore.unity3d.com/en/#!/content/69542

* * *

# BuildR Procedural Building Generator

  

![](http://upload-images.jianshu.io/upload_images/17266280-563c10d5dd059b91.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

这是一款专门用于在Unity编辑器中生成建筑的插件。BuildR简化了很多操作，基本上只需点击按钮，即可利用插件的生成功能直接创建出高楼大厦。

导入BuildR插件后，依次点击菜单项GameObject > Create New BuildR
Building新建一个建筑对象，在层级视图选中新建的对象，可以看到检视面板的脚本如下：

  

![](http://upload-images.jianshu.io/upload_images/17266280-66a3e8d5185f1454.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

这个脚本涵盖了所有的创建操作，点击其中一个按钮，即可新建地板或建筑。下面就进入了编辑模式，此时脚本显示如下：

  

![](http://upload-images.jianshu.io/upload_images/17266280-cc4e9160e3961ab6.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

看到这里就您应该就明白了，真的只需要点击就能直接生成并编辑建筑，包括添加或移除墙壁、顶点等。上面的一排按钮分别用来调整建筑结构、纹理、表面贴花、屋顶设计、建筑细节、建筑内景及设计，还有生成及导出设置。BuildR支持将建筑数据以XML形式导出。

  

![](http://upload-images.jianshu.io/upload_images/17266280-033feedf39e336ad.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

下载地址：https://www.assetstore.unity3d.com/en/#!/content/7292

* * *

# ProBuilder Advanced

  

![](http://upload-images.jianshu.io/upload_images/17266280-7cd25c45364d847a.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

ProBuilder同样是用于Unity编辑器中的建模工具。该工具最早于2012年发布，历经多次迭代，现在的版本已经非常成熟。迄今为止已有不少使用该插件制作并已成功的上线游戏，包括《Tinertia》、《SUPERHOT》及《Republique》等等，都是在Steam上广受好评的游戏。

ProBuilder同样支持快速创建，并直接点击播放按钮来预览效果，能够自动生成碰撞体和UV，还支持一些高级操作如UV展开、光照贴图设置及优化等。依次点击Tools
> ProBuilder > ProBuilder Window打开ProBuilder编辑器，界面如下：

  

![](http://upload-images.jianshu.io/upload_images/17266280-5ad0405a14b19049.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

使用方式也很简单，点击条目，即可对选中的对象进行相应的操作，过程清晰明了。以楼梯为例，点击New Shape或者使用快捷键Ctrl/Cmd +
K，新建一个可以供ProBuilder编辑的Cube。ProBuilder已经内置了一系列常见的形状，选中Cube后打开Shape
Editor，在下拉列表中选择Stair即可创建楼梯：

  

![](http://upload-images.jianshu.io/upload_images/17266280-13230b838ec7ea80.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

下面来看看使用ProBuilder创建大型建筑内景：

  

![](http://upload-images.jianshu.io/upload_images/17266280-17de0a9eea47d55b.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

另外ProBuilder还有免费版插件Probuilder Basic，包含一些基本的几何体操作，有兴趣的朋友可以先试用免费版尝鲜。

下载地址：https://www.assetstore.unity3d.com/en/#!/content/3558

