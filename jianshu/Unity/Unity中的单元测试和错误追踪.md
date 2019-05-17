---
title: Unity中的单元测试和错误追踪
thumbnail: http://upload-images.jianshu.io/upload_images/17266280-d5113ae2da1fd04e.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240
categories: Unity
tags: [Unity]
---

本文将由Unity大中华区企业支持经理高川，为大家分享Unity自带的单元测试及性能报告工具。

在游戏开发过程中，Bug的出现是无法避免的。解决Bug的重要前提是及时发现Bug，准确定位Bug。Unity提供了两个优秀的工具来帮助大家完成“杀虫”工作。

#  **Unity Editor Test Runner**

在开发过程中，一个Bug被发现的越早，其修复的可能性越高，而修复成本则越低。为了尽早发现问题，避免Bug积累重叠，单元测试就显得尤为重要。

单元测试可以针对特定功能模块进行持续的检测，帮助开发人员尽早发现问题，及时修正。在Unity编辑器中集成了单元测试模块。该模块源自著名的开源工程NUnit，与Unity引擎结合后，可以方便的完成日常开发中的单元测试功能。下面来介绍一下如何使用这个功能。

首先要建立测试用例。测试用例的脚本需要放到Editor 目录下：

  

![](http://upload-images.jianshu.io/upload_images/17266280-d5113ae2da1fd04e.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

在测试用例脚本中引入名字空间NUnit.Framework：

  

![](http://upload-images.jianshu.io/upload_images/17266280-8e2f91d10702d7ab.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

测试用例函数需要一个[Test]属性来标识：

  

![](http://upload-images.jianshu.io/upload_images/17266280-54367f8b1f3da754.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

测试用例函数中通过Assert类下面的一系列函数，进行断言测试：

  

![](http://upload-images.jianshu.io/upload_images/17266280-7cac33e4c21d3c5c.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

一个测试用例中可以有多个断言，只有所有断言都通过检测，才会认为一个测试用例通过了检测。

写好全部测试用例后，打开Unity Editor的Windows->Editor Tests Runner，在Editor
Tests窗口中我们可以看到测试工具按钮和刚刚写的一系列测试用例：

  

![](http://upload-images.jianshu.io/upload_images/17266280-dcbc0dc7972c470c.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

上面一栏中包含按钮：Run All，Run Selected和Run Failed

\- Run All：运行全部测试用例

\- Run Selected：运行当前选择的测试用例

\- Rerun Failed：重新运行全部失败的测试用例

右侧的四个图标则分别表示：

 - 成功的测试用例数

        - 失败的测试用例数

        - 被忽略的测试用例数

        - 尚未运行过的测试用例数

下方的树状结构表示具体测试用例当前的状态。

同时Editor Tests提供headless的运行模式，可以很好的与CI&CD等自动化流水线配合。

#  **Game Performance Reporting**

Unity提供的另外一个工具是Game Performance
Reporting（GPR）性能报告。这是一个用来做运行时错误追踪的系统。目前市面上也有很多运行时错误追踪系统，但很多在和Unity引擎结合使用中效果并不理想。主要表现在，追踪到的代码可读性差，错误追踪不准确，定位错误等等。结果造成了开发者看到很多错误报告上来，然而并不能解决的尴尬局面。做为Unity原生解决方案，Game
Performance Reporting性能报告系统完美解决了这个问题。下面来简单介绍一下这个系统。

首先改系统整合简单。Game Performance
Reporting性能报告继承了Unity一贯的使用简单的风格，在Unity5.4之前的Unity版本（目前仅支持Unity5.x系统），开发者需要去Unity官网下载一个UnityPackage并导入工程。然后在游戏启动时的某个脚本上加上一句代码：

> CrashReporting.Init("<Project Id>");

其中Project ID是在Unity官网上生成的唯一ID。

在Unity5.4版本中，Game Performance
Reporting系统直接被整合到了编辑器中。开发者只需要在Services窗口中将Performance Reporting的开关打开即可：

  

![](http://upload-images.jianshu.io/upload_images/17266280-637491d3bc4f9696.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

当游戏在运行时（测试期或者上线后）出现异常的时候，通过登录Unity开发者页面的Unity Online Services 就可以查看到异常的信息。

堆栈部分，在信息后台是可以看到清晰的异常定位的。这样可以快速的帮助开发者定位到问题所在：

![](http://upload-images.jianshu.io/upload_images/17266280-9769f8afc3f4ec7a.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

同时Game Performance Reporting提供异常的基本数据统计，包括异常出现的设备，异常出现的时间点，影响到的客户数量以及影响到的版本等等：

![](http://upload-images.jianshu.io/upload_images/17266280-0231eb2f52ccc398.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

通过以上两个工具，在开发期和运行时，开发者都可以很好的管理游戏的Bug数量，评估工程的质量，及时发现和修改问题，从而提供更好的游戏体验给广大玩家。

