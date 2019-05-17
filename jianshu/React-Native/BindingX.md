---
title: BindingX
thumbnail: 
categories: React-Native
tags: [React-Native,ReactNative库]
---

**基于weex / React Native的富交互解决方案。**

官网:<https://alibaba.github.io/bindingx/>

它提供了一种称之为表达式绑定(Expression Binding)的机制可以在 weex
上让手势等复杂交互操作以60fps的帧率流畅执行，而不会导致卡顿，因而带来了更优秀的用户体验 。

# 简要介绍

由于weex/RN框架底层使用的JS-Native
Bridge具有天然的异步特性，这使得JS和Native之间的通信会有固定的性能损耗，因此在一些复杂的实时交互场景中(如手势)，JS
代码很难以高帧率运行，这极大地限制了框架的能力。目前官方并没有很好的方式解决。

而我们通过探索，提出了一种全新的方式用来解决这个问题，方案称之为Expression
Binding。它的核心思想是将"交互行为"以表达式的方式描述，并提前预置到Native从而避免Native与JS频繁通信。

# 示例展示

下面展示了一部分使用bindingx的示例。您可以下载或者编译我们的playground
app来获取更多的示例。同时，您也可以在我们的[在线playground](https://alibaba.github.io/bindingx/playground)上编写您自己的demo。

注意：Weex支持两种前端写法（rax和vue），链接是直接跳转到Playground。 React-
Native由于目前Playground还不支持，所以直接跳转到源码。

# 特性

复杂但流畅的交互效果

强大的表达式解析引擎

丰富的缓动函数

# 文档与教程

<https://alibaba.github.io/bindingx/guide/introduce>

