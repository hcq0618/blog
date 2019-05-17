---
title: Unity3D如何减少安装包大小
thumbnail: http://upload-images.jianshu.io/upload_images/17266280-c1d657f342b16faf.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240
categories: Unity优化
tags: [Unity优化]
---

译官方文档：http://docs.unity3d.com/Manual/ReducingFilesize.html

PDF文档：http://www.rukawa.cn/Uploads/Attachment/ReducingFilesize/ReducingFilesize.pdf

原文地址：http://www.rukawa.cn/index.php?s=/home/article/detail/id/27.html

需要这么做的目的和好处就不多说了。

第一步要做的就是：看看哪些文件是最占空间的，那么它们就是首选优化对象了。

你可以在刚刚完成一次build之后在“Editor Log”中找到这些信息。

如何打开Editor Log：

  

![](http://upload-images.jianshu.io/upload_images/17266280-c1d657f342b16faf.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

在Mac上看起来就是这样的了：

  

![](http://upload-images.jianshu.io/upload_images/17266280-de199f9854e4ea85.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

可以看出这份log提供了一份资源总括：各种类型资源的总大小，以及所占百分比。同时还降序列出了单个文件的大小。

顺带一提，资源类型中的“File
headers”它们并不是资源本身，而是加在原始资源上，用来存储“引用”与“配置信息”的额外数据。通常可以忽略这些数据的大小，但如果在你的“Resources”文件夹里有着十分庞大的资源文件的话，这些数据也可能会很大。。

这份log可以帮助你鉴定哪些文件是你或许想要删掉或者进行优化的。

不过在开工之前，还需要先了解几点：

1、Unity再编码会把资源导成它自己的内部格式，所以资源源文件的类型是不相干的。比如你有一个多图层的PS纹理，那么在build之前它就会被拼接、压缩。所以刻意把这份纹理转成PNG格式其实对减少包大小并没有帮助。在开发时还是用最方便的格式就好了。

2、Unity会在build时去掉那些你的项目中没有使用到的资源，所以不需要我们手动找出来删掉了。但是脚本是不会被删掉的（不过它们不占资源），还有“Resources”文件夹里的全部资源，也是不会自动帮你删除的（因为Unity无法判断这里面哪些是需要用到的）。所以我们要确保“Resources”文件夹里的都是我们真正要用到的。当然，你还可以通过动态加载AssetBundles的方式来代替“Resources”文件夹里的资源，以减少包大小。

一些建议：

# 纹理（Textures）

纹理通常会占据大部分空间。第一步要做的就是选用经压缩的纹理格式（DXT 或者
PVRTC）。如果这样没有减少它的所占用空间，那么试试缩小纹理的尺寸吧。你不需要对资源本身进行修改，只要在 Project 下选中纹理，然后在
Inspectpr 下设置Max Size就行了。

  

![](http://upload-images.jianshu.io/upload_images/17266280-9d7ef3defcab6302.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

有一个好办法就是：在场景中找到使用了该纹理的object，放大画面，然后一边降低 Max Size
，一边看场景中的object，直到它看起来比较糟糕，就可以知道怎样是最合适的了。。

  

![](http://upload-images.jianshu.io/upload_images/17266280-f3125f0c116b127e.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

  

![](http://upload-images.jianshu.io/upload_images/17266280-8d3a0300b461de44.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

  

![](http://upload-images.jianshu.io/upload_images/17266280-7ba2e814b5f046be.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

  

![](http://upload-images.jianshu.io/upload_images/17266280-79717e71aea46cf2.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

  

![](http://upload-images.jianshu.io/upload_images/17266280-71da3b61680f2960.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

  

  

![](http://upload-images.jianshu.io/upload_images/17266280-902e9a4669c6324a.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

![](http://upload-images.jianshu.io/upload_images/17266280-ee0768a059325237.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

  

  

![](http://upload-images.jianshu.io/upload_images/17266280-d8532c8cc0ec48b9.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

由以上几张图对比来看，我们就能发现，选择512甚至256的Max Size，效果都是可以的，而且资源大小也能有显著的减少。修改纹理的Max
Size并不会影响到资源本身，只是改变了它在游戏里的分辨率。下表列出了不同图片格式所占用空间的大小（单位bpp：字节/像素）

  

![](http://upload-images.jianshu.io/upload_images/17266280-7d87338448f068b3.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

一张图片的大小计算公式：width * height * bpp，如果你使用的是mipmap贴图，那么其大小将是普通图片的3倍左右。

Unity默认在导入纹理时就会进行压缩，为了在开发时节约时间，我们可以在偏好设置里手动关掉此功能

  

![](http://upload-images.jianshu.io/upload_images/17266280-1cad54699bfbda78.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

而在build时，Unity不管你有没有勾选这一项，都会对纹理进行压缩。

# 网格与动画（Meshes and Animations）

网格与导入的动画（Animation Clips）都可以被压缩。在选中一个模型之后，就可以在Inspector中进行设置了。

  

![](http://upload-images.jianshu.io/upload_images/17266280-71d05cc9f3db328e.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

不过对它们进行压缩，是可能造成误差的。所以最好先弄清楚什么程度的压缩是可接受范围内的。另外，mesh的压缩仅仅是减少数据文件的大小，并不会减少运行时的内存消耗。而减少动画关键帧，则会让两者都有所减少，一般情况下我们都应该开启。

  

![](http://upload-images.jianshu.io/upload_images/17266280-b8ff1dfd1b8f5e7e.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

# **动态链接库（DLLs）**

默认情况下，Unity只会在build时包含以下dll：

  

![](http://upload-images.jianshu.io/upload_images/17266280-128d2aca3da06ffd.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

我们应该避免对 System.dll 或者 System.Xml.dll 有所引用，否则还是会在build时包含进来，而它们也会占用数M的空间。

如果在游戏中确实需要解析XML，那么可以使用“Mono.Xml.zip”来代替系统级的dll。此外，大多数泛型容器都已经包含在标准库中，只有少数几个在System.dll里，所以可能的话，也应该避免使用到它。

# 减少手机上使用的 .NET 库的大小

Unity为移动设备提供了两套 .NET 的API：.NET 2.0 和.NET 2.0 Subset

.NET 2.0
提供了几乎整套的API功能，但是很多时候游戏都用不上那么多，导致大量多余的代码占用了宝贵的空间资源。为了避免浪费，我们就可以用Unity提供的 .NET
2.0 Subset（相当于.NET
2.0的一个子集）。为节省资源，这里面很多一般用不到的例程库都被移除了，所以这一优化也会是很有用的，只是需要确保我们的代码能够正常工作。

可在“Player Settings”中进行设置

  

![](http://upload-images.jianshu.io/upload_images/17266280-93da9c6ccea4c153.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

# **移除无用的代码**

目前我们的项目比较适合使用Strip ByteCode选项,并配合link.xml使用,link.xml放到项目的Assetes目录下:

  

![](http://upload-images.jianshu.io/upload_images/17266280-d0d88f4dda548d0e.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

# **对于android平台，如果包实在太大，可以使用 Split Application Binary 功能**

在Player Setting > Publishing Settings里，

  

![](http://upload-images.jianshu.io/upload_images/17266280-837f37c15dc3cffd.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

关于Split Application Binary<http://www.ceeger.com/Manual/android-
OBBsupport.html>

