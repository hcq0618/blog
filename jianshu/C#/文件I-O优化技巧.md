---
title: 文件I-O优化技巧
thumbnail: http://upload-images.jianshu.io/upload_images/17266280-f7ec40182cd55f8d.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240
categories: C#
tags: [C#,C#优化]
---

一般来说，所有工程都会有对文件进行读写的操作。如果你不仅是要存储少量字节（例如JSON文件），就有必要考虑性能问题了。因为这种情况下很容易写出低效率的文件读写代码，而且编译器和Unity都无法帮助你优化。今天这篇文章将分享文件读写代码中一些常见的误区，希望对大家有所帮助。

.NET
API提供了很多完善的写入文件系统相关的类。Stream抽象类和其子类FileStream，还有File类，带有静态函数Open以及很方便的读写函数如BinaryReader和BinaryWriter。C#语言本身提供了using语法可以方便地关闭文件流、文件读写对象实例和文件句柄。这类代码使用便利，安全系数高，容易实现：

  

![](http://upload-images.jianshu.io/upload_images/17266280-f7ec40182cd55f8d.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

基本来说，文件操作可以归纳为以下五个步骤：

打开文件：File.Open

读取字节：stream.Read

写入字节：stream.Write

查询位置： stream.Position 或 stream.Seek

关闭文件：stream.Dispose 或 stream.Close

如果反编译FileStream类，你会发现stream.Position和stream.Seek其实没有什么区别，仅仅是API叫法上的不同。还有，stream.Dispose和stream.Close也基本上没什么区别，都能关掉文件。

得益于streams，readers，writers的便利性，想要测试它们的性能也很方便。进行读写操作只需调用一个函数即可，但这些读写操作函数的性能消耗可大不相同。接下来我针对这些不同的读写方式写了一个测试程序，下面是程序将要做的工作：

写入20MB，每次写入4KB的数据块

写入20MB，每次写入1字节

读取20MB，每次读取4KB的数据块

读取20MB，每次读取1字节

数次查找流的某个位置，次数与数据块的读写次数相同

数次打开某个文件，次数与数据块的读写次数相同

测试脚本如下：

  

![](http://upload-images.jianshu.io/upload_images/17266280-d4978bbf7a7a7a23.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

  

![](http://upload-images.jianshu.io/upload_images/17266280-7ff0719f2b05e64c.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

  

![](http://upload-images.jianshu.io/upload_images/17266280-af728080f4ee40c6.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

新建Unity工程，在Assets目录下新建TestScript.cs脚本并复制以上代码。然后在默认的空场景中将TestScript附加到Camera游戏对象上，最后编译。注意编译平台使用64位，在非Development模式下编译，画质设置为最快，分辨率设为最低（640x480）。测试环境如下：

2.3 Ghz Intel Core i7-3615QM

Mac OS X 10.11.2

Apple SSD SM256E, HFS+ format

Unity 5.3.0f4, Mac OS X Standalone, x86_64, non-development

640×480, Fastest, Windowed

测试结果如下：

  

![](http://upload-images.jianshu.io/upload_images/17266280-96b6695ea864c905.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

  

  

![](http://upload-images.jianshu.io/upload_images/17266280-4bf5935b1bc31318.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

  

  

![](http://upload-images.jianshu.io/upload_images/17266280-a4dd6d043419dc77.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

真是有着天壤之别，因此我单独提取出了最快的三个数据，得到了第二张图表。

可以看出，以数据块的方式进行读写操作的效率非常之高。虽然你可能不会一个一个字节地去写，但却有可能以4字节（整数）或类似大小为数据块单位进行写入操作。所以尽可能以较大的数据块为单位进行操作，这将提高38倍的写入效率，205倍的读取效率！

流查找（不论设置Position或调用Seek）不会进行字节读写，但这种操作是有代价的，虽然没有其它类型的操作那样多，它需要相当于读取4KB数据块三分之一的资源。所以最好避免这种查找操作，尽量线性读写文件，这样才能在各层面最大限度地发挥缓存的优势。

最后，打开或关闭文件同样不需要读取任何字节，但需要的时间会很长。事实证明，非常之长！打开和关闭文件需要的时间是以字节块写入整个文件所需时间的6.5倍，是字节块方式读取整个文件所需时间的40倍。考虑到读写操作的重要性，以及打开和关闭文件是操作系统的唯一需求，所以，除非特别需要，不要打开关闭文件。而且操作大文件要比操作多个小文件更好。

以上包括了关于I/O性能的一些建议，如有疑问，欢迎来下方评论区留言。

本文来源于：jacksondunstan.com

原作者：Jackson Dunstan

