---
title: VR效果神器，Unity精品相机插件
thumbnail: http://upload-images.jianshu.io/upload_images/17266280-fdac312f305497a4.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240
categories: Unity插件
tags: [Unity插件]
---

今天向大家推荐几款强大易用的相机插件，可以用于录制高清VR游戏视频、实现各种炫酷的相机特效，甚至有便利实现移动VR环境的移动解决方案。

# Helios

  

![](http://upload-images.jianshu.io/upload_images/17266280-fdac312f305497a4.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

Helios是用于录制高清流畅视频的插件，不但支持普通的2D视频、3D视频，而且有适用于VR环境的全景视频，还可以同时录制音频。Helios利用特别设计的着色器来获取场景截图，并将这些图片转换为适用于各种3D及全景视频平台所需的视频格式。

目前Helios仅支持在Unity编辑器模式下使用。相比其它的全景视频解决方案，Helios功能更加完善，而且支持主流的VR头盔包括Oculus、Gear
VR、HTC Vive、Google
Cardboard。同时，全景视频平台如Facebook和YouTube。Helios可以直接导出6种不同质量的视频，最高支持90FPS的8K全景视频。当然，它还可以导出高清的GIF、JPEG或PNG图片。

  

![](http://upload-images.jianshu.io/upload_images/17266280-c50db0b6679632db.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

使用Helios也非常简单，其中已经内置好了用于录制不同视频的预制件（Prefab），并包含所有必需的脚本，只需将这些预制件添加到场景中，再简单进行一些设置即可。以录制3D视频为例，只需将Helios3D预制件拖拽至场景，然后在检视面板中设置Helios脚本的参数，以选择视频类型、质量、特效及存储目录等。剩下的就等Helios自动完成即可。

  

![](http://upload-images.jianshu.io/upload_images/17266280-40e007df16a5e140.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

下载地址：

https://www.assetstore.unity3d.com/en/#!/content/63643

# Camera Transitions

  

![](http://upload-images.jianshu.io/upload_images/17266280-f210c078e7076c5c.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

Camera
Transitions可用来实现一系列的相机变换特效，适用于各种画面切换效果，包括缩放、盒式切换、渐变、闪现、翻转、翻页、折叠、抖动、线性模糊等等。Camera
Transitions几乎可以满足所有的全画面变换需求。

Camera Transitions需要硬件GPU支持Shader Model
3.0及以上版本，基本上只要是2009年以后面世的GPU就没有问题。有些效果在移动设备上可能消耗比较大，例如翻页。类似的注意事项都已标示在插件网页上，使用时可以作为参考。

  

![](http://upload-images.jianshu.io/upload_images/17266280-250281f3e6907680.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

使用Camera Transitions首先需要在场景中新建一个空GameObject，然后为其添加Camera Transitions脚本。Camera
Transitions脚本会对所有特效做全局设置，如自动或手动切换、更新频率、特效的范围等。

  

![](http://upload-images.jianshu.io/upload_images/17266280-80655fab050a536c.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

针对所有特效的使用代码，作者也给出了示例，只需调用一句代码即可。以圆圈扩散特效为例，只需调用DoTransition函数即可，其参数分别表示变换类型、原始相机、目标相机、变换时间以及一些可选的传入参数：

  

![](http://upload-images.jianshu.io/upload_images/17266280-ec3b45c0c518e4c4.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

上面的代码可实现如下效果：

  

![](http://upload-images.jianshu.io/upload_images/17266280-177bb8dce44ea717.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

而除了代码调用外，还可以利用CameraAssistantTransitions组件直接在检视面板中进行设置，免去手动编写代码的步骤。

  

![](http://upload-images.jianshu.io/upload_images/17266280-fa9da4d30941b425.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

下载地址：

https://www.assetstore.unity3d.com/en/#!/content/36055

# Mobile VR Movement Pack

  

![](http://upload-images.jianshu.io/upload_images/17266280-1087903426222419.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

Mobile VR Movement
Pack提供了5种移动VR环境下的移动方案示例，包括路径点系统、导航网格、摇杆控制、自动行走及视线控制（向下看行走，向上看停止）几种方式。每个都提供了示例场景，可以支持Gear
VR、Google VR、Cardboard及Daydream平台。

使用Mobile VR Movement Pack非常简单，插件提供了代表不同移动方式的预制件，只需将这些预制件拖拽至场景，然后删除场景中的其它相机即可。

  

![](http://upload-images.jianshu.io/upload_images/17266280-722d5eb9da5cbd0f.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

插件还包括一系列用于实现各种不同效果的简明脚本。例如，添加了VR
WalkableSuface脚本的对象会被导航网格视为“可通过的”，以便找到正确的路径。VR Waypoint脚本则用来设置路径点。

  

![](http://upload-images.jianshu.io/upload_images/17266280-ef1cb677599406e5.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

下载地址：

https://www.assetstore.unity3d.com/en/#!/content/69041

