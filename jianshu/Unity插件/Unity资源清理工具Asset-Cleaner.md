---
title: Unity资源清理工具Asset-Cleaner
thumbnail: http://upload-images.jianshu.io/upload_images/17266280-bf2544dff8e4c04e.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240
categories: Unity插件
tags: [Unity插件]
---

Unity Global Support部门制作了一些实用的小工具免费供大家使用，前面已经分享过了[批量处理资源的Asset
Auditing](http://mp.weixin.qq.com/s?__biz=MjM5NjE1MTkwMg==&mid=2651038011&idx=1&sn=a6695849c1aaa87cfcad56534ec83dbf&scene=21#wechat_redirect)，今天继续为大家推荐用于批量清理资源的小工具：Asset
Cleaner。

Unity Global
Support部门主要负责对使用Unity引擎的企业级VIP客户提供技术支持，大中华区已实现全面覆盖，目前包括腾讯，网易，巨人，完美世界等公司已属于Unity的企业级VIP客户。
Asset Cleaner主要用于查找并删除没有被引用的资源，简单易用，且具有高度可扩展性。

# 项目背景

在Unity项目中，我们习惯将所有的资源统称为Asset。Asset一般存放在Assets目录及其子目录。随着项目的研发进度，Asset数量也会爆发式地增长，资源管理面临很大的挑战。如何查找并区分有效和无效的资源，是很多项目管理者非常重视的事情。本文介绍的这个工具可以自动分析查找项目中未使用到的资源，在选择删除的时候还可以将这些文件打包备份，确保资源的安全性、提高项目管理的效率。

# 实现原理

该工程只有四个CS文件，需存放在Editor目录下。

  

![](http://upload-images.jianshu.io/upload_images/17266280-bf2544dff8e4c04e.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

FindUnusedAssets是这个工具的主要入口，实现了编辑器的扩展菜单及其内部调用。

AssetCollector是总的工具类，用来收集所有的asset文件

ClassReferenceCollection用来收集所有的.cs脚本文件。

ShaderReferenceCollection用来收集所有的Shader文件。

# AssetCollector

AssetCollector实现了这个工具的核心代码，点击菜单时会调用定义在它内部的Collection函数。AssetCollector中声明了两个变量，useCodeStrip和saveEditorExtensions。useCodeStrip用来控制要不要删除未使用的脚本文件，saveEditorExtensions用来控制检测资源是否被Editor脚本引用。工具中提供了三个菜单项，分别是only
resource、unused by editor、unused by
game。这三个菜单项执行的代码就是通过设置useCodeStrip和saveEditorExtensions为不同的值来控制过滤的方式。

  

![](http://upload-images.jianshu.io/upload_images/17266280-c8d82a48bd35c054.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

# 资源搜集

Collection函数内实现了各种类型资源文件的搜索过滤。

Directory.GetFiles()获取“Asset”目录及其子目录下所有相关资源的名字,通过Linq语法进行过滤，获取需要的文件类型。

  

![](http://upload-images.jianshu.io/upload_images/17266280-5d3ae04b50d153d7.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

依赖关系获取

通过AssetDatabase.GetDependencies获取当前有效的场景文件及场景依赖文件。

  

![](http://upload-images.jianshu.io/upload_images/17266280-24de90cca04d50b7.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

# 使用介绍

首先我们要保证当前工程中存在有效的场景文件，因为Asset资源的有效性依赖于是否被场景引用。

![](http://upload-images.jianshu.io/upload_images/17266280-5f429b5eb4ed5b9b.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

使用时需要找到这个菜单项Assets->Delete Unused Assets,如下图所示。

![](http://upload-images.jianshu.io/upload_images/17266280-e1b0ce5422ad4937.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

Delete Unused Assets下有三个选项，分别是删除未使用的资源文件（only resource），删除编辑器未使用的Asset（unused
by editor）和删除游戏未使用的Asset（unused by game）。

# 使用方法

在开始使用该工具时，要保证有效的EditorBuildSettings.scenes

选择Delete Unused Assets下“only resource”选项，弹出对应的删除列表。如下图所示：

![](http://upload-images.jianshu.io/upload_images/17266280-633690095fbc78c4.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

显示在删除列表中文件。单击“Delete”，列表中的文件从项目中移除，工具会把这些文件作为一个UnityPackage导出到“../
BackupUnusedAssets/”。这个包作为被删除文件的备份，如果后期发现有资源丢失，可以从这个包内找到对应的资源文件重新导入。

![](http://upload-images.jianshu.io/upload_images/17266280-957a25fafe467c39.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

上面简单介绍了Asset Cleaner工程的工作原理及使用方式。在实战中，我们可以根据需求自定义查找文件的格式。

