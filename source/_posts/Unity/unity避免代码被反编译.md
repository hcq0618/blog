---
title: unity避免代码被反编译
thumbnail: http://upload-images.jianshu.io/upload_images/17266280-0f49f10a73b88cde.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240
categories: Unity
tags: [Unity]
---

我最近研究发现80%以上的Unity3D游戏都没有做代码混淆。而且我觉得反编译后的代码可阅读性更加好。今天把《锁链战记》的代码和资源都反编译出来了。

1.Unity编译后最终会将代码编译在dll里面，无论是ios还是Android解开包以后都可以拿到dll，路径在Data/Managed
/Assembly-CSharp.dll

2.IOS其实不用做代码混淆，应该是苹果帮我们做了，反编译以后只能看到变量名，和方法名，但是具体的方法体内的代码是万全看不到的，不过安卓不行！！！

3.所以如果要反编译某游戏的代码，一定要去找它的Android版本，然后解开包，拿出它的Assembly-CSharp.dl

4.在Windows上去下载.NET Reflector
8这个反编译dll的软件，网上一大堆，但是一定要下载最新版本。目前我没找到可以在MAC上反编译dll的软件，如果那位大神知道请一定要告诉我噢。

5.mac 上反编译，请看我的另一篇文章 [http://www.xuanyusong.com/archives/2675
](http://www.xuanyusong.com/archives/2675)

使用步骤

把Assembly-CSharp直接拖进去。

  

![](http://upload-images.jianshu.io/upload_images/17266280-0f49f10a73b88cde.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

所有的代码，类名，方法名，方法体，一清二楚。这代码，这缩进，嘿嘿。AssetbundleManager应该就是他们自己写的处理Assetbundle的下载管理类了。

  

![](http://upload-images.jianshu.io/upload_images/17266280-655f1bcb2f172fc7.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

如果有心的话你可以全局搜索一下”http”关键字 可能就能找到CDN或者Assetbundle的下载地址了。

如果避免自己的游戏被反编译

大家可以去搜索一下Codeguard这个插件，（网上可以找到破解版）它可以防止你的代码被反编译。它主要是改名，把你的方法名，方法体名子修改了，变量名修改了。虽然有点弱但是它的优点是比较方便，因为可以在打包的时候自动完成代码混淆的工作。不用自己去手工做混淆，我不知道有没有更好的自动混淆方法，如果那位大神知道请一定要告诉我。

另外，还有一个更高级的办法。直接找unity官方，它们有防止代码反编译的服务，绝对有效。还有一个方法 用Crypto Obfuscator for .Net
这东西可以完美混淆Unity for Android的代码，也支持打包APK 时批处理脚本完成混淆部分。但是MAC 上不支持，看了一大堆混淆.net
的方法，全部是基于windows上的。 有哪位大神知道怎么在mac上进行Andorid的混淆工作。。

作者：雨松MOMO

