---
title: 5分钟使用Unity制作AR应用
thumbnail: http://upload-images.jianshu.io/upload_images/17266280-e77a8ae9ad1efdd7.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240
categories: Unity
tags: [Unity]
---

今天这篇课程将为大家介绍使用Unity结合Vuforia
SDK制作AR应用的过程，非常简单且容易上手，适合Unity初学者。最后效果是制作出向上跳跃的Unity酱。

  

注意：本文教程使用Unity 5.3.4制作，Unity编辑器及Android设备测试通过。

  

* * *

# 第一步 注册Vuforia

首先需要到Vuforia官网进行注册，注册成功后跳转至License Manager页面。

  

然后点击“Add License
Key”按钮创建许可证，创建过程中需要输入应用名称、设备及许可证类型。这里应用名称任意填写，设备选择Mobile，许可证类型使用免费版即可。

  

![](http://upload-images.jianshu.io/upload_images/17266280-e77a8ae9ad1efdd7.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

点击下一步并同意条款后再点击“Confirm”按钮确认注册应用。成功注册后点击应用会显示License Key，后面会用到。

  

![](http://upload-images.jianshu.io/upload_images/17266280-656cd94bac3044c8.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

* * *

# 第二步 下载SDK并导入Unity

在Vuforia官网的下载页面找到Download for
Unity下载供Unity使用的SDK，本文使用最新版5.5.9。下载完成后双击打开文件，点击“Import”按钮将下载的SDK导入Unity项目。

  

![](http://upload-images.jianshu.io/upload_images/17266280-4a29799e8090fc87.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

* * *

# 第三步 添加并设置ARCamera

  

新建场景并将Prefabs文件夹下的ARCamera预设体拖拽至场景，如下：

  

![](http://upload-images.jianshu.io/upload_images/17266280-d2ac62c821ffc83d.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

将Vuforia网页上的License Key信息复制到Vuforia Behaviour脚本的App License Key字段，如下：

  

![](http://upload-images.jianshu.io/upload_images/17266280-291a0fcaa659cef6.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

* * *

# 第四步 添加识别标记

首先挑一张分辨率高且比较有特点（尽量少有重复）的图。

  

![](http://upload-images.jianshu.io/upload_images/17266280-2cc047cb5a8b9c73.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

然后打开Vuforia网页的Target Manager网页点击“Add
Database”按钮，随意填写名称并选择类型为“Device”。点击新创建的Database名称，会出现Add Target界面，设置如下：

  

![](http://upload-images.jianshu.io/upload_images/17266280-b8cd556bbd06b99c.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

将Width设为1并随意命名后点击“Add”按钮。回到列表页会发现Database中多了个5星级的识别标记。

点击页面上的“Download Dataset(All)”按钮，选择开发平台为Unity Editor后下载该资源。

  

![](http://upload-images.jianshu.io/upload_images/17266280-31151350cc7717a6.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

将下载的资源导入Unity项目，然后选中层级视图中的ARCamera，勾选Database Load Behaviour脚本下的“Load XX
Database”与“Active”。

  

![](http://upload-images.jianshu.io/upload_images/17266280-443e52a50ea29fa8.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

将Prefabs文件夹下的ImageTarget预设体拖拽至场景，然后点击Image Target
Behaviour脚本下的“Type”下拉列表，将类型设为“Predefined”，分别在“Database”和“ImageTarget”下拉列表中选择之前创建的Database和识别标记。此时场景示意图如下：

  

![](http://upload-images.jianshu.io/upload_images/17266280-12750fa48fe1413d.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

* * *

# 第五步 添加目标物体

接下来将UnityChan的模型作为目标物体添加为ImageTarget的子对象，可以按照自己的喜好调整UnityChan的位置及旋转角度或添加动画等。UnityChan的模型资源可在Asset
Store中免费下载，添加UnityChan后的场景如下：

  

![](http://upload-images.jianshu.io/upload_images/17266280-6d5ac48f38520b3c.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

到此就大功告成了，接下来打包运行，最终效果如下：

  

![](http://upload-images.jianshu.io/upload_images/17266280-52b85dc0dc2a21f0.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

