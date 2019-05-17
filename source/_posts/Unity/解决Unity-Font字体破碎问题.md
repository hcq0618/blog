---
title: 解决Unity-Font字体破碎问题
thumbnail: 
categories: Unity
tags: [Unity]
---

 使用Unity的动态字体绘制文字的时候，在多次打开面板时出现文字破裂问题。

文字渲染原理：

通过RequestCharactersInTexture函数向Font请求更新文字信息，然后使用GetCharacterInfo获取文字信息来渲染。在调用GetCharacterInfo的时候要保证所有文字都通过RequestCharactersInTexture请求过了，这样文字才能顺利的被渲染出来。
如果请求的时候，Font内部维护的texture不够用了，就会触发textureRebuildCallback的回调，通知外部使用Font的对象，其内部的texture被更新了，外部应该重新刷新。而这个重新刷新的过程就往往会导致界面上的文字破裂，因为外部的Texture重新计算并调整大小，其上面原来的文本信息就会被破坏。

解决方法：

在启动游戏时通过预加载的方法改变Font内部维护的Textrue的大小，让其有足够的空间容纳外部请求的文本信息。

我的方法是
在网上下载一个常用汉字3500字的txt文档，将它导入到项目中，然后再启动游戏后首先使用这个文本向Font请求信息，这样便会在一开始就将Font内部的Texture设置的较大。

> public static string generalCharacter = null;

>

> public static void PreLoadGeneralText()

>

>         {

>

>             if (generalCharacter == null)

>

>             {

>

>                 TextAsset txt = LoadResource("Base/Font/generalText") as
TextAsset;

>

>                 generalCharacter = txt.ToString();

>

>             }

>

>             Font font = GetDefaultFont().dynamicFont;

>

>             font.RequestCharactersInTexture(generalCharacter);

>

>         }

其中LoadResource方法是封装的一个加载方法， 这里可以替换成 Resources.Load;

GetDefaultFont()方法是加载我项目中使用的默认字体

