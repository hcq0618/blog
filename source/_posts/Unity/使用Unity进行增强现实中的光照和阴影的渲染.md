---
title: 使用Unity进行增强现实中的光照和阴影的渲染
thumbnail: http://upload-images.jianshu.io/upload_images/17266280-f82f876cc7529e84.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240
categories: Unity
tags: [Unity]
---

我们曾经为大家介绍过Unity中光照和阴影有关的内容，比如[Unity实时阴影实现图解](http://mp.weixin.qq.com/s?__biz=MjM5NjE1MTkwMg==&mid=2651040181&idx=1&sn=445efe3c8e751d56b0c6770123bede7c&chksm=bd1a9e848a6d17929b6164bf09c60c20255afa2413aeb47dae7d799fabac2ad5b3f084dc198f&scene=21#wechat_redirect)。近几年，增强现实应用开发者越来越多，相应的开发技巧被众多开发者所关注。本文将指导您对Unity和Vuforia
SDK增强现实的应用进行光照和阴影渲染。这背后的理论同样适用于其它的SDK和游戏引擎。

# 光照与阴影的重要性

想要使用Unity创建优质的游戏场景，光照和阴影的设置是非常重要的，因为它们被用来制造场景的景深，从而让画面更加自然与真实。缺少阴影会使得画面缺乏真实感，如果没有阴影，您无法区分出人物是站在平面上还是漂浮在空中，如下图所示。

  

![](http://upload-images.jianshu.io/upload_images/17266280-f82f876cc7529e84.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

从上图中可以看出有无阴影的明显区别，在AR增强现实应用开发中也是如此。

# 渲染光照和阴影存在的问题

如果想在Unity中渲染光照或者阴影，就必须有网格。但是，添加网格会遮挡相机视图。如下图所示，灰色的平板挡住了桌面。

  

![](http://upload-images.jianshu.io/upload_images/17266280-1d5084c38c067bd6.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

如果把灰色平板换成透明材质不就可以解决这个问题么？其实不然，如果使用透明材质替代上图的灰色平面，使用Unity的标准着色器就无法在上面投射阴影（虽然可能有些自定义着色器可以投射）。如下图所示，使用透明材质可以看到桌面，但没有阴影。

  

![](http://upload-images.jianshu.io/upload_images/17266280-2d10f9b638961038.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

# 解决思路：分别渲染光照和阴影

最初的想法是利用叠加(Addition)或者复合(Multiplication)效果，可以分别渲染光照和阴影，然后使用后处理效果将阴影和相机视图结合起来。

我们可以将场景内容分为三层：背景、光照和阴影、3D对象，然后将它们合并到一起。

 _  
_

![](http://upload-images.jianshu.io/upload_images/17266280-478cdc0790993382.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

_背景层：只包含相机渲染的图像_

 _  
_

![](http://upload-images.jianshu.io/upload_images/17266280-7145bea574b0331b.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

_光照和阴影层_

 _  
_

![](http://upload-images.jianshu.io/upload_images/17266280-9265171cfd5cc871.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

_3D对象层_

 _  
_

![](http://upload-images.jianshu.io/upload_images/17266280-423eeaa522ae7aaf.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

_三层叠加的最终效果_

上图由于桌面太黑了，因此可能看不清阴影。您可以查看下面的视频了解更多详情。

# 详细步骤

如果您还不清楚Unity结合Vuforia开发AR应用的基本步骤，可以先看看之前的文章[《5分钟使用Unity制作AR应用》](http://mp.weixin.qq.com/s?__biz=MjM5NjE1MTkwMg==&mid=2651037404&idx=1&sn=57a673dd0ec93dc3e4f44323dc70ade1&scene=21#wechat_redirect)。

  

![](http://upload-images.jianshu.io/upload_images/17266280-2ddd9a81ddb38e84.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

总得来讲，我们需要添加三个相机分别用来渲染背景、光照和阴影以及增强现实对象，这三个相机的视角与Vuforia的Augmented Reality
Camera相机完全一样，本例中使用CopyCameraData.cs来实现上述功能。另外，由于无法将对象的阴影渲染到另外一层，因此需要将其进行拷贝，我们需要编辑副本的“Mesh
Renderer”，将“Cast Shadows”属性设置为“Shadow Only”。最后，本例中使用了Color
FX插件实现后处理效果。您可以在文末查看教程的视频演示，并点击【阅读原文】下载教程相关素材。

使用Unity实现本例中AR环境下的阴影与光照渲染效果的详细步骤如下：

1）新建场景，删除新场景默认的主相机和平行光。

2）将Vuforia中的预制件ARCamera拖拽至场景中，在检视面板中加入App License Key(Vuforia 的激活码),
并勾选配置文件的Datasets(数据集)中的Load MyTargets Database和Active。

  

![](http://upload-images.jianshu.io/upload_images/17266280-f30052f926cf96c1.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

3）将Vuforia 中的预制件ImageTarget拖拽至场景中，设置好Database中的目标识别图。

4）新建一个Plane，将其Position的Y值设为-0.01(略低于识别目标图)。

5）新建一个立方体和球体，作为光照遮挡物。

6）新建一个点光源，设置好光照范围和阴影类型。

  

![](http://upload-images.jianshu.io/upload_images/17266280-95be33a91bfa8b19.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

7）将ARCamera的中的World Center
Mode由FIRST_TARGET改为SPECIFIC_TARGET。并将目标图像(ImageTarget)指定给World Center。

  

![](http://upload-images.jianshu.io/upload_images/17266280-3c6433d2134fa8f7.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

8）在ARCamera下再创建两个Camera分别命名为Light Camera和ARObject Camera。

9）打开Tags & Layers检视面板，分别添加Background Layer、Light Layer 和 ARObject Layer三个层。

  

![](http://upload-images.jianshu.io/upload_images/17266280-2be7a2f094cc986e.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

10）设置ARCamera下方的三个相机。将Light Camera的Culling Mask设置为Light Layer和Default；ARObject
Camera的Culling Mask设置为ARObject Layer和Default；Camera 的Clear Flags设置为Solid
Color, Culling Mask设置为Background Layer,
并且其子节点BackgroundPlane的Layer设置为Background Layer。

11）分别为Light Camera和ARObject Camera 添加 CopyCameraData脚本并将TargetCamera指定为Camera。

12）调整一下相机的视角，创建一个空对象命名为_ARObjects并将Plane、Cube和Sphere拖拽至其下方。然后复制_ARObjects对象并命名为_Light
Layer Objects，并将Cube和Sphere的Cast Shadows 设置为Shadows Only。将_Light Layer
Objects的层级设置为Light Layer。

  

![](http://upload-images.jianshu.io/upload_images/17266280-770171f1a9cca70d.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

13）删除_ARObjects中的 Plane，并将其层级设置为ARObject Layer。

  

![](http://upload-images.jianshu.io/upload_images/17266280-6fa62b9fa4a7f284.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

这样三个相机对应三层就设置好了。最后在Camera上添加后处理脚本对图像进行混合。本例中使用Colorful
FX插件进行混合以实现后处理效果，您也可以使用其它的后处理脚本。在Light
Camera上添加RendderTextureToBlend脚本并将Camera赋给脚本的Blend属性。最后将ARObject Camera的Clear
Flags设置为Depth only并调整深度值即可。调整混合模式选取最理想的效果。

您可以跟着下面的视频一起练习一下：

在教学视频中所涉及一些自定义的脚本，您可以点击【阅读原文】进行下载。

# 总结

希望本文可以帮您实现增强现实项目中的光照和阴影渲染。

