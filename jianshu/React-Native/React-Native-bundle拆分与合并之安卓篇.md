---
title: React-Native-bundle拆分与合并之安卓篇
thumbnail: http://upload-images.jianshu.io/upload_images/17266280-6ab32592593a178b.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240
categories: React-Native
tags: [React-Native,ReactNative]
---

在网上看到携程之前拆分的一些经验

先来说一组数据，一个Helloorld的App，如果使用0.30 RN 官方命令react-native
bundle打包出来的JSBundle文件大小大约为531KB，RN框架JavaScript本身占了530KB， zip压缩之后也有148KB。

如果只有一两个业务使用，这点大小算不了什么，但是对于我们这种动辄几十个业务的场景，如果每个业务的JSBundle都需要这么大的一个RN框架本身，那将是不可接受的。

因此，我们需要对RN官方的打包脚本做改造，将框架代码拆分出来，让所有业务使用一份框架代码。

开始拆分之前, 我们先以HelloWorld的RNApp为基础介绍几个背景知识。

  

![](http://upload-images.jianshu.io/upload_images/17266280-6ab32592593a178b.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

上述是一个HelloWorld RNApp代码的结构，基本分为3部分

头部：各依赖模块引用部分；

中间：入口模块和各业务模块定义部分；

尾部：入口模块注册部分；

  

![](http://upload-images.jianshu.io/upload_images/17266280-cf75780b9fa73565.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

上述是HelloWorld RNApp打包之后JSBundle文件的结构，基本分为3部分
头部：全局定义，主要是define，require等全局模块的定义； 中间：模块定义，RN框架和业务的各个模块定义； 尾部：引擎初始化和入口函数执行；

__d是RN自定义的define，符合[CommonJS规范](https://link.jianshu.com/?t=http://javascript.ruanyifeng.com/nodejs/module.html)，__d后面的数字是模块的id，是在RN打包过程中，解析依赖关系，自增长生成的。

如果所有业务代码，都遵照一个规则：入口JS文件首先require的都是react/react-native, 则打包生成的JSBundle里面react
/react-native相关的模块id都是固定的。

拆分方案一

基于上面2点背景知识介绍，我们很容易发现，如果将打包之后的JSBundle文件，拆分成2部分(框架部分+业务模块部分)，使用的时候合并起来，然后去加载，即可实现拆分功能。

具体实现步骤：

创建一个空工程，入口文件只需要2行代码，require react/react-native即可；

使用react-native bundle命令，打包该入口文件，生成common.js;

使用react-native bundle打包业务工程(有一点要保证，业务工程入口文件前面2行代码也是require react/react-
native), 生成business_all.js；

开发工具，从business_all.js里面删除common.js的内容，剩下的就是business.js;

App加载的时候将common.js和business.js合并在一起，然后加载；

貌似功能完成，可是回到Dive into React Native performance，
这么做还是优化不了JSBundle的执行时间，因为我们不能把拆分开的2个文件分别执行，因为加载common.js会提示找不到RNApp的入口，先执行business.js,会提示一堆依赖的RN模块找不到。

显然，这种拆分方式不能满足我们这种需要。

那这个方案就完全没有价值吗？不是的，如果你做的是一个纯RNApp，native只是一个壳，里面业务全是RN开发的，完全可以使用这种方式做拆分，这种方案简单，无侵入，实现成本低，不需要修改任何RN打包代码和RN
Runtime代码。

拆分方案二

RN框架部分文件(common.js)大小530KB，如此大的js文件，占用了绝大部分的JS执行时间，这块时间如果能放到后台预先做完，进入业务也只需执行业务页面的几个JS文件，将可以大大提升页面加载速度，参考上面的RN性能瓶颈图，预估可以提升100%。

按照这个思路，能后台加载的JS文件, 实际上是就是一个RNApp，因此
我们设计了一个空白页面的FakeApp，这个FakeApp做一件事情，就是监听要显示的真实的业务JS模块，收到监听之后，渲染业务模块，显示页面。

FakeApp设计如下：

  

![](http://upload-images.jianshu.io/upload_images/17266280-1f1b3db65e8a62ec.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

为了实现该拆包方案，需要改造react-native的打包命令；

基于FakeApp打common.js包的时候， 需要记录RN各个模块名和模块id之间的mapping关系；

打业务模块包的时候，判断，如果已经在mapping文件里面的模块，不要打包到业务包中

改造页面加载流程：

因为要能够后台加载，所以需分离UI和JS加载引擎<iOS-RCTBridge, Android-ReactInstanceManager>;

进入业务RN页面时候，获取预加载好的JS引擎，然后发送消息给FakeApp，告知该渲染的业务JS模块；

通过后台预加载，省去了绝大部分的JS加载时间，似乎问题已经完美解决。

但是，如果随着业务不断膨胀，一个RN业务JS代码也达到500KB，进入这个业务页面，500多KB JS文件读取出来，执行，整个JS执行的时间瓶颈会再次出现。

拆分方案三

正在此时，我们研究RN在Facebook App里面的使用情况，发现了Unbundle，简单点说，就是将所有的JS模块都拆分成独立的文件。

下面截图就是unbundle打包的文件格式：

  

![](http://upload-images.jianshu.io/upload_images/17266280-47a36a0fbf3ebd81.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

entry.js就是global部分定义+RNApp入口；

UNBUNDLE文件是用于标识这是一个unbundle包的flag；

12.js,13.js就是各个模块，文件名就是模块id；

在业务执行，需要加载模块(require)的时候，就去磁盘查找该文件，读取、执行。

RN里面加载模块流程说明,以require(66666)模块为例：

首先从__d<就是前文提到的define>的缓存列表里面查找是否有定义过模块66666，如果有，直接返回，如果没有走到下面第二步的nativeRequire；

nativeRequire根据模块id，查找文件所在路径，读取文件内容；

定义模块，_d(66666)＝eval(JS文件内容)，会将这个模块ID和JS代码执行结果记录在define的缓存列表里面；

打包通过react-native unbundle 命令，可以给android平台打出这样的unbundle包。

顺便提一下，这个unbundle方案，只在android上有效，打ios平台的unbundle包，是打不出来的，在RN的打包脚本上有一行注释，大致意思是在iOS上众多小文件读取，文件IO效率不够高，android上没这样的问题，然后判断如果是打iOS的unbundle包的时候，直接return了。

相对应的，iOS开发了一个prepack的打包模式，简单点说，就是把所有的JS模块打包到一个文件里面，打包成一个二进制文件，并固定0xFB0BD1E5为文件开始
，这个二进制文件里面有个meta-
table，记录各个模块在文件中的相对位置，在加载模块(require)的时候，通过fseek，找到相应的文件开始，读取，执行。

在Unbundle的启发下，我们修改打包工具，开发了CRNUnbunle，做了简单的优化，把众多零散的JS文件做了简单的合并。

  

![](http://upload-images.jianshu.io/upload_images/17266280-30b314cee44495a0.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

将common部分的JS文件，合并成一个common_ios(android).js.

_crn_config记录了这个RNApp的入口模块ID以及其他配置信息，详见下图：

  

![](http://upload-images.jianshu.io/upload_images/17266280-f6539a2b77cd6057.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

main_module为当前业务模块入口模块ID；

module_path为业务模块JS文件所在当前包的相对路径；

666666=0.js,说明666666这个模块在0.js文件里面；

做完这个拆包和加载优化之后，我们用自己的几个业务做了下测试，下图是当时的测试验证数据。

  

![](http://upload-images.jianshu.io/upload_images/17266280-8755141d89f28f26.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

可以看出，iOS和android基本都比官方打包方式的加载时间，减少了50%。

这是自己单机测试的数据，那上线之后，数据如何呢？

下图，是我们分析一天的数据，得出的平均值<排除掉了5s以上的异常数据，后面实测下来5s以上数据极少>；

  

![](http://upload-images.jianshu.io/upload_images/17266280-624375b1394ac359.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

看到这个数据，发现和我们自己测试的基本一致，但是还有一个疑问，加载的时间分布，是否服从正态分布，会不会很离散，快的设备很快，慢的设备很慢呢？

然后我又进一步分析这一天的数据，按照页面加载时间区间分布统计。

![](http://upload-images.jianshu.io/upload_images/17266280-5c1aa6b23090fd40.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

看图上数据，很明显，iOS&Android基本一致，将近98%的用户都能在1s内加载完成页面，符合我们期望的正态分布，所以bundle拆分到此基本完成。

# 实践

我先用bundle打包命令打一个bundle出来

react-nativebundle --platform android --devfalse--entry-file index.android.js
--bundle-output finalbundle/index.android.bundle --assets-dest finalbundle/

只有一个简单的3k左右的index.android.js,打出了一个五百多k的index.android.bundle，看看里面是些什么

![](http://upload-images.jianshu.io/upload_images/17266280-2d4f82c2063e9870.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

  

![](http://upload-images.jianshu.io/upload_images/17266280-1e4060ae8d48d0d5.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

密密麻麻但又有规则

!function打头的是公共的头部部分

_d(function是JS文件，用ctrl+s搜索welcome，找到我们的index.android.js,原来是在第一行的_d(function,而且结尾有个参数0，其余部分其实都是公共的js

;require(120)，是基础文件的配置入口，require（0）则是业务的入口

基于以上，能想到一个办法：

内置一个common.js文件，里面包含了bundle文件公共部分的代码，

业务代码单独生成一个js文件

在需要展示加载某一个页面的时，将common.js和当前页面需要加载的业务js合并，然后再加载

这个办法解决了一部分问题，但加载时还是一个整体。如果common部分能重用，就能大大提升效率。所以就来试试上面提到的unbundle命令

> react-nativeunbundle --platform android --devfalse--entry-file
index.android.js --bundle-output build/index.android.bundle

生成的bundle只有14行了

![](http://upload-images.jianshu.io/upload_images/17266280-8e2a4c11a820b05a.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

但多了一个js-
modules文件夹，里面的xx.js里面的内容就是将之前的__d(xx)抽出来单独放到一个文件里面，通过require(xx)加载到内存供调用

![](http://upload-images.jianshu.io/upload_images/17266280-66c27828bd40d267.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

基于unbundle命令再设计一个上面提到的fake页面用来加载相应的业务模块，这个页面可以预先在后台初始化js引擎，将公共部分的common.js文件读取到内存，然后设置一个监听事件，通过emmit方式，当需要加载某个页面的的module的时候讲这个页面的module的id传递过来，然后通过require方法调用这个模块。

> 思路差不多是这样了，来试试看实现起来有没什么坑。

# 首先

我拿[例子](https://link.jianshu.com/?t=https://github.com/pukaicom/reactNativeBundleBreak)跑了一下，瞬间明白了流程是怎么回事，有几个关键：

DeviceEventEmitter

前端发起监听，后端需要用的时候调用emit触发，通过返回模块id,然后return
React.createElement(返回的模块ID,this.props)即可定制加载

配置文件

![](http://upload-images.jianshu.io/upload_images/17266280-dc1ff6ad811f63c3.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

这个配置文件之前不是很理解为什么好多等于0.js、等于1.js,现在明白其实就是不同bu的入口JS,因为都是单页路由的形式，不过这个配置其实是一套打包的一个流程，不在这里做，以后研究打包工具的时候加上。

然后

我试着把这样融入到之前的demo里。

先建两个test页面，用于测试切换。

> importReact, { Component }from'react';

>

> import{

>

> AppRegistry,

>

> StyleSheet,

>

> Text,

>

> View,

>

> }from'react-native';

>

> classtesteightextendsComponent{

>

> render() {

>

> return(

>

> <Viewstyle={styles.container}>

>

> <Textstyle={styles.welcome}>

>

> Welcome to Test 8888

>

> </Text>

>

> </View>

>

> );

>

> }

>

> }

>

> conststyles = StyleSheet.create({

>

> welcome: {

>

> fontSize:20,

>

> textAlign:'center',

>

> margin:10,

>

> }

>

> });

>

> module.exports = testeight;

然后在index.android.js加入切换按钮

> /**

>

> * Sample React Native App

>

> * https://github.com/facebook/react-native

>

> * @flow

>

> */

>

> importReact, { Component }from'react';

>

> import{

>

> AppRegistry,

>

> StyleSheet,

>

> Text,

>

> View,

>

> Image,

>

> NativeModules,

>

> DeviceEventEmitter,

>

> }from'react-native';

>

> exportdefaultclassAwesomeProjectextendsComponent{

>

> constructor(props){

>

> super(props);

>

> this.state = {

>

> content:null,showModule:false

>

> };

>

> DeviceEventEmitter.addListener("test", (result) => {

>

> letmainComponent =require(result.name);

>

> this.setState({

>

> content:mainComponent,

>

> showModule:true

>

> })

>

> });

>

> }

>

> render() {

>

> let_content =null;

>

> if(this.state.content){

>

> _content = React.createElement(this.state.content,this.props);

>

> return_content;

>

> }else{

>

> return(

>

> <Viewstyle={styles.container}>

>

> <Textstyle={styles.welcome}>

>

> Welcome to React Native!

>

> </Text>

>

> <Textstyle={styles.instructions}>

>

> To get started, edit index.android.js

>

> </Text>

>

> <Textstyle={styles.instructions}>

>

> Double tap R on your keyboard to reload,{'\n'}

>

> Shake or press menu button for dev menu

>

> </Text>

>

> <Textstyle={styles.instructions}onPress={()=>this.showToast()}>

>

> 点我调用原生

>

> </Text>

>

> <Textstyle={styles.instructions}onPress={()=>this.updateBundle()}>

>

> 点我更新bundle

>

> </Text>

>

> <Textstyle={styles.instructions}onPress={()=>this.goNine()}>

>

> 点我加载页面9999

>

> </Text>

>

> <Textstyle={styles.instructions}onPress={()=>this.goEight()}>

>

> 点我加载页面8888

>

> </Text>

>

> <Image

>

> source={require('./img/music_play.png')}

>

> style={{width:92,height:92}}

>

> />

>

> </View>

>

> );

>

> }

>

> }

>

> updateBundle () {

>

> NativeModules.updateBundle.check("5.0.0");

>

> }

>

> showToast () {

>

> //调用原生

>

> NativeModules.RNToastAndroid.show('from native',100);

>

> }

>

> goNine () {

>

> NativeModules.BundleLoad.goPage(9999);

>

> }

>

> goEight () {

>

> NativeModules.BundleLoad.goPage(8888);

>

> }

>

> }

>

> const styles = StyleSheet.create({

>

> container: {

>

> flex: 1,

>

> justifyContent: 'center',

>

> alignItems: 'center',

>

> backgroundColor: '#F5FCFF',

>

> },

>

> welcome: {

>

> fontSize: 20,

>

> textAlign: 'center',

>

> margin: 10,

>

> },

>

> instructions: {

>

> textAlign: 'center',

>

> color: '#333333',

>

> marginBottom: 5,

>

> },

>

> });

>

> AppRegistry.registerComponent('rnandnative', () => AwesomeProject);

然后把index.android和两个test页面都用unbundle打包

> react-nativeunbundle --platform android --devfalse--entry-file
index.android.js --bundle-output unbundle/index.android.bundle

>

> react-nativeunbundle --platform android --devfalse--entry-file
bundletest1.js --bundle-output unbundle/index.android.bundle1

>

> react-nativeunbundle --platform android --devfalse--entry-file
bundletest2.js --bundle-output unbundle/index.android.bundle2

然后把index.android.bundle1、index.android.bundle2中除了_d的那句打头的去掉,把__d(0的0改为9999、8888，把文件名改为9999.js和8888
.js丢到js-modules里，这个讲的估计不是很明白，但去看看代码就懂了。

然后建一个触发emit的方法

> public class RNBundleLoadModule extends ReactContextBaseJavaModule{

>

> private ReactApplicationContext reactApplicationContext;

>

> public RNBundleLoadModule(ReactApplicationContext reactApplicationContext){

>

> super(reactApplicationContext);

>

> }

>

> @Override

>

> public String  getName(){

>

> return "BundleLoad";

>

> }

>

> @ReactMethod

>

> public void goPage(final Integer pageid){

>

> System.out.print("########"+pageid+"########");

>

> // failedCallback.invoke();

>

> WritableMap params = Arguments.createMap();

>

> params.putInt("name", pageid);

>

> reactApplicationContext

>

> .getJSModule(DeviceEventManagerModule.RCTDeviceEventEmitter.class)

>

> .emit("test", params);

>

> }

>

> }

跑起来，一切OK。

参考

[https://github.com/pukaicom/reactNativeBundleBreak](https://link.jianshu.com/?t=https://github.com/pukaicom/reactNativeBundleBreak)

