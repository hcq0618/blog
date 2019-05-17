---
title: FX-Maker
thumbnail: http://upload-images.jianshu.io/upload_images/17266280-bdfac16af5b2839c.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240
categories: Unity插件
tags: [Unity插件]
---

插件介绍

    FX
Maker是一款制作特效的工具，它专为移动操作系统做了优化。包括300种Prefab特效，300种纹理结构、100种网格、100种曲线效果。支持英文和韩文，由开发商IGSoft提供。是UNT3D中一款强大的粒子特效制作工具。

概述

-  FX Maker包含300个特效Prefabs。

-  已经为移动设备进行了优化。FX Maker是用来产生特效的工具（创建、查看、分析、测试）。

-  支持BuildSprite功能，可以把数百个三角形转化为仅仅2个三角形。

-  支持Mesh、Legacy和Shuriken粒子系统。

-  粒子大小调节（Transform.Scale）

-  调整速度（Mesh, Legacy, Shuriken）

-  适用于Unity 4.3.4或更高版本（支持Unity5）。

-  包含的资源：300个特效，300个纹理，100个Mesh，100个曲线动画。

FX Maker是Unity3d一款非常流行的效果制作插件。不但有超过300种效果预制体， 还可以自己制作效果。包含Mesh Effect
和Particle Effect。

优点：资源库大，可以将消耗资源非常多的粒子效果
转换为帧动画效果。当然也可以直接用不转帧动画的效果，这种效果是画面最好的，但是对显卡开销大。帧动画显卡开销小，占内存大，适合移动平台。Fx
Maker还能自动保存。

使用步骤:

 **一:导入包**

 **<http://jingyan.baidu.com/article/cb5d6105fda595005d2fe068.html>**

 **二:打开主场景sceneFXMaker**

  

![](http://upload-images.jianshu.io/upload_images/17266280-bdfac16af5b2839c.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

**三:运行**

运行界面如下，注意不要选全屏运行，要在运行时至少同时有Game界面和Inspector界面。

  

![](http://upload-images.jianshu.io/upload_images/17266280-368037fafdb02e0d.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

当前运行的效果对应 _CurrentObject下面的物体。既可以对下图左侧的UI界面操作，亦可以对Hierarchy下面的物体进行直接操作。

  

![](http://upload-images.jianshu.io/upload_images/17266280-c6e6a1e96c871ef1.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

EffectMesh

网格动画，主要是平面的网格动画，Mesh_Ring和Mesh_Virtical有特殊形状的形状片的动画。

  

![](http://upload-images.jianshu.io/upload_images/17266280-098d2b794259c85e.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

EffectParticle

粒子效果，其中最后的Shuriken里包含的是新的Shuriken粒子系统，其他全是旧的粒子系统。

  

![](http://upload-images.jianshu.io/upload_images/17266280-6b71f8fac79b364d.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

EffectSample

效果样例展示

  

![](http://upload-images.jianshu.io/upload_images/17266280-405675a540b71ae2.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

Resources

包含一些资源，其中最重要的是Animation的曲线效果 和 Mesh下的网格

  

![](http://upload-images.jianshu.io/upload_images/17266280-3c59d87459ba8efe.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

**四:做简单的帧动画效果**

1.选第一个Project文件夹，新建一个空效果

  

![](http://upload-images.jianshu.io/upload_images/17266280-6250b847fcda0fa1.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

2.从已有的效果拷贝物体过来

已有效果，对着FX Maker UI里的物体点击右键，Copy

  

![](http://upload-images.jianshu.io/upload_images/17266280-19fdd0b35db64029.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

3.运行看看效果

4.做成帧动画(精灵动画)

先点击Sprite

  

![](http://upload-images.jianshu.io/upload_images/17266280-42d11dc429993e3d.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

在出现下图左侧的Build Sprite界面时，用鼠标滚轮调整视口，如右侧红框，使之刚好涵盖效果区域。

接着可以直接点“Build Sprite”按钮

  

![](http://upload-images.jianshu.io/upload_images/17266280-5ed42aa30c036b90.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

之后就生成了新的效果,名字是 原名+_1 之类的,就在原效果旁边。

对着新效果点右键，Export。 之后就生成了一般的Unity Package。

包括了所有这个效果需要用到的资源。

  

![](http://upload-images.jianshu.io/upload_images/17266280-d58c25f8fdad2ac4.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

  

![](http://upload-images.jianshu.io/upload_images/17266280-4c347ee10f34bef2.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

**五:使用导出的效果**

直接导入使用即可。效果路径和原工程下的路径完全一样。

  

![](http://upload-images.jianshu.io/upload_images/17266280-47a3bc9dce185ef1.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

**六 加入其他东西Build Sprite**

并不一定要FxMaker的效果才可以拿来Build Sprite。任何东西，只要相机看得见就可以放进去Build
Sprite。并且可以和FxMaker的混合Build。

将东西加到效果下，这里是将Unity包里的Constructor放到效果 NewEffect1里。

正常Build Sprite

Build好后把新效果里的NcBillboard去掉，或者NcBillboard里的Front Axis设置为 Axis_Back。不然方向会颠倒。

由于使用的是Particle下的Addictive Shader,所以是与背景混合的半透明效果。

所以只适合拿来做效果。

至于真实物体的3D转2D,有兴趣的朋友可以自己去研究。

帧数起码要在FPS20以上，否则卡顿感太明显。

帧动画虽然不消耗显卡，但是贴图占内存还是比较大的。所以用完一定要释放内存。

