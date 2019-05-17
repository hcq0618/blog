---
title: unity性能优化
thumbnail: http://upload-images.jianshu.io/upload_images/17266280-7fb41c46969884b9.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240
categories: Unity优化
tags: [Unity优化]
---

#  **资源管理**  

**Q：我们图标现在是制作成图集后再使用的，但是当图标数量很多的时候，图集的膨胀就很厉害了。对此我们的做法有两种：1）拆为多个图集；**

 **2）不再使用图集转而使用UITexture来使用。请问UWA有什么建议呢？**

使用图集的主要缺点在于内存较大，且管理不便；而使用UITexture的主要缺点在于产生的Draw Call较多（每个UITexture都会产生一个Draw
Call且无法拼合），影响运行效率。因此，如果同时出现在屏幕上的图标不多，即UITexture所产生的Draw
Call数量不大时，可以考虑直接使用；但如果图标数量较多，且目前项目的Draw
Call已经较高，那么我们依然建议继续使用图集，按照一定的规则拆分为若干组，从而将 Draw Call控制在较低的范围内。

 **Q：粒子系统的Prewarm主要用来做什么的，这个怎么优化呢？**

![](http://upload-images.jianshu.io/upload_images/17266280-7fb41c46969884b9.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

ParticleSystem.Prewarm的出现表示当前加载、激活或者首次渲染的粒子系统开启了"Prewarm"选项，而开启该选项的粒子系统在加载后会立即执行一次完整的模拟。以“火焰”为例，Prewarm开启时，加载后第一帧即能看到“大火”，而不是从“火苗”开始逐渐变大。但Prewarm的操作通常都有一定的耗时，建议在可以不用的情况下，将其关闭。

**Q：我们为了降低像素填充就限制了最大分辨率，但是发现限制之后NGUI的字体显示就变得模糊了。是否可以避免NGUI字体模糊呢？下图是我们在小米5上测试得到的结果：低分辨率下文字就模糊了。**

![](http://upload-images.jianshu.io/upload_images/17266280-2861f09ace9e3d1a.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

从开发团队提供的图片上看，小米5上的低分辨率用的是983x552，相当于将原来的画面的四分之一分辨率。此时，降低分辨率的做法可以理解为把983x552的纹理拉伸后贴到1920x1080的屏幕上，而“贴”的过程还会涉及到重新采样，因此造成模糊是正常的，而不仅仅是文本。只是文本的边缘对比度较高，拉伸后变糊的现象会更加明显。

我们建议尝试通过RenderTexture来控制不同内容的分辨率，对于UI部分尽量不要把分辨率降得太低。

**Q：打包AssetBundle的时候，我发现切换场景时，即使打同一个场景的AssetBundle，它们的Hash值都是不一样的，可能是什么原因造成的呢？**

在不同的场景下打包同一个资源或场景时，如果出现AssetBundle的差异，目前很可能是Shader
Stripping造成的，其原理可见文档：<https://docs.unity3d.com/Manual/class-
GraphicsSettings.html>

简单来说就是根据当前场景对Shader进行简化，因此如果打包时包含的场景的Lightmap或Fog设置不同，打出来的AssetBundle包也有可能是不同的。可以尝试通过把Graphics
Settings中的Shader Stripping设置进行修改来避免这个问题。

**Q：当UI关闭后，Texture图片却还留在内存，是下次垃圾回收或者Resources.UnloadUnusedAssets调用的时候就会清除吗？如果想立即清除，该如何操作？**

垃圾回收并不会卸载内存中的资源，而Resources.UnloadUnusedAssets是可以的，但前提是纹理资源已经不再被其他Object引用。如果要立即清除，可以尝试直接调用Resources.UnloadAsset来进行卸载。

 **Q：我们的游戏中，不透明渲染在总体渲染里占比较高，主要的开销在于 MeshSkinning.Render 部分，这部分的Draw
Call过高，共有65个， 请问该如何优化呢？**

默认情况下Skinned Mesh是无法合并Draw Call的，从而导致Draw Call过高的问题。 我们建议尝试通过
SkinnedMeshRenderer的BakeMesh接口，将蒙皮动画转为网格序列帧，同时确保顶点属性的数目符合动态拼合的条件，从而降低这部分的Draw
Call。另外，这种做法也可以降低MeshSkinning.Update以及Animator.Update的CPU耗时，只是网格序列帧会占用较大的内存，研发团队可以尝试做一个评估。

 **Q:预设中的变量，拖拽到Inspector面板和Transform.find这两种方法对加载影响是一样的吗？**

对加载性能有微小的不同。Transform.Find
是可以灵活控制调用时机的，可以真正要用的时候再进行Transform.Find，这样GameObject被实例化时效率会更高一些
。但如果拖上去，GameObject被实例化时，该变量就需要进行序列化。因此，加载和实例化时两者的性能会存在一些微小的变化。

  

![](http://upload-images.jianshu.io/upload_images/17266280-b77a817a400c9202.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

![](http://upload-images.jianshu.io/upload_images/17266280-c9b9dd614f4f20d8.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

![](http://upload-images.jianshu.io/upload_images/17266280-752a890121644eaf.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

![](http://upload-images.jianshu.io/upload_images/17266280-f855e9770472a5af.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

![](http://upload-images.jianshu.io/upload_images/17266280-5a4319cb87d9cb13.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

# **UI**

 **Q：我发现当把UI挪到屏幕外时，Draw Call不会减少，只有设置Enabled去掉才能减少。UI是没有遮罩剔除这类功能吗？
那是否意味着ScrollRect只能自己做动态加载或者动态设置Enabled之类的优化了？**

因为UGUI合并网格时是以Canvas为单位的，所以只把一部分UI元素移除屏幕并不能降低Draw Call，在Unity 5.2版本以前需要满足两点：

1． 使用Screen Space – Camera 的 Render Mode；

2． 需要将移出的UI元素放在独立的Canvas中，然后整体移出屏幕。

但在Unity 5.2版本之后，上述方法也已经失效。

因此我们建议，在移出后，通过将Canvas的Layer修改为相机Culling Mask中未选中的Layer来去除这部分多余的Draw Call，>
但这种方法同样需要将移出的UI元素放在独立的Canvas中。这种方法，相比Enabled的设置，可以减少一定的CPU开销。而对于ScrollRect，如果包含的UI元素较多，确实需要自己做动态加载和动态设置Enabled来进行优化。

 **Q：UI展示动画时，使用Mask做和使用UI本身做 ，哪个效率会更高些?**

一般来说建议尽可能少用Mask组件，该组件的使用对于Draw Call会有较大的影响，也可尝试用 Rect2D
Mask来代替。而如果直接通过改变UI元素本身来做动画，当涉及的UI元素数量较大时，容易引起较高的网格重建开销。

**Q：GameObject.Instantiate()每实例化一个GameObject到场景中，会造成卡顿，有什么办法可以优化吗？就算我采用了异步加载，仍然会有稍许的卡顿感。除了缓存池，是否还有别的方法？**

建议研发团队先通过Unity
Profiler来确定该性能卡顿的位置。如果只是一个空的GameObject，Instantiate实例化是很快的。一般来说，Instantiate实例化时间较长，主要由以下三个原因：

（1）与资源的加载有关：对于这种情况，研发团度需要精简资源，或者预加载资源来降低实例化的开销；

（2）序列化信息比较多：当GameObject上的Component比较多时，其Instantiate实例化性能会受到影响，比如说粒子系统，这种情况就只能通过分帧实例化，或者通过缓存池来避免；

（3）自定义组件的Awake：在Instantiate实例化时，其GameObject上挂载脚本的Awake函数也会被触发，其中产生的CPU占用，也会被计算在Instantiate实例化内。

