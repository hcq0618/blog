---
title: 实用资源报告工具Unity-AssetsReporter
thumbnail: http://upload-images.jianshu.io/upload_images/17266280-d9bd711f81c73ffe.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240
categories: Unity插件
tags: [Unity插件]
---

Unity Global Support部门制作了一些实用的小工具免费供大家使用，此前已为大家介绍过[批量处理资源的Asset
Auditing](http://mp.weixin.qq.com/s?__biz=MjM5NjE1MTkwMg==&mid=2651038011&idx=1&sn=a6695849c1aaa87cfcad56534ec83dbf&scene=21#wechat_redirect)以及[批量清理资源的小工具Asset
Cleaner](http://mp.weixin.qq.com/s?__biz=MjM5NjE1MTkwMg==&mid=2651038723&idx=1&sn=e5adc5c20193372b6899c840913a63f2&chksm=bd1a93328a6d1a24af34177e59dbb14246fdc6dba6f06432db8b964773db7e3ad43fbbd67871&scene=21#wechat_redirect)，
今天要给大家推荐的是一款名叫AssetsReporter的插件，可以辅助开发者管理几类Asset的导入设置并发现可能存在问题，另外还提供了AssetBundle的资源与依赖查看功能。

# 项目介绍

Unity对导入项目的资源如Texture、Model和Audio等都要根据其导入设置生成新的资源文件，以供之后打包使用。开发者一般需要根据发布平台的性能、内存、包体占用等方面的需求，对资源采取特定的导入设置，因此，保证所有资源的导入设置都正确配置是比较重要的一环。

AssetsReporter提供了对Texture、Model和Audio这几种常用资源的导入设置进行检查的功能，其生成的网页报告可以在浏览器端通过勾选特定的设置选项来搜索某类资源，以确定资源是否都正确配置。另外对于Resources文件夹及AssetBundle资源也提供搜索检视功能（鉴于Resources对Splash
Scene时间影响较大，Resources检视功能主要方便让开发者完全使用AssetBundle来取代其）。

使用方法

点击菜单栏Tools->AssetsReporter，弹出AssetsReporter窗口，然后点击对应类型资源名称下的Report按钮生成报告（每次对资源进行修改后需要重新生成报告），点击Open可以打开上次生成的报告，报告会以网页的形式在浏览器端展现。

  

![](http://upload-images.jianshu.io/upload_images/17266280-d9bd711f81c73ffe.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

  

![](http://upload-images.jianshu.io/upload_images/17266280-0f7b4b3104991226.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

# 报告类型

 **Texture Reporter**

  

![](http://upload-images.jianshu.io/upload_images/17266280-1a33952fd98e186a.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

此报告管理Texture的导入设置，设置好搜索条件后点击Search后会出现符合条件的资源，可以预览图片并展示此Texture的一些常用属性。较常关注的设置包括压缩格式是否适合以及分辨率是否2的N次幂等。

 **Model Reporter**

  

![](http://upload-images.jianshu.io/upload_images/17266280-8dd3d1dd293dde14.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

此报告管理Model的导入设置，可以显示搜索结果的各种常用属性，包括顶点数，动画类型及包含的动画列表等。较常关注的设置包括mesh是否优化，Rig设置以及mesh是否Read/Write
Enable等。

 **Audio Reporter**

  

![](http://upload-images.jianshu.io/upload_images/17266280-88be656603a4e934.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

此报告管理Audio的导入设置，可以预览音频并展示常用的属性。较常关注的设置包括压缩格式是否适合，加载方式是否适合等。

 **AssetBundle Reporter**

  

![](http://upload-images.jianshu.io/upload_images/17266280-e59836692fa3a2b6.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

此报告提供AssetBundle的可视化检视界面，可通过资源名称搜索包含其的AssetBundle文件，并查看AssetBundle中打入的资源以及依赖的文件或者其他AssetBundle。

 **Resources Reporter**

  

![](http://upload-images.jianshu.io/upload_images/17266280-cfaf2db5a9ab6f80.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

此报告主要根据勾选的资源类型来搜索并显示项目中Resources文件夹中的资源，方便开发者确认是否仍存在无需放入Resources文件夹的资源。由于Resources中文件需要构建的内存映射结构对Splash
Screen的时间影响较大，除了常驻在项目内存中的资源，Unity建议开发者仅仅把Resources文件夹作为方便制作demo的工具，项目打包的时候还是要使用AssetBundle来做资源的动态加载。

