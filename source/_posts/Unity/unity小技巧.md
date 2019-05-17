---
title: unity小技巧
thumbnail: http://upload-images.jianshu.io/upload_images/17266280-383e1d6dcaddd627.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240
categories: Unity
tags: [Unity]
---

>
大家使用Unity的经验都有多长呢？Unity编辑器中还有这样的隐藏功能你知道吗？本系列文章为大家介绍Unity使用小技巧，文末附上Unity大中华区Evangelist
Kelvin Lo录制的视频，希望对你有帮助。

# 技巧一

如果编辑器意外崩溃了，但场景未保存，这时可以打开工程目录，找到/Temp/_Backupscenes/文件夹，可以看到有后缀名为.backup的文件，将该文件的后缀名改为.unity拖拽到项目视图，即可还原编辑器崩溃前的场景。

  

![](http://upload-images.jianshu.io/upload_images/17266280-383e1d6dcaddd627.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

# 技巧二

所有数值类型的字段，都支持在检视面板中直接输入简单的数值表达式。

  

![](http://upload-images.jianshu.io/upload_images/17266280-222b5ebcea39205c.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

# 技巧三

好不容易才调好的坐标，结果发现是在运行模式下，如果退出运行模式就还原了怎么办？可以在检视面板右键点击组件名，在弹出界面中选择Copy
Component，然后退出运行模式后同样右键点击组件名，在弹出界面中选择Paste Component Values即可。

  

![](http://upload-images.jianshu.io/upload_images/17266280-bbcf90e0826c73bb.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

# 技巧四

分别按键盘键Q、W、E、R、T可以依次切换界面上的小工具。除此之外，按数字键2或3还可以切换场景为2D模式或3D模式。

  

![](http://upload-images.jianshu.io/upload_images/17266280-6595b299e70ee3ec.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

# 技巧五

右键点击检视面板下方的预览窗口即可让预览窗口跳出来，然后自己选择合适的地方停靠，这样切换模型查看就不会影响到其它面板。想让预览窗口回到原位，只需右键点击窗口，在弹出菜单中选择Close
Tab即可。

  

![](http://upload-images.jianshu.io/upload_images/17266280-89af173bc6ce8967.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

# 技巧六

在层次视图的搜索框中输入完整的脚本或组件名称，即可找到所有绑定了该脚本或组件的对象。或者在搜索框中输入t:加上某个类别如light，即可找到使用同类组件的对象。

  

![](http://upload-images.jianshu.io/upload_images/17266280-0009e8f22283ec6d.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

# 技巧七

如果想在检视面板查看脚本的私有变量，只需点击Inspectore，在弹出菜单中选择Debug即可。

  

![](http://upload-images.jianshu.io/upload_images/17266280-7c4beb4456aafe54.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

# 技巧八

如果希望游戏运行第一帧暂停，可以先点击暂停按钮，然后点击播放按钮，这样程序就会在Update函数执行一次后暂停。

  

![](http://upload-images.jianshu.io/upload_images/17266280-28a9505d9ba28170.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

# 技巧九

在使用Debug.Log函数时传递游戏对象给第二个参数，既可在点击控制面板的输出信息时自动定位到对应的游戏对象。

  

![](http://upload-images.jianshu.io/upload_images/17266280-24ffd5280b9d3b38.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

# 技巧十

可以借助编辑器自带的标记功能为脚本分类，在检视面板中点击脚本图标下方的小三角，即可为脚本设置颜色或选择图标。

  

![](http://upload-images.jianshu.io/upload_images/17266280-695983b115091045.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

>
上周为大家分享了两篇Unity小技巧介绍文章，不少开发者反应平时都忽视了这些技巧，原来编辑器已经默默帮大家实现了很多的快捷操作，今天继续为大家介绍第三篇。

# 技巧一

程序员们应该都知道，从项目视图点击右键创建的脚本会自动填充一些代码。其实这些自动填充的代码模板也是可以自定义的。

如果使用Mac，找到应用程序中的Unity.app，右键单击显示包内容，找到Resources>ScriptTemplates文件夹，然后选择你要创建模板的脚本类型，复制一份自己命名并编辑后保存，然后退出编辑器之后重新打开，再在项目视图中右键单击创建，就会出现刚刚添加的脚本类型。打开新建的脚本就可以看到自定义的模板代码。

  

![](http://upload-images.jianshu.io/upload_images/17266280-c318a69749613d6f.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

如果使用Windows，则在ProgramFiles(x86)或ProgramFiles目录下的Unity/Data/Resources/ScriptTemplates文件夹下进行同样的操作即可。

# 技巧二

如果发现Unity打包安卓平台生成的apk体积过大，可以找到PlayerSettings中的安卓平台，默认情况下Device
Filter设定为FAT(ARMv7+x86)，即同时打包32位和64位。如果只需发布到32位或64位平台则单独选择对应的一种即可。这样可以有效减小包体积。

  

![](http://upload-images.jianshu.io/upload_images/17266280-a9cd439b0d4a7b53.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

# 技巧三

在项目视图的搜索框中输入资源名称，可以找到项目中所有具有该关键字的资源。将搜索类型换成Asset Store，则可以找到Asset
Store上所有拥有该关键字的资源，并按免费和付费分类。

  

![](http://upload-images.jianshu.io/upload_images/17266280-9d3e2dd1a0db2f1e.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

# 技巧四

如果希望物体可以紧贴地面，但倾斜角度不好调整，这时可以在物体上添加Mesh
Collider和Rigidbody组件，然后点击运行，借助Unity的物体引擎来计算位置。待物体坠落到地面后复制所有物体，停止运行后删除原先的物体再粘贴运行时复制的内容，并删除所有物体上的Mesh
Collider和Rigidbody组件即可。

  

![](http://upload-images.jianshu.io/upload_images/17266280-0b863ab1c876e66e.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

# 技巧五

如果需要拼合两个物体，可以自己分别在两个物体上创建立方体当作锚点，按住V键进入顶点选择模式，然后选择锚定立方体上需要拼合的两个顶点，即可将物体无缝拼接在一起。

  

![](http://upload-images.jianshu.io/upload_images/17266280-458c81316b632f37.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

如果需要旋转物体，可以按下Cmd/Ctrl键后用鼠标操作旋转，这样可以让物体每次固定旋转15度，最终转到正确位置。

# 技巧六

在场景中按住右键可以以视点为中心查看整个场景。如果希望物体始终保持在焦点处，可以在层次面板双击该物体，然后按住Alt键后用鼠标查看周围场景，并且物体一直位于焦点。

  

![](http://upload-images.jianshu.io/upload_images/17266280-597f3f3c0226771a.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

# 技巧七

如果脚本出现错误，Unity编辑器会因为检查到出错而无法进入运行模式，这时可以在项目视图中新建文件夹WebplayerTemplates，然后将出错的脚本拖入此文件夹下，所有位于该文件夹下的文件都会被识别为一般文件从而不会当作脚本被编译，这样就可以运行游戏了。

  

![](http://upload-images.jianshu.io/upload_images/17266280-e7c8abe360ecc2a5.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

# 技巧八

如果你的鼠标的中键是可以按下的，可以按住鼠标中键来平移整个场景。或者将鼠标移至物体上后点击中键按钮，编辑器会以平移的方式将物体中心移动鼠标位置。

  

![](http://upload-images.jianshu.io/upload_images/17266280-065d0b5fb291f9ec.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

# 技巧九

当需要拖拽对象至检视面板时，常常会因为操作原因导致检视面板的内容已经改变了。这时可以点击检视面板右上方的锁图标，锁定检视面板，这样不论其它视图如何切换，检视面板都会显示固定内容。

  

![](http://upload-images.jianshu.io/upload_images/17266280-eaa48001c711ed6f.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

# 技巧十

如果编辑2D游戏的图片时总是不小心点选到背景，可以在Layer里边设置哪些层是锁定或不可见的，将背景层锁定后就不能点选到它了，这样在编辑时就不会出现误操作。但锁定图层后还是可以从层次面板上选中背景来进行调整，这样就不用每次反复锁定和解锁图层。

  

![](http://upload-images.jianshu.io/upload_images/17266280-887919e79d21b1cd.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

> 前面已经为大家分享了三篇Unity小技巧相关的文章，涉及到编辑器操作及脚本等多方面的内容，掌握这些小技巧能大大提高我们的开发效率。今天为大家介绍第四篇。

# 技巧一

在float型的字段前添加范围属性声明如[Range(0, 10)]，即可在检视面板中使用滑动条来设置该字段的值。

  

![](http://upload-images.jianshu.io/upload_images/17266280-cfe225ea88c6cb0d.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

# 技巧二

对一组字段使用属性声明[Heaader(“XX”)]，可以在检视面板中将字段进行分组。

  

![](http://upload-images.jianshu.io/upload_images/17266280-dc6953a52eb38e88.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

# 技巧三

从Unity 5开始，新建场景默认会带有天空盒，可以利用Unity自带的天空盒材质来自定义天空盒颜色。

  

![](http://upload-images.jianshu.io/upload_images/17266280-45a25960391ec1f6.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

# 技巧四

如果常常不小心进入播放模式后编辑场景内容，其实可以依次点击菜单项Edit > Preferences > Colors >
Playmode设置编辑器在进入播放模式后的颜色，与正常模式下明显区分开来。

  

![](http://upload-images.jianshu.io/upload_images/17266280-aa4b2c8ed63c3f06.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

# 技巧五

将鼠标聚焦于编辑器内的某个窗口，按住Shift＋空格键，可以将该窗口最大化至编辑器范围或者还原为原先大小。

  

![](http://upload-images.jianshu.io/upload_images/17266280-90e7ae8b57fa2d6c.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

# 技巧六

如果场景中某个物体与另一物体相对的位置、旋转及缩放均保持不变，那么在调整目标物体的方向时，可以先选中编辑器界面的小工具，按住Ctrl/Cmd＋Shift键，这样在操作其中一个物体时，另一个也会随之变化。

  

![](http://upload-images.jianshu.io/upload_images/17266280-ad63948a00b5479c.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

# 技巧七

如果脚本中有变量名打错，需要批量修改，在Mac上可以按住Cmd＋R键，Windows上按住F2键，然后选中需要修改的变量名进行批量修改。

  

![](http://upload-images.jianshu.io/upload_images/17266280-984cabf7583069b3.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

# 技巧八

使用UI中的Mask组件时，需要指定一张图片作为遮罩对其子对象进行裁剪，取消勾选组件上的Show Mask
Graphic则可以在保持裁剪效果的同时隐藏Mask本身的图片。

  

![](http://upload-images.jianshu.io/upload_images/17266280-ed6a8541142aa838.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

# 技巧九

在设置所有颜色类型的属性时，可以将当前颜色值加入预设，该预设会保存在本地且可以在不同的工程间共用。

  

![](http://upload-images.jianshu.io/upload_images/17266280-bb16d110b6d0a225.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

# 技巧十

你知道矩形工具也可以用来操作3D物体吗？

  

![](http://upload-images.jianshu.io/upload_images/17266280-00a3fc7051056781.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

![](http://upload-images.jianshu.io/upload_images/17266280-82ae6b06499c77f6.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

