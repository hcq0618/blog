---
title: Unity基础
thumbnail: 
categories: Unity
tags: [Unity]
---

# 第三方插件及使用

  

 **BestHttp** : 功能主要有连接池 缓存 超时 代理 重定向 gzip 大文件上传下载 断点续传 socket
已经封装了一个类HttpUtils

文档[https://docs.google.com/document/d/181l8SggPrVF1qRoPMEwobN_1Fn7NXOu-
VtfjE6wvokg/edit?pref=2&pli=1#](https://docs.google.com/document/d
/181l8SggPrVF1qRoPMEwobN_1Fn7NXOu-VtfjE6wvokg/edit?pref=2&pli=1)

pro版提供源码<https://www.assetstore.unity3d.com/en/#!/content/10872>

1.9.8版本下载<http://www.seedpeer.eu/details/10707104/Unity-Asset---Best-HTTP-Pro-
Edition-v1.9.8%5BAKD%5D%5BCTRC%5D.html>

 **LitJson** : 支持ORM对象关系映射 对象和json互转 和gson一样 官网<http://lbv.github.io/litjson/>

 **PoolManager** : 对象缓存池
用法参考<http://blog.csdn.net/henren555/article/details/42100881><http://www.xuanyusong.com/archives/2974>

#  **工程文件的作用**

Assembly-CSharp-vs.csproj 和 Assembly-CSharp.csproj ：Visual Studio（带有-
vs后缀）和MonoDevelop为C#脚本生成的项目文件。

Assembly-UnityScript-vs.unityproj 和 Assembly-
UnityScript.unityproj：相同的项目文件，只不过是为JavaScript脚本。

testproject.sln 和 testproject-
csharp.sln：IDE的解决方案文件，第一个包括所有的C#、JavaScript和Boo脚本；而第二个只包括C#脚本，被设计用来在Visual
Studio中打开，因为VS不知道如何处理JavaScript和Boo项目。

testproject.userprefs 和 testproject-
csharp.userprefs：MonoDevelop用来存储当前打开文件、断点、观测等的配置文件。

Assets：存储所有游戏资源的文件夹，包括脚本、纹理、声音、编辑器定制等。当然是项目中最重要的文件夹。

ProjectSettings：在这个文件夹中Unity存储所有的项目设置，如物理、标签、角色设置等。或者说，所有你从 Edit → Project
的菜单中设置的都在这个文件夹中。

Library：被导入资源的本地缓存，当使用外部版本控制系统时应当被完全忽略。

obj 和 Temp：存储构建时产生的临时文件的文件夹，第一个用于MonoDevelop，第二个用于Unity。

  

看完了以上的内容就可以知道，我们只需要将Assets和ProjectSettings两个文件夹纳入版本控制即可。但在编写.gitignore文件前，还需要以下几个步骤，将设置以文本形式存储以利于版本控制：

在 Edit->Project Settings->Editor->Version Control Mode 中选择 Visible Meta files。

表示以meta文件来记录资源版本。 默认为Disabled，这样在无Library目录情况下会出现各种问题（后面会讲到Library不会提到版本库）。

在 Edit->Project Settings->Editor->Asset Serialization Mode 中选择 Force Text。

表示以纯文本形式保存unity文件。 Mixed和Force Binary都是二进制，不利于版本管理。

将Assets、ProjectSettings目录传到SVN、GIT或其它版本库

别人CheckOut这两目录后，第一次在Unity Editor中Open
Project…后会自动生成Library目录，所以Library无需纳入版本管理

#  **特殊文件夹及作用**

<http://www.xuanyusong.com/archives/3229>

#  **渲染顺序和层级关系**

<http://blog.csdn.net/kingsea168/article/details/50252733>

1.Unity3d中的渲染顺序如下：

不同的Camera的Depth

相同Camera下的不同SortingLayer

相同SortingLayer下的不同Z轴/Order in Layer

2.改变控件之间的层级关系

(1)同一canvas下：

改变控件transform的SiblingIndex,

> transform.GetSiblingIndex();

>

> transform.SetSiblingIndex(int index); //index值越大，越后渲染，层级越大，越显示在前面

(2)不同Canvas下：

设置Canvas下的Sort Order //Sort Order值越大，越后渲染，层级越大，越显示在前面

  

#  **属性面板定制化**

<http://blog.sina.com.cn/s/blog_5b6cb9500101857b.html>

<http://www.360doc.com/content/15/1205/14/25502502_518083734.shtml>

