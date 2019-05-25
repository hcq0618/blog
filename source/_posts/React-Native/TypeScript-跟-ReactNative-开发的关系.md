---
title: TypeScript-跟-ReactNative-开发的关系
thumbnail: 
categories: ReactNative
tags: [ReactNative]
---

你用 TypeScript 语法写的 .ts .tsx 等后缀的程序是不能直接运行的，而是会被 tsconfig.json 配置中的 “target”:
“es6”, 这项配置转换为 es6 语法的 .js 文件。

TypeScript 中的 import 只会加载 .ts .tsx 后缀的文件，而 Javascript 中的 import 只能加载 .js
等后缀的文件，

所以，当 ReactNative 启动时，首先加载入口文件，如 index.android.js ,代码如下：

```
 import{ AppRegistry } from'react-native';



 importIndexNavigator
from'./application/src/controller/navigator/IndexNavigator';



 AppRegistry.registerComponent('mogudan', () = IndexNavigator);

```
其中 import IndexNavigator from … 这一行加载的不是 IndexNavigator.ts 而是编译后生成的
IndexNavigator.js 文件，下面对比两个文件的差异：

 IndexNavigator.ts



 ```
/**



 * Created by ZHOUZ on 2016-08-26.



 */



 import* as React from'react';



 import{Navigator}  from'react-native';



 importIndexPage from'../page/IndexPage'



 exportdefaultclassIndexNavigatorextendsReact.Component<any,any {



     render() {



         let defaultName ='IndexPage3311113';



         let defaultComponent = IndexPage;



        return(



             <Navigator



                 initialRoute={{ name: defaultName, component:
defaultComponent }}



                 configureScene={(route) =
Navigator.SceneConfigs.VerticalDownSwipeJump }



                 renderScene={(route: any, navigator) = {



 let Component =[route.component;](http://route.component%3B/)



                    return<Component {...route.params} navigator={navigator}
/



                 }}



             /



         );



     }



 }
```

IndexNavigator.js

为自动编译后生成的es6语法的 javascript 代码

 ```
"use strict";



 var__assign = (this&&this.__assign) ||Object.assign ||function(t){



    for(vars, i =1, n =arguments.length; i < n; i++) {



         s =arguments[i];



        for(varpins)if(Object.prototype.hasOwnProperty.call(s, p))



             t[p] = s[p];



     }



    returnt;



 };



 /**



 * Created by ZHOUZ on 2016-08-26.



 */



 constReact =require('react');



 constreact_native_1 =require('react-native');



 constIndexPage_1 =require('../page/IndexPage');



 classIndexNavigator extends[React.Component](http://react.component/){



     render() {



        letdefaultName ='IndexPage3311113';



        letdefaultComponent = IndexPage_1.default;



        return(React.createElement(react_native_1.Navigator, {initialRoute: {
name: defaultName, component: defaultComponent }, configureScene: (route) =
react_native_1.Navigator.SceneConfigs.VerticalDownSwipeJump, renderScene:
(route, navigator) = {



            letComponent =[route.component;](http://route.component%3B/)



            returnReact.createElement(Component, __assign({}, route.params,
{navigator: navigator}));



         }}));



     }



 }



 Object.defineProperty(exports,"__esModule", { value:true});



 exports.default = IndexNavigator;
```

