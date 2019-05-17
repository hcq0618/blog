---
title: 在Unity中实现小地图（Minimap）
thumbnail: http://upload-images.jianshu.io/upload_images/17266280-ec6f1999c85fce86.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240
categories: Unity
tags: [Unity]
---

# 小地图的基本概念

  

![](http://upload-images.jianshu.io/upload_images/17266280-ec6f1999c85fce86.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

众所周知，小地图（或雷达）是用于显示周围环境信息的。首先，小地图是以主角为中心的。其次，小地图上应该用图标来代替真实的人物模型，因为小地图通常很小，玩家可能无法看清真实的模型。

大多数小地图都是圆形的，所以本文也将创建圆形小地图。通常小地图周围还会有一些按钮和标签，本文也会介绍。

# 创建场景

新建场景，导入Unity Chan模型作为玩家，导入两个机器人作为敌人。

  

![](http://upload-images.jianshu.io/upload_images/17266280-6d769f4455cbd080.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

# 游戏视图

添加一个新的相机。依次点击菜单项GameObject -> Camera新建相机并命名为Minimap Camera。然后将该相机设为Unity
Chan的子对象，并将其坐标设为Unity Chan上方10个单位，把相机对准Unity Chan模型。

  

![](http://upload-images.jianshu.io/upload_images/17266280-75b26582fabb0924.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

# 设置Minimap Camera

为了达到更好的效果，将position设为(0, 10, 0)，rotation设为(90, 0, 0)。现在相机显示效果如下：

  

![](http://upload-images.jianshu.io/upload_images/17266280-4be3e33d1b0f27d7.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

但这还不是小地图。现在运行场景，你可以看到只有上图中的内容显示出来。我们必须把小地图做成一个UI元素。

# 渲染到UI层

这里需要用到Render Texture来实现。依次点击菜单项Assets -> Create -> Render Texture新建Render
Texture并命名为Minimap Render Texture。

  

![](http://upload-images.jianshu.io/upload_images/17266280-864f566e5c5af9b5.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

选中Minimap Camera后在检视面板将Target Texture字段设为Minimap Render Texture。

  

![](http://upload-images.jianshu.io/upload_images/17266280-279aa0dc04d82b23.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

现在运行场景会发现Minimap Camera中的内容不见了，这是因为它被显示到了新建的Render Texture中。

下面新建Canvas来添加UI元素。依次点击菜单项GameObject -> UI -> Canvas来新建Canvas。

  

![](http://upload-images.jianshu.io/upload_images/17266280-0ba8cfeaab714dfa.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

这里需要使用Raw Image在Canvas中显示Render Texture的内容。依次点击菜单项GameObject -> UI -> Raw
Image新建Raw Image，然后命名为Minimap Image，在检视面板中将Texture字段设为Minimap Render Texture。

  

![](http://upload-images.jianshu.io/upload_images/17266280-3435654af4af757f.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

现在Minimap Camera相机中的内容可以作为UI来显示了！

  

![](http://upload-images.jianshu.io/upload_images/17266280-cd3b2d7c72585244.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

下面将小地图变为圆形。这里需要用到一张简单的遮罩纹理：

  

![](http://upload-images.jianshu.io/upload_images/17266280-568fbb00966b7937.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

新建Image并为其添加Mask组件，将Image的Source Image字段设为上面的遮罩图片，并将Minimap Image设为Mask的子对象。

注意：为了达到更好的视觉效果，记得禁用遮罩纹理的Mipmap。

  

![](http://upload-images.jianshu.io/upload_images/17266280-aed332c254c5fd23.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

现在小地图显示效果如下：

  

![](http://upload-images.jianshu.io/upload_images/17266280-9304337bf6a53e0e.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

小地图的白色背景看起来不太美观，给它加一个边框：

  

![](http://upload-images.jianshu.io/upload_images/17266280-15b6f67134f06b2e.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

  

![](http://upload-images.jianshu.io/upload_images/17266280-16e6590df9d36fa8.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

为了让整个小地图移动起来更方便，新建一个空的GameObject命名为Minimap，并将所有对象设为Minimap子对象。

  

![](http://upload-images.jianshu.io/upload_images/17266280-dbad70d367fcc83e.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

最后将小地图移至屏幕右上角。

  

![](http://upload-images.jianshu.io/upload_images/17266280-153a6a121210c7f7.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

效果不错吧？但这还不是真正意义上的小地图，只是相机从顶部取景的图像而已。接下来通过Layer来做一些设置！

# 设置Layer

这里需要新建一个Layer。依次点击菜单项Edit -> Project Settings -> Tags and
Layers新建Layer命名为Minimap。

  

![](http://upload-images.jianshu.io/upload_images/17266280-f96f6a1a4c01bae2.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

然后新建三个球体。一个设为蓝色代表Unity Chan。将该球体设为Unity Chan的子对象，并将其Layer设为Minimap。

  

![](http://upload-images.jianshu.io/upload_images/17266280-dfdc8f16823fbf32.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

对两个机器人进行同样的操作，将球体改为红色。

  

![](http://upload-images.jianshu.io/upload_images/17266280-4b34ec3b3279e6aa.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

现在最关键的一步来了！选中Main Camera并确保其Culling Mask中不包括Minimap这一层。

  

![](http://upload-images.jianshu.io/upload_images/17266280-1eb8533ebe757f7d.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

然后选中Minimap Camera让其Culling Mask只包括Minimap这一层。

  

![](http://upload-images.jianshu.io/upload_images/17266280-e16613658b088db8.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

现在这个小地图看起来就比较完善了！

  

![](http://upload-images.jianshu.io/upload_images/17266280-694ef4f538aae2e1.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

# 最后步骤

还可以做一些调整。首先将Minimap Camera的Clear Flags设为Solid
Color并将其颜色改为浅灰色，以便让小地图背景与小球的对比度更强。

  

![](http://upload-images.jianshu.io/upload_images/17266280-45846eed67c63e6d.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

还可以添加一些UI元素来操作小地图。这里使用标签作为示例，最后结果如下：

  

![](http://upload-images.jianshu.io/upload_images/17266280-7aeb79400ddd9827.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

当角色或机器人移动时，小地图上的小球也会即时更新位置。

  

![](http://upload-images.jianshu.io/upload_images/17266280-f97d835fe2d7b272.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

到此整个制作小地图的教程就结束了，如有任何问题，欢迎来下方评论区留言！

本文来源于：http://blog.theknightsofunity.com   作者：Piotr Korzuszek

