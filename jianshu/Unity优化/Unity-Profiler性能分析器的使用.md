---
title: Unity-Profiler性能分析器的使用
thumbnail: http://upload-images.jianshu.io/upload_images/17266280-9eb4cfdebc873de1.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240
categories: Unity优化
tags: [Unity优化]
---

长话短说，我整理了一下mac版Unity3D
pro下的Profiler连接Android的使用。注意是专业版的Unity3D。在Window下会有Profiler

  

![](http://upload-images.jianshu.io/upload_images/17266280-9eb4cfdebc873de1.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

这个工具的意义是，游戏在客户端跑然后UnityProfile测试一些参数

连接手机有两种方式。

1.wifi：让手机和电脑痛处于同一局域网内。

2.数据线连接（下好各种驱动），一般只要Unity中 Build And Run 时游戏能在客户端跑  就基本连接没问题

1.File->Build Setting

  

![](http://upload-images.jianshu.io/upload_images/17266280-6a6264a5921acf6c.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

注意勾选 Development  Build

点击 Player Settings  找到ProductName 记录下来

2.数据线连接手机，File->Build And Run

3.打开终端，找到adb的文件

cd /Applications/android/adt-bundle-mac-x86_64-20140702/sdk/platform-tools

每个mac  不一样

./adb forward tcp:54999 localabstract:Unity-<包名>

4.window->profiler 同时手机运行游戏

  

![](http://upload-images.jianshu.io/upload_images/17266280-2247239bbaf353df.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

如果用wifi连接 先Enter IP 输入手机在局域网中ip即会成为2

如果是数据线 直接选一

ok，随玩游戏随测，数据线连接的话 ，注意不要断开连接。

