---
title: Unity中的批处理优化与GPU-Instancing
thumbnail: http://upload-images.jianshu.io/upload_images/17266280-e6663ef6e366ef72.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240
categories: Unity优化
tags: [Unity优化]
---

>
Unity大中华区技术经理马瑞曾经为大家带来[《Unity中的Daydream开发与实例》](http://mp.weixin.qq.com/s?__biz=MjM5NjE1MTkwMg==&mid=2651040100&idx=1&sn=b6c2a5704626c9fd76936e6ca3e70105&chksm=bd1a9e558a6d1743b21d1982198e8eff42b3e2d9dc225401700884e5461abaaa7d351bbf947f&scene=21#wechat_redirect)，本文马瑞将继续为大家分享Unity中的批处理优化与GPU
Instancing技术。

我们都希望能够在场景中投入一百万个物体，不幸的是，渲染和管理大量的游戏对象是以牺牲CPU和GPU性能为代价的，因为有太多Draw
Call的问题，最后我们必须找到其他的解决方案。

在本文中，我们将讨论两种优化技术，它们可以帮助您减少Unity游戏中的Draw Call数量以提高整体性能：批处理和GPU Instancing。

# 批处理

开发者在日常工作中遇到的最常见的问题之一是性能不足，这是由于CPU和GPU的运行能力不足。一些游戏可以运行在PC上，但是在移动设备上不行。游戏运行时运行是否流畅受Draw
Call数量的影响很大。有几个解决方案能帮助您解决这个问题。最常见的是批处理，包括Static Batching和Dynamic Batching。

Static Batching可以让引擎降低任何尺寸网格的Draw Call，如下图所示：

  

![](http://upload-images.jianshu.io/upload_images/17266280-e6663ef6e366ef72.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

要让场景中的物体使用Static Batching，需要将其标记为Static，并在Mesh Renderer中共享相同的材质，因为Static
Batching不会在CPU上做顶点转换，所以它通常比Dynamic
Batching更有效。不过它会使用更多的内存，例如你的场景中有相同物体的多个副本，Unity会将它们组合成一个大网格并可能会增加内存使用。Unity将尽可能多的网格结合到一个静态网格中，并将其作为一个Draw
Call提交。这种方法的缺点是：标记为Static的物体在其生命周期中不能移动。

Dynamic Batching启用时，Unity将尝试自动批量移动物体到一个Draw
Call中。要使物体可以被动态批处理，它们应该共享相同的材质，但是还有一些其他限制：

 **顶点数量：** Dynamic
Batching场景中物体的每个顶点都有一定的开销，因此批处理只适用于少于900个顶点属性的网格物体。举个例子，如果你的着色器使用顶点位置，法线和一个UV，那么你可以动态批处理多达300个顶点；而如果你的着色器使用顶点位置，法线，UV0，UV1和切线，那么只有180个顶点。值得注意的是，属性计数限制可能会在将来更改。

 **镜像信息：** 如果物体包含的Transform具备镜像信息，例如A物体的大小是(1f, 1f, 1f)，而B物体的大小则是(-1f, -1f,
-1f)，则无法做批处理。

 **材质** ：如果物体使用不同的材质实例，即使它们本质上相同，也不会被批量处理。而Shadow Caster Rendering是个例外。

 **渲染器：**
拥有光照贴图的物体有其他渲染器参数，例如光照贴图索引或光照贴图的偏移与缩放。一般来说，动态光照贴图的游戏对象应该指向要批量处理的完全相同光照贴图的位置。

 **不能使用Multi-pass着色器的情况：** 几乎所有的Unity着色器都支持多个灯光的正向渲染模式（Forward
Rendering），这要求额外的渲染次数，所以绘制 “额外的每像素灯”时不会被批处理；Legacy Deferred（Light Pre-
Pass）渲染路径不能被动态批处理，因为它必须绘制物体两次。

Dynamic Batching通过将所有物体的顶点转换为CPU上的世界空间来工作，所以它只能在渲染Draw
Call的工作量小于CPU顶点转换工作量的时候，才会起到提高性能的作用。当用游戏机或如Metal这样的现代API，Draw
Call的开销通常低得多，Dynamic Batching就无法提高性能了。了解到以上限制后，如果明智地使用批处理，可以显著提高您游戏的性能。

# GPU Instancing

提高图形性能的另一个好办法是使用GPU Instancing。GPU Instancing的最大优势是可以减少内存使用和CPU开销。当使用GPU
Instancing时，不需要打开批处理，GPU Instancing的目的是一个网格可以与一系列附加参数一起被推送到GPU。要利用GPU
Instancing，您必须使用相同的材质，且可以传递额外的参数到着色器，如颜色，浮点数等。

  

Unity从5.4版本开始支持GPU Instancing。 唯一的限制是在游戏物体上要使用相同的材质和网格。 目前支持以下平台：

Windows DX11/DX12 和 SM 4.0 或更高/OpenGL 4.1 或更高

OS X and Linux：OpenGL 4.1 and above

移动：OpenGL ES 3.0 或更高/Metal

PlayStation 4

Xbox One

  

如果您想要进行进一步的优化，例如减少管理场景物体的开销，您也可以使用Graphics.DrawMeshInstanced方法。
您只需要传递您的网格，材质和附加属性来绘制您的物体。现在的限制是一次最多1023个实例。在Unity
5.6中，我们添加了Graphics.DrawMeshInstancedIndirect的新方法，可以用来指定需要渲染的实例数量。

# GPU Instancing案例

要创建支持GPU Instancing的基本标准表面着色器，可以在您的项目里面点击：

Create->Shader->StandardSurfaceShader(Instanced)。

  

![](http://upload-images.jianshu.io/upload_images/17266280-c755236ca3a49904.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

然后，在材质属性中选择新创建的着色器。

  

![](http://upload-images.jianshu.io/upload_images/17266280-be6b5b5113d07a08.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

虽然实例化的物体共享相同的网格和材质，但您可以使用MaterialPropertyBlock API为每一个物体设置单独的着色器属性。

如果一个游戏对象被标记为“Static”并且打开了Static Batching，那么这个游戏对象就不能进行GPU
Instancing，检视器中会出现一个警告框，提示“静态批处理”标志可以在播放器设置（Player
Settings）中取消。如果游戏对象支持Dynamic
Batching，但是它使用的某个材质可以进行实例化，那么这个游戏对象将不会被批处理，并且将被自动实例化。

当使用Forward Rendering渲染模式，受多个灯光影响的物体无法有效地实例化。只有Base
Pass可以有效地利用实例化，而不是添加的Pass。此外，使用光照贴图或受不同光或Reflection
probe影响的物体无法实例化。如下图所示，您可以在Frame Debug中发现和GPU Instancing相关的Draw Call被标记为“Draw
Mesh（Instanced）”。

  

![](http://upload-images.jianshu.io/upload_images/17266280-cc44411a14a95ec0.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

GPU Instancing是一个非常强大的功能。在Unity
5.6中，您可以使用Graphics.DrawMeshInstancedIndirect绘制大量网格。在Mac
Pro中，我们能够画出约68万个具有不同颜色的移动立方体并保持稳定的60帧每秒的帧率。

下图是一个示例场景，超过6千个包子在天空中围绕一个大碗飞翔，它们都投射和接收阴影。由于使用了GPU
Instancing，几乎没有性能开销。这里的包子模型使用了StandardSurface Shader（Instanced）。

  

![](http://upload-images.jianshu.io/upload_images/17266280-83b94c5104e681a7.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

# 总结

在本文中，我们描述了用于优化渲染性能的两种最流行的技术：批处理和GPU
Instancing。我们向您展示了如何在实践中使用它们并讨论可能的应用。正因为有诸如批处理和GPU
Instancing等优化技术的存在，我们能够绘制大量的对象并保持稳定的性能。

