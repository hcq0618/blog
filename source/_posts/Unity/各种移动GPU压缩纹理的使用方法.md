---
title: 各种移动GPU压缩纹理的使用方法
thumbnail: http://upload-images.jianshu.io/upload_images/17266280-a5b11ca81bf78d8c.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240
categories: Unity
tags: [Unity]
---

![](http://upload-images.jianshu.io/upload_images/17266280-a5b11ca81bf78d8c.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

# 1\. 移动GPU大全

目前移动市场的GPU主要有四大厂商系列：

## 1）Imagination Technologies的PowerVR SGX系列

  

![](http://upload-images.jianshu.io/upload_images/17266280-1e6e5e642b0c94bd.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

代表型号：PowerVR SGX 535、PowerVR SGX 540、PowerVR SGX 543MP、PowerVR SGX 554MP等

代表作 ：Apple iPhone全系、iPad全系，三星I9000、P3100等

## 2）Qualcomm(高通)的Adreno系列

  

![](http://upload-images.jianshu.io/upload_images/17266280-9ee4d1c5a8f505f9.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

代表型号：Adreno 200、Adreno 205、Adreno 220、Adreno 320等

代表作 ：HTC G10、G14，小米1、2等

## 3）ARM的Mali系列

  

![](http://upload-images.jianshu.io/upload_images/17266280-2c545ed953743eb1.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

代表型号：Mali-400、Mali-T604等

代表作 ：三星Galaxy SII、Galaxy SIII、Galaxy Note1、Galaxy Note2(亚版)等

## 4）nVIDIA(英伟达)的Tegra系列

  

![](http://upload-images.jianshu.io/upload_images/17266280-ae5934eb260ad1f1.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

代表型号：nVIDIA Tegra2、nVIDIA Tegra3等

代表作 ：Google Nexus 7，HTC One X等

  

# 2\. 压缩纹理的必要性

## 1）首先要说一下图像文件格式和纹理格式的区别。

常用的图像文件格式有BMP，TGA，JPG，GIF，PNG等；

常用的纹理格式有R5G6B5，A4R4G4B4，A1R5G5B5，R8G8B8, A8R8G8B8等。

文件格式是图像为了存储信息而使用的对信息的特殊编码方式，它存储在磁盘中，或者内存中，但是并不能被GPU所识别，因为以向量计算见长的GPU对于这些复杂的计算无能为力。这些文件格式当被游戏读入后，还是需要经过CPU解压成R5G6B5，A4R4G4B4，A1R5G5B5，R8G8B8,
A8R8G8B8等像素格式，再传送到GPU端进行使用。

纹理格式是能被GPU所识别的像素格式，能被快速寻址并采样。

举个例子，DDS文件是游戏开发中常用的文件格式，它内部可以包含A4R4G4B4的纹理格式，也可以包含A8R8G8B8的纹理格式，甚至可以包含DXT1的纹理格式。在这里DDS文件有点容器的意味。

OpenGL ES 2.0支持以上提到的R5G6B5，A4R4G4B4，A1R5G5B5，R8G8B8，A8R8G8B8等纹理格式，其中
R5G6B5，A4R4G4B4，A1R5G5B5每个像素占用2个字节(BYTE)，R8G8B8每个像素占用3个字节，A8R8G8B8每个像素占用 4个字节。

  

![](http://upload-images.jianshu.io/upload_images/17266280-afc478ca46e0683e.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

对于一张512*512的纹理的话，R5G6B5格式的文件需要占用512KB的容量，A8R8G8B8格式的文件需要占用1MB的容量；如果是1024*1024的纹理，则各需要2M和4M的容量，这对于动辄需要几十、几百张甚至更多纹理的游戏，上G容量的游戏在移动平台上是不容易被接受的(当然，还是有1、2G的大作的，里面包含了几千张的纹理)。

聪明的设计师们在想，有没有其他办法，既能表现丰富的色彩和细节，又能是最小失真的情况下，达到更小的纹理容量呢。压缩纹理格式应运而生(当然，并不是在移动平台后才有的产物)。

#  

# 3\. 常见的压缩纹理格式

基于OpenGL ES的压缩纹理有常见的如下几种实现：

1）ETC1（Ericsson texture compression)

2）PVRTC (PowerVR texture compression)

3）ATITC (ATI texture compression)

4）S3TC (S3 texture compression)

 **ETC1:**

ETC1格式是OpenGL ES图形标准的一部分，并且被所有的Android设备所支持。

扩展名为: GL_OES_compressed_ETC1_RGB8_texture，不支持透明通道，所以仅能用于不透明纹理。

当加载压缩纹理时， 参数支持如下格式：

GL_ETC1_RGB8_OES(RGB，每个像素0.5个字节)

 **PVRTC:**

支持的GPU为Imagination Technologies的PowerVR SGX系列。

OpenGL ES的扩展名为: GL_IMG_texture_compression_pvrtc。

当加载压缩纹理时， 参数支持如下几种格式：

GL_COMPRESSED_RGB_PVRTC_4BPPV1_IMG (RGB，每个像素0.5个字节)

GL_COMPRESSED_RGB_PVRTC_2BPPV1_IMG (RGB，每个像素0.25个字节)

GL_COMPRESSED_RGBA_PVRTC_4BPPV1_IMG (RGBA，每个像素0.5个字节)

GL_COMPRESSED_RGBA_PVRTC_2BPPV1_IMG (RGBA，每个像素0.25个字节)

 **ATITC:**

支持的GPU为Qualcomm的Adreno系列。

支持的OpenGL ES扩展名为: GL_ATI_texture_compression_atitc。

当加载压缩纹理时， 参数支持如下类型的纹理：

GL_ATC_RGB_AMD (RGB，每个像素0.5个字节)

GL_ATC_RGBA_EXPLICIT_ALPHA_AMD (RGBA，每个像素1个字节)

GL_ATC_RGBA_INTERPOLATED_ALPHA_AMD (RGBA，每个像素1个字节)

 **S3TC:**

也被称为DXTC，在PC上广泛被使用，但是在移动设备上还是属于新鲜事物。支持的GPU为NVIDIA Tegra系列。

OpenGL ES扩展名为:

GL_EXT_texture_compression_dxt1和GL_EXT_texture_compression_s3tc。

当加载压缩纹理时， 的参数有如下几种格式：

GL_COMPRESSED_RGB_S3TC_DXT1 (RGB，每个像素0.5个字节)

GL_COMPRESSED_RGBA_S3TC_DXT1 (RGBA，每个像素0.5个字节)

GL_COMPRESSED_RGBA_S3TC_DXT3 (RGBA，每个像素1个字节)

GL_COMPRESSED_RGBA_S3TC_DXT5 (RGBA，每个像素1个字节)

由此可见，Mali系列GPU只支持ETC1格式的压缩纹理，而且该纹理不支持透明通道，有一定局限性。

以上压缩纹理格式每个像素大小相对A8R8G8B8格式的比例，最高压缩比是16:1，最低压缩比是4:1，对于减小纹理的数据容量有明显作用，相应在显存带宽上也有明显优势，从而提高游戏的运行效率(此特性没有绝对数值，根据每个游戏的用法和瓶颈点不同而有差别)。

#  

# 4\. OpenGL中相关API的使用

## 1） 获得GPU的型号

> glGetString(GL_RENDERER)

## 2） 获得GPU的生产厂商

> glGetString(GL_VENDOR);

## 3） 获取GPU支持哪些压缩纹理

> string extensions = (const char*)glGetString(GL_EXTENSIONS);

a. 判断是否支持ETC1格式的压缩纹理

> return (extensions.find("GL_OES_compressed_ETC1_RGB8_texture")!=
string::npos);

b. 判断是否支持DXT格式的压缩纹理

> return (extensions.find("GL_EXT_texture_compression_dxt1")!= string::npos ||

>

> extensions.find("GL_EXT_texture_compression_s3tc")!= string::npos);

c. 判断是否支持PVRTC格式的压缩纹理

> return (extensions.find("GL_IMG_texture_compression_pvrtc")!= string::npos);

d. 判断是否支持ATITC格式的压缩纹理

> return (extensions.find("GL_AMD_compressed_ATC_texture")!= string::npos ||

>

> extensions.find("GL_ATI_texture_compression_atitc")!= string::npos);

## 4） 填充压缩纹理数据

> void glCompressedTexImage2D (

>

> GLenum target,

>

> GLint level,

>

> GLenum internalformat,

>

> GLsizei width,

>

> GLsizei height,

>

> GLint border,

>

> GLsizei imageSize,

>

> const GLvoid * data);

这里的参数不做详细解释，其中internalformat即是压缩纹理格式的类型。

#  

# 5\. 压缩纹理工具的使用

每种压缩纹理以及相应的厂商都提供了压缩纹理的工具，工具都分两个版本：

a. 可视化转换工具 (给美工或小白少量使用)

b. 命令行转换工具 (给程序批量使用)

下面对每个工具的用法进行说明。

## 1）Imagination Technologies PowerVR

工具下载地址

[http://www.imgtec.com/powervr/insider/sdkdownloads/index.asp?installer=W...](http://www.imgtec.com/powervr/insider/sdkdownloads/index.asp?installer=Windows%20Installer)

可视化转换界面

  

![](http://upload-images.jianshu.io/upload_images/17266280-35c50cd1fd618328.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

命令行转换脚本

> for %%i in (*.tga) do PVRTexTool.exe -f PVRTC4 -i %%i

(将本目录下的所有tga文件，转换成"PVRTC4"编码格式的pvr文件，不带mipmap)

详细使用说明：PvrTexTool.exe /?

## 2）Qualcomm Adreno

工具下载地址

[https://developer.qualcomm.com/mobile-development/mobile-
technologies/ga...](https://developer.qualcomm.com/mobile-development/mobile-
technologies/gaming-graphics-optimization-adreno/tools-and-resources)

可视化转换界面

  

![](http://upload-images.jianshu.io/upload_images/17266280-36c46a0c34eb288d.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

命令行转换脚本

> for %%i in (*.tga) do QCompressCmd.exe %%i %%i.ktx "ATC RGBA Explicit" yes

(将本目录下的所有tga文件，转换成"ATC RGBA Explicit"编码格式的ktx文件，带mipmap)

详细使用说明：QCompressCmd.exe /?

## 3）ARM Mali

工具下载地址

[http://malideveloper.arm.com/develop-for-mali/mali-gpu-texture-
compressi...](http://malideveloper.arm.com/develop-for-mali/mali-gpu-texture-
compression-tool/)

可视化转换界面

  

![](http://upload-images.jianshu.io/upload_images/17266280-4ebfa9d4786cd7a1.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

命令行转换脚本

> for %%i in (*.tga) do PVRTexTool.exe -f ETC -i %%i

(将本目录下的所有tga文件，转换成"ETC"编码格式的pvr文件，不带mipmap这里还是使用的PVRTexTool.exe，也可以使用QCompressCmd.exe)

详细使用说明：PVRTexTool.exe /?

## 4）nVIDIA Tegra

可以使用DirectX SDK中自带的DirectX Texture Tool进行转换

可视化转换界面

  

![](http://upload-images.jianshu.io/upload_images/17266280-b6363ea714f2057c.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

命令行转换脚本

> for %%i in (*.tga) do texconv.exe -f DXT5 %%i

(将本目录下的所有tga文件，转换成"DXT5"编码格式的dds文件，不带mipmap)

详细使用说明：TexConv.exe /?

本文来源： <http://www.cnblogs.com/luming1979/archive/2013/02/04/2891421.html>

 **主流纹理压缩标准：ETC、PVRTC、S3TC**

首先说OpenGL ES标准中的，2.0版规范中将ETC(Ericsson Texture
Compression)作为基本的纹理压缩标准，这是大部分移动GPU都会支持的纹理标准。OpenGL ES
3.0中还引入了ETC2、EAC纹理压缩格式，二者基本一致，只不过EAC主要用于1-2通道数据的情况。目前ECT2还在改进中，除了高通的Adreno
320之外还没有移动GPU支持，Tgera 4也不行。

此外，OpenGL ES 3.0中还有一种可选纹理压缩格式——ASTC(Adaptive Scalable Texture
Compression，自适应扩展纹理压缩)，这是ARM提出的，去年被Khronos组织认可，纳入到标准中来，不过并不是强制性的，目前也只有Mali-
T600系列支持。

 **Imagination旗下的PowerVR GPU支持的是PVRTC(PowerVR texture
compression)和ETC，高通的Adreno 2xx系列支持ETC之外还有3Dc和ATITC。** 后两者都是原来的ATI开发的，Adreno
320除了前面三种标准之外还支持ETC2纹理压缩。

 **ARM的Mali-300/400系列支持ETC，Mali-T600还多了ASTC纹理支持。**

NVIDIA的Tegra系列更有趣。之前的说法称Tegra支持自己的纹理格式， **实际上除了通用的ETC之外，Tegra支持的纹理叫做S3TC(S3
Texture Compression)，也被称为DXTn或者DXTC。** S3TC是S3公司在1999年引入的，后来被DX 6.0和OpenGL
1.3吸收为官方标准，DXTC相当于Windows版的名字，S3TC是OpenGL中的名字。

说到S3TC，之前苹果和HTC大打专利战的时候就涉及到了这个标准。S3已经归为VIA威盛旗下，HTC和威盛又有同一个老板——王雪红。为了支援HTC打专利战，威盛去年就把S3部门出售给了HTC，算是左手倒右手吧。

S3TC是DX显卡都支持的标准，NVIDIA也在Tegra中支持了这个标准，S3TC根据不同算法又分为DXT1-DXT5这五个级别，Terga支持的实际上是DXT1、DXT3和DXT5。

 **Vivante的GC系列也支持ETC和S3TC，跟NVIDIA的Tegra路线相同。** 以前都说Vivante支持的是NVIDIA
Tegra的纹理数据，实际上二者是选择了共同的路线而已，DXT也不是NVIDIA的专利。

目前来说我们能常用到的纹理压缩主要是ETC、PVRTC、S3TC、ATITC这四种种。

 **主流紋理压缩格式优缺点**

  

![](http://upload-images.jianshu.io/upload_images/17266280-e966558af279a67c.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

常见的TC格式压缩比

先来看压缩比。如果无失真的PNG容量是5.4MB，那么S3TC和ETC都能压缩到1.1MB，PVRTC压缩最高，可压缩到528KB，不过PVRTC的问题在于它只支持PowerVR系列GPU，有排他性，高通的Adreno支持的ATITC同样有排他性，其他厂商并不支持。

 **  
**

![](http://upload-images.jianshu.io/upload_images/17266280-0738096c692324d9.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

**ETC是最通用的纹理压缩格式，不过ETC并不招厂商待见，因为ETC纹理压缩不支持Alpha通道，只能用于压缩不透明的材质，不过ETC也有自己的优点，几乎所有的安卓设备都可以支持ETC压缩的GPU加速。**

S3TC无论压缩速度还是压缩比都不错，也支持GPU加速，而且是桌面显卡通用的压缩格式，看起来是最完美的选择，可惜的是移动市场跟PC不一样，大家各自为王，NVIDIA现在还没强大到让其他GPU厂商低头采用S3TC标准的程度，因为
**S3TC说到底还是一种私有的标准，有专利上的麻烦。**

**ETC2压缩标准补全了ETC1不支持Alpha通道的缺陷，支持更高质量的RGBA(RGB+Alpha)压缩，而ARM提出的ASTC标准在压缩速度和质量上比S3TC要好，但是这两种压缩格式都是新出的，支持的厂商实在太少了。**

