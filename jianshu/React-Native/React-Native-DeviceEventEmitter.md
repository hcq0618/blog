---
title: React-Native-DeviceEventEmitter
thumbnail: 
categories: React-Native
tags: [React-Native,ReactNative库]
---

# 实现  

DeviceEventEmitter在RN内的发送和接受消息。例如：

A页面注册通知：

> import {DeviceEventEmitter} from'react-native';

>

> //…

>

> //调用事件通知

>

> DeviceEventEmitter.emit('xxxName’,param);

>

> //xxxName:通知的名称 param：发送的消息（传参）

B页面接收通知：

> componentDidMount(){

>

> varself =this;

>

> this.listener =DeviceEventEmitter.addListener('xxxName',function(param){

>

> // use param do something

>

> });

>

> }

>

> //xxxName:通知的名称 param:接收到的消息（传参）

>

> componentWillUnmount(){

>

> this.listener.remove();

>

> }

>

> //在componentWillUnmount 内需要我们手动移除通知

知道DeviceEventEmitter的简单使用后

我的页面在获取到用户数据后：

> //注册监听事件，时间名称：changeMine 传参：jsonData.avatar（头像url）

>

> DeviceEventEmitter.emit('changeMine',jsonData.avatar);

tabbar.js 文件:

> componentDidMount(){

>

> varself =this;

>

> this.listener = DeviceEventEmitter.addListener('changeMine',function(url){

>

> self.setState({

>

> avatar:url

>

> })

>

> });

>

> //通知开始，获取到url，调用setState 方法，刷新状态机，这时候实时的刷新了‘我的’图标

>

> //最后别忘了移除通知

>

> componentWillUnmount(){

>

> this.listener.remove();

>

> }

# js 向 js 发送数据

DeviceEventEmitter.emit('自定义名称',发送数据);

例：边看边买退出登录之后，我的淘宝和详情页的钱包数据应该改变。这时，我们可以在退出登录请求返回退出登录成功时发送一个通知

> userInfo.userLogout((success) => {

>

> if (success) {

>

>
DeviceEventEmitter.emit('taobaoBind',{taobaoBind:false,walletSum:0.00,couponNum:0});

>

> const nav = this.props.navigator;

>

> const routers = nav.getCurrentRoutes();

>

> if (routers.length > 1) {

>

> nav.pop();

>

> }

>

> }

>

> });

然后在我的淘宝和详情页接收通知，并使用setState改变数据

> DeviceEventEmitter.addListener('taobaoBind',(events)
=>{this.setState({walletSum : events.walletSum});});

js接受数据

> DeviceEventEmitter.addListener('名称',(events) ={使用数据events});

android向js发送数据

> WritableMap params = Arguments.createMap();

>

> params.putString("message",msg.obj.toString());

>

>
reactContext.getJSModule(DeviceEventManagerModule.RCTDeviceEventEmitter.class)

>

> .emit(eventName, params);

例：扫码轮询时，扫码成功可以向扫码页发送一个扫码成功的状态，输入密码完成时，也可以发送一个状态，使扫码页自动关闭。并将用户信息发给我的淘宝，详情页等。

