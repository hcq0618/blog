---
title: Unity内存优化
thumbnail: http://upload-images.jianshu.io/upload_images/17266280-cb56c20da91a2855.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240
categories: Unity优化
tags: [Unity优化]
---

**一、内存使用**

 **Q1：在Unity的内存管理机制中, Reserved Total 和 Used Total之间的关系是怎样的？**

Reserved Total 和 Used Total为Unity引擎在内存方面的总体分配量和总体使用量。 一般来说，引擎在分配内存时并不是向操作系统
“即拿即用”，而是首先获取一定量的连续内存，然后供自己内部使用，待空余内存不够时，引擎才会向系统再次申请一定量的连续内存进行使用。所以，从图表中可以看到，Reserved
Total 的内存占用量略大于 Used Total， 且两者走势基本一致。

  

![](http://upload-images.jianshu.io/upload_images/17266280-cb56c20da91a2855.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

注意：对于绝大多数平台而言，Reserved Total内存 = Reserved Unity内存 + GFX内存 + FMOD内存 +
Mono内存。大家可以参考
[《性能优化,进无止境——内存篇（上）》](http://blog.uwa4d.com/archives/optimzation_memory_1.html)

 **Q2：在UWA的帮助下，我们追踪到了一个Reserved GFX的内存占用，并且显示比较高。我们应当如何降低该内存占用呢？**

一般来说，Reserved GFX
中的内存，主要是纹理和网格资源，可以尝试对纹理格式进行检测，尽可能使用硬件支持的压缩纹理；而对于网格资源，则可以从减少顶点或者顶点属性入手。

另外，更重要的是检测纹理和网格资源是否存在冗余（多份一样的资源）或者泄露（比如，主城中的大纹理出现在战斗场景中），这是需要极力避免的。关于资源冗余、内存泄露，开发者可以参考我们之前的文章[《
性能优化，进无止境——内存篇（下）》](http://blog.uwa4d.com/archives/optimzation_memory_2.html)。

 **Q3：Profiler中Not Saved是指什么？**

  

![](http://upload-images.jianshu.io/upload_images/17266280-3a5032ff9bff2f43.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

Profiler中的Not Saved指的是项目中通过代码生成的各种资源记录。如上图所示，其Mesh均为NGUI插件通过脚本生成的UI界面Mesh资源。

 **Q4：如图，在Editor中查看Profiler里的内存详细信息，发现Used Total中有个“Unity”，请问是什么意思？为什么会特别大？**

  

![](http://upload-images.jianshu.io/upload_images/17266280-ff4bf509ff4ec558.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

在Editor中运行时，“Unity”大是正常的，因为在Editor中运行项目时，引擎包含了所有的资源占用的内存（除了部分纹理和Mesh是在GFX中），同时自身会进行很多的辅助操作来记录各种游戏运行信息。一般来说，在查看游戏运行时的真实消耗内存，我们均是推荐直接在发布游戏上通过Profiler进行查看，在Editor中运行游戏所看到的内存是要大很多的。

 **Q5：不太明白Profiler中ManagedHeap.UsedSize是什么，以及这个参数的意义何在？是否重要？**

ManagedHeap.UsedSize是项目逻辑代码在运行时申请的堆内存，该选项只能通过优化代码来进行降低。 优化方法一般如下：

尽可能地复用变量，减少new的次数；

使用StringBuilder代替String连接，使用for代替foreach；

对于局部变量或非常驻变量，尽可能使用Struct来代替Class。

ManagedHeap.UsedSize过大，一方面可能会影响一次GC的耗时；另一方面也可能反映出脚本中不合理的GC Alloc。

 **Q6：System.ExecutableAndDlls占内存巨大，且一直在增长，这个属于正常情况吗？**

System.ExecutableAndDlls该项显示的是执行文件和所调用的库（物理、渲染、IO等系统库）的总和。开发团队不用太担心该选项的数值，因为很多应用均在共用这些库，并且它对于真实项目的内存压力非常小，几乎没有影响，而且OS也不会因为该内存而杀掉游戏或应用。

 **Q7：如下图：我在Profiler中看到这些没有引用的资源，他们是否还在内存中？**

  

![](http://upload-images.jianshu.io/upload_images/17266280-39136b3e9db47abe.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

是的，凡是在Unity Profiler中能看到的资源就会保留在内存中。对于这种资源，在切换场景时调一下UnloadUnusedAssets
API就可以释放。

**Q8：有没有办法可以减少游戏中Mono内存占用的大小？我现在读完游戏表以后就占用了60MB，我看其他游戏读完配置表也才10MB左右，这个是怎么做到的呀？**

如果刚进入游戏后，Mono堆内存就达到了60MB，那么你的游戏项目极有可能在一开始加载了一个非常大的配置表。对此，我们建议出现该问题的研发团队对配置文件的初始加载进行详细检测，查看是否可以精简配置文件信息。如果不行，则尝试将配置文件拆散，按需加载，从而降低Mono内存上升过快问题发生的概率。

 **Q9：我用Profiler.BeginSample统计到的数据与直接看Memory下的不一样，前者比后者的数据更大，这是为何？
用Profiler的API获取到的这一帧的内存消耗是85.6MB，而堆内存中显示的是62.9MB，这怎么理解？**

 **  
**

![](http://upload-images.jianshu.io/upload_images/17266280-ecd798a21703e3ce.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

**Profiler中数据**

  

![](http://upload-images.jianshu.io/upload_images/17266280-70398c7a597b7817.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

这种情况确实也是经常会遇到的。一帧中分配如此高的内存是会触发GC.Collect的，而Mono中显示的数值则是GC之后的Mono内存数值。

 **Q10：正常情况下游戏如果一直玩下去，Mono是不是会一直增加？ 比如频繁打开一个界面，界面里有脚本会不断创建一些东西
，那么Mono是否会不断增加？对性能上会不会造成影响呢？**

Mono 确实是不会下降，但并不应该一直上升。

创建出来的东西，如果被引用在一个容器里，或者被某些脚本的变量引用，那么这部分堆内存就释放不掉；但如果没有被任何容器或者变量引用（比如，临时拼一个
String），那么这部分堆内存会在 GC 的时候释放（释放是指变为空闲的堆内存，堆内存的总量是不会下降的）。

对于后者，频繁地 new 对象虽然不会一直增加堆内存，但是会加速 GC 调用的频率，所以同样是需要尽量避免的。

 **Q11：我想请教一下，下图这个函数中，每次我都申请了一个List temp =
list();在这里存放6KB的数据，但是如果不做GC处理，这6KB是否就一直累加，直到做GC处理了才会释放掉，是这样么？如果调用次数很多，每次都调用一点点，也会推高内存占用吗？**

  

![](http://upload-images.jianshu.io/upload_images/17266280-d5bdb48f3871a39a.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

是的，这个6KB堆内存会随着Update的执行一直分配内存，所累积的堆内存会在GC触发时进行销毁。一般来说，研发团队需要尽可能避免在高频次调用函数中进行堆内存的分配。

 **Q12：在进行内存优化时，Unity Profiler给出的数据和Android系统(adb dumpsys
meminfo,已经考虑memtrack的影响
)的数据差距较大（已经分析了Profiler自身的内存占用），如何分析这部分差异，比如包括对显存消耗进行准确统计，OS消耗的统计等等？**

内存差异较大是正常的，一般来说，Profiler统计的内存较为一致，而Android系统通过ADB反馈的PSS、Private
Dirty等值则是差别很大。这主要是因为芯片和OS的不同而导致。具体的Android内存，建议直接查看Google Android OS的相关文档。

Unity Profiler反馈的则是引擎的真实物理使用内存，一般我们都建议通过Profiler来查看内存是否存在冗余、泄露等问题。

 **Q13：已经预加载怪物，然后显示怪物 PSS上升，并且在隐藏怪物后并没有下降，这是什么原因导致？显存上去了吗？**

仅仅隐藏怪物的话，内存是不会下降的。因为隐藏只是改变了GameObject的状态，并没有对内存中的Object和资源进行移除。同时，即使是提前加载了怪物，也依然可能存在以上问题，因为某些资源是在显示的时候，才会传输一份到GPU的，比如Mesh。一般情况下，显存都不会即刻降低，这个是由Graphics
Driver来管理的。建议可以看Profiler是否增长，如果Profiler没有问题而PSS持续增长，就有可能发生了内存泄露。

对于这个问题，建议查看[《性能优化，进无止境---
内存篇（下）》](http://blog.uwa4d.com/archives/optimzation_memory_2.html)加深理解。

 **Q14：对于Handheld.PlayFullScreenMovie
这个Unity播放开场动画的API，会有内存问题吗？比如我的mp4动画有20MB，那么这个动画会撑高mono堆内存吗？**

Android上PlayFullScreenMovie
的实现实际上是通过Android原生的接口直接播放的，播放过程中Unity也是停止更新的，因此这部分的内存理论上并不会记录在 Unity
中，同样也不影响mono。

 **Q15：Texture占用内存总是双倍，这个是我们自己的问题，还是Unity引擎的机制？**

出现这种情况的原因有两种：一种是你在真机运行时开启了Read&Write。另一种可能是Unity的Bug，目前的Unity 5.2.3 release
note如下 ：

(735644) - OpenGL: Fixed texture memory usage reporting in profiler, was twice
the actual size for most textures.

开发者需要关注下自己的开发版本，5.2.3以前类似情况的项目可以参考一下。

 **Q16：如果脚本引用了GameObject，那转换场景的时候脚本和GameObject都没了，还会产生堆内存的吗？**

如果脚本是MonoBehaviour，而且在切换场景后所挂的Game Object被释放了，那么这个脚本对象所引用的堆内存就会在GC的时候被释放。
但有一种例外，如果是通过Static变量引用的堆内存，那么依然是释放不掉的，除非手动解开引用，比如变量置Null，数组Clear等等。

 **二、内存泄露 &冗余**

 **Q1：我们测试了下发现，在名为A的MonoBehaviour中，有个数组来存放名为B的
MonoBehaviour对象的引用。当我们其他的逻辑去Destroy了B对象所在的GameObject后，在A对象中的数组里，遍历打印，它们（B的引用）都为Null，在Inspector面板上看是missing。而这时候进行GC，堆内存其实并未释放这些B对象。只有当A对象中的数组被清空后，再调用GC，才可释放这些对象所占内存。这种现象是否正常？为什么值为Null但却还是被引用着，无法通过GC释放呢？**

首先这种现象是正常的。这是Unity中对Null的检测做了特殊的处理所致，在Unity中MonoBehaviour对象除了存在于Managed
Heap中（作为“壳”），在Native内存中还会有一个相对应的“实体”，在调用Destroy时，真正被释放的正是这个“实体”。而在判断一个MonoBehaviour对象是否为Null时，Unity会首先检测“实体”是否已经被销毁，如果是则返回为true，但此时Managed
Heap中的“壳”实际上依然是被引用的，从而就会出现对象的Null判断为true，但实际上还是被引用着，无法被GC释放的问题。

相关的细节可见官方blog对Unity中Null判断的解释：<http://blogs.unity3d.com/2014/05/16/custom-
operator-should-we-keep-it/>

 **Q2：字体作为多个资源的依赖包，会在游戏中被加载多次。我们现在有个问题，AssetBundle
A资源依赖于这个字体，加载A的时候加载了一份字体，然后B资源也依赖这字体，而后加载B的时候我们没有去重复加载字体，这时候发现B资源上出现了字体丢失的现象。请问加载资源的时候，Unity会自动去识别内存里是否有它的资源依赖包吗？如果有的话，为什么B加载的时候找不到已经存在内存中的字体？这里需要手动去做些什么处理吗？**

**同时我发现依赖包资源如果进行了bundle.m_AssetBundle.Unload(false)以后，其他依赖于这个包的资源就引用不到了。我们流程上对于每个读进来的AssetBundle，都会加载完后马上进行Unload(false)，请问如果是依赖包的话，是不是不能对其进行这步操作？**

Unity引擎是会自动根据依赖关系去搜寻依赖的资源的，但需要注意的是，依赖的AssetBundle文件必须存在。也就是说，依赖关系包如果后续还会使用的话，是不应该被Unload的，否则后续AssetBundle加载上来后，被依赖的资源是无法找到的。对于Unity
5.3之前的版本，出于内存的考虑，开发团队可以通过CreateFromFile或LoadFromCacheorDownload来加载AssetBundle，既可以保留AssetBundle之间的依赖关系，同时又不会产生Webstream。

开发团队可以参考[《你应该了解的AssetBundle管理机制》](http://blog.uwa4d.com/archives/ABTheory.html)，进一步了解相关API。

**Q3：我们的游戏玩了20分钟后，Texture2D的内存涨到了60MB多，并且重复的资源很多，是否由于没有卸载完全？还是打包AssetBundle依赖性的问题？用的是UGUI。**

 **  
**

![](http://upload-images.jianshu.io/upload_images/17266280-80a2cba6ed7f07c5.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

  

![](http://upload-images.jianshu.io/upload_images/17266280-3d11073d555935df.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

存在如下两个原因：

1、AB依赖关系打包存在问题，即atlas没有被依赖打包；

2、加载卸载的管理问题，可能是加载了一次后被一个Container索引了，这时又加载了一次同样的AssetBundle又被索引。如果这些一直没有释放，也会出现这种情况。

