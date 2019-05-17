---
title: Unity层级细节（LOD）的使用
thumbnail: http://upload-images.jianshu.io/upload_images/17266280-15edca7139c63fa6.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240
categories: Unity
tags: [Unity]
---

层次细节（LOD），它是根据物体在游戏画面中所占视图的百分比来调用不同复杂度的模型的。简单而言，就是当一个物体距离摄像机比较远的时候使用低模，当物体距离摄像机比较近的时候使用高模。这是一种优化游戏渲染效率的常用方法，缺点是占用大量内存。使用这个技术，一般是在解决运行时流畅度的问题，采用的是空间换时间的方式。

       下面我们分步骤来构造一个最简单的LOD模型示例：

步骤1：准备3组模型，高精度模型，中精度模型，和低精度模型，并按照复杂程度自高向低的为模型命名，如“模型名称LODO0”、“模型名称LOD1”等，最后的数字序号越低，表示复杂程度越高。如图所示：

  

![](http://upload-images.jianshu.io/upload_images/17266280-15edca7139c63fa6.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

步骤2：定义一个空对象，添加LODGroup组件，如图所示：

  

![](http://upload-images.jianshu.io/upload_images/17266280-ac1ef95d8ad8788d.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

步骤三：分别将刚刚准备好的三种不同精度的模型，拖拽到空对象的LODGroup组件的各个级别上。首先给LOD组件的“LOD 0”（LOD 0
表示摄像机最近距离显示）添加对应的模型。（LOD 0 对应高精度模型，然后拖拽到Add上面即可）如图所示：

  

![](http://upload-images.jianshu.io/upload_images/17266280-47d4129be8698e28.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

步骤四：在LOD组件添加模型的过程中会弹出如图所示的提示信息，表明要把添加的模型作为LODGroup组件所属对象的子物体，单击"Yes,Reparent"按钮即可。

  

![](http://upload-images.jianshu.io/upload_images/17266280-ef9a3684894163fe.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

步骤五：为使构造的LOD游戏对象显示得更加自然，需要把LOD下的三个子物体进行”对齐“处理。（将其相对于父物体的坐标置为0）如图所示：

  

![](http://upload-images.jianshu.io/upload_images/17266280-f768f15f9cf6a31b.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

步骤六：在Scenes视图中，拖动摄像机分别近距离与远距离观察模型的变化。

 **注：Project Settings中与LOD组件相关参数**

 **LOD Bias和Maximum LOD Level**

\- 执行unity编辑器菜单：Edit > Project Settings > Quality，会打开Quality Setting窗口
，找到Other下的参数，如图所示：

  

![](http://upload-images.jianshu.io/upload_images/17266280-bea640af550a16b2.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

Maximum LOD
Level：是最大LOD级别，表示游戏中使用的最高LOD级别。在该级别以上的模型不会被使用，并且在编译时忽略。（这将节省存储空间和内存空间）。

Bias LOD：LOD偏离
，LOD级别基于物体在屏幕上的大小。当物体大小在两个LOD级别之间，可以选择使用低细节模型或高细节模型。数值取值范围为0-1，数值越接近0，越偏向于选择低细节模型。大白话描述即是：如果该值小那么，摄像机离物体距离稍微有些变化，不同细节物体即会切换，该值大，那么摄像机需要与物体有很大的距离才会切换。

