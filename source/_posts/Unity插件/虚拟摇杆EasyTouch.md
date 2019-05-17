---
title: 虚拟摇杆EasyTouch
thumbnail: http://upload-images.jianshu.io/upload_images/17266280-f9f6499d5185f13a.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240
categories: Unity插件
tags: [Unity插件]
---

对于移动平台上的RPG类的游戏，我们常用虚拟摇杆来控制人物角色的行走和一些行为，相信我们对它并不陌生，之前尝试了EasyTouch2.5，发现并没有最新版的3.1好用，2.5版本的对于自适应没有做的很好，而最新版的已经解决了这一问题。当然unity也自带了摇杆Joystick，用起来也简单，但存在不少局限，不会满足普通mmo游戏的需求，比如指定显示区域或者是更改一些素材等等，而这些EasyTouch插件都已经帮你实现，不得不佩服插件的原作者，能做出这么炫酷好用的插件，当然这估计是老外开发的，关于插件的下载，你可以在AssetStore上购买，当然也可以使用free版。

我这里也提供一个3.1版本的插件下载地址： <http://download.csdn.net/detail/s10141303/6962919

#  **一、效果图**

  

![](http://upload-images.jianshu.io/upload_images/17266280-f9f6499d5185f13a.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

  

![](http://upload-images.jianshu.io/upload_images/17266280-fbe8d10aa2e67ea8.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

感觉很酷有木有！接下来就看一下创建的过程吧！

# 二、操作步骤

## 1.官方文档上的步骤

Quick Start (C#)

1-Import EasyTouch Package.

2-Create an empty gameObject, and name it EasyTouch.(You can choose another
name)

Step 1 & 2 can be replace by the option menu

  

![](http://upload-images.jianshu.io/upload_images/17266280-7399514313146199.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

3-Add the EasyTouch.cs script on the EasyTouch gameObject that you just
created.

4-Select the EasyTouch gameobject, and verifies that Broadcast messages is set
to FALSE in the inspector.

  

![](http://upload-images.jianshu.io/upload_images/17266280-9dc3ee3597dd9b52.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

5-Create a new C# script MyFirstTouch

6-Add these methods

 ```
// Subscribe to events



 void OnEnable(){



 EasyTouch.On_TouchStart += On_TouchStart;



 }



 // Unsubscribe



 void OnDisable(){



 EasyTouch.On_TouchStart -= On_TouchStart;



 }



 // Unsubscribe



 void OnDestroy(){



 EasyTouch.On_TouchStart -= On_TouchStart;



 }



 // Touch start event



 public void On_TouchStart(Gesture gesture){



 Debug.Log( "Touch in " + gesture.position);



 }

```
7-Create an empty gameObject, and name it Receiver.

8- Add MyFirstTouch script to the gameObject Receiver.

9- Run it in editor, and click on the screen

## 2.翻译一下以上的步骤

1.import“EasyTouch”资源包

2.创建空物体，命名为EasyTouch(当然你也可以改成其他名字)

3.添加EasyTouch.cs脚本在刚刚创建的空物体（EasyTouch）上

4.选择改物体但不要将BroadcastMessages勾选

5.创建一个新的C#脚本，命名MyFirstTouch

6.添加这些方法

7.再创建一个空物体，命名为Receiver

8.将MyFirstTouch脚本添加到空物体Receiver上

9.运行并且点击遥感，会发现控制台打印了当前按下的坐标

## 3.根据官方的这些提示，自己来做一个属于自己的人物遥感控制

1.导入EasyTouch3资源包

2.做好前期准备，包括人物模型、地形的创建

3.添加JoyStick实例：Hedgehog Team-Easy Touch-Extensions-Add a new
Joystick。此时就会在左下角创建了虚拟遥感的实例。

4.设置遥感的相关参数

  

![](http://upload-images.jianshu.io/upload_images/17266280-d63f7a1741d0a440.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

.创建脚本MoveController.cs用来接收遥感事件控制角色的移动

 ```
using UnityEngine;



 using System.Collections;



 public class MoveController : MonoBehaviour {



     void OnEnable()



     {



         EasyJoystick.On_JoystickMove += OnJoystickMove;



         EasyJoystick.On_JoystickMoveEnd += OnJoystickMoveEnd;



     }



     //移动摇杆结束



     void OnJoystickMoveEnd(MovingJoystick move)



     {



         //停止时，角色恢复idle



         if (move.joystickName == "MoveJoystick")



         {



             animation.CrossFade("idle");



         }



     }



     //移动摇杆中



     void OnJoystickMove(MovingJoystick move)



     {



         if (move.joystickName != "MoveJoystick")



         {



             return;



         }



         //获取摇杆中心偏移的坐标



         float joyPositionX = move.joystickAxis.x;



         float joyPositionY = move.joystickAxis.y;



         if (joyPositionY != 0 || joyPositionX != 0)



         {



             //设置角色的朝向（朝向当前坐标+摇杆偏移量）



            transform.LookAt(new Vector3(transform.position.x + joyPositionX,
transform.position.y, transform.position.z + joyPositionY));



             //移动玩家的位置（按朝向位置移动）



             transform.Translate(Vector3.forward * Time.deltaTime * 5);



             //播放奔跑动画



             animation.CrossFade("run");



         }



     }



 }
```

几个函数的执行顺序：

  

![](http://upload-images.jianshu.io/upload_images/17266280-bc66eae1984685ef.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

6.效果图

  

![](http://upload-images.jianshu.io/upload_images/17266280-338cbbe5e1d99bf7.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

7.创建点击按钮

点击HedgehogTeam-EasyTouch-Extensions-Create a new Button,会在屏幕右下角创建一个button

  

![](http://upload-images.jianshu.io/upload_images/17266280-75d36b726eb6a798.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

如何让有下角的按钮点击能做出我们想要的效果呢？

  

![](http://upload-images.jianshu.io/upload_images/17266280-821fa06a97c0dbfe.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

jump方法：

  

![](http://upload-images.jianshu.io/upload_images/17266280-87d670465948f1b7.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

然后点击一下按钮，人物就会跳跃动作！

其他教程：

<http://blog.csdn.net/janeky/article/details/17364903

<http://www.newbieol.com/information/564.html

