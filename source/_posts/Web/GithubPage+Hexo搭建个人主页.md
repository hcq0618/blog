---
title: GithubPage+Hexo搭建个人主页
thumbnail: 
categories: Web
tags: [Web]
---
## 安装配置部署

[https://zirho.github.io/2016/06/04/hexo/](https://zirho.github.io/2016/06/04/hexo/)

  

* * *

## 添加评论

这个主题的评论已经集成了，并不需要我们进行手工导入，要求你有多说/disqus的账号，并在跟目录的_config.yml中，删去注释#：

**DuoShuo**

duoshuo_shortname: 多说设置的名称
* * *
## 添加友情链接  

我们在主题的_config.yml中已经有设置links的了。只是没有显示出来：

修改主题的_config.yml

  

```
# Links 通过links来设置友情链接

links:

  Hexo: http://hexo.io

  foam | 我一直在找寻有你的世界: http://zoufeng.net/

  getNway的博客: http://www.luojiawei.me/

  HCLAB-环宇创意电脑工作室: http://hclab.cn/hclab/index.php/

# Sidebar # 网站右边框

sidebar: right # set to false if you don't want a sidebar

widgets:

- category
- links
```

  
* * *
## 发布博客，markdown文件的格式

markdown文件需要添加categories进行归档区分。

相应的为：

  

```
title: "java-Map集合-HashMap"

thumbnail: http://XXXXXXX (或者相对路径)

date: 2015-07-28 10:48:16

categories: java

tags: [java,Map,HashMap,Hashtable]

---
```

  

thumbnail也可以在配置文件中关闭不显示  

  

其中categories/tags的格式也可以为：

```
categories/tags:
    - java
```

  

具体格式相应属性的设置，直接去hexo提供的文档：

[Front-matter](https://link.jianshu.com/?t=https://hexo.io/zh-cn/docs/front-
matter.html)，直接查看官方的文档就可以很快地知道个所以然了。

* * *
## 添加站长统计

我们通过站长统计来及时查看我们个人网站的浏览情况。首先，我们需要进行注册：[站长统计](https://link.jianshu.com/?t=http://zhanzhang.cnzz.com/)

以下参考：[添加cnzz站长统计](https://link.jianshu.com/?t=https://github.com/woheme/hexo-
theme-icarus/commit/5b3da36aaffa4947cca358f40d5db09eddf3b9b8)

  1. 在theme的_config.yml中的末尾添加以下：(这部很重要，不添加web_id将无法显示出来)

CNZZ id

cnzz: 这里填入你在站长统计注册后的web_id

  1. 在目录：主题的layout/_partial/添加文件为cnzz.ejs，内容如下：

```
<% if (theme.cnzz){ %>

Analyse with <script src="http://s23.cnzz.com/z_stat.php?id=<%= theme.cnzz
%>&web_id=<%= theme.cnzz %>" language="JavaScript"></script>

<% } %>
```

  1. 最后进行显示，在路径layout/_partial/footer.ejs里面添加：

```
...PPOffice</a>.<%- partial('cnzz') %>
```

再次提醒注意在_config.xml中添加web_id，否则无法显示。当显示出来了，又有一个问题，那就是要填写查看密码了。

查看以下即可：[【设置】如何设置查看密码？（此功能只限站长用户）](https://link.jianshu.com/?t=http://help.cnzz.com/support/zhandianshezhi/chankanmimazhezhi/20130903/27.html)

* * *
## 百度/谷歌验证站点

为什么要验证站点了，因为要搜索引擎进行收录，说白了就是让别人更容易搜索到你的网站，仅此而已。

首先需要到百度/谷歌站长统计中注册，以及验证：

[Google网站管理员工具地址](https://link.jianshu.com/?t=http://www.google.com/webmasters/tools/?hl=zh_CN)

[百度站长工具](https://link.jianshu.com/?t=http://zhanzhang.baidu.com/)

注册完后，进行输入相应的网站地址，然后选择html验证，将代码加入以下路径layout/_partial/head.ejs：（截取部分）
```

<head>

<meta name="baidu-site-verification" content="tqvy7RDErf" />

<meta name="google-site-verification" content="hjN29-PO_KfE-dgow-
7hcz75xJj0qzZ6G2OkXZ3FVd8" />

<meta charset="utf-8">

....
```

然后发布到github中，再进行验证即可。

* * *
## 发布后无法加载样式

因为默认的路径的为http://uername.com/hexo-theme-
icarus而你解析的路径直接为http://uername.com/导致无法加载样式，或者无法显示文章。那么，该如何进行修改呢？

我们需要对路径进行提升，从hexo-theme-
icarus到/，你可以按着[Hexo使用总结](https://link.jianshu.com/?t=http://wohe.me/2015/06/04/Hexo%E4%BD%BF%E7%94%A8%E6%80%BB%E7%BB%93/)中的配置进行修改_config.yml，即可。修改完后，不要着急，我的情况要等好久才回显示正常，真是郁闷。下面是个别的设置：

**站点的_config.yml**
```
root: /
```

**theme的_config.yml**
```

Home: /

  Archives: /archives

  Categories: /categories

  About: /about
```

* * *
## 扩展插件的使用

强大的插件供你使用，插件集合：[Hexo
Plugins](https://link.jianshu.com/?t=https://github.com/hexojs/hexo/wiki/Plugins)。

下面展示一个插件sitemap的使用：[hexo优化--
向Google提交sitemap](https://link.jianshu.com/?t=http://ppting.me/2015/01/25/sitemap/)

还必须在根目录的_config.yml加入以下配置：

Extensions 这里配置站点所用主题和插件，暂默认，后面会介绍怎么修改

Plugins: https://github.com/tommy351/hexo/wiki/Plugins

  

exclude_generator:

plugins:

\- hexo-generator-feed

\- hexo-generator-sitemap</pre>

* * *
## 发布后显示404：

查看配置文件_config.yml中的配置是否与实际情况相符：

```
url: https://hcq0618.github.io/blog/

root: /blog/
```

* * *

## 在文章中插入本地图片

<https://cloud.tencent.com/developer/article/1019861>  

  

**遇到问题**

遇到没能成功显示的问题，查看网页，结果是` <img src="2017/02/26/2017-02-23-c/图片名.jpg">` 的形式，然后查看 hexo
的目录，发现路径是 `/public/2017/02/26/c/a.jpg`。

之前在 md 文件中引用时写作：

```
![你想输入的替代文字](xxxx/图片名.jpg)
```
改为：

```
![](a.jpg)
```

就可以了。

* * *
## 创建Github Page
在Github上创建一个仓库，可以新建一个source分支用于存在主页项目源码，master用于存放主页网页静态代码，
然后在项目Settings里找到Github Page，选择master分支，即可创建一个github page主页
url一般为：
```
<github用户名>.github.io/<项目名>
```
然后每次都可以通过github desktop，将主页的项目源码上传到source分支
依次通过hexo的命令
- `hexo generate`或者`hexo g`或者`hexo g -f`
- `hexo deploy`或者`hexo d`
 
就会自动生成静态网页并将主页网页静态代码push到master分支（当然先会要求验证github账号密码），主页就随即更新了


  

