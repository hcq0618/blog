---
title: 使用link-xml来控制strippinglevel减少dll库大小技巧、优化安装包大小
thumbnail: 
categories: Unity优化
tags: [Unity优化]
---

无论从减少安装包大小还是迎合unity64位IL2CPP默认就会打开StrippingLevel功能，通过库剖离来减少DLL的空间大小。

那么问题是我们自定义库使用了一些type，例如xml，或者webclient c#封装的http请求等，如果被任性解剖出去，那么肯定是不允许的。

可以在Assets/下添加link.xml文件来手动排除不被剖离的类。

> <linker>

>

>       <assembly fullname="mscorlib">

>

>                 < fullname="System.Reflection" preserve="all"/>

>

>                 < fullname="System.Security.Cryptography" preserve="all"/>

>

>                 < fullname="System.Runtime.CompilerServices"
preserve="all"/>

>

>                 < fullname="System.Runtime.InteropServices" preserve="all"/>

>

>                 < fullname="System.Diagnostics" preserve="all"/>

>

>                 < fullname="System.Security" preserve="all"/>

>

>                 < fullname="System.Security.Permissions" preserve="all"/>

>

>       </assembly>

>

> </linker>

如上我们保持link.xml里面的格式这样既可
assembly其实就是dll库名，我们要排除这个dll库里面的1：整个命名空间；2：某个命名空间里面的某个具体类

补充针对排除整个命名空间可以这样加：

> <assembly fullname="JsonDotNet">

>

>                 <namespace fullname="Newtonsoft.Json" preserve="all"/>

>

> </assembly>

关于查看dll库可以用默认的mono编辑器或者vs点进目录文件分类的dll就能看见了。

关于如何知道什么类或者命名空间你需要添加进去link.xml，只能你使用这个特殊命名空间才知道了。或者你通过xcode debug出错、eclipse
debug真机运行时出错来查看那些类空间报错添加进去即可。

