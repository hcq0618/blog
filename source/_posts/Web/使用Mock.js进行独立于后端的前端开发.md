---
title: 使用Mock.js进行独立于后端的前端开发
thumbnail: 
categories: Web
tags: [Web,后端]
---
## 解决的问题

开发时，后端还没完成数据输出，前端只好写静态模拟数据。

  * 数据太长了，将数据写在js文件里，完成后挨个改url。

  * 某些逻辑复杂的代码，加入或去除模拟数据时得小心翼翼。

  * 想要尽可能还原真实的数据，要么编写更多代码，要么手动修改模拟数据。

  * 特殊的格式，例如IP,随机数，图片，地址，需要去收集。

  * 超烂的破网速…

  * …

## 以上都不再是问题

接下来体验 拦截ajax请求并返回模拟数据。

  

## 概述

### Mock.js实现的功能

  1. 基于 数据模板 生成数据

  2. 基于 HTML模板 生成数据

  3. 拦截并模拟 Ajax请求

## 用法

### 浏览器：

  

```
<!-- （必选）加载 Mock -->

<script src="http://mockjs.com/dist/mock.js"></script>

<script>

// 使用 Mock

var data = Mock.mock({

    'list|1-10': [{

        'id|+1': 1

    }]

});

$('<pre>').text(JSON.stringify(data, null, 4))

.appendTo('body')

</script>

 _  
```
_

返回值:

  

```
{

"list": [

    {

        "id": 1

    },

    {

        "id": 2

    },

    {

        "id": 3

    }

    ]

}

```
  

* * *

### JQuery：

配置模拟数据：

  

```
Mock.mock('http://g.cn', {

    'name'     : '@name',

    'age|1-100': 100,

    'color'    : '@color'

});
```

发送Ajax请求：

```
$.ajax({

    url: 'http://g.cn',

    dataType:'json'

    }).done(function(data, status, xhr){

    console.log(

    JSON.stringify(data, null, 4)

    )

})；
```

 **  
**

返回数据：

  

```
// 结果1

{

"name": "Elizabeth Hall",

"age": 91,

"color": "#0e64ea"

}

// 结果2

{

"name": "Michael Taylor",

"age": 61,

"color": "#081086"

}

```
 _  
_

* * *

### Node.js：

  

// 安装

`npm install mockjs
`
// 使用

```
var Mock = require('mockjs');

var data = Mock.mock({

    'list|1-10': [{

        'id|+1': 1

    }]

});

console.log(JSON.stringify(data, null, 4))
```

 _  
_

* * *

### Angular.js:

  

```
<!-- 引用 -->

<script src="http://mockjs.com/dist/mock-min.js"></script>

<script
src="http://cdn.staticfile.org/angular.js/1.3.0-beta.13/angular.min.js"></script>

<!-- 兼容angular (mock.js默认不兼容angular，需额外引用兼容包)-->

<script src="./src/mock.angular.js"></script>

<!-- 模拟数据 -->

<script src="./mockData.js"></script>

<!-- 使用 -->

<script>

(function() {

    (function() {

        var app;

        app = angular.module('app', []);

        //使用mockjax方法覆盖Ajax请求

        Mock.mockjax(app);

        return app.controller('appCtrl', function($scope, $http) {

            var box;

            box = $scope.box = [];

            $scope.get = function() {

                $http({

                    url: 'http://www.baidu.com',

                    method: 'POST',

                    params: {a: 1},

                    data  : {b:1}

                }).success(function(data) {

                return box.push(data);

            });

            $http({

                url: 'http://baidu.com'

                }).success(function(data) {

                console.log(data);

                });

            };

        return $scope.get();

        });

    })();

}).call(this);

</script>
```

 _  
_

#### mock数据mockData.js:

  

```
Mock.mock('http://www.baidu.com', {

    'name': '@name()',

    'age|1-100': 100,

    'color': '@color'

});
```

 **  
**

* * *

## 语法

Mock.js 的语法规范包括两部分：

  1. 数据模板定义（Data Temaplte Definition，DTD）

  2. 数据占位符定义（Data Placeholder Definition，DPD）

### 数据模板定义 DTD

数据模板中的每个属性由 3 部分构成：属性名、生成规则、属性值：

`// 属性名 name`

`// 生成规则 rule`

`// 属性值 value`

'name|rule': value

注意：

  * 属性名 和 生成规则 之间用 | 分隔。

  * 生成规则 是可选的。

  * 生成规则 有 7 种格式：

    1. 'name|min-max': value

    2. 'name|count': value

    3. 'name|min-max.dmin-dmax': value

    4. 'name|min-max.dcount': value

    5. 'name|count.dmin-dmax': value

    6. 'name|count.dcount': value

    7. 'name|+step': value

  * 生成规则 的 含义 需要依赖 属性值 才能确定。

  * 属性值 中可以含有 @占位符。

  * 属性值 还指定了最终值的初始值和类型。

#### 生成规则和示例：

##### 1\. 属性值是字符串 String

  1. 'name|min-max': 'value' 通过重复 'value' 生成一个字符串，重复次数大于等于 min，小于等于 max。

  2. 'name|count': 'value' 通过重复 'value' 生成一个字符串，重复次数等于 count。

##### 2\. 属性值是数字 Number

  1. 'name|+1': 100 属性值自动加 1，初始值为 100

  2. 'name|1-100': 100 生成一个大于等于 1、小于等于 100 的整数，属性值 100 只用来确定类型。

  3. 'name|1-100.1-10': 100 生成一个浮点数，整数部分大于等于 1、小于等于 100，小数部分保留 1 到 10 位。

```
{

'number1|1-100.1-10': 1,

'number2|123.1-10': 1,

'number3|123.3': 1,

'number4|123.10': 1.123

}

// =>

{

"number1": 12.92,

"number2": 123.51,

"number3": 123.777,

"number4": 123.1231091814

}
```

##### 3\. 属性值是布尔型 Boolean

  1. 'name|1': value 随机生成一个布尔值，值为 true 的概率是 1/2，值为 false 的概率是 1/2。

  2. 'name|min-max': value 随机生成一个布尔值，值为 value 的概率是 min / (min + max)，值为 !value 的概率是 max / (min + max)。

##### 4\. 属性值是对象 Object

  1. 'name|min-max': {} 从属性值 {} 中随机选取 min 到 max 个属性。

  2. 'name|count': {} 从属性值 {} 中随机选取 count 个属性。

##### 5\. 属性值是数组 Array

  1. 'name|1': [{}, {} ...] 从属性值 [{}, {} ...] 中随机选取 1 个元素，作为最终值。

  2. 'name|min-max': [{}, {} ...] 通过重复属性值 [{}, {} ...] 生成一个新数组，重复次数大于等于 min，小于等于 max。

  3. 'name|count': [{}, {} ...] 通过重复属性值 [{}, {} ...] 生成一个新数组，重复次数为 count。

##### 6\. 属性值是数组 Function

'name': function(){} 执行函数 function(){}，取其返回值作为最终的属性值，上下文为 'name' 所在的对象。

### 数据占位符定义 DPD

占位符 只是在属性值字符串中占个位置，并不出现在最终的属性值中。占位符 的格式为：

`@占位符`

@占位符(参数 [, 参数])

注意：

  1. 用 @ 来标识其后的字符串是 占位符。

  2. 占位符 引用的是 Mock.Random 中的方法。

  3. 通过 Mock.Random.extend() 来扩展自定义占位符。

  4. 占位符 也可以引用 数据模板 中的属性。

  5. 占位符 会优先引用 数据模板 中的属性

```
{

name: {

first: '@FIRST',

middle: '@FIRST',

last: '@LAST',

full: '@first @middle @last'

}

}

// =>

{

"name": {

"first": "Charles",

"middle": "Brenda",

"last": "Lopez",

"full": "Charles Brenda Lopez"

}

}
```

* * *

## 常用方法

### Mock.mock( rurl?, rtype?, template|function(options) )

根据数据模板生成模拟数据。

##### 参数的含义和默认值如下所示：

  * 参数 rurl：可选。表示需要拦截的 URL，可以是 URL 字符串或 URL 正则。例如 /\/domain\/list.json/、'/domian/list.json'。

  * 参数 rtype：可选。表示需要拦截的 Ajax 请求类型。例如 GET、POST、PUT、DELETE 等。

  * 参数 template：可选。表示数据模板，可以是对象或字符串。例如 { 'data|1-10':[{}] }、'@EMAIL'。

  * 参数 function(options)：可选。表示用于生成响应数据的函数。

  * 参数 options：指向本次请求的 Ajax 选项集。

### Mock.mockjax(library)

覆盖（拦截） Ajax 请求，目前内置支持 jQuery、Zepto、KISSY。

### Mock.Random

Mock.Random 是一个工具类，用于生成各种随机数据。Mock.Random 的方法在数据模板中称为“占位符”，引用格式为 @占位符(参数 [,
参数]) 。

### Mock.tpl(input, options, helpers, partials)

基于 Handlebars、Mustache 的 HTML 模板生成模拟数据。

方法使用详情请参考[mock.js文档](http://mockjs.com/#mock)

* * *

## 参考

演示： [mock-demo](http://mockjs.com/editor.html#help)

演示： [mock-angular-demo](http://think2011.github.io/mock-angular/)

参考： [mock.js](http://mockjs.com/#mock)

源码： [mock-angular](https://github.com/think2011/mock-angular)

