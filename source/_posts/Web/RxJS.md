---
title: RxJS
thumbnail: 
categories: Web
tags: [Web,RxJs]
---
## 1\. 前言

### 1.1 什么是RxJS？

RxJS是ReactiveX编程理念的JavaScript版本。ReactiveX来自微软，它是一种针对异步数据流的编程。简单来说，它将一切数据，包括HTTP请求，DOM事件或者普通数据等包装成流的形式，然后用强大丰富的操作符对流进行处理，使你能以同步编程的方式处理异步数据，并组合不同的操作符来轻松优雅的实现你所需要的功能。

### 1.2 RxJS可用于生产吗？

ReactiveX由微软于2012年开源，目前各语言库由ReactiveX组织维护。RxJS在GitHub上已有8782个star，目前最新版本为5.5.2，并持续开发维护中，其中官方测试用例共计2699个。

![](bVXtzg)  

### 1.3 RxJS对项目代码的影响？

RxJS中的流以Observable对象呈现，获取数据需要订阅Observable，形式如下：

```
const ob = http$.getSomeList(); //getSomeList()返回某个由`Observable`包装后的http请求

ob.subscribe((data) =>console.log(data));

`//在变量末尾加$表示Observable类型的对象。`
```

以上与Promise类似：

```
const promise = http.getSomeList(); // 返回由`Promise`包装的http请求

promise.then((data) =>console.log(data));
```

实际上Observable可以认为是加强版的Promise，它们之间是可以通过RxJS的API互相转换的：

```
const ob = Observable.fromPromise(somePromise); // Promise转为Observable

const promise = someObservable.toPromise(); // Observable转为Promise
```

因此可以在Promise方案的项目中安全使用RxJS，并能够随时升级到完整的RxJS方案。

### 1.4 RxJS会增加多少体积？

RxJS(v5)整个库压缩后约为140KB，由于其模块化可扩展的设计，因此仅需导入所用到的类与操作符即可。导入RxJS常用类与操作符后，打包后的体积约增加30-60KB，具体取决于导入的数量。

> 不要用 import { Observable } from 'rxjs'这种方式导入，这会导入整个rxjs库，按需导入的方式如下：


> import { Observable } from 'rxjs/Observable' //导入类


> import 'rxjs/add/operator/map' // 导入实例操作符


> import 'rxjs/add/observable/forkJoin' // 导入类操作符

## 2\. RxJS快速入门

### 2.1 初级核心概念

  * Observable

  * Observer

  * Operator

Observable被称为可观察序列，简单来说数据就在Observable中流动，你可以使用各种operator对流进行处理，例如：

```
const ob = Observable.interval(1000);

ob.take(3).map(n => n * 2).filter(n => n > 2);
```

第一步代码我们通过类方法interval创建了一个Observable序列，ob作为源会每隔1000ms发射一个递增的数据，即0 -> 1 ->
2。第二步我们使用操作符对流进行处理，take(3)表示只取源发射的前3个数据，取完第三个后关闭源的发射；map表示将流中的数据进行映射处理，这里我们将数据翻倍；filter表示过滤掉出符合条件的数据，根据上一步map的结果，只有第二和第三个数据会留下来。

上面我们已经使用同步编程创建好了一个流的处理过程，但此时ob作为源并不会立刻发射数据，如果我们在map中打印n是不会得到任何输出的，因为ob作为Observable序列必须被“订阅”才能够触发上述过程，也就是subscribe（发布/订阅模式）。
```
const ob = Observable.interval(1000);

ob.take(3).map(n => n * 2).filter(n => n > 0).subscribe(n =>console.log(n));
```

结果：

2 //第2秒

4 //第3秒

上面代码中我们给subscribe传入了一个函数，这其实是一种简写，subscribe完整的函数签名如下：

```
ob.subscribe({

next: d => console.log(d),

error: err => console.error(err),

complete: () => console.log('end of the stream')

})
```

直接给subscribe传入一个函数会被当做是next函数。这个完整的包含3个函数的对象被称为observer（观察者），表示的是对序列结果的处理方式。next表示数据正常流动，没有出现异常；error表示流中出错，可能是运行出错，http报错等等；complete表示流结束，不再发射新的数据。在一个流的生命周期中，error和complete只会触发其中一个，可以有多个next（表示多次发射数据），直到complete或者error。

observer.next可以认为是Promise中then的第一个参数，observer.error对应第二个参数或者Promise的catch。

RxJS同样提供了catch操作符，err流入catch后，catch必须返回一个新的Observable。被catch后的错误流将不会进入observer的error函数，除非其返回的新observable出错。

```
Observable.of(1).map(n => n.undefinedMethod()).catch(err => {

// 此处处理catch之前发生的错误

return Observable.of(0); // 返回一个新的序列，该序列成为新的流。

});
```

### 2.2 创建可观察序列

创建一个序列有很多种方式，我们仅列举常用的几种：

#### Observable.of(...args)

Observable.of()可以将普通JavaScript数据转为可观察序列，[点我测试](http://xgrommx.github.io/rx-
book/content/observable/observable_methods/of.html)。

#### Observable.fromPromise(promise)

将Promise转化为Observable，[点我测试](http://xgrommx.github.io/rx-
book/content/observable/observable_methods/frompromise.html)。

#### Observable.fromEvent(elment, eventName)

从DOM事件创建序列，例如Observable.fromEvent($input,
'click')，[点我测试](http://xgrommx.github.io/rx-
book/content/observable/observable_methods/fromevent.html)。

#### Observable.ajax(url | AjaxRequest)

发送http请求，AjaxRequest参考[这里](http://cn.rx.js.org/class/es6/observable/dom/MiscJSDoc.js~AjaxRequestDoc.html)

#### Observable.create(subscribe)

这个属于万能的创建方法，一般用于只提供了回调函数的某些功能或者库，在你用这个方法之前先想想能不能用RxJS上的类方法来创建你所需要的序列，[点我测试](http://xgrommx.github.io
/rx-book/content/observable/observable_methods/create.html)。

### 2.3 合并序列

合并序列也属于创建序列的一种，例如有这样的需求：进入某个页面后拿到了一个列表，然后需要对列表每一项发出一个http请求来获取对应的详细信息，这里我们把每个http请求作为一个序列，然后我们希望合并它们。

合并有很多种方式，例如N个请求按顺序串行发出（前一个结束再发下一个）；N个请求同时发出并且要求全部到达后合并为数组，触发一次回调；N个请求同时发出，对于每一个到达就触发一次回调。

如果不用RxJS，我们会比较难处理这么多情形，不仅实现麻烦，维护更麻烦，下面是使用RxJS对上述需求的解决方案：

```
const ob1 = Observable.ajax('api/detail/1');

const ob2 = Observable.ajax('api/detail/2');

...

const obs = [ob1, ob2...];

`// 分别创建对应的HTTP请求。`
```

  1. N个请求按顺序串行发出（前一个结束再发下一个）

Observable.concat(...obs).subscribe(detail =>console.log('每个请求都触发回调'));

  1. N个请求同时并行发出，对于每一个到达就触发一次回调

Observable.merge(...obs).subscribe(detail =>console.log('每个请求都触发回调'));

  1. N个请求同时发出并且要求全部到达后合并为数组，触发一次回调

Observable.forkJoin(...obs).subscribe(detailArray =>console.log('触发一次回调'));

## 3\. 使用RxJS实现搜索功能

搜索是前端开发中很常见的功能，一般是监听<input />的keyup事件，然后将内容发送到后台，并展示后台返回的数据。


<inputid="text"></input>`

`<script>`

`var text = document.querySelector('#text');`

` text.addEventListener('keyup', (e) =>{`

`var searchText = e.target.value;`

` // 发送输入内容到后台`

` $.ajax({`

`url: `/search/${searchText}`,`

`success: data => {`

` // 拿到后台返回数据，并展示搜索结果`

` render(data);`

` }`

` });`

` });`

`</script>`


上面代码实现我们要的功能，但存在两个较大的问题：

  * 多余的请求

当想搜索“爱迪生”时，输入框可能会存在三种情况，“爱”、“爱迪”、“爱迪生”。而这三种情况将会发起 3 次请求，存在 2 次多余的请求。

  * 已无用的请求仍然执行

一开始搜了“爱迪生”，然后马上改搜索“达尔文”。结果后台返回了“爱迪生”的搜索结果，执行渲染逻辑后结果框展示了“爱迪生”的结果，而不是当前正在搜索的“达尔文”，这是不正确的。

减少多余请求数，可以用 setTimeout 函数节流的方式来处理，核心代码如下：


<inputid="text"></input>`

`<script>`

`var text = document.querySelector('#text'),`

` timer = null;`

` text.addEventListener('keyup', (e) =>{`

` // 在 250 毫秒内进行其他输入，则清除上一个定时器`

` clearTimeout(timer);`

` // 定时器，在 250 毫秒后触发`

` timer = setTimeout(() => {`

`console.log('发起请求..');`

` },250)`

` })`

`</script>`


已无用的请求仍然执行
的解决方式，可以在发起请求前声明一个当前搜索的状态变量，后台将搜索的内容及结果一起返回，前端判断返回数据与当前搜索是否一致，一致才走到渲染逻辑。最终代码为：

````
<inputid="text"></input>`

`<script>`

`var text = document.querySelector('#text'),`

` timer = null,`

` currentSearch = '';`

  

` text.addEventListener('keyup', (e) =>{`

` clearTimeout(timer)`

` timer = setTimeout(() => {`

` // 声明一个当前所搜的状态变量`

` currentSearch ＝ '书'; `

  

`var searchText = e.target.value;`

` $.ajax({`

`url: `/search/${searchText}`,`

`success: data => {`

` // 判断后台返回的标志与我们存的当前搜索变量是否一致`

`if (data.search === currentSearch) {`

` // 渲染展示`

` render(data);`

` } else {`

` // ..`

` }`

` } `

` });`

` },250)`

` })`

`</script>`
```

上面代码基本满足需求，但代码开始显得乱糟糟。我们来使用RxJS实现上面代码功能，如下:

```
var text = document.querySelector('#text');

var inputStream = Rx.Observable.fromEvent(text, 'keyup') //为dom元素绑定'keyup'事件

.debounceTime(250) // 防抖动

.pluck('target', 'value') // 取值

.switchMap(url => Http.get(url)) // 将当前输入流替换为http请求

.subscribe(data => render(data)); // 接收数据
```

RxJS能简化你的代码，它将与流有关的内部状态封装在流中，而不需要在流外定义各种变量来以一种上帝视角控制流程。Rx的编程方式使你的业务逻辑流程清晰，易维护，并显著减少出bug的概率。

### 个人总结的常用操作符：

类操作符（通常为合并序列或从已有数据创建序列）

合并forkJoin, merge, concat

创建of, from, fromPromise, fromEvent, ajax, throw

实例操作符（对流中的数据进行处理或者控制流程）

map, filter,switchMap, toPromise, catch, take, takeUntil, timeout,
debounceTime, distinctUntilChanged, pluck。

对于这些操作符的使用不再详细描述，请参阅网上资料。

中文官网 <http://cn.rx.js.org/>

附上个人翻译的一些文章

  * [RxJS：冷热模式的比较](https://segmentfault.com/a/1190000011052037)

  * [RxJS: map, flatMap和flatMapLatest的区别](https://segmentfault.com/a/1190000011070872)

  * [RxJS: 详解forkJoin, zip, combineLatest之间的区别](https://segmentfault.com/a/1190000012369871)

参考文章：[构建流式应用：RxJS 详解](https://cloud.tencent.com/developer/article/1004937)

* * *

# RxJS 6有哪些新变化？

RxJs 6于2018年4月24日正式发布，为开发人员带来了一些令人兴奋的增补和改进。Ben Lesh, rxJS核心开发成员，强调：

  1. RxJS 6在拥有更小API的同时，带来了更整洁的引入方式

  2. 提供一个npm包，该package可以处理RxJS的向后兼容性，使得开发人员可以在不更改代码的情况下进行更新，同时还可以帮助TypeScript代码自动迁移。

RxJs
6这些新的改动为开发人员提供了以下三方面的优化：模块化方面的改进、性能提升、调试更方便。RxJs团队尽力保持新版本的向后兼容性，但是为了减少RxJs的API数量，还是引入了一些重大修改。

下面让我们一起来看一下RxJs团队在新版本中引入了哪些修改。

## RxJS 6的向后兼容性

为了便捷地从RxJS 5迁移到RxJS 6，RxJS团队发布了一个名为rxjs-compat的兄弟软件包。该软件包在v6和v5的API之间创建了一个兼容层。

RxJs团队建议开发人员通过安装^6.0.0版本的rxjs和rxjs-compat包来升级现有应用:

npm install rxjs@6 rxjs-compat@6 \--save

此包允许您在升级RxJS 6的同时继续运行现有代码库，而不会出现问题。他支持在RxJs 6中移除掉的功能。

安装rxjs-compat会导致打包后代码包体积的增加，如果你使用的是4.0.0版本以下的Webpack，该影响会被放大。

因此建议升级完成后将rxjs-compat移除。

## 使用rxjs-compat升级RxJS的限制

只有两个重大修改在rxjs-compat中未覆盖：

### TypeScript原型操作符

在极少数情况下，您的代码库定义了它自己的TypeScript原型操作符并修改了Observable命名空间。该情况下，您需要更新你的操作符相关代码才能使TypeScript正常编译。

在版本发布说明中，用户自定义的原型操作符可按如下方式创建：

```
Observable.prototype.userDefined = () => {

return new Observable((subscriber) => {

this.subscribe({

next(value) { subscriber.next(value); },

error(err) { subscriber.error(err); },

complete() { [subscriber.complete();](http://subscriber.complete\(\);/) },

});

});

});

  

source$.userDefined().subscribe();
```

为编译该类型的自定义操作符，需要做如下修改：
```

const userDefined = <T>() => (source: Observable<T>) => new
Observable<T>((subscriber) => {

this.subscribe({

next(value) { subscriber.next(value); },

error(err) { subscriber.error(err); },

complete() { [subscriber.complete();](http://subscriber.complete\(\);/) },

});

});

});

  

source$.pipe(

userDefined(),

)
```

### 同步错误处理

不再支持在try /
catch块内调用Observable.subscribe()。使用用Observable.subscribe()方法中的错误回调方法替换原先的try /
catch块来完成的异步错误的处理。

示例如下：

```
// deprecated

try {

source$.subscribe(nextFn, undefined, completeFn);

} catch (err) {

handleError(err);

}

  

// use instead

source$.subscribe(nextFn, handleError, completeFn);

```
现在在Observable.subscribe()中必须定义一个错误回调方法来异步处理错误。

## 删除RxJs兼容层前需要做的修改

如上所诉，rxjs-compat提供了V5与v6API间的临时兼容层，实质上rxjs-
compat为您的代码库提供了所需的v5版本功能，使得您可以逐步将您的代码库升级到v6版本。为了完成升级并移除rxjs-
compat依赖，您的代码库需要重构并停止使用v5版本中的如下功能：

### 修改import路径

建议TypeScript开发人员使用rxjs-tslint来重构import路径。

RxJS团队设计了以下规则来帮助JavaScript开发人员重构import路径：

  * rxjs: 包含创建方法，类型，调度程序和工具库。

`import { Observable, Subject, asapScheduler, pipe, of, from, interval, merge,
fromEvent } from'rxjs';`

  * rxjs/operators: 包含所有的管道操作符

`import { map, filter, scan } from 'rxjs/operators';`

  * rxjs/webSocket: 包含websocket subject实现.

`import { webSocket } from'rxjs/webSocket';`

  * rxjs/ajax: 包含Rx ajax实现.

`import { ajax } from'rxjs/ajax';`

  * rxjs/testing: 包含RxJS的测试工具库.

`import { TestScheduler } from'rxjs/testing';`

以下是一项小调查：您是否有常识使用rxjs-tslint升级您的应用程序？

![](bVbaUii)  

### 使用管道操作而不是链式操作

使用新的管道操作符语法替换旧有的链式操作。上一个操作符方法的结果会被传递到下一个操作符方法中。

不要移除rxjs-compat包，直到你将所有的链式操作修改为管道操作符。如果您使用TypeScript, ts-lint会在某种程度上自动执行此项重构。

Ben Lesh在[ng-conf 2018](https://www.ng-conf.org/sessions/introducing-
rxjs6/)上解释了[为什么我们应该使用管道操作符](https://youtu.be/JCXZhe6KsxQ?t=2m30s)。

请按照如下步骤将您的链式操作替换为管道操作：

  * 从rxjs-operators中引入您需要的操作符

> 注意：由于与Javascript保留字冲突，以下运算符名字做了修改：do -> tap, catch ->


> catchError, switch -> switchAll, finally -> finalize

import { map, filter, catchError, mergeMap } from 'rxjs/operators';

  * 使用pipe()包裹所有的操作符方法。确保所有操作符间的.被移除，转而使用,连接。记住！！！有些操作符的名称变了！！！

以下为升级示例：

// an operator chain

source

.map(x => x + x)

.mergeMap(n =>of(n + 1, n + 2)

.filter(x => x % 1 == 0)

.scan((acc, x) => acc + x, 0)

)

.catch(err =>of('error found'))

.subscribe(printResult);

  

// must be updated to a pipe flow

  

source.pipe(

map(x => x + x),

mergeMap(n =>of(n + 1, n + 2).pipe(

filter(x => x % 1 == 0),

scan((acc, x) => acc + x, 0),

)),

catchError(err =>of('error found')),

).subscribe(printResult);

注意我们在以上代码中嵌套使用了pipe()。

### 使用函数而不是类

使用函数而不是类来操作可观察对象(Observables)。所有的Observable类已被移除。他们的功能被新旧操作符及函数替代。这些替代品的功能与之前的类功能一模一样。

示例如下：

// removed

ArrayObservable.create(myArray)

  

// use instead

  

from(myArray)

  

// you may also use

  

newoperatorfromArray().

有关替换v5类为v6函数的完整列表，请查看[RxJS文档](https://github.com/ReactiveX/rxjs)。

#### 特殊情况

  * ConnectableObservable在v6中不能直接使用，要访问它，请使用操作符multicast，publish，publishReplay和publishLast。

  * SubscribeOnObservable在v6中不能直接使用，要访问它，请使用操作符subscribeOn

### 移除resultSelector

Result Selectors是一项没有被广泛使用甚至没有文档说明的RxJs特性，同时Result
Selectors严重的增加了RxJs代码库的体积，因此RxJs团队决定弃用或删除他。

对于使用到该功能的开发人员，他们需要将esultSelector参数替换为外部代码。

对于first(), last()这两个函数，这些参数已被移除，在删除rxjs-compat之前务必升级代码。

对于其他拥有resultSelector参数的函数，如mapping操作符，该参数已被弃用，并

以其他方式重写。如果您移除rxjs-compat，这些函数仍可正常工作，但是RxJs团队声明他们必须在v7版本发布之前将其移除。

针对该情况的更多详情，请查阅[RxJs文档](https://github.com/ReactiveX/rxjs)

## 其他RxJs6弃用

### Observable.if and Observable.throw

Observable.if已被iif()取代，Observable.throw已被throwError()取代。您可使用rxjs-
tslint将这些废弃的成员方法修改为函数调用。

代码示例如下：

#### OBSERVABLE.IF > IIF()

// deprecated

Observable.if(test, a$, b$);

  

// use instead

  

iif(test, a$, b$);

#### OBSERVABLE.ERROR > THROWERROR()

// deprecated

Observable.throw(newError());

  

//use instead

  

throwError(newError());

### 已弃用的方法

根据迁移指南，以下方法已被弃用或重构：

#### merge

import { merge } from'rxjs/operators';

a$.pipe(merge(b$, c$));

  

// becomes

  

import { merge } from'rxjs';

merge(a$, b$, c$);

#### concat

import { concat } from 'rxjs/operators';

a$.pipe(concat(b$, c$));

  

// becomes

  

import { concat } from 'rxjs';

concat(a$, b$, c$);

#### combineLatest

import { combineLatest } from 'rxjs/operators';

a$.pipe(combineLatest(b$, c$));

  

// becomes

  

import { combineLatest } from 'rxjs';

combineLatest(a$, b$, c$);

#### race

import { race } from 'rxjs/operators';

a$.pipe(race(b$, c$));

  

// becomes

  

import { race } from 'rxjs';

race(a$, b$, c$);

#### zip

import { zip } from 'rxjs/operators';

a$.pipe(zip(b$, c$));

  

// becomes

  

import { zip } from 'rxjs';

zip(a$, b$, c$);

## 总结

RxJS 6带来了一些重大改变，但是通过添加rxjs-
compat软件包可以缓解这一问题，该软件包允许您在保持v5代码运行的同时逐渐迁移。对于Typescript用户，其他中包括大多数Angular开发人员，tslint提供了大量的自动重构功能，使转换变得更加简单。

任何升级与代码修改都会引入一些bug到代码库中。因此请务必测试您的功能以确保您的终端用户最终接受到相同的质量体验。

视频：[RxJS 6详细介绍 by Ben Lesh](https://youtu.be/JCXZhe6KsxQ)

[原文链接](https://auth0.com/blog/whats-new-in-rxjs-6/)

* * *

# RxJS 6发布，改进了性能和模块化

文章来源：infoqDylan Schiemann

RxJS团队[宣布RxJS
6.0发布](https://twitter.com/BenLesh/status/98892202170575667)。6.0改进了模块化方法和平滑迁移性能、为简化升级而添加了反向兼容软件包，并为TypeScript用户提供了代码迁移。

rxjs-compat软件包提供了一个版本间的兼容层，用于实现从RxJS 5到6的平滑迁移，

用户可以使用npm安装RxJS 6和兼容层，命令如下：

npm install rxjs@6 rxjs-compat@6\--save

兼容层使代码无需更改即可升级到6。但如果开发人员想在部署到生产环境前降低RxJS源包的大小，还应于此后升级自身的源代码。

Angular 6用户也可受益于RxJS的Schematics。他们可以利用Angular 6提供的 ng update 机制在应用中自动安装rxjs-
compat。

RxJS 6将模块导入路径重新组织为如下几类：

  * rxjs: 创建方法、类型、调度器和工具。

  * rxjs/ajax: RxJS HTTP请求实现。

  * rxjs/operators: 可链式调用（Pipeable）的RxJS操作符。

  * rxjs/testing: RxJS测试工具。

  * rxjs/webSocket: RxJS WebSocket实现。

推荐RxJS的TypeScript用户使用 rxjs-tslint ，它有助于将版本5的导入路径重构为版本6。

RxJS
6的另一个显著改进，是将操作符转变为使用链式调用API。RxJS的前期版本中以对操作法原型打补丁的方式提供了链式调用，但这样的全局实现引入了一些挑战，包括对WebPack的摇树
（tree-shaking）优化功能，以及对代码检查（linting）工具。

例如，下面给出的例子代码使用了RxJS 5：

source

.map(x => x + x)

.mergeMap(n =>of(n +1, n +2)

.filter(x => x %1==0)

.scan((acc, x)=> acc + x,0)

)

.catch(err =>of('error found'))

.subscribe(printResult);

如果使用RxJS 6，那么代码变为：

source.pipe(

map(x => x + x),

mergeMap(n =>of(n +1, n +2).pipe(

filter(x => x %1==0),

scan((acc, x)=> acc + x,0),

)),

catchError(err =>of('error found')),

).subscribe(printResult);

近期，RxJS项目牵头人[Ben Lesh也谈及了RxJS
6](https://youtu.be/JCXZhe6KsxQ)，并介绍了支持项目改进的动机所在。

RxJS使用Apache 2许可发布。更多信息，请访问[RxJS网站](http://reactivex.io/rxjs/)。欢迎开发人员通过[RxJS
GitHub项目](https://github.com/ReactiveX/rxjs/)做出贡献。

查看英文原文：[RxJS 6 Release Improves Performance and
Modularity](https://www.infoq.com/news/2018/05/rxjs-6-released)

  

