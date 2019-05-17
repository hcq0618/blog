---
title: CanvasGroup
thumbnail: http://upload-images.jianshu.io/upload_images/17266280-58ebbef548fed048.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240
categories: Unity
tags: [Unity]
---

Canvas Group可以用来控制一组不需要个别控制的UI元素的某些方面，CanvasGroup的属性会影响他所有children的GameObject

  

![](http://upload-images.jianshu.io/upload_images/17266280-58ebbef548fed048.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

其中有四个选项：

-Alpha：这个选项很多组件都有，用处也是一样的，在美术中，这个叫做Alpha通道的东东是用来控制透明度的，他的值从0到1.0是完全透明，1是完全不透明；

-Interactable确认该组件是否接受输入，当他被设置为false时，交互功能将被禁用；

-Block Raycasts是否让该组件像collider一样接受射线检测？你需要在依赖于Canvas的图形射线检测者上唤醒射线检测方法。这个不会作用于Physics.Raycast;

-Ignore Parent Groups(忽略父级团)是否响应父级group的方法

Canvas Group的经典使用：

-在窗口的GameObject上添加一个CanvasGroup，通过控制它的Alpha值来淡入或淡出整个窗口；

-通过给父级GameObject添加一个CanvasGroup并设置它的Interactable值为false来制作一整套没有交互（灰色）的控制；

-通过将元素或元素的一个父级添加CanvasGroup并设置BlockRaycasts值为false来制作一个或多个不阻止鼠标事件的UI元素

 **应用：（重要的地方写大字）**

结合后面两点或者1,3点，都可以实现很牛叉的功能

比如说游戏里某些情况某个按钮（或者其他UI）是不能点的，而另外一些情况可以点，这样就可以通过动态改变这个组件的BlocksRaycasts值以及Interactable来实现

再比如说游戏里点击某个按钮要让这个按钮不可点并逐渐消失掉，当然啦，也可以让别的东西消失啦，这就可以通过改变alpha值来实现

恩，CanvasGroup这个组件已经被我玩坏啦~。~

至此，canvas的四个组件（Canvas、Canvas Render、Canvas Scaler、Canvas
Group）都学完了，勃主的装逼之路越走越远了哈！

抽空再补上例子。。。

