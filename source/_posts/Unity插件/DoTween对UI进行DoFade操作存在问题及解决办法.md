---
title: DoTween对UI进行DoFade操作存在问题及解决办法
thumbnail: 
categories: Unity插件
tags: [Unity插件]
---

Unity版本：5.2, 5.4

当使用this.GetComponent<Image().material.DOFade(0,
2).SetEase(Ease.InBounce);来对UGUI的Image进行褪色操作的时候本质是对UI的Graphic对象（Text，Image等都为Graphic的子类）的material进行操作,下例是对Text组件进行褪色操作：Transform.GetComponent().material.DoFade(0,1)。虽然脚本只挂在一个Text组件的物体上，但1秒之后发现，整个UI界面全部变为透明。

（我也很纳闷，cube01.GetComponent<Renderer ().material.color =
Color.black;这样的代码照理说是这样执行的（<http://www.jianshu.com/p/ababf547d992）：

 Material lastMat = cube01.GetComponent<Renderer ().material



 Material m = Instantiate(lastMat) as Material



 cube01.GetComponent<Renderer ().material = m



 m.color = Color.black

应该是最自己持有的material进行操做。。。

）

经测试发现，所有使用缺省material的组件都是使用的默认的material，而这个material只存在一份，所有UI组件使用的默认material都只是该material的引用，在DoTween对其进行褪色操作之后，该material的alpha值保持为0不变，且游戏重新开始也不会将其alpha值重置为1。

解决办法:

导入DoTween后请确保Setup DoTween， Tools/DoTween Utility Panel/Setup
DoTween…。导入后就可以使用Image.DoFade了。

使用Unity自带的Graphic.CrossFadeAlpha(float alpha, float duration, bool
ignoreTimeScale)函数来操作

自己扩展DoTween的方法，下面是我扩展的一个例子,可以参考DoTwen官网的[Creating custom plugins
example](http://dotween.demigiant.com/examples.php)

 ```
/  DoFadeTest.cs



 /  Project: GUITest



 /  Created by zhiheng.shao



 /  Copyright  2016年 zhiheng.shao. All rights reserved.



 /  Description



 using UnityEngine;



 using System.Collections;



 using DG.Tweening;



 using UnityEngine.UI;



 using DG.Tweening.RickExtension;



 public class DoFadeTest : MonoBehaviour



 {



     // Use this for initialization



     Start()



     {



         .GetComponent<Image().DOFade(, ).SetEase(Ease.InBounce);



     }



 }



 namespace DG.Tweening.RickExtension



 {



     public static class DOTweenExteion



     {



         public static Tweener DOFade( Image image, float endValue, float
duration)



         {



             Debug.Log("CustomDoFade");



             return DOTween.To(image.AlphaGetter, image.AlphaSetter,
endValue, duration);



         }



         private static float AlphaGetter( Image image)



         {



             return image.color.a;



         }



         private static  AlphaSetter( Image image, float alpha)



         {



             Color oldColor = image.color;



             oldColor.a = alpha;



             image.color = oldColor;



         }



     }



 }
```

附：[DoTween官网](http://dotween.demigiant.com/index.php)

