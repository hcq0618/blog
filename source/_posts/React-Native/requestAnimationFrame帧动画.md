---
title: requestAnimationFrame帧动画
thumbnail: 
categories: ReactNative
tags: [ReactNative]
---

# 前言  

动画是移动应用中的一个相当重要的组成部分，一个用户体验良好的应用通常都具有流畅、有意义的动画。类似原生平台，React
Native也为我们提供了丰富的动画API：requestAnimationFrame、LayoutAnimation、Animated。

requestAnimationFrame:帧动画，是最容易实现的一种动画，通过不断改变组件的state值，从而在视觉上产生一种动画的效果，类似于gif动画的方式。

LayoutAnimation:布局动画，当布局发生改变时的动画模块，允许在全局范围内创建和更新动画，这些动画会在下一次渲染或布局周期运行，实现单个动画非常简洁，体验和性能良好。

Animated:用于创建更精细的交互控制的动画，可进行多个动画的组合动画，具备极高的性能，是功能最强大的动画API。

本节我们先介绍requestAnimationFrame。

# requestAnimationFrame帧动画的实现

requestAnimationFrame实现帧动画的原理非常粗暴简洁，即通过修改state值来不断得改变视图上的样式，从而在视觉上产生一种动画的效果。

 ```
import React, { Component } from'react';



 import {



 AppRegistry,



 StyleSheet,



 Text,



 View,



 TouchableOpacity,



 Platform,



 } from'react-native';



 exportdefaultclassFrameAnimationDemo extends Component {



 constructor(props){



 super(props);



 this.state = {



 width:200,



 height:20,



 };



 }



 _onPress() {



 //每按一次增加近30宽高



 varcount =0;



 while(++count<30){



 requestAnimationFrame(()={



 this.setState({



 width:this.state.width +1,



 height:this.state.height +1



 });



 })



 }



 }



 render() {



 return(



 <Viewstyle={styles.container}>




<Viewstyle={[styles.content,{width:this.state.width,height:this.state.height}]}>



 <Textstyle={[{textAlign:'center'}]}>Hello World!</Text>



 </View>



 <TouchableOpacitystyle={styles.content}onPress={this._onPress.bind(this)}>



 <Viewstyle={styles.button}>



 <Textstyle={styles.buttonText}Press me!></Text>



 </View>



 </TouchableOpacity>



 </View>



 );



 }



 }



 const styles = StyleSheet.create({



 container: {



 marginTop:25,



 flex: 1,



 },



 content: {



 backgroundColor: 'rgba(200, 230, 255, 0.8)',



 marginBottom:10,



 justifyContent:"center",



 alignSelf:"center",



 },



 button: Platform.select({



 ios: {},



 android: {



 elevation: 4,



 // Material design blue from https://material.google.com/style/color.html
#color-color-palette



 backgroundColor: '#2196F3',



 borderRadius: 2,



 width:100,



 height:30,



 },



 justifyContent:"center",



 alignSelf:"center",



 }),



 buttonText: {



 alignSelf:"center",



 }



 });
```

从效果上看动画有种一顿一顿的感觉。这是由于通过修改state值，导致频繁地销毁、重绘视图，内存开销大，从而使得动画卡顿明显。另外对于帧动画而言，如果帧数较少，动画的效果会比较生硬，帧数过多又会引发性能问题。

# 优化

如果帧动画的方式更符合当前对动画的控制方式，我们可以对上述方法做一点优化，在requestAnimationFrame中采用setNativeProps直接修改组件的属性并触发局部刷新，不会导致重绘组件，因此在性能上优于直接修改state的方法。

修改_onPress方法，将对this.setState的直接修改改为对”Hello
World”按钮的属性修改this.refs.view1.setNativeProps。

 ```
_onPress() {



 varcount =0;



 while(++count<30){



 requestAnimationFrame(()={



 this.refs.view1.setNativeProps({



 style: {



 width:this.state.width++,



 height:this.state.height++



 }



 });



 });



 }



 }
```

this.refs.view1指向的是”Hello World”文字的父视图。

 ```
<View ref="view1"style={[styles.content, {width:this.state.width,
height:this.state.height}]}>



 <Textstyle={[{textAlign:'center'}]}>Hello World!</Text>



 </View>
```

通过对比可以看出流畅顺滑多了。

每个动画API都有其适应和不适应的场景，如果要实现“弹性动画”，“缓入缓出”等效果，使用requestAnimationFrame还是比较难的，需要辅助各种函数。下一节将介绍另一种动画API——LayoutAnimation。

[GitHub地址](https://github.com/mronion0603/ReactNativeExercise/blob/master/src/13_animation/FrameAnimationDemo.js)

