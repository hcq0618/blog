---
title: 在Unity中使用UFPS创建第一人称射击游戏
thumbnail: http://upload-images.jianshu.io/upload_images/17266280-d07fa67a628d85ac.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240
categories: Unity插件
tags: [Unity插件]
---

Unity Asset Store资源商店中总有很多功能强大的插件让开发者事半功倍，例如UFPS : Ultimate
FPS因其具备的平滑控制、流畅实时生成的相机和武器动作的功能，而受到广大开发者的欢迎。本文由Unity大中华区技术经理马瑞为大家介绍一下UFPS :
Ultimate FPS这款插件对创建第一人称射击游戏的贡献。

# UFPS: Ultimate FPS是什么？

UFPS，即 Ultimate FPS，是由Opsive(FPS)
开发的模板项目，这个项目对初级或中级开发者来说是必不可少的，因为它可以帮助您提高FPS游戏运行效率。它是Unity Asset
Store中维护时间最长的资源之一, 在整个生命周期中，得到了来自开发者的诸多好评。已经有很多游戏使用了这个模板，例如：

Time Rifters

Slender: The Arrival

Rambo (the mobile game)

Shark Attack Deathmatch 2

Gone Home

Tacoma

Grave

Reflections

Ascend

Surviving Pangea

# 强大的功能

UFPS: Ultimate FPS有一些很有用的功能：

基于物理的动画 — 让流畅的枪击和相机抖动等动作更加真实

鼠标平滑和加速 — 您可以选择不同的鼠标移动模式，这样在为不同类型的角色，如机甲，士兵等开发角色控制器时，可能会很方便。

支持本地Oculus VR — 在日益增长的VR市场环境下，开发者将VR结合进来是被很多人看好的。

拥有机械动画播放器的全身感知 —
含有一个全身模型和动画。生成地形(Terrain)或可步行空间后，您可以指定曲面的材质，并将不同的声效和粒子分配给不同的材质。

手榴弹，爆炸系统和掩护(Cover)支持 — 大多数现代FPS游戏允许玩家使用手榴弹。您可以借助UFPS创造全新爆炸型手榴弹并且在躲在墙后以免受伤。

具有方向攻击指示器和血液飞溅效果的HUD — 当玩家受到伤害时，这个HUD会变得“血腥”。此外，箭头可以帮助我们辨别我们在哪个方向被攻击。

地震、冲击波、Boss挑战和相机反馈 —
UFPS为开发者提供了一套漂亮的相机抖动。他们被某些事件触发，例如：玩家从高处跌落，或者附近有一个强烈的爆炸/地震。

库存和物品捡起系统。

高级表面碰撞系统 —  如果您射击沙子或草地，会发现有不同的粒子产生。

Spawnpoint系统与智能障碍检测。

基于键盘，鼠标或触摸屏的UFPS输入管理器 — 允许在运行时重新绑定控制器。

拆除系统 — 玩家销毁的对象(Object)将被新对象(Object)替换。

交互系统 —门，平台，触发器，开关，抓取和投掷东西的交互。

表面系统允许通用和强大的物理模拟

高级移动平台支持

慢动作模式 — 像Max Payne游戏中让时间变慢

支持Unity Pro专业版图像FX

支持反欺诈工具箱ObscuedTypes

完整且良好注释的C＃代码

100多页详细的在线学习手册

  

下载地址：

https://www.assetstore.unity3d.com/en/#!/content/2943

# 演示场景

下面我们介绍几个演示场景，包括简单场景和完整项目，以便更清晰地了解UFPS的功能。

 **Clean Scene**

这个场景不太复杂，含有地形(Terrain)和第一视角摄像机控制器。您可以尝试跌落悬崖，看看相机如何对这个事件做出反应。

 **  
**

![](http://upload-images.jianshu.io/upload_images/17266280-d07fa67a628d85ac.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

**Demo Scene 1**

这个场景包含很多例子。第一个例子演示了在使用UFPS时可以实现多少不同的效果。您可以轻松实现西部牛仔风格的游戏、现代FPS、太空宇航员、炮塔、狙击步枪、甚至控制机甲！
如下图所示。

  

![](http://upload-images.jianshu.io/upload_images/17266280-7a5597e3cd5f3820.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

第二个示例为您展示了可以实现的不同的相机抖动，比如地震，Boss挑战，进攻的炮兵和撞毁的飞机。它们其中的任何一个事件将带来不同的相机抖动。您可以在后面即将介绍的Sky
City演示中了解到：当您在玩家的附近投掷手榴弹时，看到类似的效果如下图所示。

  

![](http://upload-images.jianshu.io/upload_images/17266280-b2f8731eeff9628b.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

每种类型的游戏需要的鼠标控制方式略有不同。例如使用手枪相对于使用狙击步枪时，可能想要实现不同的效果。从下面的例子中您可以了解到如何实现不同的鼠标模式，并在游戏视图中看到不同的效果。

  

![](http://upload-images.jianshu.io/upload_images/17266280-0363fe1c11cc7a21.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

您可以改变持有的武器风格，比如Old School和Modern Shooter等，如下图所示。

 **  
**

![](http://upload-images.jianshu.io/upload_images/17266280-41055b1ea13b824a.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

**Demo Scene 2**

这个场景的目的是展示基于物理的摄像机动画如何对不同的事件作出反应，如掉下屋顶，从高处跳跃等。我们很期待看到当玩家附近发生爆炸以及当玩家用他的头撞到墙上等情况发生时，相机会作何反应。

 **  
**

![](http://upload-images.jianshu.io/upload_images/17266280-2706a946ccc8b4d8.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

**Demo Scene 3**

这个演示场景看起来更像一个完整的项目。您可以收集武器，用步枪、手枪或者替换其他武器进行射击，爆炸的对象可能会造成损害，并降低您的生命值。您还可以在场景周围抓取和移动对象，销毁一些对象
。当您进入白色气泡，就会切换为慢动作模式，时间将减慢几秒钟，产生Matrix/Max Payne效果。

 **  
**

![](http://upload-images.jianshu.io/upload_images/17266280-1efb6654b7b4ed97.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

**Sky City**

最后的演示是一个完整的项目。在这个场景中，你将围绕建筑物攻击敌人的塔楼。玩家可以藏在墙后面躲避子弹。
您可以在猎枪，步枪，手枪和手榴弹之间切换，体会到在一个完整的FPS游戏中，不同的系统是如何协同工作的。

  

![](http://upload-images.jianshu.io/upload_images/17266280-df24791351e3a66c.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

# 总结

如果想要建立第一视角射击游戏，UFPS是一个非常好的起点。它的一系列有用的元素可以被用来构建游戏，例如将UFPS作为坚实的框架，并添加游戏特定的逻辑和资源后，就可以变成一个完整的游戏。不过请记住，插件本身不是最终产品，您仍然需要在资源和代码方面之下一些功夫，来完善您的游戏。想要了解更多技术相关内容，请访问Unity官方中文社区(forum.china.unity3d.com)。

