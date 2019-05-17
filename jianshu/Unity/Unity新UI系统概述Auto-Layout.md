---
title: Unity新UI系统概述Auto-Layout
thumbnail: http://upload-images.jianshu.io/upload_images/17266280-b1546a28d27953a6.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240
categories: Unity
tags: [Unity]
---

Rect Transform拥有的布局系统对于各种类型的布局是足够灵活的，并且它也可以让你自由放置元素。但是，有时候更多结构化的东西是需要的。

自动布局系统提供了在嵌套布局组（如水平组、竖直组或者格子组）中放置元素的方法。它还允许元素根据包含的内容量自动调整大小。例如，一个按钮可以根据文本的内容自动缩放大小。

自动布局系统是一个构造在基本Rect Transform布局系统之上的系统。它可以选择性的对一些或全部元素使用。

# 理解布局元素

自动布局系统是基 **layout elements** （布局元素）和 **layout controllers**
（布局控制器）的。布局元素是一个含有RectTransform组件和其它可选组件的游戏对象。Thelayout element has certain
knowledge about which size it should
have.布局元素不能直接设置自己的大小，但是其它作为布局控制器的组件可以使用它们提供的信息用来为它们计算尺寸。

一个布局元素用下列属性来定义自身：

Minimun width（最小宽度）

Minimum height（最小高度）

Preferred width（首选宽度）

Preferred height（首选高度）

Flexible width（灵活宽度）

Flexible height（灵活高度）

使用布局元素提供信息的布局控制器的例子是 **Content Size Fitter** 和各种 **Layout Group**
组件。在布局组中如何按大小来布局元素的基本原则如下：

最开始只分配最小尺寸；

如果有足够的空间，分配首选尺寸；

如果有额外的空间，分配灵活尺寸；

含有RectTransform组件的任何游戏对象都可以作为布局元素使用。默认它们的最小、首选和灵活尺寸都是0。某些组件添加到游戏对象上后会改变这些布局属性值。

Image和Text组件就是两个会提供布局元素属性值的例子。它们会改变首选宽度和高度以匹配精灵或者文本内容。

# Layout Element组件

如果你想覆盖最小、首选或者灵活尺寸，你可以通过为游戏对象添加一个Layout Element组件来完成。

  

![](http://upload-images.jianshu.io/upload_images/17266280-b1546a28d27953a6.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

Layout Element组件可以让你覆盖一个或多个布局属性值。勾选对应控件，然后指定你需要覆盖的数值。

请参看Layout Element参考文档获取更多的信息。

# 理解布局控制器

布局控制器一些是用来控制一个或多个布局元素尺寸和位置的组件，它也含有Rect Trasnform组件。一个布局控制器可能控制它的 **own layout
element** （自己所在的同一个对象）或者控制 **child layout elements** 。

# Content Size Fitter（内容尺寸适应器）

Content Size Fitter用于控制自身布局元素的尺寸。查看自动布局系统执行方式的最简单方法就是增加一个Content Size
Fitter组件到含有Text组件的游戏对象上。

  

![](http://upload-images.jianshu.io/upload_images/17266280-63cb29fea819c29f.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

如果你将Horizontal Fit或Vertical Fit设置为Preferred Size，Rect
Transform组件就会自动调整它的宽或高以适应文本呢内容。

请参看Content Size Fitter相关参考文档。

# Aspect Ratio Fitter（纵横比适应器）

Aspcet Ratio Fitter用于控制自身布局元素的尺寸。

  

![](http://upload-images.jianshu.io/upload_images/17266280-652ca13ec7aee713.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

它可以让高度适应宽度，反之亦然，也可以让元素放在父对象的内部或者包裹父对象。Aspcet Ratio Fitter不会考虑最小尺寸和首选尺寸等布局信息。

请参看Aspect Ratio Fitter相关参考文档。

# Layout Group（布局组）

Layout Group是用来控制子布局元素的大小和位置的控制器。例如，水平的布局组将它的子对象相邻的放置，而格子布局组将它的子对象放在格子里。

布局组不能控制自己的大小。但可以作为一个布局元素被其它控制器控制或者手动设置。

不管布局组如何分配尺寸，大多数时候它都是试图用每一个子布局元素设置的minimum,preferred和flexible尺寸来分配适当数量的空间。布局组也可以任意嵌套。

请参看Horizontal Layout Group, Vertical Layout Group和Gird LayoutGroup相关的参考文档。

# 驱动Rect Transform属性

因为自动布局系统中的布局控制器会自动控制那些不能通过观察窗口或者场景窗口同时进行手动编辑的UI元素的尺寸和位置。而且这些被改变的值在下一次布局计算时会将被重新设置。

为了解决这个问题，Rect Transform有一个 **driven properties（被驱动属性）**
的概念。比如，将HorizontalFit属性设置到Minimum或者Preferred的Content Size Fitter组件会驱动同对象上Rect
Transform组件的宽度。这个宽度值变为只读并且在Rect Transform的顶端会出现一个小的信息框告知一个或多个属性值被content Size
Fitter驱动。

Rect
Transform属性被驱动除了避免手动编辑之外还有其它原因。仅仅是通过改变分辨率或者游戏窗口大小就会引起布局的改变。这反过来会改变布局元素的尺寸和位置，也就会改变被驱动属性的值。但是并不希望仅仅因为改变了游戏窗口的大小就会造成场景被标记为未被保存状态。为了避免这个问题，被驱动属性的值不会和场景一起保存并且他们的改变也不会引起场景数据的改变。

自动布局系统伴随着会使用一些内建的组件，但是它也可能用自定义的方式创建出新的组件来控制布局。这是通过能被自动布局系统的特殊组件接口来实现的。

如果执行了 **ILayoutElement** 接口，组件就会被自动布局系统当作一个布局元素来对待。

如果执行了 **ILayoutGroup** 接口，组件就会驱动子对象的RectTransform。

如果执行了 **ILayoutSelfController** 接口，组件就去驱动自身的Rect Transform。

自动布局系统会按下面的步骤计算并执行布局：

1\.
通过调用ILayoutElement组件上的CalculateLayoutInputHorizontal接口计算最小，首选和灵活的宽度。这是按从自下而上的顺序，即子对象比父对象先执行，这样的话，父对象才能拿到子对象的数据以便进行自身的计算；

2\.
布局元素的有效宽度被ILayoutController组件上的SetLaytouHorizontal接口计算并设置。这是自上而下进行的，即子对象在父对象之后计算，因为子对象的分配需要根据父对象完整的可用宽度来决定。这一步之后，布局元素的Rect
Transform会拥有新的宽度；

3\. 计算高度的最小，首选和灵活值，计算方法和第1步类似，只是接口为CalculateLaytouInputVertical；

4\. 计算高度的有效值，计算方法和第2步类似，只是接口为SetLaytouVertical。

# 触发布局的重建

当组件上的一个属性改变后，会导致当前的布局不再有效，就需要做一个布局的重计算。者会被这个调用触发：

LayoutRebuilder.MarkLayoutForRebuild(transformas RectTransform)；

这个重建不会立即发生，而是等到这帧的末尾，也就是渲染之前。不立即执行的理由是因为它会导致在同一帧内地进行多次潜在的布局重建，这会导致性能下降。

RectTransform刷新不及时的解决办法：

<http://www.tuicool.com/articles/AnQv2yB>

<http://www.xuanyusong.com/archives/4234>

会触发重建的时机为：

会改变布局的属性设置器(setters)；

这些回调函数种：

   OnEnable

   OnDisable

   OnRectRansformDimensionsChange

   OnValidate（只有编辑器状态需要，运行时不用）

   OnDidApplyAnimationProperties

unity的LayoutGroup分为三种， Horizontal Layout Group（水平布局）Vertical Layout
Group（垂直布局）Grid Layout Group （网格布局）
以前NGUI没有这东西都是自己写工具实现的。为什么我们要布局？我举个例子，布局的时候可以两个cell 和三个cell都居中显示。如下图所示。。

  

![](http://upload-images.jianshu.io/upload_images/17266280-fb7ab1de5cb71ef6.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

  

![](http://upload-images.jianshu.io/upload_images/17266280-62912cf4c377f0ef.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

尤其在奖励窗口，因为获取道具的数量是不固定的，所以需要根据不同数量的道具来居中对齐。如下图所示，Padding 就是偏移，因为我的cell 是
95X95，为了居中所以这里设置成 right = -95 top = -95。

Spacing 表示 cell之间的距离。

Child Alignment 表示对齐方式。

Child Force Expand 表示 自适应 宽 和高

  

![](http://upload-images.jianshu.io/upload_images/17266280-9a665ef5be3d3397.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

在看看cell，注意Layout Group节点下面的所有cell节点都是不能修改Rect
Transform的。因为cell可能下面会放很多图片，这样我们会用个空的gameObject来当父节点。但是这个gameObject的width 和
height 是最小单位，那么Layout Group就不知道怎么来算居中了。如下图所示 这个时候就轮到LayoutElement登场了，
用它来设置一个cell的最大或者最小宽度。

  

![](http://upload-images.jianshu.io/upload_images/17266280-693e3c907420c47b.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

如果运行时实例化后的gameObject 直接放在 Layout Group下面即可。Layout Group会自动计算布局，真的是非常方便。

> for(int i =0 ;i <10;i++){

>

> GameObject go = (GameObject)Instantiate(Resources.Load<GameObject>(“item”));

>

> go.transform.parent = transform;

>

> go.transform.localScale = Vector3.one;

>

> }

还有个问题就是隐藏，比如把其中的一个cell setActive = false ，为了不计算隐藏的cell 所以要先把 IngonreLaytout =
true 再 setActivity = false  这一切都可以在代码里面来设置。

  

![](http://upload-images.jianshu.io/upload_images/17266280-60beb071159428d2.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

代码这样即可。

> gameObject.GetComponent<LayoutElement>().ignoreLayout = true;

>

> gameObject.SetActive(false);

在unity3D4.6中加入了新的Transform 系统”Rect Transform”。新的Rect Transform对应的是以前旧版本的“
Transform  2D”。在这里不过多的介绍Rect Transform，今后我会在之后的文章中讲解到新的Rect Transform。

用过Rect Transform的人都知道，Rect
Transform中rect的Widh/Health并不能Set，于是这样就导致了Widh/Health不能动态的修改。这里我给大家提供一个方法，通过添加Aspect
Ratio Fitter/Content Size Fitter组件，来实现Widh/Health的动态变化。

# Aspect Ratio Fitter

Aspect Mode以什么样的模式去调整矩形的纵横比。

None不使用适合的纵横比。

Width Controls Height让Height随着width自动调节

Height Controls Width让width随着Height自动调节

Fit In Parent宽度，高度，位置和锚点被自动调整，以使该矩形拟合父物体的矩形内，同时保持高宽比。该可以是不包括在本RECT父矩形里面的一些空间。

Envelope Parent宽度，高度，位置和锚被自动调整，以使该矩形覆盖父的整个区域，同时保持高宽比。此矩形可能进一步延伸出，使他比父物体正确。

Aspect Ratio宽高比来执行。这是宽度除以身高。

# Content Size Fitter

Horizontal Fit用什么样的方法来控制宽度

None不使用任何基于布局元素的宽度。

Minimum使用基于布局元素的最小宽度的宽度。

Preferred使用基于布局元件的优选宽度的宽度。

Vertical Fit用什么样的方法来控制高度

None不使用任何基于布局元素的高度。

Minimum使用基于布局元素的最小高度的高度。

Preferred使用基于布局元件的优选高度的高度。

我个人比较习惯用Content Size
Fitter，只要管理好子物体的元素布局与大小就可以很好的控制Widh/Health。当然，在使用过程中，根据具体情况来选择适合的方法来实现动态的调整Widh/Health。

