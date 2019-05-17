---
title: Unity图集的理解和使用
thumbnail: http://upload-images.jianshu.io/upload_images/17266280-ce5db986bb1a13ad.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240
categories: Unity优化
tags: [Unity优化]
---

图集的好处：

1.减少draw call: 多张图片需要多次draw call，合成了一张大图则只需要一次draw call。

2.减少内存占用：OpenGL
ES中每张贴图都需要设置成2的n次方才能使用。比如你有一张宽高为100x100和一张宽高为10x10的图片,如果不合成大贴图,那么需要使用128x128和16x16的两张图片(分别是2的7次方和2的4次方),但如果使用一张大图的话，可以把100x100和10x10的图片放到128x128的大图中,这样就用一张图片。

UGUI的图集打包与工作原理，整整看了一天多，终于看明白了～晕～还是记录一下我研究的成果，也希望大家在下面给我留言我们一起讨论一下。

先说说UGUI的Atlas和NGUI的Atlas的区别，NGUI是必须先打出图集然后才能开始做界面。这一点很烦，因为始终都要去考虑你的UI图集。比如图集会不会超1024
，图集该如何来规划等等。而UGUI的原理则是，让开发者彻底模糊图集的概念，让开发者不要去关心自己的图集。做界面的时候只用小图，而在最终打包的时候unity才会把你的小图和并在一张大的图集里面。然而这一切一切都是自动完成的，开发者不需要去care它。

如下图所示，Editor->Project Settings 下面有sprite packer的模式。Disabled表示不启用它，Enabled For
Builds 表示只有打包的时候才会启用它，Always Enabled 表示永远启用它。 这里的启用它就表示是否将小图自动打成图集。

  

![](http://upload-images.jianshu.io/upload_images/17266280-ce5db986bb1a13ad.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

我的选项是Always Enabled 。因为开发的时候我们需要清楚的看到现在是几个Draw
Call，从而才能优化小图。在最终打包的时候unity会自动构建大的图集，可是我开发的时候就想看图集会占几个Draw
Call，这怎么办呢？如下图所示，首先将你的图片拖入unity中，将同一图集的所有图片的packing tag设置成一个名子即可。

  

![](http://upload-images.jianshu.io/upload_images/17266280-dc922416b373d48a.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

注意你的图片不能放在Resources文件夹下面，Resources文件夹下的资源将不会被打入图集，切记（也就是在这里混淆了我很久）。然后在Windows->Sprite
Packer 里，点击packer
在这里你就可以预览到你的图集信息。图集的大小还有图集的格式等等很多参数我们都是可以控制的，也可以通过脚本来设置。我在下一篇文章里详细说这个（请期待嘿嘿）。

  

![](http://upload-images.jianshu.io/upload_images/17266280-1a44840b1d9ef060.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

图集的预览紧紧是让你看看你的图集大概张什么样子。那么我们的图集的这张图片保存在了哪里呢？它保存在和Assets文件夹同级的目录，Libary/AtlasCache里面。你不用管它，也不要删除它，就算你删除了也没用因为只要你打包，它就会生成并且会打到包中。

此时在Hierarchy视图中创建两个Image对象。如下图所示，我们可以清楚的看到此时我的draw call已经被合并成了1 。

  

![](http://upload-images.jianshu.io/upload_images/17266280-0ffe79cd589f1ada.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

这两个图片是我是在Editor模式下预先拖入Hierarchy视图中的，可是如果我想运行时根据图片的名子来动态创建精灵该如何？可是unity根本没有提供加载图集的方法，也没有提供加载图集上某个图片的方法。
因为UGUI就不像让开发者有图集的这个概念，可是我们肯定是要实现这个需求的。。怎么办呢？

第一个设想，先把散＝小图打包成图集，然后再把所有散图拷贝在Resources文件夹下，这样运行时就能用Resources.load了。

第二个设想，还是先把小图打成图集，然后把所有小图关联在prefab上，拷贝在Resources文件夹下，这样运行时也能用Resources.load了。到底那个靠谱呢？
给大家看一个图大家就知道答案了。

如下图所示，打成图集的图片如果在放在Resources那么资源就变成双份了。。
所以我们只能把小图关联在Prefab上，把所有的Prefab放在Resources下面，这样就不占用多余的空间了。

  

![](http://upload-images.jianshu.io/upload_images/17266280-192071356a4488e1.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

好了，现在方法我们已经掌握，那么就开始写工具吧。如下图所示可以按文件夹分，每一个文件夹就是一个图集。然后每一张小图创建一个Prefab，Prefab的名子就起小图的名子，文件关联在Resources下面。

  

![](http://upload-images.jianshu.io/upload_images/17266280-29752791f390e6ae.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

、

代码比较简单，我就不注释了。

> [MenuItem ("MyMenu/AtlasMaker")]

>

> static private void MakeAtlas()

>

> {

>

> string spriteDir = Application.dataPath +"/Resources/Sprite";

>

> if(!Directory.Exists(spriteDir)){

>

> Directory.CreateDirectory(spriteDir);

>

> }

>

>  
>

>

> DirectoryInfo rootDirInfo = new DirectoryInfo (Application.dataPath
+"/Atlas");

>

> foreach (DirectoryInfo dirInfo in rootDirInfo.GetDirectories()) {

>

> foreach (FileInfo pngFile in
dirInfo.GetFiles("*.png",SearchOption.AllDirectories)) {

>

> string allPath = pngFile.FullName;

>

> string assetPath = allPath.Substring(allPath.IndexOf("Assets"));

>

> Sprite sprite = Resources.LoadAssetAtPath<Sprite>(assetPath);

>

> GameObject go = new GameObject(sprite.name);

>

> go.AddComponent<SpriteRenderer>().sprite = sprite;

>

> allPath = spriteDir+"/"+sprite.name+".prefab";

>

> string prefabPath = allPath.Substring(allPath.IndexOf("Assets"));

>

> PrefabUtility.CreatePrefab(prefabPath,go);

>

> GameObject.DestroyImmediate(go);

>

> }

>

> }

>

> }

然后是运行时的代码。

> using UnityEngine;

>

> using System.Collections;

>

> using UnityEngine.UI;

>

>  
>

>

> public class UIMain : MonoBehaviour {

>

>  
>

>

> void Start ()

>

> {

>

> CreatImage(loadSprite("image0"));

>

> CreatImage(loadSprite("image1"));

>

> }

>

>  
>

>

> private void CreatImage(Sprite sprite ){

>

> GameObject go = new GameObject(sprite.name);

>

> go.layer = LayerMask.NameToLayer("UI");

>

> go.transform.parent = transform;

>

> go.transform.localScale= Vector3.one;

>

> Image image = go.AddComponent<Image>();

>

> image.sprite = sprite;

>

> image.SetNativeSize();

>

> }

>

>  
>

>

> private Sprite loadSprite(string spriteName){

>

> return Resources.Load<GameObject>("Sprite/" +
spriteName).GetComponent<SpriteRenderer>().sprite;

>

> }

>

> }

因为这两个图是在同一个图集上，所以drawcall就是1了。这样我们就可以根据图片的名子来运行时加载图片了。

  

![](http://upload-images.jianshu.io/upload_images/17266280-352f1ddadc200796.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

接下来就是Assetbundle了，如果我们的图集需要在线更新那该怎么办呢？
其实Assetbundle比Resources要更简单一些，无论如何我们要先开始打图集。

> [MenuItem ("MyMenu/Build Assetbundle")]

>

> static private void BuildAssetBundle()

>

> {

>

> string dir = Application.dataPath +"/StreamingAssets";

>

>  
>

>

> if(!Directory.Exists(dir)){

>

> Directory.CreateDirectory(dir);

>

> }

>

> DirectoryInfo rootDirInfo = new DirectoryInfo (Application.dataPath
+"/Atlas");

>

> foreach (DirectoryInfo dirInfo in rootDirInfo.GetDirectories()) {

>

> List<Sprite> assets = new List<Sprite>();

>

> string path = dir +"/"+dirInfo.Name+".assetbundle";

>

> foreach (FileInfo pngFile in
dirInfo.GetFiles("*.png",SearchOption.AllDirectories))

>

> {

>

> string allPath = pngFile.FullName;

>

> string assetPath = allPath.Substring(allPath.IndexOf("Assets"));

>

> assets.Add(Resources.LoadAssetAtPath<Sprite>(assetPath));

>

> }

>

> if(BuildPipeline.BuildAssetBundle(null, assets.ToArray(),
path,BuildAssetBundleOptions.UncompressedAssetBundle|
BuildAssetBundleOptions.CollectDependencies, GetBuildTarget())){

>

> }

>

> }

>

> }

>

> static private BuildTarget GetBuildTarget()

>

> {

>

> BuildTarget target = BuildTarget.WebPlayer;

>

> #if UNITY_STANDALONE

>

> target = BuildTarget.StandaloneWindows;

>

> #elif UNITY_IPHONE

>

> target = BuildTarget.iPhone;

>

> #elif UNITY_ANDROID

>

> target = BuildTarget.Android;

>

> #endif

>

> return target;

>

> }

如下图所示，我的assetbundle已经打出来了。

  

![](http://upload-images.jianshu.io/upload_images/17266280-a157c0bfa10e43ce.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

然后把UIMain.cs在改一改。

> using UnityEngine;

>

> using System.Collections;

>

> using UnityEngine.UI;

>

>  
>

>

> public class UIMain : MonoBehaviour {

>

>  
>

>

> AssetBundle assetbundle = null;

>

> void Start ()

>

> {

>

> CreatImage(loadSprite("image0"));

>

> CreatImage(loadSprite("image1"));

>

> }

>

>  
>

>

> private void CreatImage(Sprite sprite ){

>

> GameObject go = new GameObject(sprite.name);

>

> go.layer = LayerMask.NameToLayer("UI");

>

> go.transform.parent = transform;

>

> go.transform.localScale= Vector3.one;

>

> Image image = go.AddComponent<Image>();

>

> image.sprite = sprite;

>

> image.SetNativeSize();

>

> }

>

>  
>

>

> private Sprite loadSprite(string spriteName){

>

> #if USE_ASSETBUNDLE

>

> if(assetbundle == null)

>

> assetbundle = AssetBundle.CreateFromFile(Application.streamingAssetsPath
+"/Main.assetbundle");

>

> return assetbundle.Load(spriteName) as Sprite;

>

> #else

>

> return Resources.Load<GameObject>("Sprite/" +
spriteName).GetComponent<SpriteRenderer>().sprite;

>

> #endif

>

> }

>

> }

如下图所示，依然还是一个drawcall。

![](http://upload-images.jianshu.io/upload_images/17266280-6b3672bdc9a57aa0.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

衷心希望有经验的朋友在留言处给我提提意见， 或者大家一起讨论讨论。。 我们共同为把NGUI干掉的目标而奋斗，嘻嘻。

