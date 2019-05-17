---
title: FingerGestures
thumbnail: http://upload-images.jianshu.io/upload_images/17266280-15840cd3f641eccb.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240
categories: Unity插件
tags: [Unity插件]
---

FingerGestures是一款强大的手势识别插件，支持鼠标和触控。跨平台，最新的3.0版本支持自定义手势识别。

其中CustomGestures的识别还是挺准的。测试画个一笔五角星，能被容易的识别。

直接解压包，里面还有samples和对playerMaker拓展 2个子包。

# 二.导入Sample包

在搜索栏里输入 t:scene,  然后全选场景并拖入Build Setting里的Scenes in Build

把'Sample Browser'场景调整到第一个场景

也可在player setting里把屏幕设置为600x400

  

![](http://upload-images.jianshu.io/upload_images/17266280-15840cd3f641eccb.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

# [三.基本识别
GestureRecognizers(检测用户输入并发送事件)](http://photo.blog.sina.com.cn/showpic.html#blogid=471132920101hlwt&url=http://s14.sinaimg.cn/orignal/47113292gd94359d9fddd)

场景里必须只有一个FingerGestures组件示例。它相当于Manager。

(1)直接新建GameObject起名Manager，并加FingerGestures脚本

(2)直接新建GameObject起名Gestures，并加TapRecognizer脚本

直接新建TapTutorial.cs 并放到Gestures上

Gestures里TapRecognizer面板下，点"Copy Event To Clipboard"
把对应代码拷贝到粘贴板上，并在TapTutorial脚本里粘贴代码。

当recognizer检测对应输入到后， 会在obj上发对应的SendMessage消息。但是SendMessage开销大
，可以自己实现开销更小的delegate-based events.

  

![](http://upload-images.jianshu.io/upload_images/17266280-9fbab1de22861328.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

(5)打输出debug信息的代码

 ```
using UnityEngine;



 using System.Collections;



 publicclass TapTutorial : MonoBehaviour



  OnTap(TapGesture gesture)



   Debug.Log( "Tap gesture detected at " + gesture.Position +



             ". It was sent by " + gesture.Recognizer.name );
```

识别单击物体

(1)创建球，确保有collider或者trigger,位置(0,1,0),缩放(4,4,4)

(2)Gesture物体上加  **ScreenRaycaster**

当Ray Thickness为0时  可以是collider或者trigger，

当Ray Thickness不为0时  必须是collider， 可以模拟厚手指的操作。

  

![](http://upload-images.jianshu.io/upload_images/17266280-717d287f0070d2c7.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

(2)  脚本变为

 ```
using UnityEngine;



 using System.Collections;



 public class TapTutorial : MonoBehaviour



 OnTap( TapGesture gesture )



     ( gesture.Selection )



         Debug.Log( "Tapped object: " + gesture.Selection.name );



         Debug.Log( "No object was tapped at " + gesture.Position );

```
之后就能检测到点击物体了，并且被点击的圆球同样的收到同名事件

识别2手指Tap3下

设置 Required Finger Count为2

设置 Required Taps为3

如果是电脑运行，用鼠标左右键同时按模拟

四.FingerEventDetector

检测单手指的按下 松开 经过 移动 静止，与GesturesRecognizers类似，发消息，用ScreenRaycaster与物体互动。

FingerEventDetector是抽象类，各种finger event detectors继承自它。

也可以提供finger index跟踪某指定手指。

(1)新场景，加FingerGestures管理

(2)新物体起名FingerEvent，并加FingerDownDetector

(3)新建脚本FingerEventTutor.cs, 并从FingerDownDetector拷贝粘贴脚本

 ```
using UnityEngine;



 using System.Collections;



 public class FingerEventTutor : MonoBehaviour



 OnFingerDown(FingerDownEvent e)



 Debug.Log( e.Finger + " Down at " + e.Position + " on object:" + e.Selection
);
```

点击运行，即可检测任何手指按下的事件。

每个手指事件都要添加对应的detector

  

![](http://upload-images.jianshu.io/upload_images/17266280-da96ac7817738bca.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

 ```
using UnityEngine;



 using System.Collections;



 public class FingerEventTutor : MonoBehaviour



 OnFingerDown(FingerDownEvent e)



 Debug.Log( e.Finger + " Down at " + e.Position + " on object:" + e.Selection
);



 OnFingerUp( FingerUpEvent e )



 // time the finger has been held down before being released



     float elapsedTime = e.TimeHeldDown;



 Debug.Log( e.Finger + " Up at " + e.Position + " on object:" + e.Selection
);

```
# 五.自定义手势识别

3.0后可以用PointCloudRecognizer来识别自定义手势。算法使用的是$P recognizer. 现在只支持single-
stroke(单手指单次画)，将会支持multi-strokes.

PointCloudRecognizer将会对比一些gesture模板并返回最接近的 匹配图形，并返回分数和距离值。

PointCloud
gestures手势，和缩放以及画的方向无关。但是图形的旋转必须是固定的，例如一个正着摆放的三角形你必须画正的，你画一个倒着摆放的三角形它是不能被识别的。

绘制PointCloud

(1)在Assets栏下，创建 PointCloud Gesture Template,起名MyPCGesture

(2)点击Edit,绘制图形，然后Apply

使用PointCloud

(1)新场景，加FingerGestures管理

(2)创建新的物体起名Gestures

Gestures加  **PointCloudRecognizer 组件。**

Max Match Distance 用户画的图形distance必须在该值之下， 设定得越小，画得就必须越精确。

Sampling Distance  两个连续手指位置的最小间距。越小表示越精确，但更多的采样

Gesture Template List  要去匹配的图形库

MyPCGesture加至 Gesture Template List

(5) 创建PointCloudTutorial.cs脚本并添加至Gestures物体下

```
 using UnityEngine;



 using System.Collections;



 public class PointCloudTutorial : MonoBehaviour



      OnCustomGesture( PointCloudGesture gesture )



         Debug.Log( "Recognized custom gesture: " +
gesture.RecognizedTemplate.name +



             ", match score: " + gesture.MatchScore +



             ", match distance: " + gesture.MatchDistance );
```

PointCloudGesture. RecognizedTemplate 对应画出的图形模板

PointCloudGesture. MatchScore 匹配百分比，1代表完美匹配

PointCloudGesture. MatchDistance 与图形有多接近

当然也可以从代码绘制PointCloudGestureTemplate

```
 Awake()



     PointCloudGestureTemplate triangle =
ScriptableObject.CreateInstance<PointCloudGestureTemplate();



     triangle.name = "Triangle Gesture Template"



     triangle.BeginPoints();



     triangle.AddPoint( , , );



     triangle.AddPoint( , , );



     triangle.AddPoint( , , );



     triangle.AddPoint( , , );



     triangle.EndPoints();



     PointCloudGestureTemplate square =
ScriptableObject.CreateInstance<PointCloudGestureTemplate();



     square.name = "Square Gesture Template"



     square.BeginPoints();



     square.AddPoint( , , );



     square.AddPoint( , , );



     square.AddPoint( , , );



     square.AddPoint( , , );



     square.AddPoint( , , );



     square.EndPoints();



     PointCloudRegognizer recognizer =
gameObject.AddComponent<PointCloudRegognizer();



     recognizer.AddTemplate( triangle );



     recognizer.AddTemplate( square );
```

AddPoint的第一个参数代表第几画，但是现在只支持一笔画出来的图形，所以该值只填0。当EndPoints()被调用的时候，所有点都会被单位化至(0,1)的范围。

