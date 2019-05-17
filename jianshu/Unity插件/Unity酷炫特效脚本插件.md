---
title: Unity酷炫特效脚本插件
thumbnail: http://upload-images.jianshu.io/upload_images/17266280-ee2bb64160017b2f.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240
categories: Unity插件
tags: [Unity插件]
---

上周为大家介绍了Asset
Store中非常受欢迎的[不同游戏类型的完整模板](http://mp.weixin.qq.com/s?__biz=MjM5NjE1MTkwMg==&mid=2651039228&idx=1&sn=54505a8bbdb8b8988d8d5a5b53eb73cf&chksm=bd1a92cd8a6d1bdbe00ca42e8f128ffef14eb4d8ade97ae6d371ffdc218f4b45cfd2dff3a704&scene=21#wechat_redirect)，今天则分享一些脚本插件，用来实现各类酷炫的特效，包括爆炸、闪电及天空盒等。

# Exploder

  

![](http://upload-images.jianshu.io/upload_images/17266280-ee2bb64160017b2f.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

看名字就知道了，Exploder就是用来在Unity中实现各种爆炸效果的脚本插件。它可以实时分解网格，在几毫秒内将任意对象分崩离析。由于是实时计算，所以不需要预定义游戏对象作为碎片，所有过程仅需调用一行代码即可瞬间完成。

  

![](http://upload-images.jianshu.io/upload_images/17266280-8a1c0ce1024c6e9b.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

该插件带有强大的网格切割器，会查找游戏对象上的网格将其切割为小碎片，在游戏对象上添加Rigidbody组件再设置好加速度即可实现爆炸效果。出于性能的考虑，这些小碎片会存放于预先分配的对象池中，以尽可能减少创建及初始化游戏对象的次数。

使用Exploder非常简单，正如之前所说，仅需一行代码即可完成。首先，将插件Prefabs目录下的Exploder预制件拖拽至层级视图。然后从检视面板中调整爆炸相关的参数，例如碎片的数量等等。这一步也可以使用代码完成。为需要爆炸的目标对象添加ExploderOption脚本。接下来只需在任意脚本中调用ExplodeObject函数即可。

  

![](http://upload-images.jianshu.io/upload_images/17266280-56515fa422f627e0.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

Exploder还提供了FPS游戏示例场景，包含了FPS游戏的基本机制如瞄准、换武器及扔手榴弹等等。该插件同样支持移动平台，但建议针对不同机型使用不同的配置。

下载地址：

https://www.assetstore.unity3d.com/en/#!/content/9771

# TENKOKU Dynamic Sky

![](http://upload-images.jianshu.io/upload_images/17266280-642afb5ef1efa0b8.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

TENKOKU Dynamic
Sky是用于实现高度精确天气系统的插件，可以按照24小时循环实时动态设置天空场景。支持动态调整大气属性，例如白天与夜晚的天空亮度、雾效距离、云层密度、灰蒙程度、降雨、降雪及彩虹等等，几乎所有天气相关的属性都可以直接进行设置。

  

![](http://upload-images.jianshu.io/upload_images/17266280-498054e498457575.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

TENKOKU Dynamic Sky提供了很方便的编辑面板，所以不需编写代码也能轻松使用该插件。首先将Prefabs目录下的Tenkoku
DynamicSky预制件拖拽至场景，放置于(0,0,0)的位置，然后在相机上添加特效脚本Tenkoku Fog等，还可以根据实际需求加入其它的特效脚本。

  

![](http://upload-images.jianshu.io/upload_images/17266280-c9d0304caa1d1d5c.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

TENKOKU所有的核心代码都位于TenkokuModule脚本中，上述提到的各种天气属性也可以通过脚本进行修改。但请注意，该插件暂不支持移动平台。

下载地址：

https://www.assetstore.unity3d.com/en/#!/content/34435

# Procedural Lightning (2D and 3D)

  

![](http://upload-images.jianshu.io/upload_images/17266280-4ba5b44a391e769a.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

Procedural Lightning用来实现各种闪电特效，当然也可以生成游戏所需的普通线性特效。该插件比较简单，仅需一个Draw
Call即可完成所有的淡入淡出、生长及发光等效果。整个渲染在GPU上完成，相比CPU渲染效率更高，并且支持一些配置较低的移动设备。

  

![](http://upload-images.jianshu.io/upload_images/17266280-8fd4951998f23f16.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

使用该插件也非常简单，将插件核心脚本LightningBoltScript加入场景中的对象，设置好闪电及发光的材质，指定起始位置与结束位置，调整一些闪电属性，剩下的就交给Procedural
Lightning来完成。LightningBoltScript提供了非常多的属性设置，包括闪电路径数量等等都是可以预先设置的，调整这些参数让闪电达到理想的效果。

  

![](http://upload-images.jianshu.io/upload_images/17266280-7917f010fb2761e5.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

Procedural Lightning同时支持2D及3D，其中也提供了19种不同的示例，除了常见的2D闪电，还演示了立体闪电特效。

  

![](http://upload-images.jianshu.io/upload_images/17266280-af1e38a648af7cfc.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

下载地址：

https://www.assetstore.unity3d.com/en/#!/content/34217

