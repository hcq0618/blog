---
title: 推荐React-Native-开源移动-UI-组件
thumbnail: 
categories: ReactNative
tags: [ReactNative库]
---

React Native 是近期 Facebook 基于 MIT 协议开源的原生移动应用开发框架，已经用于 Facebook 的生产环境。React
Native 可以使用最近非常流行的[React.js](http://www.oschina.net/p/facebook-react)库来开发 iOS
和 Android 原生 APP。

# iOS 表单处理控件 tcomb-form-native

[tcomb-form-native](http://www.oschina.net/p/tcomb-form-native)是 React Native
强大的表单处理控件，支持 JSON 模式，可插拔的外观和感觉。在线演示：<http://react.rocks/example/tcomb-form-
native>。

![](http://upload-images.jianshu.io/upload_images/17266280-034b26f120c9450e.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

# 摄像机视图 react-native-camera

[react-native-camera](http://www.oschina.net/p/react-native-camera)是 React
Native 的摄像头 viewport。这个模块应用于开发的早期阶段，它支持摄像头的转换和基本图片捕捉。

使用示例：
```

 var React = require('react-native');



 var {



   AppRegistry,



   StyleSheet,



   Text,



   View,



 } = React;



 var Camera = require('react-native-camera');



 var cameraApp = React.createClass({



   render: function() {



     return (



       <View



         <TouchableHighlight onPress={this._switchCamera}>



           <View>



             <Camera>



               ref="cam"



               aspect="Stretch"



               orientation="PortraitUpsideDown"



               style={{height: 200, width: 200}}



             />



           </View>



         </TouchableHighlight>



       </View>



     );



   },



   _switchCamera: function() {



     this.refs.cam.switch();



   }



 });



 AppRegistry.registerComponent('cameraApp', () = cameraApp);

```
# react-native-video

[react-native-video](http://www.oschina.net/p/react-native-video)是Video标签控件。

示例：

 ```
// Within your render function, assuming you have a file called



 // "background.mp4" in your project



 <Video source={"background"} style={styles.backgroundVideo} repeat={true} />



 // Later on in your styles..



 var styles = Stylesheet.create({



   backgroundVideo: {



     resizeMode: 'cover', // stretch and contain also supported



     position: 'absolute',



     top: 0,



     left: 0,



     bottom: 0,



     right: 0,



   },



 });
```

# 导航控件 react-native-navbar

[react-native-navbar](http://www.oschina.net/p/react-native-navbar)是用于 React
Native 上简单的定制化导航栏。

示例代码：

 ```
var NavigationBar = require('react-native-navbar');



 var ExampleProject = React.createClass({



   renderScene: function(route, navigator) {



     var Component = route.component;



     var navBar = route.navigationBar;



     if (navBar) {



       navBar = React.addons.cloneWithProps(navBar, {navigator: navigator,



         route: route



       });



     }    return (<View style={styles.navigator}



         {navBar}<Component navigator={navigator} route={route} /



       </View



     );



   },  render: function() {return (<Navigator



         style={styles.navigator}



         renderScene={this.renderScene}



         initialRoute={{



           component: InitialView,



           navigationBar: <NavigationBar title="Initial View"/



         }}



       /



     );



   }



 });
```

# React Native 轮播控件 react-native-carousel

[react-native-carousel](http://www.oschina.net/p/react-native-carousel)是一个简单的
React Native 轮播控件。

示例代码：

 ```
var Carousel = require('react-native-carousel');var ExampleProject =
React.createClass({



   render() {



    return (



         <Carousel width={375} indicatorColor="#ffffff"
inactiveIndicatorColor="#999999">



         <MyFirstPage />



         <MySecondPage />



         <MyThirdPage />



       </Carousel>



     );



   }



 });
```

# 下拉刷新组件 react-native-refreshable-listview

[react-native-refreshable-listview](http://www.oschina.net/p/react-native-
refreshable-listview)是下拉刷新 ListView，当数据重载的时候显示加载提示。

![](http://upload-images.jianshu.io/upload_images/17266280-69dea178605b6c57.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

# Modal 组件 react-native-modal

[react-native-modal](http://www.oschina.net/p/react-native-modal)是 React
Native 的 <Modal 组件。

![](http://upload-images.jianshu.io/upload_images/17266280-64142c5510173745.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

# 文本解析控件 react-native-htmltext

[react-native-htmltext](http://www.oschina.net/p/react-native-htmltext)可以用
HTML 像 markup 一样在 ReactNative 里创建出相应效果的样式文本。ReactNative 为那些样式文本提供一个文本元素，用于取代
NSAttributedString，你可以创建嵌套的文本：

 ```
<Text style={{fontWeight: 'bold'}}>



   I am bold



   <Text style={{color: 'red'}}> and red </Text>



 </Text>
```

# react-native-htmlview

[react-native-htmlview](http://www.oschina.net/p/react-native-htmlview)是一个将
HTML 目录作为本地视图的控件，其风格可以定制。

![](http://upload-images.jianshu.io/upload_images/17266280-7939ef617ef83e93.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

# LinearGradient 组件 react-native-linear-gradient

[react-native-linear-gradient](http://www.oschina.net/p/react-native-linear-
gradient)是一个 React Native 的 LinearGradient 组件。

![](http://upload-images.jianshu.io/upload_images/17266280-2438e3c6c57ef076.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

# 双向循环播放 react-native-looped-carousel

[react-native-looped-carousel](http://www.oschina.net/p/react-native-looped-
carousel)是基于 React Native 的双向循环播放控件。

 示例代码：

 ```
'use strict';var React = require('react-native');var Carousel = require
('react-native-looped-carousel');var Dimensions = require('Dimensions');var
{width, height} = Dimensions.get('window');var {



   AppRegistry,



   StyleSheet,  Text,



   View



 } = React;var carouselTest = React.createClass({  render: function() {
return (      <Carousel delay={500}>



           <View
style={{backgroundColor:'#BADA55',width:width,height:height}}/>



           <View style={{backgroundColor:'red',width:width,height:height}}/>



           <View style={{backgroundColor:'blue',width:width,height:height}}/>



       </Carousel>



     );



   }



 });



 AppRegistry.registerComponent('carouselTest', () = carouselTest);
```

# Teaset

React Native UI 组件库

<https://github.com/rilyu/teaset/blob/master/docs/cn/README.md>

如果你知道其他 React Native 插件，在评论与大家分享一下吧～

