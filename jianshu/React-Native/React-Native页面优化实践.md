---
title: React-Native页面优化实践
thumbnail: 
categories: React-Native
tags: [React-Native,ReactNative优化]
---

# 生产环境下日志输出禁用  

接入babel-plugin-transform-remove-console

> npm install babel-plugin-transform-remove-console --save-dev

配置.babelrc

> // 生产环境下配置去掉console输出

>

> {

>

>   ...

>

>   "plugins": [

>

>     ...

>

>   ],

>

>   "env": {"production": {

>

>       "plugins": [["transform-remove-console", {"exclude": ["error"]}]]

>

>   }

>

>   }

>

> }

# 采用setNativeProps

在RN中，如果需要频繁刷新view，建议使用setNativeProps，避免使用setState导致的频繁render。

类似顶部tab的透明度渐变，就适用这种情况

官方原文建议

> 在（不得不）频繁刷新而又遇到了性能瓶颈的时候。
直接操作组件并不是应该经常使用的工具。一般来说只是用来创建连续的动画，同时避免渲染组件结构和同步太多视图变化所带来的大量开销。setNativeProps
是一个“简单粗暴”的方法，它直接在底层（DOM、UIView等）而不是React组件中记录state，这样会使代码逻辑难以理清。所以在使用这个方法之前，请尽量先尝试用setState
和shouldComponentUpdate方法来解决问题。

# 使用PureComponent或shouldComponentUpdate

 **PureComponent**

当组件更新时，如果组件的 props 和 state 都没发生改变， render 方法就不会触发，省去 Virtual DOM
的生成和比对过程，达到提升性能的目的。

具体原理是 在shouldComponentUpdate回调中，对oldState和newState 及
oldProps和newProps进行浅比较，如不同，才return true，进而回调render。

 **重写shouldComponentUpdate**

代码块

> shouldComponentUpdate() {

>

>      return this.state.update;

>

> }

控制在需要的时候才去刷新，根据需求或者业务去控制。

# Android硬件加速

通过启用View的renderToHardwareTextureAndroid属性
为true，可以开启View的硬件加速。（决定这个视图是否要把它自己（以及所有的子视图）渲染到一个 GPU 上的硬件纹理中。）

在 Android
上，这对于只修改不透明度、旋转、位移、或缩放的动画和交互十分有用：在这些情况下，视图不必每次都重新绘制，显示列表也不需要重新执行。纹理可以被重用于不同的参数。负面作用是这会大量消耗显存，所以当交互/动画结束后应该把此属性设置回
false。

 **shouldRasterizeIOS** 在iOS上有个 **shouldRasterizeIOS属性，**
可以设置该view在被渲染到屏幕之前，先绘制到一个位图上，这个我理解和Android中的双缓冲区比较想像。

这个属性对于不会修改组件和子视图尺寸的动画和交互十分有用。举例来说，当我们移动一个静态视图的位置的时候，预渲染允许渲染器重用一个缓存了静态视图的位图，并快速合成。

# 长列表加载

使用用复用性更强的FlatList或SectionList

 **FlatList或SectionList优化：**

Item采用PureComponent或重写shouldComponentUpdate

getItemLayout如果行高是固定的，可以使用getItemLayout，避免动态测量内容尺寸的开销。

# 首屏进入时间优化

 **减少bundle包大小**

图片压缩；

图片上传到图片服务器，再引用；

mrn团队的拆包策略（目前有bug）

 **懒加载**

JS在执行import时有时很需要时间，首屏不需要展示的组件可以懒加载

代码块

> import React, { Component } from 'react';

>

> import { TouchableOpacity, View, Text } from 'react-native';

>

> // 先把这个组件赋值为null

>

> let VeryExpensive = null;

>

> export default class Optimized extends Component {

>

>   state = { needsExpensive: false };

>

>   didPress = () => {

>

>     if (VeryExpensive == null) {

>

>     // 真正需要这个组件的时候才加载

>

>       VeryExpensive = require('./VeryExpensive').default;

>

>     }

>

>     this.setState(() => ({

>

>       needsExpensive: true,

>

>     }));

>

>   };

>

>   render() {

>

>     return (

>

>       <View style={{ marginTop: 20 }}>

>

>         <TouchableOpacity onPress={this.didPress}>

>

>           <Text>Load</Text>

>

>         </TouchableOpacity>

>

>       // 根据需要判断是否渲染该组件

>

>         {this.state.needsExpensive ? <VeryExpensive /> : null}

>

>       </View>

>

>     );

>

>   }

>

> }

