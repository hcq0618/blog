---
title: unity图片mipmap
thumbnail: 
categories: Unity优化
tags: [Unity优化]
---

Mipmap技术有点类似于LOD技术，但是不同的是，LOD针对的是模型资源，而Mipmap针对的纹理贴图资源

使用Mipmap后，贴图会根据摄像机距离的远近，选择使用不同精度的贴图。

会占用内存，因为mipmap会根据摄像机远近不同而生成对应的八个贴图，所以必然占内存！

 **优点：** 会优化显存带宽，用来减少渲染，因为可以根据实际情况，会选择适合的贴图来渲染，距离摄像机越远，显示的贴图像素越低，反之，像素越高！

MipMap可以用于跑酷类游戏，当角色靠近时，贴图清晰显示，否则模糊显示

如果我们使用的贴图不需要这样效果的话，就一定要把Generate Mip Maps选项和Read/Write
Enabled选项取消勾选！因为Mipmap会十分占内存！

mipMap会让你的包占更大的容量！

下面来看下怎么设置贴图的mipmap：

设置贴图的Texture Type为Advanced类型 → 勾选Generate Mip Maps → Apply应用

来看看贴图的变化，可以看出生成了对应的8个Mip

那么贴图就会根据摄像机的远近，显示相应的贴图了！

