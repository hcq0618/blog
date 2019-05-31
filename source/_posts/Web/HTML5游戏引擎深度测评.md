---
title: HTML5游戏引擎深度测评
thumbnail: 
categories: Web
tags: [Web,h5]
---
最近看到网上一篇文章，标题叫做《[2016年 最火的 15 款 HTML5 游戏引擎
__](https://link.zhihu.com/?target=http%3A//www.oschina.net/news/72092/2016-top-15-html5
-game-
engines)》。目前针对HTML5游戏的解决方案已经非常多，但谁好谁差却没有对比性资料。特意花了几天时间，针对文章中出现的12款免费开源引擎做了一次相对完整的对比分析，希望能对大家有所帮助。

针对技术类产品对比，通常有多个维度进行对比，不仅仅是技术层面，还有许多非技术层面的内容会影响我们的使用结果。本文从如下几个维度进行多重对比。

  1. 2D与3D
  2. 编程语言
  3. 产品定位&amp;功能
  4. 工作流
  5. 性能
  6. 学习资料
  7. 商业应用

### 2D与3D、编程语言对比

 **2D与3D**

游戏领域中，最直白的一种分类方法便是2D与3D的区分。通常我们都会认为它们是游戏引擎领域两类不同的产品。

 **编程语言**

基于HTML5技术的游戏引擎，所需要的脚本必定是JavaScript，只有JavaScript脚本语言才能运行于浏览器中。但目前市场上，出现了很多JavaScript代替品，例如TypeScript、CoffeeScript、LiveScript等等。不同语言直接的定位不同，语言哲学也不尽相同。一些游戏引擎在语言选择上也颇有意思。

![](https://pic3.zhimg.com/3ba3083ddd17ecdce1a725f2f880455a_b.png)

 **结论**

可以从表格中看出，下面三个引擎属于2D和3D通吃类型。

  * Egret
  * Turbulenz
  * PlayCanvas

在Web游戏领域胜出的编程语言是JavaScript和TypeScript。但绝大部分HTML5游戏引擎还是采用JavaScript语言。只有三款引擎选择支持TypeScript。

### 产品定位&amp;功能

一个引擎的功能并非越多越好，功能应围绕引擎定位而定，这样的思路在一些引擎中体现尤为明显，下面我们针对每个引擎一一分析。

#### Three.js

 **定位**

Three.js项目创建时间是在2010年的4月24日，到目前位置，应该算是比较老牌的开源项目了。事实上Three.js定义并非一个游戏引擎。在Github主页中，作者很明确的定义了Three.js的定位，叫做“JavaScript
3D library”。它仅仅是一个基于JavaScript语言的3D库而已。

 **功能**

文本主要想对2D游戏引擎做深入分析，所有没有对Three.js的功能与那些流行的3D引擎加以对比。

#### Pixi.js

 **定位**

Pixi.js的定义为“2D WebGL renderer with canvas
fallback”，翻译为中文是一款依赖于canvas的WebGL渲染器。所以当你看到Pixi.js提供了为数不多的功能时。

 **功能**

游戏引擎中的功能，我们可以细分非常多分类，一篇文章无法讲解所有分类细节讲解明白。我将所有功能做了一个二级分类，方便分析。

![](https://pic2.zhimg.com/bb895b62afd3756ee30a88ce0be01831_b.png)

#### Phaser

 **定位**

Phaser的定位是 "Desktop and Mobile HTML5 game
framework"，中为称之为“桌面与移动端的HTML5游戏框架”。Phaser并不把自己定义为Engine，而是框架，同时渲染内核使用Pixi.js。

 **功能**

Phaser功能众多，但绝大部分应用其他第三方作为实现。  

![](https://pic2.zhimg.com/fc365cb286b434b156d6a6dfc34bdb95_b.png)

#### Egret

 **定位**

Egret算是HTML5游戏引擎中的新起之秀，其定位已不单纯为HTML5游戏引擎。官方将其定位为“游戏解决方案”，同时也并未过多提及HTML5。究其原因在于Egret不仅仅提供了一个基于HTML5技术的游戏引擎，更是提供了原生打包工具和众多周边产品，使其成为“解决方案”。

这里单独分析Egret
Engine这个产品，其语言使用TypeScript，有2D和3D版本。在架构设计上，同Pixi.js一样，参考了Flash成熟的2D架构体系。API方面，也参考了ActionScript。不仅如此，由于TypeScript的缘故，在事件系统中，也仿照ActionScript实现了addEventListener
这样的事件注册机制。

内核方面，Egret Engine采用了模块化的设计。这样可以将不同的功能进行解耦。更加有趣的是，Flash中引以为傲的自动脏矩形技术在Egret
Engine中也被实现。在canvas模式下，脏矩形会是渲染性能得到提升，比其他引擎更加有优势。

 **功能**

Egret
Engine由于模块化设计的原因，将不同功能放到了不同模块中。这些模块以库的形式提供，下面表中是所有支持模块的总和，但不含平台API部分，例如微信API的封装。  

![](https://pic2.zhimg.com/cee709e5fc168e05610de89b23cda419_b.png)

#### enchant.js

 **定位**

enchant.js并非一个引擎，而是一个框架。同时，enchant.js也不仅仅用于游戏，还可以用于app。

 **功能**

enchant.js框架自身提供的功能非常有限，如果需要其他功能，必须自己扩展或者寻找响应的插件。

![](https://pic1.zhimg.com/14ea57fa972d16f2d1c8e3c0bc5dfe34_b.png)

#### craftyJS

 **定位**

craftyJS将自己定义为针对JavaScript游戏的框架。

 **功能**  

![](https://pic2.zhimg.com/2a50920209cbba7bfeaaeada5819f3f5_b.png)

#### Turbulenz

 **定位**

Turbulenz引擎实际上是为自己的游戏渠道中的游戏提供的游戏引擎。因为和自身渠道绑定，所以在引擎中提供了很多low level
API。借助这些底层API，可以呼叫Turbulenz游戏渠道中的一些系统级别功能。

 **功能**

由于Turbulenz对很多功能做了扩展，同时推出Low Level API和 High Level
API。这里不再对其中庞杂的系统进行功能分析，大家如果有兴趣可以到其官网查看。

#### cocos2d-js

 **定位**

cocos2d-js是喊着Cocos2D-X的金钥匙出身的，它仅仅是Cocos2D-X的一个HTML5实现的分支。

 **功能**

cocos2d-js的功能提供的相当完整，你在游戏中需要的功能几乎都能够找到。

![](https://pic2.zhimg.com/3027da65aee964df23754d96563aeaa5_b.png)

#### PlayCanvas

 **定位**

PlayCanvas主要用于3D渲染，本文还是以2D讨论为主，对PlayCanvas的分析就不做过多分析。

#### melonJS

 **定位**

melonJS是一个轻量级的HTML5游戏框架，并且通过插件机制扩展其功能。

 **功能**

![](https://pic3.zhimg.com/327e662ec22012f9b30a756819ea499a_b.png)

#### Quintus

 **定位**

Quintus将自己定位为简单好用的JavaScript游戏引擎，同时支持移动和PC端。

 **功能**

Quintus自身并不支持WebGL，同时提供的功能也较少，在Github中排名也很靠后。

![](https://pic3.zhimg.com/ece57b2f301a1f6ab04da0a07228a802_b.png)

#### Hilo

 **定位**

Hilo这个引擎来源于阿里前端团队，从官网的主页上看，这个引擎的定位比较模糊。Hilo作为一个跨终端的互动小游戏解决方案，同时有称综合解决方案。从它的演变来看，Hilo属于阿里前端在实践总总结出来的一套工具库。整体引擎并非最初有计划设计构想。

 **功能**

Hilo功能相对比较简单，对于游戏开发来说，缺失功能较多。

![](https://pic4.zhimg.com/4d19638cd0d482f6983410d6b3ca7383_b.png)

### 工作流

对团队开发来讲，工作流搭建是非常重要的，我个人比较看重这点。如果是小型团队或者个人开发者可能对此需求并不大。当项目规模变大时，一个好的工作流会事半功倍。

 **Three.js**

3D并不在本篇文章的讨论范围之内，同时Three.js也并非游戏引擎，不存在游戏开发工作流一说。这里简单介绍一下Three.js所提供的在线编辑器。

Three.js提供的在线编辑器应该是基于Three.js开发的，功能不多，但相当小巧。

![](https://pic4.zhimg.com/bae54192885f1727132e4fef21eaf7db_b.png)

**Pixi.js**

Pixi.js作为一个渲染器，其工具支持也是相当清爽，除了一个程序库之外，没有提供任何工具。

 **Phaser**

Phaser和Pixi.js一样，没有提供任何工具支持，在其官网上只是推荐了两个代码编辑器。还提供了一个简单的在线代码编辑器。

![](https://pic3.zhimg.com/538783a7e1def04b90d73d43ea78e31e_b.png)

 **Egret**

Egret提供的工具非常多，也复合其解决方案的定位。在Egret整个体系下你可以看到如下工具支撑。

Egret Wing：Egret出品的一个IDE编辑器。在提供代码编辑功能的同时，还内置可视化的UI编辑器。与Egret
Engine中的GUI、EUI框架配合使用。

![](https://pic4.zhimg.com/8d74fbdbf422915621378246d006e653_b.jpg)

ResDepot：这是个小工具，用来配置游戏资源加载表。如果游戏资源多的话，用这个小工具拖拽一下就完成了。

TextureMerger：一个纹理合并的小工具，功能有点像TexturePacker。

DragonBones Pro：针对Egret中骨骼动画解决方案提供的DragonBones动画编辑器。

![](https://pic3.zhimg.com/dfb90eced652e8753a42a7ae6ab51d1a_b.png)

Egret Inspector：一个基于Chrome浏览器的插件，可以针对Egret游戏进行调试。

Egret iOS &amp; Android Support：这两个东西可以将你的HTML5游戏打包成原生APP。

还有一些其他的工具，但定位与游戏开发不同，有兴趣可以去它的官网看。

从上幂啊你的分析看出，Egret在工作流的支持上做的还是非常完成的，从Wing的代码编写，到ResDepot和TextureMerger的资源整合，再到Inspector调试，和原生打包。游戏开发过程中的每个环节基本都有工具支撑。

 **enchant.js**

enchant.js 没有提供任何工具支撑，在官网中也没有任何相关支持工具的介绍。

 **craftyJS**

craftyJS也没有提供任何工具支撑，仅仅是一个开源代码库。

 **Turbulenz**

Turbulenz在你下载的目录中包含了很多工具，大部分与格式转换相关。所有工具均为命令含小工具，没有提供任何可视化操作软件支持。

 **cocos2d-js**

Cocos2d-js近年来变化很大，但对于JS这个分支的支持却少之又少。前一段时间新出了一个工具叫做Cocos
Creator。我没有具体使用过，但看截图仿佛有Unity3D的影子。从介绍中看，应该对游戏支持还是不错的，编辑方面目前还欠缺。

![](https://pic4.zhimg.com/a603cf194ce1744eeb2cb7b692354233_b.png)

 **PlayCanvas**

PlayCanvas也提供了一个在线编辑器，不过是针对它的3D功能。编辑器看上去和Three.js提供的在线编辑器份很相似。这里直接借用官方文档中的截图给大家看一下。

![](https://pic3.zhimg.com/4fbaf07839cc62a63e55637069326936_b.png)

 **melonJS**

melonJS除了源码库以外，也没有提供任何工具支持。但在其官方主页中，包含几个其他编辑器的连接。比如著名的Tiled地图编辑器等。

 **Quintus**

Quintus没有提供任何工具支撑。

 **Hilo**

Hilo没有提供任何工具支撑。

 **总结**

结果并不出乎意料，对于开源游戏引擎来讲，维护库就是耗费作者很大一部分精力，更何况去制作编辑器之类的软件产品。很多引擎都会依赖一些比较流行的第三方工具，例如Tiled、TexturePacker等等。虽然可以实现功能，但整个工作流搭配起来还是多多少少会有一些问题
。只有Egret和Cocos2D-js提供了相关可视化编辑工具。而这两对于工作流的理解则完全不同。从产品中不难看出，Cocos2D-
JS更像Unity3D，提供一个大而全的软件给开发者用。Egret则是什么角色用什么工具，将产品按照角色划分，针对不同角色和开发流程中的各个环节进行产品设计。

相对来说，Egret的这种方式使得每个工具更加垂直，能够做的功能也更加深入，不会让工具显得臃肿。而Cocos
Creator则力求完整，一个软件解决所有事情。

### 性能

性能测试上，我只针对2D游戏引擎做了一个渲染压力测试。

测试内容为同屏渲染对象数量相同的情况下进行帧频数据对比，为了保证测试的公平性，我使用同一台电脑，相同版本的Chrome浏览器进行测试，游戏场景尺寸均为800*600，显示的图片也为同一张。每个引擎进行同屏5000、10000、20000个显示对象渲染。

其中craftyjs引擎渲染出现问题，这里不作数据对比。 Quintus引擎不支持WebGL渲染模式，因此这里页不作数据对比。
Phaser渲染内核使用Pixi.js，因此Phaser渲染数据参考Pixi.js结果。

所有引擎编写的代码大致相同，开始做for循环，创建定量显示对象，然后在循环中对每个显示对象做旋转操作。

核心算法代码如下：

![](https://pic1.zhimg.com/314b001abf2df1501413cbd4ef533174_b.png)我的电脑配置如下：  

![](https://pic3.zhimg.com/66222338a21b175a5dd336982bd05cd6_b.jpg)

最终测试结果

![](https://pic4.zhimg.com/f31724de09106285c1b1929bb92fc5eb_b.png)

 **结论**

按照上述测试方法，我们可以对引擎性能排名做一个大致排列：

第一名：Pixi.js 和 Turbulenz

第二名：Egret

第三名：Cocos2d-js

第四名：Hilo

第五名：enchant.js

第六名：melonJS

  

最后放出一张测试时效果图

![](https://pic3.zhimg.com/b6ab8db21ba17415190e8426d4b78fde_b.png)

### 学习资料

通常情况下，我们都会选择一个资料较全的产品进行学习使用，毕竟使用过程中会遇到各种各样的问题。现在游戏引擎的文档，讨论组等都已经成为了产品标配。下面这个表格就对各个引擎的这些“标配”做一个对比。

![](https://pic4.zhimg.com/743dabcb1a0ca9a9a1bd52ad0833a88f_b.png)

 **结论**

从上面对比表格可以看出，绝大部分引擎在文档教程方面做的还是比较深入的，但完成程度不同。大部分都为英文文档，对于国内的开发者来说可能学习起来成本略高。其中两个支持中文的引擎Egret、Hilo均为国人产品，这两款引擎在文档方面，Egret做的相当优秀，开发者可以从它的[http://edn.egret.com
__](https://link.zhihu.com/?target=http%3A//edn.egret.com)中查阅大量中文资料。

在学习难度上，Egret算是最为简单的，无论从完整度还是中文普及度上。

### 商业应用

这部分对比是在商业产品应用中的占比情况。一个引擎被商业产品应用广泛的情况下，足以证明此引擎具备商业产品使用价值。通俗的讲，别人能用这玩意做出游戏，你也能。所以针对这两方面进行一下粗略的分析。

我对国外的HTML5游戏市场完全不了解，这个市场分析的东西太大，不好做评价。就分析一下国内的，简单看一下到底哪个引擎用的多。

我用了国内比较火的HTML5游戏平台新浪微博作为数据采样基础，一个人实在精力有限，不可能做的完整。由于客户端对游戏地址进行了加密，无法直接获取。所以用了一些调试工具来看游戏网页的标记，以此判断游戏到底使用什么引擎制作。

最终统计结果如下：

![](https://pic1.zhimg.com/945d6e8bcdd0e59acb9384058adc55c8_b.png)

一共找了50款游戏，如上面表格。50款引擎，使用纯HTML5开发的6款，使用Egret开发的30款，Cocos2d-
js的14款，laya的1款，createjs的1款。

百分比统计如下：

![](https://pic3.zhimg.com/5ba06b3b8b7e2e5ef9923a78346e762e_b.png)

从网上又搜刮了一些数据，下面是国内HTML5游戏四大典型大渠道，即新浪微博（社交型APP类代表），爱微游（微信大号类代表），QQ浏览器（各大浏览器类代表），WiFi万能钥匙（超级APP类代表）统计的数据，比我自己的全。

下面是主流渠道H5游戏引擎使用率。

![](https://pic2.zhimg.com/04e6541c1c8b531f20aefff81a73a645_b.png)HTML5付费游戏全渠道累计用户排名前30的产品  

![](https://pic4.zhimg.com/7f713c138d818d99ce5dbea364d108b7_b.png)![](https://pic2.zhimg.com/ad2bbd8c412963d47d8c2040a79ed221_b.png)

不难看出，Egret 和 Cocos2D-js联合瓜分了大部分市场。而Egret占比居然过半。看来Egret在国内HTML5游戏市场还是非常强悍的。

### 总结

  1. Three.js：作为老牌的3D库，它已经有众多案例，在PC多网页3D中是目前不错的选择。
  2. Phaser：文档教程，和案例方面都很不错，功能也算的上丰富。非常适合独立游戏开发和小团队使用。
  3. Pixi.js：作为渲染器，其渲染性能绝对是非常优秀的，游戏功能方面支持很差，适合极客程序员把玩。
  4. Egret：性能不错，在工作流方面支持非常优秀，适应中度和重度HTML5游戏开发，有较多商业项目验证，非常适合商业团队使用。
  5. enchant.js：性能偏差，不太推荐。
  6. craftyJS：文档教程等方面不太完善，很难找到对应技术支持，不推荐。
  7. Turbulenz：性能极佳，但捆绑其自身业务，不太适合国内市场。
  8. cocos2d-js：老牌引擎，其性能在排名中居中，工作流支持相对完整，推荐。
  9. PlayCanvas：重度3D游戏开发引擎，本文不对3D做推荐。
  10. melonJS：性能不理想，不推荐。
  11. Quintus：不支持WebGL模式，性能较差，不推荐。
  12. Hilo：阿里前端团队作品，偏向于前端开发工程师，与游戏专业开发距离较大，推荐做HTML5营销小交互的使用。

更多详情: <https://zhuanlan.zhihu.com/p/20768495>

