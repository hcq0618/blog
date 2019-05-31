---
title: npm安装方式的区别
thumbnail: 
categories: Web
tags: [Web,npm]
---
  

npm install moduleName # 安装模块到项目目录下

npm install -g moduleName # -g 的意思是将模块安装到全局，具体安装到磁盘哪个位置，要看 npm config prefix
的位置。

npm install -save moduleName # -save
的意思是将模块安装到项目目录下，并在package文件的dependencies节点写入依赖。

npm install -save-dev moduleName # -save-dev
的意思是将模块安装到项目目录下，并在package文件的devDependencies节点写入依赖。

  

那么问题来了，在项目中我们应该使用四个命令中的哪个呢？这个就要视情况而定了。下面对这四个命令进行对比，看完后你就不再这么问了。

### npm install moduleName 命令

1\. 安装模块到项目node_modules目录下。

  

2\. 不会将模块依赖写入devDependencies或dependencies 节点。

  

3\. 运行 npm install 初始化项目时不会下载模块。

### npm install -g moduleName 命令

1\. 安装模块到全局，不会在项目node_modules目录中保存模块包。

  

2\. 不会将模块依赖写入devDependencies或dependencies 节点。

  

3\. 运行 npm install 初始化项目时不会下载模块。

### npm install -save moduleName 命令

1\. 安装模块到项目node_modules目录下。

  

2\. 会将模块依赖写入dependencies 节点。

  

3\. 运行 npm install 初始化项目时，会将模块下载到项目目录下。

  

4\. 运行npm install
--production或者注明NODE_ENV变量值为production时，会自动下载模块到node_modules目录中。

### npm install -save-dev moduleName 命令

1\. 安装模块到项目node_modules目录下。

  

2\. 会将模块依赖写入devDependencies 节点。

  

3\. 运行 npm install 初始化项目时，会将模块下载到项目目录下。

  

4\. 运行npm install
--production或者注明NODE_ENV变量值为production时，不会自动下载模块到node_modules目录中。

### 总结

devDependencies 节点下的模块是我们在开发时需要用的，比如项目中使用的 gulp
，压缩css、js的模块。这些模块在我们的项目部署后是不需要的，所以我们可以使用 -save-dev 的形式安装。像 express
这些模块是项目运行必备的，应该安装在 dependencies 节点下，所以我们应该使用 -save 的形式安装。  

  

使用原则:

运行时需要用到的包使用–save，否则使用–save-dev。  

  

npm install 会下载dependencies和devDependencies中的模块。它到哪里去找这些模块?其实，当我们执行npm intall
命令时， 会根据package.json/package-lock.json中的依赖去下载模块。

