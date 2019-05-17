---
title: Unity加载资源深度解析
thumbnail: http://upload-images.jianshu.io/upload_images/17266280-984777e717341c6d.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240
categories: Unity优化
tags: [Unity优化]
---

在游戏和VR项目的研发过程中，加载模块所带来的效率开销和内存占用（即“加载效率”、“场景切换速度”等）经常是开发团队非常头疼的问题，它不仅包括资源的加载耗时，同时也包含场景物件的实例化和资源卸载等。在我们看来，该模块的耗时是目前引擎中仅次于渲染的第二大模块。因此，我们认为非常有必要来跟大家分享一下目前加载模块的主要性能问题。

我们通过对提交到[www.uwa4d.com](http://www.uwa4d.com/)网站的大量项目进行分析，认为目前加载模块中最为耗时的性能开销可以归结为以下几类：
**资源加载、资源卸载、Object的实例化和代码的序列化等** 。今天，我们先为大家带来资源加载中纹理资源的加载性能分析。

这是侑虎科技第48篇原创文章，欢迎转发分享，未经作者授权请勿转载。同时如果您有任何独到的见解或者发现也欢迎联系我们，一起探讨。（QQ群465082844）

#  **资源加载**

资源加载是加载模块中最为耗时的部分，其CPU开销在Unity引擎中主要体现在Loading.UpdatePreloading和Loading.ReadObject两项中，相信经常查看Profiler的朋友对这两项肯定毫不陌生了。

Loading.UpdatePreloading，这一项仅在调用类似LoadLevel（Async）的接口处出现，主要负责卸载当前场景的资源，并且加载下一场景中的相关资源和序列化信息等。下一场景中，自身所拥有的GameObject和资源越多，其加载开销越大。

在很多项目中，存在另外一种加载方式，即场景为空场景，绝大部分资源和GameObject都是通过OnLevelWasLoaded回调函数中进行加载、实例化和拼合的。对于这种情况，Loading.UpdatePreloading的加载开销会很小。

Loading.ReadObject，这一项记录的则是资源加载时的真正资源读取性能开销，基本上引擎的主流资源（纹理资源、网格资源、动画片段等等）读取均是通过该项来进行体现。可以说，这一项很大程度上决定了项目场景的切换效率。正因如此，我们就当前项目中所用的主流资源进行了大量的测试和分析，下面我们将分析结果与大家一起分享，希望可以帮到正在进行开发的你。

**注意事项：本篇文章的资源性能分析主要是针对移动项目而言，因为目前UWA所测评的项目中，移动游戏/应用占比在90%以上。所以，我们选择首先在移动设备上针对每种资源的加载性能进行分析和总结。**

#  **资源加载性能测试代码**

以下为我们测试时所使用的测试代码，我们将每种资源均制作成一定大小的AssetBundle文件，并逐一通过以下代码在不同设备上进行加载，以期得到不同硬件设备上的资源加载性能比较。

 **  
**

![](http://upload-images.jianshu.io/upload_images/17266280-984777e717341c6d.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

**测试环境**

引擎版本：Unity 5.2版本

测试设备：五台不同档次的移动设备（Android：红米2、红米Note2和三星S6，iOS：iPhone 5 和 iPhone 6）

#  **纹理资源**

纹理资源是项目加载过程中开销占用最大的资源之一，其加载效率由其自身大小决定。目前，决定纹理资源大小的因素主要有三种：分辨率、格式和Mipmap是否开启。

 **1\. 分辨率 & 格式**

分辨率和格式是影响纹理资源加载效率的重要因素，因为这两项的设置对纹理资源的大小影响很大。因此，我们对这两种因素进行了详细的测试：

 **测试1：相同格式、不同分辨率的加载效率测试**

我们选取了两张分辨率为2048x2048的普通纹理资源，并在打成AssetBundle时，将其分辨率最大值分别设置为512x512、1024x1024和2048x20248，纹理格式均设置为ETC1（Android）和PVRTC（iOS）、且关闭Mipmap功能。所以，三组纹理的内存占用分别为256KB、1MB和4MB，其对应AssetBundle大小为156KB、531KB和1.92MB（对于Android平台）、175KB、628KB和2.4MB（对于iOS平台）。Unity
版本为5.2，压缩格式为默认的LZMA压缩。

Android平台测试纹理：

  

![](http://upload-images.jianshu.io/upload_images/17266280-9f7deef71a51a211.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

我们在五种不同档次的机型上加载这些纹理资源，为降低偶然性，每台设备上重复进行十次加载操作并将取其平均值作为最终性能开销。具体测试结果如下表所示。

  

![](http://upload-images.jianshu.io/upload_images/17266280-356ed3fa27b2aae3.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

通过上述测试，我们可以得到以下结论：

1、纹理资源的分辨率对加载性能影响较大，分辨率越高，其加载越为耗时。设备性能越差，其耗时差别越为明显；

2、设备越好，加载效率确实越高。但是，对于硬件支持纹理（ETC1/PVRTC）来说,中高端设备的加载效率差别已经很小，比如图中的红米Note2和三星S6设备，差别已经很不明显。

测试2：不同格式、相同分辨率的加载效率测试

我们选取了两张分辨率为1024x1024的普通纹理资源，并在打成AssetBundle时，根据不同平台将其纹理格式分别设置不同格式用于打包。对于Android平台，我们使用ETC1、ETC2、RGBA16和RGBA32四种格式，对于iOS平台，我们使用PVRTC
4BPP、RGBA16和RGBA32三种格式，同时，对于每张纹理均关闭Mipmap功能。所以，三组纹理的内存占用分别为1MB、1MB、4MB 和
8MB（Android平台）/1MB、4MB 和 8MB（iOS平台）。

Android平台测试纹理：

  

![](http://upload-images.jianshu.io/upload_images/17266280-ef0821de93838c63.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

与测试1相同，我们在五种不同档次的机型上重复进行十次加载操作并将取其平均值作为最终性能开销。具体测试结果如下图所示。

 **Android设备：**

 **  
**

![](http://upload-images.jianshu.io/upload_images/17266280-51c4a77564da0e0a.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

**iOS设备：**

  

![](http://upload-images.jianshu.io/upload_images/17266280-04244ab0fe899ee7.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

通过上述测试，我们可以得到以下结论：

1、纹理资源的格式对加载性能影响同样较大，Android平台上，ETC1和ETC2的加载效率最高。同样，iOS平台上，PVRTC 4BPP的加载效率最高。

2、RGBA16格式纹理的加载效率同样很高，与RGBA32格式相比，其加载效率与ETC1/PVRTC非常接近，并且设备越好，加载开销差别越不明显；

3、RGBA32格式纹理的加载效率受硬件设备的性能影响较大，ETC/PVRTC/RGBA16受硬件设备的影响较低。

 **注意事项：这里需要指出的是测试中所使用的ETC1和ETC2纹理均为RGB
4Bit格式，所以对于半透明纹理贴图，需要两张ETC1格式的纹理进行支持（一张RGB通道，一张Alpha通道）。逐一加载两张ETC1格式的纹理，其加载效率要低于RGBA16格式，但可以通过加载方式来进行弥补。这一点我们将在后续文章中进行详细说明。**

 **2\. 开启Mipmap功能**

开启Mipmap功能同样会增大一部分纹理大小，一般来说，其内存会增加至原始大小的1.33倍。因此，我们对开启Mipmap功能前后的加载性能进行了详细的测试：

测试3：开启/关闭Mipmap功能的加载效率测试

我们仍然使用两张分辨率为1024x1024的普通纹理资源，分别使用ETC1格式、PVRTC格式、RGBA16格式和RGBA32格式（测试所用纹理与测试2相同），并在打成AssetBundle时，一组开启Mipmap功能，一组关闭Mipmap功能。

与测试1相同，我们在五种不同档次的机型上重复进行十次加载操作并将取其平均值作为最终性能开销。具体测试结果如下图所示。

 **Android平台：**

 **  
**

![](http://upload-images.jianshu.io/upload_images/17266280-0ee8eec1b7cff964.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

**  
**

![](http://upload-images.jianshu.io/upload_images/17266280-7980b411d2e5cb4e.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

**iOS平台：**

 **  
**

![](http://upload-images.jianshu.io/upload_images/17266280-b87dd0660665d453.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

  

![](http://upload-images.jianshu.io/upload_images/17266280-3eb5145b2e723623.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

通过上述测试，我们可以看出：  **开启Mipmap功能会导致资源加载更为耗时，且设备性能越差，其加载效率影响越大。**

通过以上性能测试，我们对于纹理资源的加载建议如下：

1、严格控制RGBA32和ARGB32纹理的使用，在保证视觉效果的前提下，尽可能采用“够用就好”的原则，降低纹理资源的分辨率，以及使用硬件支持的纹理格式。

2、在硬件格式（ETC、PVRTC）无法满足视觉效果时，RGBA16格式是一种较为理想的折中选择，既可以增加视觉效果，又可以保持较低的加载耗时。

3、严格检查纹理资源的Mipmap功能，特别注意UI纹理的Mipmap是否开启。在UWA测评过的项目中，有不少项目的UI纹理均开启了Mipmap功能，不仅造成了内存占用上的浪费，同时也增加了不小的加载时间。

4、ETC2对于支持OpenGL ES3.0的Android移动设备来说，是一个很好的处理半透明的纹理格式。但是，如果你的游戏需要在大量OpenGL
ES2.0的设备上进行运行，那么我们不建议使用ETC2格式纹理。因为不仅会造成大量的内存占用（ETC2转成RGBA32），同时也增加一定的加载时间。下图为测试2中所用的测试纹理在三星S3和S4设备上加载性能表现。可以看出，在OpenGL
ES2.0设备上，ETC2格式纹理的加载要明显高于ETC1格式，且略高于RGBA16格式纹理。因此，建议研发团队在项目中谨慎使用ETC2格式纹理。

 **  
**

![](http://upload-images.jianshu.io/upload_images/17266280-ca0edc6345efdbd5.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

**正是由于以上加载效率问题，我们在UWA测评报告中加入了对每个检测到的纹理资源参数的详细展示，以方便开发团队可以快速查看资源的使用情况，只需对相关信息列进行排序，即可定位引发性能问题的具体资源。**

 **  
**

![](http://upload-images.jianshu.io/upload_images/17266280-b271fe2982298c1f.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

**说明：以上测试数据为我们所用的测试纹理加载数据，需要指出的是，不同纹理的加载效率是不相同的，因为其内容的不同会造成AssetBundle压缩包大小的不同，进而造成最终加载效率的不同。这里我们给出的具体性能比较，其本意是让大家通过数据直观了解到纹理格式、分辨率和Mipmap功能对加载性能的影响。另外，我们后续会进行更多的测试，以期为大家提供更为普遍的测试结果。**

以上为纹理资源在加载时的性能测试。关于加载模块的性能问题，
**我们会不断推出网格、音频等其他资源的加载性能分析、资源卸载性能分析、资源实例化性能分析、不同加载方式的性能分析等一系列技术文章**
，并对目前UWA所检测过项目的共性问题进行总结，以期让大家对项目的加载效率有更加深入的认知，并提升对加载模块的掌控能力。

