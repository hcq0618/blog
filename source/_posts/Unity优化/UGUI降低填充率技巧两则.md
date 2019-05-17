---
title: UGUI降低填充率技巧两则
thumbnail: http://upload-images.jianshu.io/upload_images/17266280-b041b419a8fabe09.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240
categories: Unity优化
tags: [Unity优化]
---

Fill
Rate(填充率)是指显卡每帧每秒能够渲染的像素数。在每帧绘制中，如果一个像素被反复绘制的次数越多，那么它占用的资源也必然更多。目前在移动设备上，FillRate
的压力主要来自半透明物体。因为多数情况下，半透明物体需要开启 Alpha Blend 且关闭 ZTest和 ZWrite，同时如果我们绘制像 alpha=0
这种实际上不会产生效果的颜色上去，也同样有 Blend 操作，这是一种极大的浪费。因此，今天我们为大家推荐两则UGUI 降低填充率的技巧，希望大家能受用。

这是侑虎科技第50篇原创文章，感谢作者钱康来供稿。欢迎转发分享，未经作者授权请勿转载。同时如果您有任何独到的见解或者发现也欢迎联系我们，一起探讨。（QQ群465082844）

作者博客：[http://qiankanglai.me](http://qiankanglai.me/)

知乎专栏：<https://zhuanlan.zhihu.com/soulgame

在Unity中，与能直接看到的Verts/Tris/Batches数据不同，填充率并不能被直接统计到，但是我们可以通过查看OverDraw来大致查看：

  

![](http://upload-images.jianshu.io/upload_images/17266280-b041b419a8fabe09.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

对于UI来说，后者其实是很容易被忽视的热点(特别是对于中低端移动设备来说)。下面我就以具体两个例子为例，并探讨其解决思路。

#  **滥用不可见组件**

之前在Profile手头项目的时候发现红米上一个奇怪的现象：战斗界面维持60fps没问题；进入UI界面之后瞬间掉到45fps，甚至有的复杂界面掉到30fps。但战斗场景的Tris/Verts比UI高不少。

通过工具很方便的就定位到了瓶颈在于FillRate爆了，最后发现新手教学部分用了很多“不可见”的Image作为交互响应的控件；但这些东西虽然画上去没有效果，依然占用了显卡资源，特别是有很多大块的区域...找到问题之后就解决起来很方便：实现一个只在逻辑上响应Raycast但是不参与绘制的组件即可，改完之后帧率瞬间正常。

 ```
using UnityEngine;



 using System.Collections;



 namespace UnityEngine.UI



 {



     public class Empty4Raycast : MaskableGraphic



     {



         protected Empty4Raycast()



         {



             useLegacyMeshGeneration = false;



         }



         protected override void OnPopulateMesh(VertexHelper toFill)



         {



             toFill.Clear();



         }



     }



 }
```

这里顺便提一句，显卡资源消耗在没有到瓶颈的时候，大概是随着使用的增加正相关，但是到瓶颈之后很多时候是“崩盘”节奏。

#  **Polygon Mode Sprites**

在UI部分中我们会大量使用图片作为元素，如果图片边缘有大片留白就会和上面那个问题一样，产生很多无用填充。Unity和Texture
Packer目前都支持了Polygon
Mode，也就是说将原来的矩形Sprite用更加紧致的Polygon来描述，从而能更有效的利用空白空间(顺便也减小了打包出来的图资源)。

当然，目前Unity只在Sprite Render里支持了这个模式，在UGUI的Image中还无法正常使用。我自己实现了一个挂官方论坛[UGUI Image
with polygon sprites](http://forum.unity3d.com/threads/ugui-image-with-
polygon-sprites.390039/)，Texture Packer作者也表示很感兴趣~

  

![](http://upload-images.jianshu.io/upload_images/17266280-9f345dd7a0d7eb28.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

可以看到同样的一个图片，新的模式下顶点数变多了，但是绘制的范围变小了不少；同时在打包的时候图片也更加的紧致了，因为在不规则大图周围能塞进去不少小的元素。

下面这个脚本是针对Image的扩展，使其支持Polygon Mode Sprite...不过精力有限，只支持了Simple而且没做Preserve
Aspect，有兴趣的朋友如果实现了别的模式还望多多交流(主要是Filled和Sliced下要自己重新划分三角形，想想就麻烦...)

 ```
using System.Collections.Generic;



 namespace UnityEngine.UI



 {



     [AddComponentMenu("UI/Effects/PolygonImage", 16)]



     [RequireComponent(typeof(Image))]



     public class PolygonImage : BaseMeshEffect



     {



         protected PolygonImage()



         { }



         // GC Friendly



         private static Vector3[] fourCorners = new Vector3[4];



         private static UIVertex vertice = new UIVertex();



         private RectTransform rectTransform = null;



         private Image image = null;



         public override void ModifyMesh(VertexHelper vh)



         {



             if (!isActiveAndEnabled) return;



             if (rectTransform == null)



             {



                 rectTransform = GetComponent<RectTransform();



             }



             if (image == null)



             {



                 image = GetComponent<Image();



             }



             if (image.type != Image.Type.Simple)



             {



                 return;



             }



             Sprite sprite = image.overrideSprite;



             if (sprite == null || sprite.triangles.Length == 6)



             {



                 // only 2 triangles



                 return;



             }



             // Kanglai: at first I copy codes from
Image.GetDrawingDimensions



             // to calculate Image's dimensions. But now for easy to read, I
just take usage of corners.



             if (vh.currentVertCount != 4)



             {



                 return;



             }



             rectTransform.GetLocalCorners(fourCorners);



             // Kanglai: recalculate vertices from Sprite!



             int len = sprite.vertices.Length;



             var vertices = new List<UIVertex(len);



             Vector2 Center = sprite.bounds.center;



             Vector2 invExtend = new Vector2(1 / sprite.bounds.size.x, 1 /
sprite.bounds.size.y);



             for (int i = 0; i < len; i++)



             {



                 // normalize



                 float x = (sprite.vertices[i].x - Center.x) * invExtend.x +
0.5f;



                 float y = (sprite.vertices[i].y - Center.y) * invExtend.y +
0.5f;



                 // lerp to position



                 vertice.position = new Vector2(Mathf.Lerp(fourCorners[0].x,
fourCorners[2].x, x), Mathf.Lerp(fourCorners[0].y, fourCorners[2].y, y));



                 vertice.color = image.color;



                 vertice.uv0 = sprite.uv[i];



                 vertices.Add(vertice);



             }



             len = sprite.triangles.Length;



             var triangles = new List<int(len);



             for (int i = 0; i < len; i++)



             {



                 triangles.Add(sprite.triangles[i]);



             }



             vh.Clear();



             vh.AddUIVertexStream(vertices, triangles);



         }



     }



 }
```

这个做法是用顶点数来换填充率，具体是否这么干还要看项目本身的瓶颈。这一点在官方论坛的帖子里我也和别人讨论过，这里就不再赘述了。

