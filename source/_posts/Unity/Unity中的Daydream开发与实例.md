---
title: Unity中的Daydream开发与实例
thumbnail: http://upload-images.jianshu.io/upload_images/17266280-6a243bc1f0c44753.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240
categories: Unity
tags: [Unity]
---

> 本文将由Unity大中华区技术经理马瑞，为大家分享在Unity中进行Daydream平台的开发与实例。

2016年9月，我们发布了[原生支持Daydream平台的Unity技术预览版](http://mp.weixin.qq.com/s?__biz=MjM5NjE1MTkwMg==&mid=2651038620&idx=1&sn=3b62dc12ec11505ed01d61defed0fbba&chksm=bd1a94ad8a6d1dbbc646511bd10286671dab660037b0cb869bc028fd018a2014491077c0be40&scene=21#wechat_redirect)。本文将帮助您了解开发Daydream应用所需的设备和软件并介绍安装过程，以便您可以立即开始创建Daydream平台的游戏，最后提供几个优秀的案例，为您带来更好的游戏设计思路。

# 入门

创建Daydream游戏之前，我们需要做开发前的软硬件准备，包括Daydream设备和Unity的Google VR技术预览版。

  

 **Daydream设备**

Daydream设备包括一个Daydream
View头盔、控制器和支持Daydream的手机。真机测试游戏需要以上所有设备。如果您仅希望在Unity编辑器的运行模式下测试游戏，则任何类型的Android手机均可。我们会在下文关于编辑器中的VR模拟器一节中继续讨论这个问题。

  

Daydream View套装包括虚拟现实头盔和控制器。该套装可在线购买。Cardboard和Daydream的最大区别是：Daydream
头盔由布料制造，质量更好，并配备了NFC芯片。

  

![](http://upload-images.jianshu.io/upload_images/17266280-6a243bc1f0c44753.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

**支持Daydream的手机**

目前有五类手机可用：

Pixel (Pixel, Pixel XL)

Moto Z (Moto Z, Moto Z Droid, Moto Z Force Droid)

支持Daydream的手机正在不断增加。有关详细信息，您可以查看Google官方网站。如果您没有此列表中的任何手机，也可以使用Daydream开发套件与Nexus
6P手机，但Nexus 6P的散热性能不及支持Daydream的手机。

  

 **Unity的Google VR技术预览版**

创建Daydream的Build需要使用Unity的Google VR技术预览版。您可以在Unity官网下载，OS
X和Windows版本都有。它包含基于Unity 5.4.2版本的自定义编辑器和Android Player。

# Google VR SDK

Google VR SDK是开发Daydream所必需的。SDK提供原生集成的Google VR，还包含一些其它功能，详情见下文。

  

 **SDK内容**

原生集成的功能：

头部跟踪

并排立体渲染

检测用户与系统的交互

针对特定头戴设备的自动立体渲染配置

VR头盔镜头的失真校正

对齐标记 － 当您将手机插入到头盔中时，帮助您将手机屏幕与镜头对齐

自动陀螺仪运动检测

附加功能：

Daydream控制器支持

空间音频渲染

一个简单取景器(reticle)预制件和基于凝视的用户交互相关脚本

在Unity编辑器的运行模式下进行VR模拟，您可以使用鼠标和Alt / Ctrl键平移或旋转VR摄像头

“Headset Demo”场景 － 演示一个简单的Cardboard游戏

“Controller Demo”场景 － 演示与Daydream控制器的集成

显示FPS的预制件

  

 **安装指南**

下载GoogleVR SDK以及支持Daydream的Unity预览版。打开Unity，建立一个新的3D项目，然后将SDK导入项目。

  

![](http://upload-images.jianshu.io/upload_images/17266280-bdc3a694b61c1b58.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

在Player Settings下的Android选项卡下，单击”Virtual Reality
Support”并选择Daydream平台。在Minimum API Level选择Android 7.0 Nougat或更新的版本。

  

![](http://upload-images.jianshu.io/upload_images/17266280-3de4bbe4a3d9b257.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

经过以上的步骤，您的Daydream开发环境基本就搭建完毕了。

  

 **两个演示场景**

1.  控制器演示：ControllerDemo.asset

本场景展示了Daydream控制器的简单使用。 在Unity编辑器中，您可以使用Android手机与控制器仿真来模拟Daydream控制器。

2.  头盔演示：DemoScene.asset

本场景展示了简单的Cardboard或Daydream头盔行为。可以通过按下“Alt”键并移动鼠标在Unity编辑器中移动摄像机，
您也可以通过按下“Ctrl”键并移动鼠标来旋转摄像机。

  

 **控制器**

Cardboad和Daydream的主要区别是Daydream有一个控制器，控制器使用户体验更类似于HTC Vive或者Oculus Rift。

 _  
_

![](http://upload-images.jianshu.io/upload_images/17266280-ed81a700fc12040f.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

_仿真的控制器_

控制器由三个区域组成：

TouchPad - 检测触摸区域上是否有手指，并检查手指的位置。 TouchPad也可以点击。

App按钮 - TouchPad下方的按钮。

Home按钮 - 为Android系统保留的按钮。

可以通过场景中的GvrController类来获得有关控制器的输入和状态的信息。此类通过访问此单例的静态属性来提供连接状态、方向、陀螺仪读数、加速度、触摸板和按钮状态。

  

 **编辑器中的VR模拟器**

因为Daydream平台是最近才发布的，所以您可能无法及时获得必需的硬件，在Unity编辑器的运行模式下测试游戏也是个不错的选择。在这种情况下，VR模拟器非常有用。谷歌提供一个APP，可以安装在所有类型的Android手机，它会模仿真实的Daydream控制器的行为。

使用控制器仿真可能有一点不便，就是不能触摸真的控制器。谷歌提供了解决方案： 可以下载并打印一个屏幕覆盖层，包括letter,
A4和SVG三种格式。打印好后将相应按键的位置挖洞，并放在手机上面，就可以获得更真实的体验。

  

![](http://upload-images.jianshu.io/upload_images/17266280-1b927689264dc49d.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

# 开发实例

最好的学习方法就是查看示例。 Google VR的GitHub代码库包含4个非常有用的示例，可帮助您全面了解如何使用新的Google VR：

  

 **Daydream Labs Controller Playground**

![](http://upload-images.jianshu.io/upload_images/17266280-4fab4b6920bc7786.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

这是一个结合了15个小游戏的大合集，该项目供了许多不错的例子，告诉用户如何充分利用控制器与VR头盔。介绍一些VR游戏中控制器常用的使用方法。

源码下载地址：

https://github.com/googlevr/gvr-unity-
sdk/tree/master/Samples/DaydreamLabsControllerPlayground

  

 **Cardboard Design Lab**

![](http://upload-images.jianshu.io/upload_images/17266280-954291d8e9bb9e77.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

如果您是VR初学者，那么可以从该示例开始。 在整个项目中，您将学习从设计VR的基础到创建沉浸式环境等VR设计相关内容。

源码下载地址：

https://github.com/googlevr/gvr-unity-
sdk/tree/master/Samples/CardboardDesignLab

  

 **Castle Defense**

  

![](http://upload-images.jianshu.io/upload_images/17266280-c15e8bafbc40a97d.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

这是一个简单的VR手游示例。

源码下载地址：

https://github.com/googlevr/gvr-unity-sdk/tree/master/Samples/CastleDefense

  

 **Spatial Audio**

  

![](http://upload-images.jianshu.io/upload_images/17266280-a6e9650f42150ab8.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

这个项目将帮助您了解在VR项目中实现真实音频效果的最佳做法。它用到了Google VR的音频渲染功能。

源码下载地址：

https://github.com/googlevr/gvr-unity-sdk/tree/master/Samples/CastleDefense

