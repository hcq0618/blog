---
title: ARKit：增强现实技术在美团到餐业务的实践
thumbnail: 
categories: AR
tags: [AR]
---
##  ARKit：增强现实技术在美团到餐业务的实践

原创： 曹宇  美团技术团队 __

![](640_1.png)  

**总第282篇**

 **2018年 第74篇**

  

##  **前言**

增强现实（Augmented Reality）是一种在视觉上呈现虚拟物体与现实场景结合的技术。Apple 公司在 2017 年 6 月正式推出了
ARKit，iOS 开发者可以在这个平台上使用简单便捷的 API 来开发 AR 应用程序。

本文将结合美团到餐业务场景，介绍一种基于位置服务（LBS）的 AR 应用。使用 AR
的方式展现商家相对用户的位置，这会给用户带来身临其境的沉浸式体验。下面是实现效果：

![](640_1.gif)  

图1 实现效果图

##  **项目实现**

iOS 平台的 AR 应用通常由 ARKit 和渲染引擎两部分构成：

![](640_8.jpg)  

图2 AR 应用的整体架构

ARKit 是连接真实世界与虚拟世界的桥梁，而渲染引擎是把虚拟世界的内容渲染到屏幕上。本部分会围绕这两个方面展开介绍。

## ARKit

ARKit 的 ARSession 负责管理每一帧的信息。ARSession 做了两件事：拍摄图像并获取传感器数据；对数据进行分析处理后逐帧输出。如下图：

![](640.jpg)  

图3 ARKit 结构图

### 设备追踪

设备追踪确保了虚拟物体的位置不受设备移动的影响。在启动 ARSession 时需要传入一个 ARSessionConfiguration
的子类对象，以区别三种追踪模式：

  * ARFaceTrackingConfiguration

  * ARWorldTrackingConfiguration

  * AROrientationTrackingConfiguration

其中 ARFaceTrackingConfiguration 可以识别人脸的位置、方向以及获取拓扑结构。此外，还可以探测到预设的 52
种丰富的面部动作，如眨眼、微笑、皱眉等等。ARFaceTrackingConfiguration 需要调用支持 TrueDepth
的前置摄像头进行追踪，显然不能满足我们的需求，这里就不做过多的介绍。下面只针对使用后置摄像头的另外两种类型进行对比。

#### ARWorldTrackingConfiguration

ARWorldTrackingConfiguration 提供 6DoF（Six Degree of Freedom）的设备追踪。包括三个姿态角
Yaw（偏航角）、Pitch（俯仰角）和 Roll（翻滚角），以及沿笛卡尔坐标系中 X、Y 和 Z 三轴的偏移量：

![](640_10.jpg)  

图4 6DoF

不仅如此，ARKit 还使用了 VIO（Visual-Inertial
Odometry）来提高设备运动追踪的精度。在使用惯性测量单元([](https://en.wikipedia.org/wiki/Inertial_measurement_unit)[IMU](https://en.wikipedia.org/wiki/Inertial_measurement_unit))检测运动轨迹的同时，对运动过程中摄像头拍摄到的图片进行图像处理。将图像中的一些特征点的变化轨迹与传感器的结果进行比对后，输出最终的高精度结果。

从追踪的维度和准确度来看，ARWorldTrackingConfiguration
非常强悍。但如[](https://developer.apple.com/documentation/arkit/understanding_world_tracking_in_arkit?language=objc)[官方文档](https://developer.apple.com/documentation/arkit/understanding_world_tracking_in_arkit?language=objc)所言，它也有两个致命的缺点：

  * 受环境光线质量影响

  * 受剧烈运动影响

由于在追踪过程中要通过采集图像来提取特征点，所以图像的质量会影响追踪的结果。在光线较差的环境下（比如夜晚或者强光），拍摄的图像无法提供正确的参考，追踪的质量也会随之下降。

追踪过程中会逐帧比对图像与传感器结果，如果设备在短时间内剧烈的移动，会很大程度上干扰追踪结果。追踪的结果与真实的运动轨迹有偏差，那么用户看到的商家位置就不准确。

#### AROrientationTrackingConfiguration

AROrientationTrackingConfiguration 只提供对三个姿态角的追踪（3DoF），并且不会开启 VIO。

> Because 3DOF tracking creates limited AR experiences, you should generally
not use the AROrientationTrackingConfiguration class directly. Instead, use
the subclass ARWorldTrackingConfiguration for tracking with six degrees of
freedom (6DOF), plane detection, and hit testing. Use 3DOF tracking only as a
fallback in situations where 6DOF tracking is temporarily unavailable.

通常情况下来讲，这么做的理由是因为 AROrientationTrackingConfiguration
的追踪能力受限，[](https://developer.apple.com/documentation/arkit/arorientationtrackingconfiguration?language=objc)[官方文档](https://developer.apple.com/documentation/arkit/arorientationtrackingconfiguration?language=objc)不推荐直接使用。但是鉴于：

  1. 对三个姿态角的追踪，已经足以正确的展现商家相对用户的位置了。

  2. ARWorldTrackingConfiguration 的高精度追踪，更适合于距离较近的追踪。比如设备相对桌面、地面的位移。但是商家和用户的距离动辄几百米，过于精确的位移追踪意义不大。

  3. ARWorldTrackingConfiguration 需要规范用户的操作、确保环境光线良好。这对用户来说很不友好。

最终经过讨论，我们团队决定使用
AROrientationTrackingConfiguration。这样的话，即便是在夜晚，甚至遮住摄像头，商家的位置也能够正确的进行展现。而且剧烈晃动带来的影响很小，商家位置虽然会出现短暂的角度偏差，但是在传感器数值稳定下来后就会得到校准。

### 坐标轴

ARKit 使用笛卡尔坐标系度量真实世界。ARSession 开启时的设备位置即是坐标轴的原点。而 ARSessionConfiguration 的
worldAlignment 属性决定了三个坐标轴的方向，该属性有三个枚举值：

  * ARWorldAlignmentCamera

  * ARWorldAlignmentGravity

  * ARWorldAlignmentGravityAndHeading

三种枚举值对应的坐标轴如下图所示：

![](640_3.jpg)  

图5 三种枚举值对应的坐标轴

对于 ARWorldAlignmentCamera
来说，设备的姿态决定了三个坐标轴的方向。这种坐标设定适用于以设备作为参考系的坐标计算，与真实地理环境无关，比如用 AR 技术丈量真实世界物体的尺寸。

对于 ARWorldAlignmentGravity 来说，Y 轴方向始终与重力方向平行，而其 X、Z
轴方向仍然由设备的姿态确定。这种坐标设定适用于计算拥有重力属性的物体坐标，比如放置一排氢气球，或者执行一段篮球下落的动画。

对于 ARWorldAlignmentGravityAndHeading 来说，X、Y、Z 三轴固定朝向正东、正上、正南。在这种模式下 ARKit
内部会根据设备偏航角的朝向与地磁真北（非地磁北）方向的夹角不断地做出调整，以确保 ARKit 坐标系中 -Z
方向与我们真实世界的正北方向吻合。有了这个前提条件，真实世界位置坐标才能够正确地映射到虚拟世界中。显然，ARWorldAlignmentGravityAndHeading
才是我们需要的。

### 商家坐标

商家坐标的确定，包含水平坐标和垂直坐标两部分：

#### 水平坐标

商家的水平位置只是一组经纬度值，那么如何将它对应到 ARKit 当中呢？我们通过下图来说明：

![](640_6.jpg)  

图6 经纬度转换为坐标

借助 CLLocation 中的 `distanceFromLocation:location`
方法，可以计算出两个经纬度坐标之间的距离，返回值单位是米。我们可以以用户的经度 lng1、商家的纬度 lat2 作一个辅助点（lng1,
lat2），然后分别计算出辅助点距离商家的距离 x、辅助点距离用户的距离 z。ARKit 坐标系同样以米为单位，因而可以直接确定商家的水平坐标（x,
-z）。

#### 垂直坐标

对商家地址进行中文分词可以提取出商户所在楼层数，再乘以一层楼大概的高度，以此确定商家的垂直坐标 y 值：

![](640_2.png)  

图7 高度信息提取

## 卡片渲染

通常我们想展示的信息，都是通过 UIView 及其子类来实现。但是 ARKit
只负责建立真实世界与虚拟世界的桥梁，渲染的部分还是要交给渲染引擎来处理。Apple 给我们提供了三种可选的引擎：

  * Metal

  * SpriteKit

  * SceneKit

强大的 Metal 引擎包含了 MetalKit、Metal 着色器以及标准库等等工具，可以更高效地利用 GPU，适用于高度定制化的渲染要求。不过
Metal 对于当前需求来说，有些大材小用。

SpriteKit 是 2D 渲染引擎，它提供了动画、事件处理、物理碰撞等接口，通常用于制作 2D 游戏。SceneKit 是 3D 渲染引擎，它建立在
OpenGL 之上，支持多通道渲染。除了可以处理 3D 物体的物理碰撞和动画，还可以呈现逼真的纹理和粒子特效。SceneKit 可以用于制作 3D
游戏，或者在 App 中加入 3D 内容。

虽然我们可以用 SpriteKit 把 2D 的卡片放置到 3D 的 AR 世界中，但是考虑到扩展性，方便之后为 AR 页面添加新的功能，这里我们选用 3D
渲染引擎 SceneKit。

我们可以直接通过创建 ARSCNView 来使用 SceneKit。ARSCNView 是 SCNView 的子类，它做了三件事：

  * 将设备摄像头捕捉的每一帧的图像信息作为 3D 场景的背景

  * 将设备摄像头的位置作为 3D 场景的摄像头（观察点）位置

  * 将 ARKit 追踪的真实世界坐标轴与 3D 场景坐标轴重合

### 卡片信息

SceneKit 中使用 SCNNode 来管理 3D 物体。设置 SCNNode 的 geometry 属性可以改变物体的外观。系统已经给我们提供了例如
SCNBox、SCNPlane、SCNSphere 等等一些常见的形状，其中 SCNPlane 正是我们所需要的卡片形状。借助 UIGraphics
中的一些方法可以将绘制好的 UIView 渲染成一个 UIImage 对象。根据这张图片创建 SCNPlane，以作为 SCNNode 的外观。

###  **  
**

### 卡片大小

ARKit 中的物体都是近大远小。只要固定好 SCNPlane 的宽高，ARKit 会自动根据距离的远近设置 SCNPlane
的大小。这里列出一个在屏幕上具体的像素数与距离的粗略计算公式，为笔者在开发过程中摸索的经验值：

![](640_4.jpg)  

也就是说，假如 SCNPlane 的宽度为 30，距离用户 100 米，那么在屏幕上看到这个 SCNPlane 的宽度大约为 \\(530 / 100
\times 30 = 159\) pt。

### 卡片位置

对于距离用户过近的商家卡片，会出现两个问题：

  * 由于 ARKit 自动将卡片展现得近大远小，身边的卡片会大到遮住了视野

  * 前文提到的 ARSession 使用 AROrientationTrackingConfiguration 追踪模式，由于没有追踪设备的水平位移，当用户走向商家时，并不会发觉商家卡片越来越近

这里我们将距离用户过近的卡片映射到稍远的位置。如下图所示，距离用户的距离小于 d 的卡片，会被映射到 d-k ~ d 的区间内。

![](640.png)  

图8 过近卡片位置映射

假设某商家距离用户的真实距离为 x，映射后的距离为 y，映射关系如下：

![](640_3.png)  

这样既解决了距离过近的问题，又可以保持卡片之间的远近关系。用户位置发生位移到达一定阈值后，会触发一次新的网络请求，根据新的用户位置来重新计算商家的位置。这样随着用户的移动，卡片的位置也会持续地更新。

### 卡片朝向

SceneKit 会在渲染每一帧之前，根据 SCNNode 的约束自动调整卡片的各种行为，比如碰撞、位置、速度、朝向等等。SCNConstraint
的子类中 SCNLookAtConstraint 和 SCNBillboardConstraint 可以约束卡片的朝向。

SCNLookAtConstraint 可以让卡片始终朝向空间中某一个点。这样相邻的卡片会出现交叉现象，用户看到的卡片信息很可能是不完整的。使用
SCNBillboardConstraint 可以解决这个问题，让卡片的朝向始终与摄像头的朝向平行。

![](640_2.jpg)  

图9 卡片朝向的两种约束

下面是创建卡片的示例代码：

```
// 位置

SCNVector nodePosition = SCNVectorMake(-200, 5, -80);

  

// 外观

SCNPlane *plane = [SCNPlane planeWithWidth:image.size.width

                                    height:image.size.height];

plane.firstMaterial.diffuse.contents = image;

  

// 约束

SCNBillboardConstraint *constraint = [SCNBillboardConstraint
constraint.freeAxes = SCNBillboardAxisY;

  

SCNNode *node = [SCNNode nodeWithGeometry:plane];

node.position = nodePosition;

node.constraints = @[constraint];
```

#  

#  **优化**

##  **遮挡问题**

如果同一个方向的商家数量有很多，那么卡片会出现互相重叠的现象，这会导致用户只能看到离自己近的卡片。这是个比较棘手的问题，如果在屏幕上平铺卡片的话，既牺牲了对商家高度的感知，又无法体现商家距离用户的远近关系。

### 点击散开的交互方式

经过漫长的讨论，我们最终决定采取点击重叠区域后，卡片向四周分散的交互方式来解决重叠问题，效果如下：

![](640_3.gif)  

图10 卡片散开的效果

下面围绕点击和投射两个部分，介绍该效果的实现原理。

####  **点击**

熟悉 Cocoa Touch 的朋友都了解，UIView 的层级结构是通过 hit-testing 来判断哪个视图响应事件的，在 ARKit 中也不例外。

ARSCNView 可以使用两种 hit-testing：

  * 来自 ARSCNView 的 `hitTest:types:` 方法：查找点击的位置所对应的真实世界中的物体或位置

  * 来自 SCNSceneRenderer 协议的 `hitTest:options:` 方法：查找点击位置所对应的虚拟世界中的内容。

显然，`hitTest:options:` 才是我们需要的。在 3D 世界中的 hit-testing
就像一束激光一样，向点击位置的方向发射，`hitTest:options:`
的返回值就是被激光穿透的所有卡片的数组。这样就可以检测到用户点击的位置有哪些卡片发生了重叠。

#### 投射

这里简单介绍一下散开的实现原理。SCNSceneRenderer 协议有两个方法用来投射坐标：

  * `projectPoint:`：将三维坐标系中点的坐标，投射到屏幕坐标系中

  * `unprojectPoint:`：将屏幕坐标系中的点的坐标，投射到三维坐标系中

其中屏幕坐标系中的点也是个 SCNVector3，其 z 坐标代表着深度，从 0.0（近裁面）到 1.0（远裁面）。散开的整体过程如下:

![](640_5.jpg)  

图11 投射过程

散开后，点击空白处会恢复散开的状态，回到初始位置。未参与散开的卡片会被淡化，以突出重点，减少视觉压力。

### 后台聚类

对于排布比较密集的商家，卡片的重叠现象会很严重。点击散开的卡片数量太多对用户不是很友好。后台在返回用户附近的商家数据时，按照商家的经纬度坐标，使用
K-Means 聚类算法进行二维聚类，将距离很近的商家聚合为一个卡片。由于这些商家的位置大体相同，可以采用一个带有数字的卡片来代表几个商家的位置：

![](640.gif)  

图12 聚合卡片

## 闪烁问题

实测中发现，距离较近的卡片在重叠区域会发生闪烁的现象：

![](640_2.gif)  

图13 闪烁

这里要引入一个 3D 渲染引擎普遍要面对的问题——可见性问题。简单来说就是屏幕上哪些物体应该被展示，哪些物体应该被遮挡。GPU
最终应该在屏幕上渲染出所有应该被展示的像素。

可见性问题的一个典型的解决方案就是[](https://en.wikipedia.org/wiki/Painter%27s_algorithm)[画家算法](https://en.wikipedia.org/wiki/Painter%27s_algorithm)，它像一个头脑简单的画家一样，先绘制最远的物体，然后一层层的绘制到最近的物体。可想而知，画家算法的效率很低，绘制较精细场景会很消耗资源。

### 深度缓冲

 **  
**

[深度缓冲](https://en.wikipedia.org/wiki/Z-buffering)
弥补了画家算法的缺陷，它使用一个二维数组来存储当前屏幕中每个像素的深度。如下图所示，某个像素点渲染了深度为 0.5 的像素，并储存该像素的深度：

![](640_1.jpg)  

图14 深度缓冲区

下一帧时，当另外一个物体的某个像素也在这个像素点渲染时，GPU
会对该像素的深度与缓冲区中的深度进行比较，深度小者被保留并被存入缓冲区，深度大者不被渲染。如下图所示，该像素点下一帧要渲染的像素深度为
0.2，比缓冲区存储的 0.5 小，其深度被存储，并且该像素被渲染在屏幕上：

![](640_9.jpg)  

图15 深度小的像素被保留

显然，深度缓冲技术相比画家算法，可以极大地提升渲染效率。但是它也会带来深度冲突的问题。

### 深度冲突

深度缓冲技术在处理具有相同深度的像素点时，会出现深度冲突（[](https://en.wikipedia.org/wiki/Z-fighting)[Z-fighting](https://en.wikipedia.org/wiki/Z-fighting)）现象。这些具有相同深度的像素点在竞争中只有一个“胜出”，显示在屏幕上。如下图所示：

![](640_7.jpg)  

图16 深度冲突

如果这两个像素点交替“胜出”，就会出现我们视觉上的闪烁效果。由于每个卡片都被设置了 SCNBillboardConstraint
约束，始终朝向摄像头方向。摄像头轻微的角度变化，都会引起卡片之间出现部分重合。与有厚度的物体不同，卡片之间的深度关系变化很快，很容易出现多个卡片在屏幕同一个位置渲染的情况。所以经常会出现闪烁的现象：

![](640_4.gif)  

图17 角度变化引起的深度冲突

为了解决这 Bug 般的体验，最终决定牺牲深度缓冲带来的渲染效率。SceneKit 为我们暴露了深度是否写入、读取缓冲区的接口，我们将其禁用即可：

```
 plane.firstMaterial.writesToDepthBuffer = NO;

 plane.firstMaterial.readsFromDepthBuffer = NO;
```

由于卡片内容内容相对简单，禁用缓冲区对帧率几乎没什么影响。

##  **总结**

在到餐业务场景中，以 AR+LBS 的方式展现商家信息，可以给用户带来沉浸式的体验。本文介绍了 ARKit
的一些使用细节，总结了在开发过程中遇到的问题以及解决方案，希望可以给其他开发者带来一点参考价值。

  

  

