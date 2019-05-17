---
title: 从Android读取Unity-assets下的图片并保存为Bitmap格式
thumbnail: 
categories: Unity
tags: [Unity]
---

在unity工程下，建立文件夹“Plugins/Android/assets”，然后把需要的图片放在这个文件夹下，并取一个好用的名字

（"Logo.png"），这个名字在Android这边是需要用到的，unity的工作做完之后，在Android这边写代码：

```
AssetManager asm = getAssets();

InputStream inputStream =null;

 try {

     inputStream = asm.open("Logo.png");

 }catch (IOException e) {
     // TODO Auto-generated catch block

    e.printStackTrace();
}

Drawable d =Drawable.createFromStream(inputStream,null);

Bitmap B = ((BitmapDrawable) d).getBitmap();
```

这样就完成了unity图片的读取与转化Bitmap。

