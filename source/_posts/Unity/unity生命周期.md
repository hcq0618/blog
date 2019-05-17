---
title: unity生命周期
thumbnail: http://upload-images.jianshu.io/upload_images/17266280-01392e56e46956f5.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240
categories: Unity
tags: [Unity]
---

 继承MonoBehavior的生命周期

  

![](http://upload-images.jianshu.io/upload_images/17266280-01392e56e46956f5.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

![](http://upload-images.jianshu.io/upload_images/17266280-72e1e272c117dfc4.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

![](http://upload-images.jianshu.io/upload_images/17266280-3d6a398fa366ceda.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

主要的生命周期：

Reset : 用户第一次添加组件时或用户点击见组件面板上的Reset按钮时调用

OnAwake:
当脚本实例被载入时Awake被调用，一般可以在这个地方将当前脚本禁用:this.enable=false，如果这样做了，则会直接跳转到OnDisable方法执行一次，然后其它的任何方法，都将不再被执行。如果当前脚本处于可用状态，则正常的执行顺序是继续向下执行OnEnable，当然我们可以在另外一个脚本中实现这个脚本组件的启动：this.enab=true;

OnStart:  Start仅在Update函数第一次被调用前调用。

OnUpdate：渲染一帧之前被调用。这里是大部分游戏行为代码被执行的地方，除了物理代码。

LateUpdate:
是在所有Update函数调用后被调用。这可用于调整脚本执行顺序。例如:当物体在Update里移动时，跟随物体的相机可以在LateUpdate里实现。如果后面写了Reset，则会又回到Update

OnGUI:  渲染和处理GUI事件时调用，当然，如果你使用了NGUI，这个生命周期的事情就不用考虑了。

  

FixedUpdate:
这个函数在每个物理时间步被调用一次。这是处理基于物理游戏行为的地方。常用于移动模型等操作。不受帧率影响，默认0.02s，如果卡帧了Update就不会再执行，而FixedUpdate则继续执行。

Edit->preject setting ->Time -> (Inspector监测视图）Fixed Timestep 设置刷新时间

OnDisable:
当对象变为不可用或非激活状态时此函数被调用。这个时候，脚本并不会被销毁，在这个状态下，可以重新回到OnEnable状态（enable=true）。

OnDestroy: 当MonoBehaviour将被销毁时，这个函数被调用。当前脚本的生命周期结束。

建议一般在Awake中做一些初始化，在Start中获取游戏对象

其他的生命周期：

OnPreCull:在相机剔除场景之前调用此函数。相机可见的对象取决于剔除。OnPreCull 函数调用发生在剔除之前。

OnBecameVisible/OnBecameInvisible:在对象对于相机可见/不可见时调用此函数。

OnWillRenderObject:如果对象可见，则为每个相机调用一次此函数。

OnPreRender:在相机开始渲染场景之前调用此函数。

OnRenderObject:在完成所有常规场景渲染后调用此函数。此时，可使用 GL 类或 Graphics.DrawMeshNow 绘制自定义几何图形。

OnPostRender:在相机完成场景渲染后调用此函数。

OnRenderImage（仅限专业版）：在完成场景渲染后调用此函数，以便对屏幕图像进行后处理。

OnGUI:在每帧上多次调用此函数，以响应 GUI 事件。程序首先将处理 Layout 和 Repaint 事件，然后再处理每个输入事件的 Layout 和
keyboard/鼠标事件。

OnDrawGizmos: 用于在场景视图中绘制小图示 (Gizmos)，以实现可视化目的。

