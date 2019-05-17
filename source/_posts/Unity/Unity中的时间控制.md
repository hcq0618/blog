---
title: Unity中的时间控制
thumbnail: http://upload-images.jianshu.io/upload_images/17266280-140c4eacca6d8184.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240
categories: Unity
tags: [Unity]
---

# 关卡创建  

本文会探讨如何在Unity中使用时间控制进行关卡创建。在探讨之前，可以观看视频了解拥有时间控制玩法的解谜游戏《Lintrix》：

因为与《Lintrix》拥有同样的时间控制玩法的游戏并不多见，因此本文以《Lintrix》为例，说明如何在Unity中实现该功能，以及它可以有哪些应用。
我们将以Unity引擎为例，并使用Unity相关的术语，但其概念也适用于其他引擎。

# 时间控制对创建关卡的意义

为什么要用时间控制来辅助创建关卡呢？这样设计的主要契机是：第一，《Lintrix》团队有成员在创建动画编辑器方面具有丰富经验；第二，Unity有一个时间轴，可以查看场景在任何时刻的表现。

  

我们希望状态和属性，比如Unity对象的Transforms，可依赖于时间，并且能够跳转到特定时刻，因为如果这样的话，正常进行游戏的时候，所有对象都将拥有相应的状态。

  

就游戏本身而言，因为《Lintrix》是确定性的游戏，所以可以很好地利用时间轴来实现时间控制。《Lintrix》场景的许多对象都在游戏进行时移动，并且它们彼此之间的相对位置非常重要，像时间轴这样的工具可以帮助关卡设计者更容易理解该关卡在游戏中的样子，以便在编辑器中进行创建。另外在大多数情况下，我们也很容易编辑某个时刻的关卡，从而让所有的对象在某个具体时间点定位或旋转，并且当时间设置为零或开始移动时，对象会自动重新计算其位置。

我们提供了快捷键以便于对时间进行前进和后退操作。之后，关卡创建不仅是摆放物体后运行，更多的是向前或向后跳跃，以及重新定位对象，所以这些物体在关卡的任意时刻都要保持在其预先设计的位置。

  

![](http://upload-images.jianshu.io/upload_images/17266280-140c4eacca6d8184.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

这在《Lintrix》游戏中非常有用：一方面，希望玩家能够连接晶体来消灭所有的敌人；另一方面，又不希望这些连接会覆盖其他晶体或者彼此重叠。

# 如何避免对象碰撞

实际上，在开发《Lintrix》游戏的过程中，重叠是个大问题，因为当场景中大多数对象移动时，很难防止它们过早碰撞。 大部分时间会出现类似这种糟糕的效果：

  

![](http://upload-images.jianshu.io/upload_images/17266280-1dfbf81f5821ec9a.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

为了理解物体如何移动，我们添加了移动轨迹。它让敌人在晶体之间移动而不碰撞的问题更加容易避免。

  

![](http://upload-images.jianshu.io/upload_images/17266280-ab68351f900d0193.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

它也可用于可视化晶体运动。

  

![](http://upload-images.jianshu.io/upload_images/17266280-9923e29bb11ab99d.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

我们在创建关卡时使用时间控制进行“计时”。 这里的计时表示调整关卡某些部分的运动，使得在关卡运行时物体早点或晚点出现。 有时甚至希望来回移动所有的动作。
例如，在关卡开始时可以预留给玩家一些时间，以便他们能够预估将会发生的景象。 使用时间轴可以轻松地将时间移至负值，并将此新时间设为零表示开始。

  

因为在编辑器模式下更新时间的脚本被添加到控制时间的对象，如果想要启用或禁用对象上更改时间的效果，只需启用或禁用此脚本，并使它们响应或忽略时间的更改。

# 实现方法

下面我们一起来看看如何在Unity中实现该功能。

 **创建接口**

首先创建一个非常简单的接口，让所有需要随时间变化的脚本都实现这个接口：

```
public interface ITimeChanging
{
    void AddTime(float dt);
}
```

**定义时间操控实体**

这个时间操控实体可以为一组实现了ITimeChanging接口的对象调用这些方法。 实体接口如下：

```
public class TimeManager
{
    float Time { get; set; }
    IEnumerable<ITimeChanging> TimeDependants { get; set; }
    void SetTimeBruteForce(float time);
}
```

在编辑器模式中，有一个可以让用户直接在运行模式下控制时间的脚本。如下图所示，你可以看到关卡控制器通过它的Update()来增加时间。

  

![](http://upload-images.jianshu.io/upload_images/17266280-42a1bb7af7898650.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

示例项目下载链接：

https://github.com/alexander91/timelineExample

 **为时间控制添加物体响应**

我们设置了一个时间轴管理器，允许跳转到不同的时刻。
以及几个带有线性运动（LineMovement）脚本的立方体，LineMovement脚本继承自ITimeChaning，并监听TimeManager中的时间改变（AddTime），可以在监视器面板设置这个立方体以给定速度朝预定方向移动，代码如下：

```
public class LineMovement : MonoBehaviour, ITimeChanging
{

    [SerializeField]
    Vector3 direction = Vector3.up;

    [SerializeField]
    float speed = 0.2f;

    public void AddTime(float dt)
    {
        transform.position += dt * speed * direction.normalized;
    }
}
```

综上所述，编辑器自定义时间控制工具非常适用于确定性的游戏，这将让整个工作流程分外轻松。 另外，如果游戏中的动作很简单，也可以很容易在编辑器中提供各种选项。

  

# 时间倒退  

之前我们探讨了Unity中时间控制在[关卡创建](http://mp.weixin.qq.com/s?__biz=MjM5NjE1MTkwMg==&mid=2651040085&idx=1&sn=12fe0737b989460f1573c8c38289ca11&chksm=bd1a9e648a6d17721c6e7e72aa67623e057abcf14c020e0a469fc57450b3b5631f3108de55fc&scene=21#wechat_redirect)方面的应用，今天我们将以解谜游戏[《Lintrix》](http://mp.weixin.qq.com/s?__biz=MjM5NjE1MTkwMg==&mid=2651040085&idx=1&sn=12fe0737b989460f1573c8c38289ca11&chksm=bd1a9e648a6d17721c6e7e72aa67623e057abcf14c020e0a469fc57450b3b5631f3108de55fc&scene=21#wechat_redirect)为例，继续为大家分享在开发游戏的过程中，如何在Unity中实现时间倒退功能，并且对游戏设计与机制进行深入的探讨，希望能对大家有帮助。

# 时间倒退功能的必要性

在开发并试玩游戏的过程中，我们认识到玩家往往会忘记在关卡中犯过的错误，所以需要在游戏中做大量的记录。事实上，一些游戏关卡的设计目的就是为了从各个方向分散玩家的注意力，让玩家在某个时刻忽视某个方向来的敌人，最终导致游戏失败。当然，游戏中也有很多选择可以用来帮助玩家回想起发生过的事情，例如展示遇到过敌人的轨迹，或者在玩家之前的游戏过程中角色死亡次数比较多的地方设置警示点。

但有人担心这样做会让屏幕变得混乱，或者让玩家容易重复之前的行为而不去思考新的方式，降低了游戏的趣味性。为了解决这个问题，我们发现利用时间轴复用功能进行提示似乎是个不错的选择。因为每次游戏失败之后，在玩家点击“重新开始”按钮后，以相反的方向显示之前的游戏经历，如下图所示：


![](http://upload-images.jianshu.io/upload_images/17266280-95c8da7ee1a5ea26.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

_从失败那一刻开始，呈现最有可能导致失败的片段_

但若要有一个完美的解决方案，应该还要知道之前发生了什么事情，记录下来作为回放。

# 实现方法

事实上，反向回放要做的工作几乎都在上一篇为关卡设置时间轴时就完成了。而下面将要讲述的方法，虽然可能这不是最优的解决方案，但是这种做法十分简单。

虽然用之前已经实现的后退操作就能完成敌人和水晶的运动。但是关卡中的其它事件是由玩家或者玩家动作触发的。对于这种情况，需要为TimeManager添加新的接口：

```
public delegate void ReversingTimeActionDelegate();
public class TimeManager
{
    class ReversingActionWithTime
    {
        public float Time { get; set; }
        public ReversingTimeActionDelegate ActionToCarryOut { get; set; }
    }
    public void RememberAction(ReversingTimeActionDelegate action)
 }
```

我们引入了ReversingActionWithTime这个类来记录动作的时间以及一个函数，它可以执行反向动作，这个逻辑与编程中的命令模式相似，但它是通过与时间绑定而不是点击ctrl+Z或其他类似的组合键来触发执行的。当关卡运行且动作发生时，只需要把RememberAction反向函数添加到这一时刻，如果想让时间倒退就可以调用这个函数。

例如当有敌人碰到屏障且消失时，就添加这个函数。在之后点击重新开始后，就可以回放到这一时间点了。
这个函数会自动用于再次激活敌人的TimeManager调用，使敌人出现在屏幕上：

```
public class Enemy
{
    void onCollisionWithBarrier()
    {
        timeManager.RememberAction(Activate);
        Deactivate();
    }

    void Activate()
    {
        // 进行激活相关的操作
    }
    //.. 剩下的实现
}
```

在时间倒退模式中，我们并不关心碰撞，因为这些碰撞已经在游戏正常运行的时候发生了。只需要倒退游戏状态以更快的速度跳过一些帧即可，
这里不需要太强大的设备，因为倒退可以按照正常速度的20倍进行，并且关卡倒退完成就相当于重置所有对象的位置。



但是在某些情况下，也需要将一些变量的值存储在函数中。例如下图中黄色的搬运者敌人，一种在被消灭后会产生细小敌人的角色，它的确切运动需要记录下来，是因为生成的小敌人的运动轨迹会有1秒或2秒的随机延迟。


![](http://upload-images.jianshu.io/upload_images/17266280-3af11a7f940de8e2.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

# 视觉反馈

为了让玩家更好地注意到时间倒退的发生，要添加一些视觉反馈功能。玩家非常喜欢游戏中时间倒退的部分，特别是引入像移动水晶或搬运者这些高端的东西的时候。时间倒退不仅是一个视觉体验，而且还能让玩家再回顾一次如何败给之前的敌人。这可以给玩家在游戏开始前留一些缓冲时间，可以减少一些挫败感。

  

当玩家成功地通关之后，我们大概都会做相似的事情。比如把界面切换到游戏地图，而不仅仅是打开下一关卡，播放不同类型的动画并且有专门的地方让玩家查看进度。

  

![](http://upload-images.jianshu.io/upload_images/17266280-26cf5128bea95b78.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

例如在上图中，我们把红色的敌人高亮了，因为这是玩家需要看到的最重要的东西，同时，这样还会得到一个很好的视觉效果。我们还添加了时间倒退小图标，虽然最开始我们尝试过类似VHS的时间倒退效果，但这不符合我们的视觉风格。这个简单的效果只需使用灰度就能实现，但要让值大于0.7的红色像素保持不变。

另外，如果想要将这个效果应用到相机而非单独的物体中，我们可以将着色器赋给某个材质，并将下面脚本绑定到相机中：

```
using UnityEngine;
public class BasicPostEffect : MonoBehaviour
{

    [SerializeField]
    Material mat;

    void OnRenderImage(RenderTexture src, RenderTexture dst)
    {
        Graphics.Blit(src, dst, mat);
    }
}
```

接着，将新材质赋给相机对应的字段。有趣的事情是添加了这个效果之后，玩家最终可以直观的知道发生了什么事情，并且不再点击屏幕创建屏障了。同样有趣的是，有部分玩家观察到有一个倒退回放只会在十次重新开始后出现，但对这个回放丝毫没有印象。

基于上述的讨论，我们还添加了双击屏幕任何地方就能跳过倒退回放的功能，双击屏幕也算是玩家想跳过的时候最常见的反应了。

# 延伸思考

这篇教程还可以举一反三，尝试一些其它用法。例如在游戏中，玩家失败后就及时提供指示信息，然后倒退一点时间并让玩家再次挑战。在我们看来，这比让整个关卡重新开始，或在玩家要行动的时候停下来提示的做法要好。还可以倒退回玩家连续多次失败的关节点。

# 总结

希望您能轻松上手这个功能，实现时间倒退的效果。在下一篇文章中，我们会关注利用了时间轴的游戏设计，了解如何解决一些常见的问题并提升游戏质量。

