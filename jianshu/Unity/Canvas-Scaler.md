---
title: Canvas-Scaler
thumbnail: http://upload-images.jianshu.io/upload_images/17266280-b99937e2c9c359a6.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240
categories: Unity
tags: [Unity]
---

话说坑在何方？想当年年少轻狂时，层做了个类似下图的玩意：

  

![](http://upload-images.jianshu.io/upload_images/17266280-b99937e2c9c359a6.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

    勃主大笑三声，把screen的大小拖动了一下，然后它就变成了这个样子：

  

![](http://upload-images.jianshu.io/upload_images/17266280-1dde04d56f6ca103.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

    这是一件相当窝巢的事情，勃主苦练锚点三十年，终究还是没有搞定，知道师父他老人家蛋蛋的提点了一句“看看Canvas Scaler”。。。。。。

    上图，勃主当时的scaler设定是这样的：

  

![](http://upload-images.jianshu.io/upload_images/17266280-42b6bd837d959346.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

    嗯，问题就在这里了，UI扩展模型——固定像素大小！！！！

    好吧，淡淡的改成了下面这样：

  

![](http://upload-images.jianshu.io/upload_images/17266280-62cc0b288e8a4db6.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

    问题解决了，ui怎么捏都不会变形了。。。

    到这里，好奇心颇重的勃主撩起三脚猫的English打开了官方API：

[官方API的老巢](file:///D:/Program%20Files%20%28x86%29/Unity/Editor/Data/Documentation/html/en/Manual
/script-CanvasScaler.html)

    对于Canvas Scaler的描述是这样的“The Canvas Scaler component is used for controlling
the overall scale and pixel density of UI elements in the Canvas. This scaling
affects everything under the Canvas, including font sizes and image
borders.”（画布定标器组件是用于控制UI元素的整体规模和像素密度在画布上。这个扩展影响在画布上的一切,包括字体大小和图像边界。）我知道，谁都受不了这该死的鸡翻，所以我还得重新翻过：Canvas
Scaler是用来控制Canvas上的UI元素整体规模和像素的组件，这个扩展影响Canvas上的一切，包括字体大小和图像边界。

    Canvas Scaler的ui scale mode有三种值（constan pixel size、scale with screen
size和constant physical size）,接下来我就来介（翻）绍（译）一下这三种情况下的各参数代表的含义

# 1.Constant Pixel Size 不变像素大小

  

![](http://upload-images.jianshu.io/upload_images/17266280-95f1c5d756aee58d.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

参数：

Scale Factor–大小比例；

Reference Pixels Per Unit – ,每单位代表像素量

# 2.Scale With Screen Size根据屏幕大小定标

  

![](http://upload-images.jianshu.io/upload_images/17266280-d79a9c9ac184e88b.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

-Reference Resolution(参考分辨率) 

The resolution the UI layout is designed for. if the screen resolution is
larger, the UI will be scaled up, and if it’s smaller, the UI will be scaled
down.

参照这个UI布局所依据的分辨率，如果屏幕分辨率更大，那么UI会变大，如果屏幕分辨率更小，那么UI会变小。

-Screen Match Mode(屏幕匹配模式) 

Match Width or Height 参考宽或者高或者两者来规划画布

Expand 横纵两个方向扩大画布使画布不小于参考

Shrink 裁切画布使画布不大于参考

-Reference Pixels Per Unit 每单位的参考像素

当选择Match Width or Height时会有Match滑块，用来决定width和height的影响比例

# 3.Constant Physical Size 不变的物理尺寸

  

![](http://upload-images.jianshu.io/upload_images/17266280-bb87da164114310b.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

Physical Unit可以设置物理单位

Fallback Screen DPI屏幕分辨率不明是采用的分辨率

Default Sprite DPI 精灵每英寸的默认像素

Reference Pixels Per Unit

# 4.当Canvas的Render Mode属性为world space时

  

![](http://upload-images.jianshu.io/upload_images/17266280-3d8ab4edde4c3f77.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

Canvas Scaler的ui Scale Mode为world不可改变

