---
title: Unity-AssetBundle可视化构建工具
thumbnail: http://upload-images.jianshu.io/upload_images/17266280-5987583bd0364a23.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240
categories: Unity插件
tags: [Unity插件]
---

Unity 全球技术支持部门制作了一些实用的小工具免费供大家使用，此前已为大家推荐了用于[批量处理资源文件的Asset
Auditing](http://mp.weixin.qq.com/s?__biz=MjM5NjE1MTkwMg==&mid=2651038011&idx=1&sn=a6695849c1aaa87cfcad56534ec83dbf&scene=21#wechat_redirect)。今天要给大家推荐的是一款名叫AssetGraph的插件，可以帮助开发者方便地定制AssetBundle构建规则并进行可视化的管理。

# 项目介绍

在Unity
5.x中构建AssetBundle的流程已经比4.x时代大大简化，开发者不用在资源的依赖关系上花费太多时间，但是在实际大型项目中，开发者可能会发现仅靠引擎自带的功能对AssetBundle进行管理还有不太方便的地方。例如：如果希望为不同平台对AssetBundle的构建设置不同的规则（包括打入AssetBundle内的资源，资源的导入设置等），那么开发者可能会在两套不同方案的切换中花费不少的时间，或者需要自己编写一套对应于项目需要的AssetBundle打包工具。鉴于此我们开发了AssetGraph，让开发者可以根据实际需求可视化地定制AssetBundle打包规则并有效地进行管理。

# 使用方法

 **添加节点**

打开AssetGraph窗口，在AssetGraph的画布上点击鼠标右键会弹出可以添加的节点列表，每个添加的节点都可以在其Inspector中设置对应的属性值。而首先要添加的是Loader节点，这个节点用来指示哪个文件夹下的Assets会作为Output输送给接下来的节点以进行设置或过滤直至最后打入AssetBundle中。

 **  
**

![](http://upload-images.jianshu.io/upload_images/17266280-5987583bd0364a23.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

**连接节点**

当创建了两个以上的节点时，可以通过点击并拖动节点上的小圆点到另一个节点上来创建两个节点之间的link，这时一个节点的Output即成为另一个节点的Input。通过点击link，我们可以在link的inspector窗口中实时查看此时通过此link的Asset。

 **  
**

![](http://upload-images.jianshu.io/upload_images/17266280-78fa08cfeb68930f.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

**设置节点属性**

通过点击一个节点，你可以在其inspector窗口中设置你所需要的AssetBundle构建规则属性。例如Filter节点允许你设置Asset的过滤规则，而Importer节点则允许你设置需要应用到这个节点的Input
Assets上的导入设置。

 **  
**

![](http://upload-images.jianshu.io/upload_images/17266280-62fd265bce3981c8.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

**构建AssetBundle**

最后只要点击AssetGraph上的Build按钮，就能构建出基于你所设定规则的AssetBundle了。如此，AssetGraph让你可以简单方便地管理不同的构建需求并通过可视化界面实时验证结果是否正确。

  

![](http://upload-images.jianshu.io/upload_images/17266280-20870fe4699bfefb.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

# 节点介绍

 **Loader**

Loader定义了Asset的最初源头，你可以指定一个根目录（也可以指定Assets/外部的目录）

IN: 无

OUT：指定目录下的所有Asset

 **  
**

![](http://upload-images.jianshu.io/upload_images/17266280-154864d36281ad00.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

**Filter**

Filter用于过滤输入的Asset，你可以在inspector窗口中设置多条过滤的规则。

IN: 上个节点输出的Asset

OUT：符合过滤规则的Asset

 **  
**

![](http://upload-images.jianshu.io/upload_images/17266280-9e9076e6c2300cfd.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

**Importer**

Importer可以重载输入Asset的导入设置（注意只是在构建AssetBundle的时候改变了导入设置，原来的导入设置其他时候仍然生效）

IN：上个节点输出的Asset

OUT：应用了所设导入设置的Asset

 **  
**

![](http://upload-images.jianshu.io/upload_images/17266280-ebaac45b178f9162.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

**Grouping**

Grouping可以根据设定的关键字把输入的Asset进行分组，而“*”星号可以作为关键字的一个通配符。

IN：上个节点输出的Asset

OUT：根据关键字设置的Asset分组列表

 **  
**

![](http://upload-images.jianshu.io/upload_images/17266280-3695240b298ba890.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

**  
**

![](http://upload-images.jianshu.io/upload_images/17266280-43e22c87c74272d5.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

**Prefabricator**

Prefabricator可以把输入的Asset创建成Prefab。可以通过扩展AssetGraph.PrefabricatorBase类来定制自己的Prefab创建方式，具体代码示例请参见项目GitHub说明页面。

IN：上个节点输出的Asset

OUT：包含了新生成的Prefab的Asset（Prefab被分配在对应的group中）

 **  
**

![](http://upload-images.jianshu.io/upload_images/17266280-6a611a07a3e23bcd.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

**Bundlizer**

Bundlizer用来把输入的Assets指定到特定的AssetBundle中并设置AssetBundle的命名，其中“*”星号可以适配Grouping节点的通配符。

IN：上个节点输出的Asset

OUT：包含了输入Asset的AssetBundle

 **  
**

![](http://upload-images.jianshu.io/upload_images/17266280-6aee72deda434eae.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

**BundleBuilder**

BundleBuilder用于实际构建AssetBundle。通过使用Bundlizer和BundleBuilder,你可以同时构建带有不同设置的AssetBundle（比如说压缩及非压缩）。

IN：上个节点输出的AssetBundle

OUT：构建出来的AssetBundle文件

 **  
**

![](http://upload-images.jianshu.io/upload_images/17266280-4bfba564c6bef8fb.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

**Exporter**

Exporter可以把输入的AssetBundle或Asset文件保存到指定的文件夹中（可以指定Assets/外部的目录）。

IN：上个节点输出的Asset或AssetBundle文件

  

![](http://upload-images.jianshu.io/upload_images/17266280-0e42f745ceefa1f8.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

