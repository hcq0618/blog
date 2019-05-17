---
title: Reat-Native拓展
thumbnail: 
categories: React-Native
tags: [React-Native,ReactNative]
---

# 腾讯微信小程序  

注：手机QQ未来也预期会开放一套类似的开放平台

 **React Native**

没有公开的文档在说明，但据打听和一些资料显示手机QQ和手机QQ浏览器都不同程度使用了 React
Native，QQ浏览器是在首页的feed流使用了RN；其中手机QQ团队应该还在自研一套动态化技术方案（柏拉图），未来会开放。

# 百度轻应用

百度在 2013 年百度世界大会上宣布推出“轻应用”（Light App），百度提供了配套基础设施将移动网站快速转化成轻应用。轻应用本质上是
WebApp，类似微信的公众平台，用户体验受当年手机性能的极大制约，以至于后来日渐式微。

 **React Native → HtmlNative**

贴吧微粉2016年曾经全量采用 React Native，在去年爆发 Facebook 协议事件之后，百度内部出现了大量替代 React Native
的轮子，重写了部分涉及协议冲突的组件。目前手机百度采用 HtmlNative 方案，定制了 Webkit 的增强版。

# 京东-JDReact

京东采用 React Native 的定制方案 JDReact，对 React Native
的核心库做了裁剪和二次开发，搭建了后台功能支撑平台，同时结合京东的业务特点封装了包括 UI 在内的公共组件库，实现了三端融合，目前已经推广到了20多个业务。

# 携程-Ctrip React Native

携程采用 React Native 的定制方案 CRN（Ctrip React Native），从2016年4月份开始，携程开始小范围使用 React
Native，实现了站内信和机票低价订阅，随后开始大规模在各个 BU 推广，有超过15 个业务模块在使用，涉及页面在50个以上，据称已经达到了 85%
的双端代码复用率。

# 去哪儿-Qunar React Native

去哪儿采用 React Native 的定制方案 QRN（Qunar React
Native），抹平了平台差异，降低了开发成本，广泛应用于机票、酒店等核心业务，据称已经达到了 95% 的双端代码复用率。

# 艺龙-Enjoy React Native

艺龙采用 React Native 的定制方案 ERN，基于 web → Native 的思路，将纯 Html 标签转换为 Native
组件，从而抹平了平台差异，降低开发成本。

