---
title: Canvas
thumbnail: http://upload-images.jianshu.io/upload_images/17266280-a90d6e33192f545a?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240
categories: Unity
tags: [Unity]
---

每个UI元素都必须处于一个Canvas的子级中；

一个场景中可以存在多个Canvas；

render mode 渲染模式

Render Mode-Screen Overlay

画布总会铺满整个屏幕，总是渲染在所有元素的最上层

![](http://upload-images.jianshu.io/upload_images/17266280-a90d6e33192f545a?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

  

![](http://upload-images.jianshu.io/upload_images/17266280-f277612a083a438b.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

，画布的RectTransform的大小有屏幕决定；

Pixel Perfect选项会让UI边缘锐利；

Render Mode-Camera

在没有指定摄像机的时候，和Sreen
Overlay效果完全一样。指定了摄像机以后，画布会自动调整到相机可视范围内，比Canvas更靠近相机的3Dobject会被渲染在前面，比Canvas远离相机的3dObject会被遮挡

  

![](http://upload-images.jianshu.io/upload_images/17266280-09e01122123aae22.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

  

![](http://upload-images.jianshu.io/upload_images/17266280-7f674c8e88edbcba.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

  

![](http://upload-images.jianshu.io/upload_images/17266280-32bd755b18812652.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

  

![](http://upload-images.jianshu.io/upload_images/17266280-10edc5778fa5329a.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

画布全权交由这个摄像机来渲染，多个相机的渲染次序，相机类型等都会对该画布的元素有影响。此模式下画布的RectTransform完全受到相机的ViewPort
Rect影响；

Pixel Perfect和Screen Overlay模式下的作用一样；

Plane Distance 决定Canvas与渲染相机的距离；

该模式可能有如下场景应用：

#### 1.如果渲染Canvas的相机是透视的，可以调整Canvas内某些元素的旋转角度，产生透视和深度效果；

  

![](http://upload-images.jianshu.io/upload_images/17266280-5e73315232471dc3.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

#### 2.可以通过不同相机的sorting layer和渲染的图层来实线UI上方的粒子特效等。

Render Mode-World Space

画布的Rect Transform完全自由，不受任何约束，可以自行设置大小、位置；

可以放置于物体的子级，常用作气泡、对话框等；

EventCamera 该选项决定该UI接受哪个相机的事件，如果该项为None，则默认接受主相机的事件。如果指定某个相机，则只接受该相机的事件。

  

![](http://upload-images.jianshu.io/upload_images/17266280-777fdce8d0f4214a.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

![](http://upload-images.jianshu.io/upload_images/17266280-4fd33b946b8efdb2.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

![](http://upload-images.jianshu.io/upload_images/17266280-c99766f1318214e1.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

