---
title: Unity显示内嵌网页的研究
thumbnail: 
categories: Unity
tags: [Unity]
---

最近由于有需要在Unity程序运行在iOS或Android手机上显示内嵌网页。所以遍从网上搜集了一下相关的资料。整理如下：

 **UnityWebCore**

从搜索中先看到了这个，下载下来了以后发现这个的原理好像是通过调用浏览器内核，然后将网页渲染到mesh的方式完成的。但遗憾的是只支持windows桌面版本。但还是发出来大家如果有需要可以下载

下载地址： http://pan.baidu.com/s/1nt3FVkd

 **unity-webview**

这个是在github上找到的。是一个keijiro的日本人编写。

https://github.com/keijiro/unity-webview-integration

就是根据手机平台在手机上调用相应的WebView组件显示，比如IOS上就是调用UIWebView。同时自己定义了与JavaScript交互的格式，可以在unity的c#代码中相应javascript的调用。需要的朋友可以试试。需要在ios和android上才能看到效果。

根据keijiro编写的项目，在github上你还可以搜索到其他人fork后修改的项目，应该是进行了一些封装和修改，但都是基于keijiro的。

https://github.com/Kogarasi/Unity-Webview

https://github.com/gree/unity-webview

 **UniWebView**

这个是一个中国人编写的组件，也是根据手机平台调用相应的WebView上组件来显示，也可以支持和javascript的交互。工程很完善。在mac
os以及手机的系统上直接可以看到运行效果，并且效果很不错。推荐使用的，但是我就不能提供下载地址了。因为这个插件是收费的。为了支持作者还请大家自行购买。

 **另外还有pc上的插件Awesomium**

<http://www.awesomium.com/>

<http://labs.awesomium.com/unity3d-integration-tutorial-part-1/>

[http://www.ceeger.com/forum/read.php?tid=13526&page=1](http://www.ceeger.com/forum/read.php?tid=13526&page=1)

腾讯浏览内核

<http://x5.tencent.com/tbs/>

[百度 VR 浏览器](https://vr.baidu.com/)com.baidu.vrbrowser

基于[Google VR SDK for Unity](https://github.com/googlevr/gvr-unity-sdk/)开发

[libaudioplugingvrunity.so](http://libaudioplugingvrunity.so/)
[libgvrunity.so](http://libgvrunity.so/) md5 与 GoogleVR 中的文件一致

Java C# 均未混淆

网页使用[EasyWebviewTexture](https://www.assetstore.unity3d.com/cn/#!/content/29346)

目前[EasyWebviewTexture](https://www.assetstore.unity3d.com/cn/#!/content/29346)已经停止购买/下载

Java层使用 ijkPlayer;
Unity层使用[EasyMovieTexture](https://www.assetstore.unity3d.com/cn/#!/content/10032)

浏览器内核使用crosswalk

[三星 Gear VR 浏览器
com.sec.android.app.svrbrowser](http://git.devops.letv.com/LvrBrowser/VR-
Browser-Decompile#%E4%B8%89%E6%98%9F-gear-
vr-%E6%B5%8F%E8%A7%88%E5%99%A8-comsecandroidappsvrbrowser)

[基于 Unity 开发](http://git.devops.letv.com/LvrBrowser/VR-Browser-
Decompile#%E4%B8%89%E6%98%9F-gear-
vr-%E6%B5%8F%E8%A7%88%E5%99%A8-comsecandroidappsvrbrowser)

[Java C# 均未混淆](http://git.devops.letv.com/LvrBrowser/VR-Browser-
Decompile#%E4%B8%89%E6%98%9F-gear-
vr-%E6%B5%8F%E8%A7%88%E5%99%A8-comsecandroidappsvrbrowser)

[网页使用 ](http://git.devops.letv.com/LvrBrowser/VR-Browser-
Decompile#%E4%B8%89%E6%98%9F-gear-
vr-%E6%B5%8F%E8%A7%88%E5%99%A8-comsecandroidappsvrbrowser)[EasyWebviewTexture](https://www.assetstore.unity3d.com/cn/#!/content/29346)

浏览器内核使用Chromium

[大朋 VR 浏览器](http://git.devops.letv.com/LvrBrowser/VR-Browser-
Decompile#%E5%A4%A7%E6%9C%8B-vr-%E6%B5%8F%E8%A7%88%E5%99%A8)

[普通原生浏览器， 开启了强制横屏](http://git.devops.letv.com/LvrBrowser/VR-Browser-
Decompile#%E5%A4%A7%E6%9C%8B-vr-%E6%B5%8F%E8%A7%88%E5%99%A8)

[下载 ](http://git.devops.letv.com/LvrBrowser/VR-Browser-
Decompile#%E5%A4%A7%E6%9C%8B-
vr-%E6%B5%8F%E8%A7%88%E5%99%A8)[com.android.browser](http://git.devops.letv.com/liuwencai
/DeepoonVR-App/blob/master/com.android.browser.apk);
需要先[卸载系统的浏览器](http://android.stackexchange.com/a/96479)

[ **关于crosswalk**](http://git.devops.letv.com/LvrBrowser/VR-Browser-
Decompile#easywebviewtexture)

[基于chrome内核解析网页 可以兼容android4.0以下的系统
****](http://git.devops.letv.com/LvrBrowser/VR-Browser-
Decompile#easywebviewtexture)**<https://crosswalk-project.org/>**

Android4.4版本以下webView是基于webkit，4.4以上是基于chromium。国内浏览器都是基于chromium，除了遨游是基于webkit，而safari也是基于webkit。chromium其实也是基于webkit。

 **浏览器引擎分类**

浏览器的内核引擎，基本上是四分天下：

Trident: IE 以Trident 作为内核引擎;

Gecko: Firefox 是基于 Gecko 开发;

WebKit: Safari, Google Chrome,傲游3,猎豹浏览器,百度浏览器 opera浏览器 基于 Webkit 开发。

Presto: Opera的内核，但由于市场选择问题，主要应用在手机平台--Opera mini

注：2013年2月Opera宣布转向WebKit引擎

注：2013年4月Opera宣布放弃WEBKIT，跟随GOOGLE的新开发的[blink引擎](http://baike.baidu.com/view/10399127.htm)

