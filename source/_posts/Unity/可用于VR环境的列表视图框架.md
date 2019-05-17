---
title: 可用于VR环境的列表视图框架
thumbnail: http://upload-images.jianshu.io/upload_images/17266280-713486dec6c0bbf8.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240
categories: Unity
tags: [Unity]
---

本文为大家介绍Unity Labs团队开发的可用于VR环境的列表视图框架，代码和示例场景可以从Unity Asset
Store获取，也可从Unity开源Git仓库中获取。

# Unity Labs介绍

Unity Labs是专注于研究VR、AR、图形及游戏开发等相关前沿技术的团队。目前Unity Labs最主要的项目就是Unity VR编辑器以及Carte
Blanche项目。Unity Labs团队介绍请看：

# Carte Blanche项目介绍

Carte Blanche项目（PCB）是Unity实验室的研发计划，目的是为非技术用户提供VR-in-VR的编程工具。Carte
Blanched的核心设计理念主要在于对象与行为的设计，它的一种典型示例：用户可以抓取虚拟的扑克牌，并将其放置在虚拟的桌子上，借助动作捕捉控制器真实地与卡牌互动。概念视频：

# PCB卡牌系统介绍

![](http://upload-images.jianshu.io/upload_images/17266280-713486dec6c0bbf8.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

  

PCB的卡牌系统比传统滚动列表要复杂得多。PCB系统要求卡牌必须能够动态出现或消失，且用户可以触碰到它们。此外，VR应用程序对性能的要求也极其苛刻。还要尽量避免实例化/销毁场景对象，因为这些操作的开销非常之大。最后为了可重用性，外观和感觉上的统一性起见，还需要一套可扩展的解决方案，能够使用其他类型的UI元素制造出相似的体验。

Unity Labs为列表视图开发了一套通用框架作为PCB卡牌系统的基础。代码和示例场景可以从Unity Asset
Store获取，也可从Unity开源Git仓库中获取。示例效果如下：

  

![](http://upload-images.jianshu.io/upload_images/17266280-973a3f3e72f11218.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

Model与View的解耦

本框架的一个设计目标是遵循MVC或MVVM设计模式，将数据的显示逻辑（view）与数据的状态（mode）本身解耦。对于任何一个框架而言，框架本身应自动处理列表当前状态的显示。这种实现下我们只需要考虑数据的当前状态，而不用关心如何处理视图的更新。

框架本身会负责搞定这些列表行的内存分配问题，并在列表元素离开屏幕时回收并重用在接下来要显示的元素上。

更为具体的技术实现细节请访问Unity官方中文社区阅读！

# 资源包

List View框架现已发布至Unity资源商店，一同开放的还有Unity BitBucket官方账号的开源Git仓库。本文的框架是Carte
Blanche项目资源包的首个模块，其他的模块将会陆续地以同样地方式对社区公布。

本框架可以归结为三个C#类：ListViewController（以两个文件存在），ListViewItem与ListViewItemData。这些类用来控制并处理鼠标与触摸的输入以及列表需要显示的数据。在处理游戏手柄，UI，手势输入或VR设备时这些类也能让开发者很方便地完成需要的特性。在PCB的例子中，列表视图的控制是通过手势追踪控制器来实现的。

更为具体的技术实现细节及代码下载请访问Unity官方中文社区！

