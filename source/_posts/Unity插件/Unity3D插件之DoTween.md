---
title: Unity3D插件之DoTween
thumbnail: http://upload-images.jianshu.io/upload_images/17266280-0db62e43f50ac06f.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240
categories: Unity插件
tags: [Unity插件]
---

官方下载地址：http://dotween.demigiant.com/download.php

1、把下载到压缩包中的DOTween文件夹拷贝到项目文件中

2、安装DOTween：菜单栏——》Tools——》DOTween Unility Panel——》Setup DOTween...

  

![](http://upload-images.jianshu.io/upload_images/17266280-0db62e43f50ac06f.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

# 配置DOTween（全局配置）

  

![](http://upload-images.jianshu.io/upload_images/17266280-0816bf75493f442e.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

全局参数说明：

Safe Mode：勾选时，间补动画平滑度会稍稍下降，但可以防止出现目标体被销毁，tween还在运行的情况

Editor Report：勾选时，当DOTween运行结束后会输出一份运行情况报告

Log Behaviour：调试日志输出类型，ErrorsOnly、Verbose（详细的）、Default

Settings Location：菜单文件存放目录

Recyle Tweens：勾选时，间补动画不会被销毁，会缓存到对象池中，等待启用；（建议不勾选）

AutoPlay：运行时自动播放类型，None/Auto play Sequence（自动播放Sequence）/Auto play
Tweener（自动播放Tweener）/All

Update Type：动画每帧更新类型，正常Normal，固定帧更新Fixed，晚于正常帧更新Late

TimeScale Independent：独立Tween时间缩放控制

Ease：动画缓动类型（linear（线性的）；OutQuad（前快后慢）...具体参考：http://easings.net/zh-cn）

Ease Overshot：后偏移缓动值

Ease Period：前偏移缓动值

AutoKill：是否自动释放内存，后面需要重新启用的可以单独设置.SetAutoKill(false)

Loop Type：循环类型，Restart（重新启动），Yoyo（来回循环），Incremental（增量循环）

因为NGUI中已经有UITween了，可是UGUI中是没有这样的Tween的。我看过UGUI的Demo它的实现方式是用Animator来做的，这样每一个需要移动的对象就要挂上一个AmimationController并且还要去编辑动画。。
想想都恐怖，我觉得真没必要那么做。。

我强烈建议新项目使用DoTween。<http://dotween.demigiant.com/网址要翻墙，不然打不开。不要紧后面我把下载地址提供出来。
（目前DoTween还是测试版本）DoTween的文档写的非常详细，所以我就简单的只写两句代码，为大家抛砖引玉一下即可。

不得不说的是，因为在做游戏暂停的时候通常会使用Time.Scale ＝ 0 ，可是暂停的时候UI如果需要继续有动画怎么办呢？在DoTween中只需要设置
tweener.SetUpdate(true); 即可。意思就是这个Tween是忽略TimeScale，如果不写的话 tweener.SetUpdate 是
false。

```
 using DG.Tweening; //不能少了这个命名空间。



 Start



 //让TimeScale = 0



 timeScale



 Image imagetransform"Image"GetComponentImage



 //调用DOmove方法来让图片移动



 Tweener tweenerimagerectTransformDOMoveVector3



 //设置这个Tween不受Time.scale影响



 tweenerSetUpdate



 //设置移动类型



 tweenerSetEaseLinear



 tweeneronCompletedelegate



 Debug"移动完毕事件"



 imagematerialDOFadeonCompletedelegate



 Debug"褪色完毕事件"
```

Tween的移动类型有很多种，比如匀速运动、加速运动、减速运动，等等。如果你拿捏不准你需要用什么移动类形式。

<http://www.robertpenner.com/easing/easing_demo.html你可以在这里预览一下那种移动类型更佳适合你。

最后是DoTween的类库，如果你没有翻墙就下载我的吧， 是最新的。 欢迎大家在留言处和我一起讨论，加油！Fighting!

<http://pan.baidu.com/s/1o6qiefC

官方文档链接：http://dotween.demigiant.com/documentation.php#globalSettings

普通版下载地址：http://dotween.demigiant.com/download.php

pro版下载地址：http://pan.baidu.com/s/1dEzTQkL

(pro版提供DOTween Animation和DOTween Path这两个组件，支持可视化编辑)

移动类型：http://robertpenner.com/easing/easing_demo.html

DOTween真的比iTween好很多：

1.编写方面更加人性化

2.效率高很多，其中有一点是因为iTween使用的是unity内置的SendMessage

DOTween一般的样子是这样滴：

```
using DG.Tweening;

transform.DOMoveX(45,
1).SetDelay(2).SetEase(Ease.OutQuad).OnComplete(MyCallback);
```

好了，正式开始！

一些名词：

 **Tweener** ：补间动画

 **Sequence** ：相当于一个Tweener的链表，可以通过执行一个Sequence来执行一串Tweener

 **Tween：** Tweener + Sequence

 **Nested tween** ：Sequence中的一个Tweener称为一个Nested tween

主要的方法(就是最常用的)：

1.以开头的方法：就是的方法。例如：transform.DOMoveX(,)

2.以 **Set** 开头的方法：设置补间动画的一些。例如：myTween.SetLoops(, LoopType.Yoyo)

3.以开头的方法：补间动画的 **回调** 方法。例如：myTween.OnStart(myStartFunction)

DOTween初始化与全局设置：

当你第一次创建一个Tween时，DOTween就会自动初始化(只初始化一次)，使用缺省值。

当然，也可以使用DOTween.Init方法进行自定义，但要在第一次创建一个Tween前。所有创建的Tween都会受DOTween.Init方法的影响。

但之后，你也可以通过DOTween类的一些静态方法或者变量来修改全局设置：

 ```
static LogBehaviour DOTween.logBehaviour



 static DOTween.showUnityEditorReport



 staticfloat DOTween.timeScale



 static DOTween.useSafeMode



 static DOTween.SetTweensCapacity( maxTweeners,  maxSequences)



 static DOTween.defaultAutoKill



 static AutoPlay DOTween.defaultAutoPlay



 staticfloat DOTween.defaultEaseOvershootOrAmplitude



 staticfloat DOTween.defaultEasePeriod



 static Ease DOTween.defaultEaseType



 static LoopType DOTween.defaultLoopType



 static DOTween.defaultRecyclable



 static DOTween.defaultTimeScaleIndependent



 static UpdateType DOTween.defaultUpdateType



 static DOTween.Init(bool recycleAllByDefault = false, bool useSafeMode =
true, LogBehaviour logBehaviour = LogBehaviour.ErrorsOnly)
```

recycleAllByDefault ：如果为true，则当Tween完成时就会被回收，放到一个池中；否则就会被destroy

useSafeMode ：效率会稍微降低，但更安全

logBehaviour ：默认值为只打印错误信息

创建Tweener(有三种方法)：

 static DOTween.To(getter, setter, to, float duration)

以DOTween.To(() = myVector, x = myVector = x,  Vector3(3, 4, 8),
1);为例，就是对myVector进行插值，目标值为Vector3(3, 4, 8)

 ```
transform.DOMove( Vector3(2,3,4), 1);



 rigidbody.DOMove( Vector3(2,3,4), 1);



 material.DOColor(Color.green, 1);
```

对于unity内置的一些组件，都可以通过".+DO开头的方法"的方式创建补间动画

以transform.DOMove(new Vector3(2,3,4), 1)为例，new
Vector3(2,3,4)是最终值，意思是用一秒的时间运动到Vector3(2,3,4)

而transform.DOMove(new Vector3(2, 3, 4), 1) **.From()**
，就是从Vector3(2,3,4)运动到当前位置

 ```
static DOTween.Punch(getter, setter, Vector3 direction, float duration,
vibrato, float elasticity)



 static DOTween.Shake(getter, setter, float duration, float/Vector3 strength,
vibrato, float randomness,  ignoreZAxis)



 static DOTween.ToAlpha(getter, setter, float duration)



 static DOTween.ToArray(getter, setter, float duration)



 static DOTween.ToAxis(getter, setter, float duration, AxisConstraint axis)



 static DOTween.To(setter, float startValue, float endValue, float duration)
```

创建Sequence：

Sequence可以包含Sequence，当执行一个Sequence时会 **顺序执行Tweener** ，可以使用Insert方法实现同时执行。

Sequence的方法：

 ```
static DOTween.Sequence()



 Append(Tween tween)



 AppendCallback(TweenCallback callback)



 AppendInterval(float interval)



 Insert(float atPosition, Tween tween)



 InsertCallback(float atPosition, TweenCallback callback)



 Join(Tween tween)



 Prepend(Tween tween)



 PrependCallback(TweenCallback callback)



 PrependInterval(float interval)



 // Grab a free Sequence to use



 Sequence mySequence = DOTween.Sequence();



 // Add a movement tween at the beginning



 mySequence.Append(transform.DOMoveX(1, 1));



 // Add a rotation tween as soon as the previous one is finished



 mySequence.Append(transform.DORotate( Vector3(0, 180, 0), 1));



 // Delay the whole Sequence by 1 second



 mySequence.PrependInterval(1);



 // Insert a scale tween for the whole duration of the Sequence



 mySequence.Insert(0, transform.DOScale( Vector3(3, 3, 3),
mySequence.Duration()));
```

等同于：

 ```
Sequence mySequence = DOTween.Sequence();



 mySequence.Append(transform.DOMoveX(45, 1))



           .Append(transform.DORotate( Vector3(0, 180, 0), 1))



           .PrependInterval(1)



           .Insert(0, transform.DOScale( Vector3(3, 3, 3),
mySequence.Duration()));
```

上面我们提到了全局设置，这里我们再说一说针对Tweener和Sequence的局部设置

 ```
float timeScale



 SetAs(Tween tween \ TweenParams tweenParams)



 SetAutoKill( autoKillOnCompletion =



 SetEase(Ease easeType \ AnimationCurve animCurve \ EaseFunction customEase)



 SetId(object



 SetLoops( loops, LoopType loopType = LoopType.Restart)



 SetRecyclable( recyclable)



 SetUpdate(UpdateType updateType,  isIndependentUpdate = false
```

注意的一点是SetUpdate方法可以让目标忽略timeScale

回调方法：

 ```
OnComplete(TweenCallback callback)



 OnKill(TweenCallback callback)



 OnPlay(TweenCallback callback)



 OnPause(TweenCallback callback)



 OnRewind(TweenCallback callback)



 OnStart(TweenCallback callback)



 OnStepComplete(TweenCallback callback)



 OnUpdate(TweenCallback callback)



 OnWaypointChange(TweenCallback< callback)
```

还有一些针对部分Tweener的特殊的局部设置：

 **注意SetOptions方法必须紧跟Tweener** ，就好像这样：

```
DOTween.To(()= myVector, x= myVector = x, new Vector3(2,2,2),
1).SetOptions(AxisConstraint.Y, true);
```

TweenParams：

就是可以将一些参数应用到多个Tweener中

 ```
// Store settings for an infinite looping tween with elastic ease



 TweenParams tParms =  TweenParams().SetLoops(-1).SetEase(Ease.OutElastic);



 // Apply them to a couple of tweens



 transformA.DOMoveX(15, 1).SetAs(tParms);



 transformB.DOMoveY(10, 1).SetAs(tParms);
```

操作Tweener(有三种方法)：

1.DOTween静态方法

 ```
// Pauses all tweens



 DOTween.PauseAll();



 // Pauses all tweens that have "badoom" as an id



 DOTween.Pause("badoom"



 // Pauses all tweens that have someTransform as a target



 DOTween.Pause(someTransform);
```

2.Tweener方法

```
 myTween.Pause();
```

3.部件.+以DO开头的方法

 ```
transform.DOPause();
```

以上的是Pause方法，以下的是其余的操作方法。上面三种方式中，DOTween和Tweener都有以下的操作方法，而部件的话，要在前面加上"DO"。

 ```
CompleteAll/Complete()



 FlipAll/Flip()



 GotoAll/Goto(float andPlay = false



 KillAll/Kill( complete =



 PauseAll/Pause()



 PlayAll/Play()



 PlayBackwardsAll/PlayBackwards()



 PlayForwardAll/PlayForward()



 RestartAll/Restart( includeDelay =



 RewindAll/Rewind( includeDelay =



 TogglePauseAll/TogglePause()




//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////



 using UnityEngine;



 using System.Collections;



 using DG.Tweening;



 publicclass Test : MonoBehaviour {



     public RectTransform rt;



     private isIn = false



     // Use this for initialization



      Start ()



         //修改的是世界坐标



         //Tweener t = rt.DOMove(Vector3.zero, 0.3f);



         //修改的是局部坐标



         Tweener t = rt.DOLocalMove(Vector3.zero, 0.3f);



         //默认动画播放完成会自动销毁



         t.SetAutoKill(false



         t.Pause();



     public OnClick ()



          (!isIn)



             //将开始该物体的所有Tweener



             rt.DOPlayForward();



             rt.DOPlayBackwards();



         isIn = !isIn;

```
  

![](http://upload-images.jianshu.io/upload_images/17266280-abb38803f8fd7152.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

 ```
using UnityEngine;



 using System.Collections;



 using DG.Tweening;



 using UnityEngine.UI;



 publicclass Test2 : MonoBehaviour {



     public Transform t;



     public Text text;



     // Use this for initialization



      Start ()



         //Vector3.zero是绝对位置，表示从Vector3.zero移动到当前位置



         //t.DOMove(Vector3.zero, 2).From();



         //默认为false



         //Vector3.forward是相对位置，表示从Vector3.forward加当前位置移动到当前位置



         t.DOMove(Vector3.forward, 2).From(



         //逐字显示



         text.DOText("宏哥宏哥宏哥宏哥宏哥宏哥宏哥宏哥宏哥宏哥宏哥宏哥宏哥宏哥宏哥宏哥”

  
```

![](http://upload-images.jianshu.io/upload_images/17266280-751b6c01a5d10c26.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

1.如何对变量进行动画（dotween控制的变量改变动画）

```
//对变量做一个动画（通过差值的方式去修改一个值得变化）

//当前值   把修改的值（当前值到目标值的差值）赋值给myVvalue（unity计算好的）   目标值   变化时间

//前两个参数（委托类型的变量）实为两个方法

 DOTween.To(()=myValue,x=myValue=x,new Vector3(10,10,10),2);



 DOTween.To(()=myValue2,x=myValue2=x,10,2);
```

2.控制cube和UI面板的动画（应用到实际物体上）

 ```
public RectTransform taskPanelTransform;



 //taskPanelTransform.position=myValue;//世界坐标



 taskPanelTransform.localPosition=myValue;
```

3.动画的快捷播放方式DOMove，动画的前放和倒放

```
////播放它时有一返回值Ttweener,Tweener对象保存这个动画的信息，每次调用都会创建一个tweener对象，这个对象是dotween来管理

 //Tweener tweener=taskPanelTransfrom.DOLocalMove (new Vector3 (0, 0, 0),
0.5f);//播放此动画时会创建一个动画，默认播放完成后即销毁，所以回放无效



 //tweener.SetAutoKill(false);//使动画不被销毁.但造成的后果是每次都会创建耗费性能.解决方法，将其放入start方法中



 taskPanelTransfrom.DOPlay();//只会播放一次



 taskPanelTransfrom.DOPlayForward();//与下方的成对.播放对象身上所有动画



 taskPanelTransfrom.DOPlayBackwards ();



 tweener.Pause();//为使初始不播放动画，暂停动画
```

4.From Tweens

 ```
//cubeTransform.DOLocalMoveX(5, 1);



 //cubeTransform.DOLocalMoveX(5, 1).From();



 //默认是从当前位置运行到目标位置，加上from方法后表示从目标位置移动到当前位置。from可被所有动画使用



 cubeTransform.DOLocalMoveX(5,
3).From(true);//默认为false。加上true后为相对坐标（相当于从当前坐标加上5运行到当前位置）
```

5.动画的属性设置（动画曲线和事件函数）

6.动画的生命周期和生命周期函数

 ```
Tweener tweener = this.transform.DOLocalMoveX (0, 3);



 //tweener.SetEase (Ease.InBack);//先远离目标位置再快速的到达目标位置



 //tweener.SetEase(Ease.InBounce);



 //tweener.SetEase(Ease.OutBounce);



 //tweener.SetLoops(2);//循环播放的次数



 tweener.OnComplete(OnTweenComplete);//动画播放完成后调用什么事件



 void OnTweenComplete()



 Debug.Log ("动画播放完成后”);
```

7.对话框文字动画，屏幕震动效果

 ```
text.DOText("设计模式 设计模式 设计模式",2,true);//内容设置，时间，是否使用富文本



 //只是camera随机振动，最后还会回到原地



 //transform.DOShakePosition (1);//随机振动。时间  强度（0-1的值  或者  位置向量<震动向量）



 transform.DOShakePosition(1,new Vector3(3,3,0));
```

8.颜色和透明度动画

 ```
text.DOColor (Color.red, 2);//颜色渐变



 text.DOFade (1,3);//修改alpha值
```

9.DOTween官方网站

DO开头  开启动画

Set     设置属性

10.动画的组件可视化创建方式DOTweenAnimation

11.DOTweenPath路径编辑器

（1）Tween Options.Loops  -1 循环播放

（2）Path Tween Options.Path Type路径类型（折现，圆滑）

.Close Path起点终点相连

.Orientation朝向

（3）Path Editor Options.Relative相对的，勾选后路径相对于对象，随对象移动。单个节点移动无碍

.Handles Type路径节点图标类型

.Handles Mode指向下一个点的模式（3d or 2d）

（4）Button 点击事件控制动画的播放，DOTweenPath.DOTooglePause动画播放按钮（播放时点击可暂停，暂停时点击可播放）

