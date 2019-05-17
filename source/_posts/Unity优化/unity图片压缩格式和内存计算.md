---
title: unity图片压缩格式和内存计算
thumbnail: http://upload-images.jianshu.io/upload_images/17266280-dba31eb2dd91a5ff.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240
categories: Unity优化
tags: [Unity优化]
---

![](http://upload-images.jianshu.io/upload_images/17266280-dba31eb2dd91a5ff.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

例子1：使用RGBA 32bit真彩（Truecolor），占用内存 = 4Bytes*512*512 = 1MB;

例子2：使用RGB ETC 4bit压缩，占用内存 = 0.5Bytes*512*512 = 128KB

一、2的N次方大小的图片会得到引擎更大的支持，包括压缩比率，内存消耗，打包压缩大小，而且支持的力度非常大。

二、减小图片的占用大小和内存方式有:图片大小变化(Maxsize),色彩位数变化(16位，32位)，压缩(PVRC)。

三、U3D对于图片的格式是自己生成的，而并不是你给他什么格式，他就用什么格式，一张1024*1024图在无压缩格式下，它会被U3D以无压缩文件形式存放，也就是说U3D里的Texture
Preview里显示的占用大小**MB不只是内存占用大小，还是空间占用大小

U3D的内部机制为自动生成图片类型来替换我们给的图片，在图片的压缩方式上需要进行谨慎的选择。

压缩格式在U3D的Component Reference里有介绍我就不再详细介绍，只介绍几个重点的:

RGBA32格式为无压缩最保真格式，但也是最浪费内存和空间的格式。Automatic Turecolor和它一个意思。

RGBA16格式为无压缩16位格式，比32位节省一半的空间和内存。Automatic 16bits和它一个意思。

RGBA Compressed PVRTC
4bits格式为PVRTC图片格式，它相当于把图片更改了压缩方式新生成了一个图片来替换原来的我们给的图片格式(比如我们给的是PNG格式)。

注意：U3D所有图片的压缩格式都会以另一种方式来存储，不会以你给的方式来存储，只有你指定了某种格式，它才会转成你要的格式。而且压缩格式在Android里并不一定有效，因为Android的机型多，GPU的渲染方式也不一样，有的是Nvidia，有的是PowerVR，最最好的在安卓机子上启用RGBA16方式，因为这个是适应所有机型的，并且比32位占用量少一半，但也需要因项目而异，只是推荐使用的格式，可以多用，但要权衡内存和显示效果。

