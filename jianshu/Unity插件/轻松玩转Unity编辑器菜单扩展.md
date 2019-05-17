---
title: 轻松玩转Unity编辑器菜单扩展
thumbnail: http://upload-images.jianshu.io/upload_images/17266280-2574a078728d4094.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240
categories: Unity插件
tags: [Unity插件]
---

Unity一个很强大的功能就是可扩展，你可以利用该功能创建出各种各样的工具，直接整合到Unity中使用。今天这篇文章将为大家全面介绍扩展Unity中所有菜单项的方法及各菜单项的适用场景。

# 介绍

Unity编辑器中可扩展的菜单总览如下图：

  

![](http://upload-images.jianshu.io/upload_images/17266280-2574a078728d4094.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

这些菜单分别是：

编辑器顶部的内置菜单（A、B、C、D）

层级视图右键弹出菜单（B）

项目视图右键弹出菜单（A）

检视面板中点击Add Component按钮弹出的菜单（C）

编辑器顶部的新菜单项（E）

扩展菜单项，只需在静态方法前添加[MenuItem]属性声明即可，使用该属性需要引用UnityEditor命名空间。该方法是否公有、返回类型及方法名称均无关紧要。

例如，在静态方法前添加[MenuItem(“Window/Custom SubMenu/Custom Window”)]即可实现如下效果：

  

![](http://upload-images.jianshu.io/upload_images/17266280-ee8e75f5235f3f0b.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

关于MenuItem路径参数的几点说明：

如果根目录已存在于菜单项中（如“Assets”、“Window”等），那自定义菜单项将被添加到这些菜单下（“Component”除外）

必须要指定根目录及菜单项名称

菜单及菜单项名称均支持包含空格

还可以在菜单项名称后添加某个按键代码来指定该菜单项的快捷键

子菜单没有层级限制

例如，添加以下代码：

  

![](http://upload-images.jianshu.io/upload_images/17266280-cebae67b5eb3a0e3.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

然后依次点击菜单项GameObject > Create RedBlue GameObject，就会在场景中新建名为“RedBlue
GameObject”的游戏对象。

另外MenuItem还可支持多个参数：

  

![](http://upload-images.jianshu.io/upload_images/17266280-d1afa5e64cb0d5c8.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

其中参数isValidateFunction决定是否启用菜单项，设为True时，如果函数返回值为真，则菜单项启用，函数返回值为假则禁用菜单项。参数priority决定了菜单项在菜单中显示的优先级。

# 何时使用哪种菜单

由于对菜单的使用没有严格的限制，这就需要开发者们了解各项菜单原本的目的。下面就来看看什么时候要用什么菜单。

## A

## Assets

Assets菜单用于在项目中创建或修改资源。在项目视图中右键点击也会弹出Assets菜单。另外，如果将自定义菜单项放在“Assets/Create”目录下，点击项目视图的“Create”按钮时也会出现该自定义的菜单项。

  

![](http://upload-images.jianshu.io/upload_images/17266280-5a36da78cea5bf13.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

什么情况下适合使用Assets菜单呢：

新建ScriptableObject，所有自定义的ScriptableObject都可以通过Assets >  Create子菜单来创建

重命名精灵图集，右键点击包含多个精灵图片的纹理，用菜单项帮助快速重命名所有精灵图片

## B

## GameObject

GameObject菜单用于场景中与游戏对象息息相关的方法，如新建游戏对象或编辑已有对象等。右键单击项目视图也会显示GameObject子菜单，在层级视图点击Create按钮同样会显示GameObject子菜单。

如果希望自定义菜单项可以同时出现在右键弹出菜单和层级视图的Create按钮弹出的菜单中，就必须将该自定义菜单项放置在已有的菜单项中，如2D
Object或UI等。如果没有合适的已有菜单项，也可以自己新建菜单项并将优先级设为50以下。

  

![](http://upload-images.jianshu.io/upload_images/17266280-1f1db4d7b262c212.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

如果自定义工具是用于为游戏对象添加脚本，那最好还是放在Component菜单下。使用GameObject菜单的几种情况是：

新建预定义的游戏对象，例如预设体实例，你可以使用菜单项在新场景中设置好自定义相机

将选中的游戏对象存为预设体，该工具功能与GameObject下的Break Prefab Instance正好相反

## C

## Component

Component菜单下的所有菜单项都是用于为选中的游戏对象添加组件，为了加强该功能，Unity并不允许通过MenuItem向该菜单增加菜单项，而是使用[AddComponentMenu]属性，该属性直接用于自定义的MonoBehaviour类。点击菜单项会自动添加该脚本。

  

![](http://upload-images.jianshu.io/upload_images/17266280-929dbe33570900db.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

在脚本的类声明前添加[AddComponentMenu]属性，该脚本会同时出现在Component菜单以及在检视面板中查看游戏对象时点击Add
Component弹出的菜单中。该属性带有与MenuItem相同含义的路径参数，但不支持对自定义菜单项进行排序。

添加自定义菜单项后的Component菜单如下：

  

![](http://upload-images.jianshu.io/upload_images/17266280-0a3d2662b4790bca.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

## D

## Unity、File、Edit、Window以及Help

这几个菜单比较简单，其中的菜单项也不会出现在Unity编辑器的其它地方。需要打开新窗口的功能可以放在Window菜单中。需要同时修改游戏对象及资源的工具，如自定义的重复创建或重命名等，则放在Editor菜单中。Unity对此没有具体要求，你可以按照自己的习惯来布置。

## E

## 新建菜单项

如果已有菜单项均不适合自定义工具的功能，也可以自己新建一个菜单项。但Unity并不推荐在多人合作或共享资源的项目中新建菜单项，这可能会导致工具栏异常混乱。

  

![](http://upload-images.jianshu.io/upload_images/17266280-8ca12fc4c3ec0a5b.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

关于Unity编辑器上方工具栏各菜单的扩展就介绍到这里，后续我们再为大家介绍各个菜单项的优先级如何设置。

