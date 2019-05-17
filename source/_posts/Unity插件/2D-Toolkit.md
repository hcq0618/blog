---
title: 2D-Toolkit
thumbnail: http://upload-images.jianshu.io/upload_images/17266280-9f774a895d945669.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240
categories: Unity插件
tags: [Unity插件]
---

2D Toolkit插件在2D中的地位，犹如UI中NGUI对Unity
GUI一样：虽然官方原生的2D还不错，但这是最近1年新版本才有的功能，2年前Unity 2D的王道还是得用插件的，故《2D
Toolkit》就成了目前商业不错的选择。

在上周刚开始看的时候，就给自己提了3个问题 (1周后，自己给自己尝试做了回答)：

 **2D Toolkit是类似NGUI的东西吗？**

答：是的，类似NGUI；2D toolkit是第三方插件，广泛用于2D的游戏开发；其还包括了UI，可不用NGUI就能进行不错的UI开发。

 **对比Unity Native 2D，2D Toolkit是否优势已经丧失；或者是类似UGUI和NGUI关系？**

答：这个目前不得知。 粗浅的看，Unity Native 2D比较简单，开发起来便捷，毕竟和Unity无缝集成的，且原生，另外还省钱；但是2D
Toolkit都演变到2.5.2版本了，商用应该比较成熟，如其tk2dCamera简直无敌了–能自适应各种屏幕、大大节约了编码。

 **2D Toolkit能够和Unity Native 2D同存否？**

答：目前不知道。应该可以吧，2D toolkit已经于2015.5.24 发布2.5.2版本，声明支持Unity 5了。

2D ToolKit简历

2D ToolKit是第三方2D插件，能处理图集打包(Atlas Package)、精灵渲染(Sprite)、2D动画(Sprite
Animator)、2D UI，目前中文资料少得可怜。

2D
Toolkit简称为TK2D，其功能据说是2D下最强大的，assetstore的下载点评竟然超过1200个，这个数据非常惊人，要知道售价价格要75美金呢。其插件提供了C#代码，源码之内，了无秘密。

TK2D的厂家是Unikron Software
Ltd，官方网站为[http://unikronsoftware.com](http://unikronsoftware.com/)

TK2D在assetstore的”编辑器扩充/2D与图片管理”分类下，[排名第一](https://www.assetstore.unity3d.com/cn/#!/category/142/sortby/popularity)。

  

![](http://upload-images.jianshu.io/upload_images/17266280-9f774a895d945669.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

我摘录了部分官方官网assetStore点评：

low draw calls

pixel perfect camera：Unity 4.6 pro sprite package

get a response with 24 hours

manages multiple resolutions of sprite images (1x, 2x, 4x)

Very nice package

greatly sped up my animating process.

really streamlined my workflow.

organise all your sprites how you like in collections.

It’s fast at updating and rendering too.– opitimization

The best support、comunity

other：spline、NGUI

其点评大多集中在以下几个方便

降低了DC

正版的售后服务好

图集打包很爽

2D下效率高

正文开始–本文就官方教程《[Whack a
Mole](http://unikronsoftware.com/2dtoolkit/docs/2.4/tutorial/whack_a_mole/index.html)》进行小结：

注：因为官方问答截图、文字描写清楚，我这里为节约大家时间，不会写的很细，请先预览一下官方教程。

官方提供的Whack a Mole
材质[下载地址](http://www.2dtoolkit.com/docs_extras/wam_tutorial21/whackamole_assets_part1.zip)

步骤1：了解官方文档对TK2D做的系统概括：

Tk2D在编辑期间生成脚本–Assets目录

Tk2D运行脚本生成对象–场景

  

![](http://upload-images.jianshu.io/upload_images/17266280-fcca5d8d2408a45d.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

上面这张图包含了TK2D的7个知识点 (术语) 的6个（除了Tilemaps外）

Sprite Collections: 精灵(2D下的图片)集合，用于组织图片，一般同z轴值的放在一起，效率高。

Sprites：精灵，任何需要在Scene显示的均需要精灵组件，目前包含4种Sprite

  

![](http://upload-images.jianshu.io/upload_images/17266280-706cb971c52e1521.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

Static Sprite Batcher：静态化精灵–不参与碰撞的，可明显减少DC

Sprite Animations：动画精灵

Fonts：字体

Text Meshes:显示文本

Tilemaps

步骤2：tk2d camera 自动布局的摄像机 删除新建Unity 2D工程的Main Camera，添加tk2dCamera，并设置tag为“Main
Camera”。

  

![](http://upload-images.jianshu.io/upload_images/17266280-ddfddc16cc2465f5.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

修改tk2dCamera参数如下：

  

![](http://upload-images.jianshu.io/upload_images/17266280-bdf2aeba64cb93aa.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

Native Resolution ：1024*768

Projection：Orthographic

Type：Pixels Per Meter

Pixels Per Meter：1

Origin：Bottom Left

pixel per meter – so 100×100 world units = 100×100 pixels from the bottom left

tk2dCamera实际上是对Unity的Camera进行了扩展，
[这里](http://unikronsoftware.com/2dtoolkit/docs/2.4/tutorial/choosing_camera.html)有详细的对比说明和tip技巧。

步骤3：精灵集合(Sprite Collections)、精灵(Sprite )、静态精灵批处理(Static Sprite Batcher)
要使用图片，则需要首先添加Sprite Collections，它有3个作用：

1 把图片组织管理起来–如果你有上百个图片就会发现它的价值。

2 同z轴的组织起来，方便Unity引擎优化降低DC

3 自动进行图集打包–减少图片占用空间 为什么要用Sprite Collection？ 我认为比Unity Native
2D的默认能生成精灵而言，多了2个步骤。

要添加精灵，需要先Check out–如我这里使用Perforce源码管理。

  

![](http://upload-images.jianshu.io/upload_images/17266280-56daa4592ecdef1f.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

添加精灵很简单，选择、拖放即可：

针对当前Sprite Collection，进行Settings，然后一定要记得Commit：

  

![](http://upload-images.jianshu.io/upload_images/17266280-93cf6f7faf434675.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

注意：这里的Size和Pixels Per Meter，需要和上面的tk2DCamera保障一致。
Settings最下面有Platforms的设置，这个我没有看明白：

  

![](http://upload-images.jianshu.io/upload_images/17266280-71d5d557a25f7d51.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

网上搜了一段代码，好像是为了适应不同屏幕的全局设置：

  

![](http://upload-images.jianshu.io/upload_images/17266280-49accf5156fe0705.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

点击Commit后，就生成1了文件夹，包含3个文件：*.prefab 、*.png、*.mat。

  

![](http://upload-images.jianshu.io/upload_images/17266280-959ab98c668701f8.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

使用Sprite就简单多了，添加Tk2D Sprite对象或者添加TK2D Sprite组件，选择Collection和Sprite即可：
如果有n个Sprite，需要组织管理起来，默认会想到空的对象(EGO), 如果不参与碰撞等动态监测，可使用Static Sprite Batcher。
选择需要静态化的Sprite，拖放为Batcher的子物体，在Inspator视图点击Commit，即可完成处理。 有2点  **神奇** 之处：

1 原来n个Sprite变为1个了，即仅仅是Static Sprite Batcher可见，其子物体消失了(点击Edit即可编辑)

2 明显的减少了DC。

  

![](http://upload-images.jianshu.io/upload_images/17266280-2abc8a1e42aa4268.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

  

![](http://upload-images.jianshu.io/upload_images/17266280-126d0f1fa320777f.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

步骤4： 代码实现 Clipped Sprite

Clipped Sprite是Sprite的一种，可动态实现隐藏、可见。

  

![](http://upload-images.jianshu.io/upload_images/17266280-fef5e35d3d4037a3.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

通过动态设置Clipped Sprite的ClipRect的y值（y值范围0.0~1.0f之间）
同时调整其localPostion的y轴，可模拟图片的隐藏、显示效果。 另外，这个思想也挺有趣的，使用n个return
null代替waitforSecond.

> private IEnumerator WaitForHit()

>

> {

>

> float time = 0.0f;

>

> while (!whacked && time < timeLimit)

>

> {

>

> time += Time.deltaTime;

>

> yield return null;

>

> }

>

> }

步骤5：精灵动画（Sprite Animation）

Sprite Animation也是基于Sprite Collection的。

显示动画，需要用Sprite With Animator组件，下面这张图一览无余：

[本文的整理到这里就结束了，完整的请参阅官方教程–《](http://www.xifarm.com/wp-
content/uploads/2015/05/image52.png)[Whack a
Mole](http://unikronsoftware.com/2dtoolkit/docs/2.4/tutorial/whack_a_mole/index.html)》

注，本文使用的开发环境：

Unity 4.6.3

2D toolkit 2.4.0

转载请注明转自《 [C#程序员整理的Unity 3D笔记（二十）：2D Toolkit之官方教程《Whack a
Mole》](http://www.xifarm.com/tk2d_whackamole/)》

