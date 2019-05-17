---
title: Android全自动打包生成apk
thumbnail: http://upload-images.jianshu.io/upload_images/17266280-023b15f9b35219c4.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240
categories: Unity
tags: [Unity]
---

Unity自动打包Android其实要比IOS容易得多，因为Android不用先生成java工程，然后在构建.apk包，我先说说Android打包的步骤。

1.把sdk拷贝至Plugins/Android下。

如下图所示，如果你做过Android源生开发，我相信下面的东西你不会陌生。可是如果你没做过Android原生开发，我还是详细说明以下。

AndroidManifest：这是Android程序必不可少的文件，这里记录着应用程序的启动Activity。Activity就是Android的一个界面，一般应用程序会有很多Acitivty，来回切换界面。但是游戏就不太一样了，因为游戏只需要一个Activity
一个View就可以了。（扯远了）

AndroidManifest：里面还记录着应用程序的权限，Service啊什么的，，有兴趣的同学可以谷歌搜一搜。

每次打包的时候Unity会用它默认的AndroidManifest，它默认的AndroidManifest在
unity.app/Contents/PlaybackEngines/AndroidPlayer下面。当你在进行打包apk的时候
unity会拷贝该路径下的所有参数。

在ProjectSetting里面勾选一些权限的时候，Unity会自动帮你修改AndroidManifest里面的权限，但是如果某个权限不能在Unity工程里面修改，那么就需要自己手动替换。如下图所示，我们把AndroidManifest放在Plugins/Android下面，
这样Unity在进行打包的时候就不会用它默认的，而是用我自己新写的打包。。这样就方便灵活很多了。。

bin:下面就记录着sdk用到的第三方jar

res：下面就是安卓的一些图片，资源啊什么。

你可以随便解开一个android的APK看看它的目录结构就明白了。。

  

![](http://upload-images.jianshu.io/upload_images/17266280-023b15f9b35219c4.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

这样在打包的时候unity就会自动把Plugins/Android下面的所有资源打包在你的APK里面了。但是如果你做渠道包的时候，每个包用的是不同的sdk，所以你需要在打包不同渠道的时候把相关的文件拷贝在Plugins/Android下面。

如下图所示，我在根目录下创建一个文件夹名子叫91，当我自动化打包的时候自动把91文件夹下面的资源先拷贝在Plugins/Android下面，然后在自动打包。。打完包以后再把Plugins/Andoird文件夹清空即可。。

  

![](http://upload-images.jianshu.io/upload_images/17266280-4cc6d58eb949859e.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

Ok上脚本。。代码和上一篇文章的第一步差不多，我就不多余注释，，执行下面shell脚本将自动打开unity，然后执行ProjectBuild.BuidForAndroid方法。。
project-$1 就是传入的参数。。

> #!/bin/sh

>

> #参数判断

>

> if [ $# != 1 ];then

>

>     echo "需要一个参数。 参数是游戏包的名子"

>

>     exit

>

> fi

>

> #UNITY程序的路径#

>

> UNITY_PATH=/Applications/Unity/Unity.app/Contents/MacOS/Unity

>

> #游戏程序路径#

>

> PROJECT_PATH=/Users/MOMO/commond

>

> #在Unity中构建apk#

>

> $UNITY_PATH -projectPath $PROJECT_PATH -executeMethod
ProjectBuild.BuildForAndroid project-$1 -quit

>

> echo "Apk生成完毕"

在关闭unity的情况下运行。在命令行里面执行这一条脚本， 参数一个参数 91。

![](http://upload-images.jianshu.io/upload_images/17266280-7a4cc479b9e26605.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

> using System.Collections;

>

> using System.IO;

>

> using UnityEditor;

>

> using UnityEngine;

>

> using System.Collections.Generic;

>

> using System;

>

>  
>

>

> class ProjectBuild : Editor{

>

>  
>

>

> //在这里找出你当前工程所有的场景文件，假设你只想把部分的scene文件打包 那么这里可以写你的条件判断 总之返回一个字符串数组。

>

> static string[] GetBuildScenes()

>

> {

>

> List<string> names = new List<string>();

>

> foreach(EditorBuildSettingsScene e in EditorBuildSettings.scenes)

>

> {

>

> if(e==null)

>

> continue;

>

> if(e.enabled)

>

> names.Add(e.path);

>

> }

>

> return names.ToArray();

>

> }

>

>  
>

>

> static void BuildForAndroid()

>

> {

>

> Function.DeleteFolder(Application.dataPath+"/Plugins/Android");

>

>  
>

>

> if(Function.projectName == "91")

>

> {

>

>
Function.CopyDirectory(Application.dataPath+"/91",Application.dataPath+"/Plugins/Android");

>

> PlayerSettings.SetScriptingDefineSymbolsForGroup(BuildTargetGroup.Android,
"USE_SHARE");

>

> }

>

> string path = Application.dataPath +"/" + Function.projectName+".apk";

>

> BuildPipeline.BuildPlayer(GetBuildScenes(), path, BuildTarget.Android,
BuildOptions.None);

>

> }

>

> }

程序会执行BuildForAndroid的方法，这里我把shell传入的参数取出来。根据传入的不同参数来初始化打包的一些设置。。

最终BuildPlayr就开始构建apk，第二个参数就是打包出apk保存的路径。 在打包之前你可以处理一些 游戏包名， 游戏icon
等等一些平台之间的特殊性 ，也可以设置一些 预定义标签，。

> using UnityEngine;

>

>  
>

>

> #if UNITY_EDITOR

>

> using UnityEditor;

>

> using UnityEditor.Callbacks;

>

> using UnityEditor.XCodeEditor;

>

> using System.Xml;

>

> #endif

>

> using System.IO;

>

>  
>

>

> public static class XCodePostProcess

>

> {

>

>     #if UNITY_EDITOR

>

>     [PostProcessBuild (100)]

>

>     public static void OnPostProcessBuild (BuildTarget target, string
pathToBuiltProject)

>

>     {

>

> if (target == BuildTarget.Android)

>

> {

>

> Function.DeleteFolder(Application.dataPath+"/Plugins/Android");

>

> if(Function.projectName== "91")

>

>      {

>

>              //当我们在打91包的时候 这里面做一些 操作。

>

>  
>

>

> }

>

> }

>

>     }

>

>     #endif

>

> }

**** 在回到XUPortr里面，当Android打包完毕后，这里我们清空Plugins/Android文件夹。。或者你也可以做一些操作。。

Function.cs 用到的一个工具类

> using UnityEngine;

>

> using System.Collections;

>

> using System.IO;

>

> public class Function  {

>

>  
>

>

> //得到项目的名称

>

> public static string projectName

>

> {

>

> get

>

> {

>

> //在这里分析shell传入的参数， 还记得上面我们说的哪个 project-$1 这个参数吗？

>

> //这里遍历所有参数，找到 project开头的参数， 然后把-符号 后面的字符串返回，

>

> //这个字符串就是 91 了。。

>

> foreach(string arg in System.Environment.GetCommandLineArgs()) {

>

> if(arg.StartsWith("project"))

>

> {

>

> return arg.Split("-"[0])[1];

>

> }

>

> }

>

> return "test";

>

> }

>

> }

>

>  
>

>

> public static void DeleteFolder(string dir)

>

> {

>

> foreach (string d in Directory.GetFileSystemEntries(dir))

>

> {

>

> if (File.Exists(d))

>

> {

>

> FileInfo fi = new FileInfo(d);

>

> if (fi.Attributes.ToString().IndexOf("ReadOnly") != -1)

>

> fi.Attributes = FileAttributes.Normal;

>

> File.Delete(d);

>

> }

>

> else

>

> {

>

> DirectoryInfo d1 = new DirectoryInfo(d);

>

> if (d1.GetFiles().Length != 0)

>

> {

>

> DeleteFolder(d1.FullName);////递归删除子文件夹

>

> }

>

> Directory.Delete(d);

>

> }

>

> }

>

> }

>

>  
>

>

> public static void CopyDirectory(string sourcePath, string destinationPath)

>

> {

>

> DirectoryInfo info = new DirectoryInfo(sourcePath);

>

> Directory.CreateDirectory(destinationPath);

>

> foreach (FileSystemInfo fsi in info.GetFileSystemInfos())

>

> {

>

> string destName = Path.Combine(destinationPath, fsi.Name);

>

> if (fsi is System.IO.FileInfo)

>

> File.Copy(fsi.FullName, destName);

>

> else

>

> {

>

> Directory.CreateDirectory(destName);

>

> CopyDirectory(fsi.FullName, destName);

>

> }

>

> }

>

> }

>

> }

如下图所示，脚本运行完毕，你打包的APK就静静的放在了这里，怎么样？简单吧？嘿嘿。。

![](http://upload-images.jianshu.io/upload_images/17266280-86fc0aea58f9bcb0.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

注意事项：

1、因为你的工程可能比较大，如果IOS和Android同时打包的话切个平台都要半个多小时，我建议的svn在本地check out 两个工程，一个切在ios
一个切在Android  打包的时候分开打。

2.执行shell脚本的时候请关闭保存unity工程。

3.Android 因为不受证书的限制，我上传的工程建议你下载下来看看，肯定可以直接打出来包。。

4.我建议打包的机器使用mac。 因为windows不能打包IOS 而MAC可以同时 打包 IOS 和 Android

工程下载地址：<http://pan.baidu.com/s/1o6OATcu>

