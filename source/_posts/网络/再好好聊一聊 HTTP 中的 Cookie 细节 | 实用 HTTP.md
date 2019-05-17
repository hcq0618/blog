---
title: 再好好聊一聊 HTTP 中的 Cookie 细节 | 实用 HTTP
thumbnail: 
categories: 网络
tags: [网络]
---
##  

## 一、序

Hi，大家好，我是承香墨影！

HTTP 协议在网络知识中占据了重要的地位，HTTP 协议最基础的就是请求和响应的报文，而报文又是由报文头（Header）和实体组成。大多数 HTTP
协议的使用方式，都是依赖设置不同的 HTTP 请求/响应 的 Header 来实现的。

本系列《实用 HTTP》就抛开常规的 Header 讲解式的表述方式，从实际问题出发，来分析这些 HTTP
协议的使用方式，到底是为了解决什么问题？同时讲解它是如何设计的和它实现原理。

HTTP
协议是一种无状态的“松散协议”，它不会记录不同请求的状态，并且因为它本身包含了两端（客户端和服务端），根据请求和响应来区分，它大部分的内容都只是一个建议，其实双边是可以不遵守此建议的。

> “这里写了建议零售价 2 元…”

>

> “哦，不接受建议！”

文本是本系列的第四篇，前三篇传送门：

  * [HTTP 的缓存机制](http://mp.weixin.qq.com/s?__biz=MzIxNjc0ODExMA==&mid=2247485517&idx=1&sn=3edffef8db15d92c26072d85df1cc5a8&chksm=9785116ca0f2987a4ccf77339800873d092c1bded522d50fcf03aec98a9f51b23355e28aa3b7&scene=21#wechat_redirect)

  * [HTTP 内容实体编码压缩机制](http://mp.weixin.qq.com/s?__biz=MzIxNjc0ODExMA==&mid=2247485524&idx=1&sn=183b34cfd87f2a6fddc43187dc6fa72f&chksm=97851175a0f29863245fe35a402e801cf9fb8f6864acd3e546473aded4b18dd4538154403f79&scene=21#wechat_redirect)

  * [HTTP 传输编码压缩机制](http://mp.weixin.qq.com/s?__biz=MzIxNjc0ODExMA==&mid=2247485535&idx=1&sn=2e9f9113de8b84429e19ee12b69f3336&chksm=9785117ea0f298683c0a56d016711633f7b8b86d7570f8ffbe9216ae5f175ea5fa53471e55c4&scene=21#wechat_redirect)

本身 HTTP 就是一个无状态的协议，但是有时候我们又有需要增加状态的需求，这个时候延伸出来了 Cookie，利用 Cookie
可以让传输的时候保持一些状态信息。

本文就来讲讲 Cookie 的所有细节。

## 二、Cookie的使用

### 2.1 什么是 Cookie？

先明确一点，Cookie 就是为了解决 HTTP 协议无状态的问题，接下来举个例子说明。

早年间医院对患者的病例还没有在线建档的时候，都需要患者在就医之前，办理一个病历的小册子，医生会在病历中写上此次就医的情况，什么时间、有什么表现的反映、诊断是什么病、开了一些什么药等等。如果下次又生病了，有病历的情况下，都会要求患者再把病历带上，这样医生就能通过病历了解到之前的情况。

在 Cookie 的实现上，也是这样的。

服务端（医生）在收到客户端（患者）请求的时候，将一些用户标识信息加入到 Cookie （病例）中，随着响应返回给客户端，客户端将 Cookie
中的信息存储在本地，下次再请求此服务器的时候，再将 Cookie 中携带的数据原样传输给服务端，此时服务端就能通过 Cookie
中的用户标识，识别出这是之前请求过的某个用户。

在这个例子中，服务端就是医生的角色、客户端是患者的角色、Cookie 就是病历。

Netscape 官方文档中的定义为：Cookie 是指在 HTTP 协议下，服务器或脚本可以维护客户端计算机上信息的一种方式 。通俗地说，Cookie
是一种能够让网站 Web 服务器把少量数据储存到客户端的硬盘或内存里，或是从客户端的硬盘里读取数据的一种技术。 Cookie 文件则是指在浏览某个网站时，由
Web 服务器的 CGI 脚本创建的存储在浏览器客户端计算机上的一个小文本文件。

### 2.2 一个完整的 Cookie 传输流程

HTTP 协议中的规则，都是通过在请求头和响应头中写入输入来实现，Cookie 也是这样的。

服务端通过 Set-Cookie 这个响应头来向客户端中写入 Cookie 信息，而客户端读取 Set-Cookie
这个响应头中的信息存储起来，在下次请求的时候取出来，再通过 Cookie 这个请求头，将 Cookie 的数据传输给服务端。

![](640.jpg)

再看一个浏览器中，Cookie 使用的实例。

![](640_1.jpg)

在响应头（Response Header）中，使用 Set-Cookie 传递不同的 Cookie 数据，多个数据可以分开成多个 Set-Cookie 头。

在请求头中（Request Header）中，使用 Cookie 这个请求头传递 Cookie 数据，不同的数据通过 ;分割。

## 三、Cookie 的细节

到这里，我想你应该弄清楚了 cookie 的整个执行流程，接下来我们再来探究一些 cookie 的细节。

### 3.1 Cookie 的类型

cookie 其实都是存储在客户端，通常我们说 cookie 对应的客户端，就是在说浏览器。

对于 cookie，我们可以简单的将 cookie 分为两类：

  * 会话 cookie。

  * 持久 cookie。

会话 cookie 是一种临时的 cookie，用于存储一些临时的信息，存储在内存中，会话 cookie 在用户退出浏览器的时候，会被清空删除。而持久
cookie 的生存周期会更长久一些，被存储在磁盘上，浏览器重启后它们依然存在，但是他们会有一个过期的时间，只在此时间之后会被置为失效。

会话 cookie 和持久 cookie 之间唯一的区别就是它们的过期时间，只要是设置了过期时间的 cookie 就是持久 cookie，反之则是会话
cookie。

仔细看前面的流程图中，有一个 domain 的字段是用于标识当前 Cookie 支持的域名的，而想要设置过期时间，可以使用 Expires 或者 Max-
Age 参数进行设置，有点类似我们前面讲 HTTP 缓存的参数。

### 3.2 Cookie 的配置参数

到现在我们已经介绍了两个 Cookie 配置的信息，Domain 和 Expires/Max-Age，分别用来配置域名和过期策略。

这些都很好理解，毕竟浏览器是开放的，它会访问很多不同的网址，如果每个请求都将所有的 Cookie 信息都传递过去，基本上是不现实的。而这些配置参数，就是对
Cookie 增加一些附加的设置，进行一些简单的限制和过滤，在减少传输量的同时也保证了安全。

Domain 这个参数可以限制只在此域名下的请求，才传递该 Cookie，其他的不传递。

Cookie 其实还支持其他的一些参数配置，打开 Chrome 的调试模式，在 Application 中就可以看到当前页面的 Cookie 信息。

下面以一篇微信文章页面所存储的 Cookie 为例。

![](640_2.jpg)

这个表中，就是当前存储的所有 Cookie 信息，而表头，则是 Chrome 支持的 Cookie 信息。

下面我们分别来介绍它们。

  * Name:Value ：Cookie 存储的数据就是一个 Key-Value 的键值对，所以这两个参数没什么争议，就是数据的 Key 和 Value。

  * Domain：Cookie 的域，限制请求头传输的域。

  * Path：域中与 Cookie 相关的路径前缀。

  * Expires/Max-Age：过期时间或者超时间隔。

  * http：此属性为 True，表示只会在 HTTP 请求头中携带此 Cookie 信息，而无法通过 document.cookie 来访问此 Cookie。

  * Secure：安全，是否只有在使用 SSL 连接时才发送这个 Cookie。

其实都很好理解，就不展开讲解了。

### 3.3 Set-Cookie2 和 Cookie2

有些资料里会提到 Set-Cookie2 和 Cookie2 ，这些都是历史遗留问题，当初想对 Cookie
再进行一些功能上的扩展，但并未得到广泛的实施，现在已经弃用了。

大家了解一下即可，有兴趣可以参考 RFC 6265。

> RFC 6265:

>

> https://tools.ietf.org/html/rfc6265

### 3.4 浏览器对 Cookie 的限制

大部分时候我们聊到 Cookie 都在说的是服务器和浏览器进行通信时候，而不同的浏览器对 Cookie 存储的限制是不一样的。例如：单个域名可存储的
Cookie 数量、Cookie 大小等。

我简单找了一些资料，来说明不同浏览器对 Cookie 的支持情况。

![](640.png)

这些数据我没有验证过，但是也能说明不同浏览器对 Cookie 的支持情况。在进行页面 Cookie 操作的时候，应该尽量保证 Cookie 的个数小于 20
个，总大小小于 4KB，这是一个安全且保险的范围。

## 四、Cookie的查缺补漏

### 4.1 Cookie 安全

前面配置 Cookie 参数的时候，有两个参数：http 和 secure 属性，它们就在一定程度上保证了安全。

1. http 属性

设置了 http 属性，标识它是一个 “HttpOnly” 的，那么通过一些脚本程序（例如 JS的 document.cookie）将无法读取到这个
Cookie 信息，它只会出现在请求的报文头内。

2. secure 属性

secure 属性强制该 Cookie 只有在 SSL 的环境下才会想服务器传输，相对也保证了传输的安全。

### 4.2 Cookie 不支持跨域

Cookie 本身是不支持跨域的，一定程度也保证了 Cookie 的安全，如果非要跨域其实作为前端基本上能做的很少，大部分都需要服务端的二次配合。

例如：nginx 反向代理、Jsonp、nodejs 的 superagent、iframe 等方法。

有兴趣再单独了解就好了。

## 五、Cookie 小结

HTTP 中的 Cookie 知识点，基本上都已经讲解清楚了，我们再次总结一下关键知识点。

1. Cookie 主要是为了解决 HTTP 协议无状态的问题。

2. 服务端通过 Set-Cookie 响应头来向客户端设置 Cookie。

3. 客户端通过 Cookie 请求头向服务端发送之前存储的 Cookie 数据。

4. Cookie 依据过期时间进行区分，将类型分为：临时 Cookie 和 持久 Cookie。

5. Cookie 可以通过配置不同的参数，进行限制，例如过期时间、支持的域名、是否安全（secure）等。

6. Cookie 不支持跨域，跨域还需要其他的方式绕开来实现。

7. Cookie 只能做到相对的安全，任何事情没有绝对的安全。

参考：

  * Cookie 个数限制及大小：https://my.oschina.net/gaollg/blog/71299。

  * RFC 6265：https://tools.ietf.org/html/rfc6265

  * cookie 小结：http://www.cnblogs.com/xianyulaodi/p/6476991.html

  

  

