---
title: Weex&ReactNative对比
thumbnail: 
categories: React-Native
tags: [React-Native,ReactNative]
---

>
weex开源有一段时间了，其实去年刚听说weex这个项目的时候，我就对它很感兴趣，很大程度上是因为我自己对vue的喜爱。我从13年左右开始接触vue，14年开始熟悉这个轻量的框架，并慢慢的推荐给了身边的朋友，当我得知手淘的weex是基于vue的时候，就有了想了解一下的冲动。在weex开源之前，我刚好有几个月的时间一直在致力于ReactNative的优化改造，加上自己之前使用ReactJS的一些经验，对于ReactNative项目也算有了一些自己的见解。趁着weex开源了，赶在前几天，我花了两三天的时间把weex
android的源码完整的看了一遍，前端js代码也粗略看了一下，结合自己对ReactNative源码的一些了解，正好在这里对两者做一个尽量中立的比对。

首先，我们要承认，weex的确是站在ReactNative的肩膀上的，核心思想上两者并没有大的区别，直观的看上去，我认为有三个主要的区别：

# JS引擎

weex使用V8， ReactNative使用JSCore

# JS开发框架

weex基于vue.js(2W+ star)。小巧轻量的前端开发框架，组件化，数据绑定，2.0引入virtual dom。

ReactNative使用React(4W+ star)。革命性的前端开发框架，组件化，数据绑定，virtual dom。

# Android版本要求

ReactNative使用了Choreographer，因此必须在API16以上才可以使用。

weex使用handler来代替Choreographer，可以在API14以上使用。

> weex出来的初衷也是为了解决ReactNative使用过程中遇到的一些问题，当然具体决定使用那个框架，我觉得需要从一下几个方面来做对比

# 学习成本

1\. 环境配置：

ReactNative需要按照文档安装配置很多依赖的工具，相对比较麻烦。 weex安装cli之后就可以使用

2\. vue vs react

react模板JSX学习使用有一定的成本 vue更接近常用的web开发方式，模板就是普通的html，数据绑定使用mustache风格，样式直接使用css

3\. 布局

两者实现了flexbox的相同子集（都使用了FaceBook的代码解析），基本没有区别

# 易用性

1\. sdk使用

ReactNative需要解决mvn依赖的问题，因此必须自己修改源码，打包发布

weex可以直接在mvn项目中使用

2 调试

都可以在chrome中调试JS代码

weex支持在chrome中预览页面dom节点，ReactNative不支持

3 页面开发

weex提供了一个playground，可以方便的预览正在开发的页面

ReactNative开发一个页面，需要建立一个native工程，然后编译运行

4 即时预览

weex和ReactNative都有提供hot reload功能，可以边更改代码，边在手机上看到效果

5 打包

ReactNative官方只能将ReactNative基础js库和业务js一起打成一个js bundle，没有提供分包的功能，需要制作分包打包工具

weex默认打的js bundle只包含业务js代码，体积小很多，基础js库包含在weex sdk中

6 部署

斑马目前同时支持weex和ReactNative页面，但是中心已经转向weex

另外斑马提供了可以拖拽搭建weex活动页面的功能

7 扩展性

组件的扩展上，weex和ReactNative具有一样的能力

三方库的接入上，weex对网络，图片，统计等常见的用户可能想自己定制的功能，提供了相应的适配接口，可以由用户方便的定制，ReactNative需要自己修改源码

8 集团库接入

weex有默认的mtop接入实现，UT接入实现

windvane也提供了对weex页面的支持，可以复用app中的web容器

9 跨平台

ReactNative支持Android iOS两个平台，需要自己扩展去支持web，windows和node-webkit的支持正在开发中

weex可以支持Android iOS web三个平台

10 Moudle方法调用线程

weex 可以通过注解标注是否在UI线程执行

ReactNative在native_modules线程执行

11 异步

weex只支持callback

ReactNative提供了Promise的支持

# 性能

1 分包加载

ReactNative需要自己实现，从而优化JS加载执行时间

weex默认提供分包实现

2 官方支持

ReactNative官方关注的重心目前并不在性能上

weex持续关注性能优化

3 大块view渲染

ReactNative默认没有优化机制，长view渲染性能会比较差

weex提供了node和tree两种渲染模式，优化长view的渲染

4 ListView Android

ReactNative目前采用scrollView使用，有一些性能问题

weex使用recyclerview实现，性能稍好

# 社区

ReactNative 3w+ star，issue，pull request， contributor多，社区活跃，围绕react产生了许多开发框架

weex开源较晚，目前只有4k+ start，contributor以阿里人为主，较少，issue和pull request也比较少，社区目前规模比较小

# 工具链

1 debug tool

都有提供在chrome中调试的支持

2 打包工具

ReactNative需要自己改造

weex默认提供的足够满足使用需求

3 webpack，gulp，脚手架工程

weex有相应的插件，方便开发，部署使用

ReactNative有，但是很久未更新，需要自己维护

>
通过上面的一些对比，就我个人来说，我还是比较倾向于使用weex，我比较熟悉vue是一方面，另外性能和发布这一块也是我比较关注的点。使用ReactNative确实也可以做到不错，但是最终我发现，自己其实是在做weex团队已经做的事情。与其这样，为什么我不选择weex，去帮助weex解决一些其他问题，给自己留更多时间去做业务开发呢？另外从业务开发的角度，我也觉得weex的门槛相对比较低，更适合业务开发同学上手，简单就是不简单。

<http://dev.bingocc.com/buiweex/docs/>

<http://weex.apache.org/cn/guide/>

