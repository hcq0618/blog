---
title: UGUI一个优化效率小技巧
thumbnail: http://upload-images.jianshu.io/upload_images/17266280-cbac9b6a4fcf7076.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240
categories: Unity优化
tags: [Unity优化]
---

无意间发现了一个小技巧。如下图所示，可以发现UGUI的Image组件的RaycastTarget勾选以后会消耗一些效率，为了节省效率就不要勾选它了，不仅Image组件Text组件也有这样的问题。
一般UI里也就是按钮才需要接收响应事件，那么大部分image和text是是不需要开RaycastTarget的。

  

![](http://upload-images.jianshu.io/upload_images/17266280-cbac9b6a4fcf7076.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

但是问题就来了，Unity默认在hierarchy窗口Create-UI-Image 、Text的时候就会自动帮我们勾选上RaycastTarget，
一个复杂点的界面至少也300+个Image和Text， 总不能一个个取消吧。 所以我们可以重写Create-UI-Image的事件。

  

![](http://upload-images.jianshu.io/upload_images/17266280-3d0147f90b0733ee.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

 ```
[MenuItem("GameObject/UI/Image")]



 static void CreatImage()



 {



 if(Selection.activeTransform)



 {



 if(Selection.activeTransform.GetComponentInParent<Canvas())



 {



 GameObject go = new GameObject("image",typeof(Image));



 go.GetComponent<Image().raycastTarget = false;



 go.transform.SetParent(Selection.activeTransform);



 }



 }



 }
```

 这样创建出来的Image就不带 RaycastTarget,Text组件原理同上。 Unity版本5.3.3

 **作者：雨松MOMO**

