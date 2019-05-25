---
title: React-Native国际化多语言
thumbnail: 
categories: ReactNative
tags: [ReactNative库]
---

# 库属性介绍  

项目地址：<https://github.com/AlexanderZaytsev/react-native-i18n

属性                                                            解释

支持RN版本                                            所有版本

支持平台                                                iOS+Android

是否需要NativeModule                                是

是否可移植                                                    是

是否含有jni模块                                            否

# 使用

1.install（略，git里都写着了，就是npm那些事）

2.项目中使用

因为是一些静态属性引用，所以你用redux做储存替换也可以，直接做饮用也可以(本文拿en,zh为例)。

首先是建英文版本的配置文件，en/index.js

 ```
exportdefault{



 home:{



 greeting:'Greeting in en',



 tab_home:'Home',



 tab_donate:'Donate',



 tab_demo:'Demo',



 language:'language',



 live_demo:'Live Demo',



 buy_me_coffee:'Buy me a coffee',



 gitee:'Gitee',



 star_me:'Star me',



 donate:'donate',



 exit:'exit?',



 },



 donate:{



 donate:'donate us~~~',



 donate_desc:'© 2017 Pactera Technology International Limited. All rights
reserved.',



 },



 demo:{



 dialog:'dialog',



 button:'button',



 switch:'switch',



 action_sheet:'Action Sheet',



 }



 };
```

然后是中文的zh/index.js

```
 exportdefault{



 home:{



 greeting:'Greeting in zh',



 tab_home:'首页',



 tab_donate:'捐赠',



 tab_demo:'例子',



 language:'语言',



 live_demo:'例子',



 buy_me_coffee:'请我一杯coffee',



 gitee:'Gitee',



 star_me:'关注我',



 donate:'贡献',



 exit:'是否退出?',



 },



 donate:{



 donate:'支持我们～~',



 donate_desc:'© 2017 Pactera Technology International Limited. All rights
reserved.',



 },



 demo:{



 dialog:'提示框',



 button:'按钮',



 switch:'开关',



 action_sheet:'',



 }



 };
```

属性名，结构是一致的只是属性不同，当然这里是静态的2个文件，如果场景需要可以服务端下发json,那就是完全动态的了，这部分看业务需求了。

## 默认的语言环境

我们在上面写了2种语言配置，那么哪种作为初始化的呢？在业务层调用前，我们可以先进行预设

i18n/index.js

 ```
import i18nfrom'react-native-i18n';



 import enfrom'./en';



 import zhfrom'./zh';



 i18n.defaultLocale ='en';



 i18n.fallbacks = true;



 i18n.translations = {



 en,



 zh,



 };



 export {i18n};
```

这边进行了一些预设，默认语境为en，允许fallbacks状态（为true时，顺序向下遍历翻译），预设转换的文件就2个，一个en一个zh，这个你也可以自行后续添加根据需求而定。

## 业务层调用

先是倒包

 import {i18n} from '你预设的index的目录';

调用(拿一个Toast做个例子)

 ToastAndroid.show(i18n.t('home.exit'),ToastAndroid.SHORT);

  

# 源码分析

这个库的实现分为2部分，一部分是Native的版本判断等功能以及js部分的核心实现fnando/i18n-js

i18n-js是一个轻量级的js翻译库，他支持各种格式和内容的换算和语言内容的切换，地址如下：<https://github.com/fnando
/i18n-js

那么翻译转换这块是 I18n.js做的那么Native做了些啥呢？我们来一探究竟(以安卓为例，苹果看不懂，抱歉)

Native代码就两个类，所以我之前说你直接把Native代码copy走然后项目依赖I18n.js也能达到这个效果

RNI18nPackage是一个普通的Package类，它的作用就是把我们的module加到主应用的getPackages()方法中的列表里，然后一起打进包里而已。

具体功能都在RNI18nModule里

 ```
publicclassRNI18nModuleextendsReactContextBaseJavaModule{



 publicRNI18nModule(ReactApplicationContext reactContext) {



 super(reactContext);



 }



 //RN调用的控件名



 @Override



 publicStringgetName() {



 return"RNI18n";



 }



 //对取出的Locale列表进行格式化的方法



 privateStringtoLanguageTag(Locale locale) {



 if(Build.VERSION.SDK_INT = Build.VERSION_CODES.LOLLIPOP) {



 returnlocale.toLanguageTag();



 }



 StringBuilder builder =newStringBuilder();



 builder.append(locale.getLanguage());



 if(locale.getCountry() !=null) {



 builder.append("-");



 builder.append(locale.getCountry());



 }



 returnbuilder.toString();



 }



 privateWritableArraygetLocaleList() {



 WritableArray array = Arguments.createArray();



 if(Build.VERSION.SDK_INT = Build.VERSION_CODES.N) {



 //获取区域设置列表。这是获取区域的首选方法。



 LocaleList locales = getReactApplicationContext()



 .getResources().getConfiguration().getLocales();



 for(inti =0; i < locales.size(); i++) {



 array.pushString(this.toLanguageTag(locales.get(i)));



 }



 }else{



 array.pushString(this.toLanguageTag(getReactApplicationContext()



 .getResources().getConfiguration().locale));



 }



 returnarray;



 }



 //js端可获取属性的列表



 @Override



 publicMap<String, ObjectgetConstants() {



 HashMap<String, Object constants =newHashMap<String,Object();



 constants.put("languages",this.getLocaleList());



 returnconstants;



 }



 //提供给js端调用的方法，用来获取默认的语言环境，回调方式用的是promise



 @ReactMethod



 publicvoidgetLanguages(Promise promise) {



 try{



 promise.resolve(this.getLocaleList());



 }catch(Exception e) {



 promise.reject(e);



 }



 }



 }
```

加一个toast看下locale会出现什么

 Toast.makeText(getReactApplicationContext(),"locales.get(i)
"+locales.get(i),Toast.LENGTH_LONG).show();

本想一探究竟内部的实现，结果是个不公开的类

# 总结

首先Native那里获取本手机的LocaleList然后格式化取第一个元素交由I18n.js处理，然后I18n.js根据key选用一套有效的语言规则，再之后流程就和使用时候的顺序一样了。

整个库集成难度较低，使用起来比较简便，使用下来没碰到大坑，配合redux更美味。

# 准备阶段

[react-native-i18n](https://github.com/AlexanderZaytsev/react-native-
i18n)第三方多语言库

安装:yarn add react-native-i18n

[react-native-device-
info](https://www.jianshu.com/p/%5Bhttps://github.com/rebeccahughes/react-
native-device-info%5D\(https://github.com/rebeccahughes/react-native-device-
info\))用户获取系统本地语言环境

安装:yarn add react-native-device-infoandreact-native link react-native-device-
info

实践阶段：

在项目中创建zh.js、en.js、I18n.js三个js文件，DataRepository.js是一个我自定义的数据持久化类，在这个demo中的作用是存取用户改变后的语言环境，直接拷贝过去就可以用(不是必须的)。

代码分别为：

zh.js

 ```
exportdefault{



 english:'英文',



 chinese:'中文',



 changeToEnglish:'切换到英文',



 changeToChinese:'切换到中文',



 changeToSystem:'切换到系统语言',



 }
```

en.js

 ```
exportdefault{



 english:'english',



 chinese:'chinese',



 changeToEnglish:'change to english',



 changeToChinese:'change to chinese',



 changeToSystem:'change to System',



 }
```

I18n.js

 ```
importI18n,{ getLanguages }from'react-native-i18n'



 importDeviceInfofrom'react-native-device-info'



 importDataRepositoryfrom'../dao/DataRepository'



 importenfrom'./en'



 importzhfrom'./zh'



 I18n.defaultLocale ='en';



 I18n.fallbacks =true;



 I18n.translations = {



 en,



 zh,



 };



 I18n.localeLanguage =()={



 newDataRepository().fetchLocalRepository('localLanguage')



 .then((res)={



 I18n.locale = res;



 })



 .catch((error)={



 I18n.locale = DeviceInfo.getDeviceLocale();



 });



 returnI18n.locale;



 };



 export{ I18n, getLanguages };
```

重点方法、属性讲解

I18n.t(): 使用频率是最高的，举个栗子：

 <Textstyle={styles.welcome}



 {I18n.t('english')}



 </Text

以上I18n.t('english')中的english参数就是在zh.js、en.js文件中的语言配置项

![](http://upload-images.jianshu.io/upload_images/17266280-bff22bd8361f8dbd.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

  

![](http://upload-images.jianshu.io/upload_images/17266280-d3a0ae910943a8c9.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

具体显示内容会随着语言环境调用相应的语言配置文件，呈现给用户相应的语言内容。

I18n.getLanguages获取用户首选的语言环境

I18n.locale: 设置本地语言环境。

I18n.defaultLocale首选默认语言

I18n.fallbacks: 看文档说明我理解的意思是：如果获取到的系统语言类似en_USen-GB这样的，插件初始化的时候发现没有en_US.jsen-
GB.js，这个时候如果设置了I18n.fallbacks =
true;系统就会按这样的（en_USen.js）顺序去查找文件，就会去找有一个en.js这样的文件， 官方建议使用I18n.fallbacks =
true;

更多关于i18n-js的属性和方法请[点击这里查看](https://github.com/fnando/i18n-js#setting-up)

# ios需要配置语言环境

![](http://upload-images.jianshu.io/upload_images/17266280-bff44df987d83437.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

使用过程中发现一个刷新的问题：

我在使用过程中发现调用了I18n.locale=‘我设置的语言’后，当前的界面语言并没有改变，而其他界面的语言已经改变了，就比如说我上面截图的侧滑菜单，当我在侧滑菜单切换语言后发现侧滑菜单里面的语言并没有发现变化，而首页的语言环境已经改变了，我不知道为什么，摸索最后找到了一种解决方案（可能不是最佳方案，但是解决了刷新当前界面语言的问题，如果有更好的方法欢迎分享），解决方案：调用一下setState（无论设置的这个state属性在render中有没有被使用，都有效）。
具体代码看App.js，我项目中有使用localeLanguage所以我把改变后的语言存到state中

 ```
this.setState({



 localeLanguage: I18n.locale



 });
```

![](http://upload-images.jianshu.io/upload_images/17266280-867fa9db46b8b45f.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

![](http://upload-images.jianshu.io/upload_images/17266280-92d2154acd865e3e.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

请注意，js的名字最好都是语言的缩写，下面提供参考：

![](http://upload-images.jianshu.io/upload_images/17266280-3593a655a97142fd.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

突然有个想法看看没有支持的语言会变成什么：看来如果没有支持某种语言就会默认使用英语，我曾经试过分别调换这两个的引入顺序发现结果还是英语

