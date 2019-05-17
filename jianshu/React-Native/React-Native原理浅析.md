---
title: React-Native原理浅析
thumbnail: http://upload-images.jianshu.io/upload_images/17266280-18d8eca295182b6b.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240
categories: React-Native
tags: [React-Native,ReactNative]
---

<https://github.com/guoxiaoxing/react-
native/tree/master/doc/ReactNative%E6%BA%90%E7%A0%81%E7%AF%87>

# 线程模型

RN应用中存在3个线程：

UI线程：即Android中的主线程，负责绘制UI以及监听用户操作。

Native线程：负责执行C++代码，该线程主要负责Java与C++的通信。

JS线程：负责解释执行JS。

# 渲染模型

 **渲染模型框架：**

![](http://upload-images.jianshu.io/upload_images/17266280-18d8eca295182b6b.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

**VirtualDom的diff模型：**

具体VirtualDom的算法模型可以参考这篇文章：

[深度剖析：如何实现一个 Virtual DOM 算法](https://www.cnblogs.com/fengyuqing/p/virtual-
dom.html)

 **Js渲染Native具体范例：**

JS端通过调用RCTUIManager的createView的方法,传递json格式的数据,通知native端进行UI组件的初始化和渲染。

![](http://upload-images.jianshu.io/upload_images/17266280-655a3bd0eb6a8efa.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

# 通信模型

> JNI作为C++与Java的桥梁，JSC作为C++与JavaScript的桥梁，而C++最终连接了Java与JavaScript。

 **Java调Js**

原理使用了JSCore从Native执行JS代码，RN在此基础上给我们提供了通知发送的执行方式

具体实现：Java通过注册表调用到CatalystInstance实例，透过ReactBridge的jni，调用到Onload.cpp中的callFunction，最后通过javascriptCore，调用BatchedBridge.js，根据参数｛moduleID,methodID｝require相应Js模块执行。流程如下图：

![](http://upload-images.jianshu.io/upload_images/17266280-4d8c81a2f0015553.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

**Js调Java**

一般情况下，JS调Java的机制是［JS把对应的methodId和params
push到MessageQueue中，等待native调用JS，然后把MessageQueue中的数据发送到C层，再通过jni转到java层］

但如果JS的MessageQueue中的message超过 5ms 都没有取走，那么 JavaScript
就会主动调用方法nativeFlushQueueImmediate，通知C层将message取走。流程如下图：

![](http://upload-images.jianshu.io/upload_images/17266280-e4c8ad694eed6563.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

> JS的解析是在Webkit-JavaScriptCore中完成的，JSCExexutor对JavaScriptCore的功能做了进一步的封装

