---
title: C#字符串连接的效率问题
thumbnail: 
categories: C#
tags: [C#,C#优化]
---

C#字符串连接常用的四种方式：StringBuilder、+、string.Format、List<string>。

# 1.+的方式

```
string sql = "update tableName set int1=" + int1.ToString() + ",int2=" +
int2.ToString() + ",int3=" + int3.ToString() + " where id=" + id.ToString();
```

编译器会优化为：

```
string sql = string.Concat(new string[] { "update tableName set int1=",
int1.ToString(), ",int2=", int2.ToString(), ",int3=", int3.ToString(), " where
id=", id.ToString() });
```

下面是string.Concat的实现：

```
public static string Concat(params string[] values)

{

    int totalLength = 0;



    if (values == null)



    {



        throw new ArgumentNullException("values");



    }



    string[] strArray = new string[values.Length];



    for (int i = 0; i < values.Length; i++)



    {



        string str = values[i];



        strArray[i] = (str == null) ? Empty : str;



        totalLength += strArray[i].Length;



        if (totalLength < 0)



        {



            throw new OutOfMemoryException();



        }



    }



    return ConcatArray(strArray, totalLength);



}



private static string ConcatArray(string[] values, int totalLength)



{



    string dest = FastAllocateString(totalLength);



    int destPos = 0;



    for (int i = 0; i < values.Length; i++)



    {



        FillStringChecked(dest, destPos, values[i]);



        destPos += values[i].Length;



    }



    return dest;



}



private static unsafe void FillStringChecked(string dest, int destPos,
string src)



{



    int length = src.Length;



    if (length(dest.Length - destPos))



    {



        throw new IndexOutOfRangeException();



    }



    fixed (char* chRef = &dest.m_firstChar)



    {



        fixed (char* chRef2 = &src.m_firstChar)



        {



            wstrcpy(chRef + destPos, chRef2, length);



        }



    }



}
```

先计算目标字符串的长度，然后申请相应的空间，最后逐一复制，时间复杂度为o(n)，常数为1。固定数量的字符串连接效率最高的是+。但是字符串的连+不要拆成多条语句，比如：

```
string sql = "update tableName set int1=";
sql += int1.ToString();
sql += ...
```

这样的代码，不会被优化为string.Concat，就变成了性能杀手，因为第i个字符串需要复制n-i次，时间复杂度就成了o(n^2)。

# 2.StringBuilder的方式

如果字符串的数量不固定，就用StringBuilder，一般情况下它使用2n的空间来保证o(n)的整体时间复杂度，常数项接近于2。

因为这个算法的实用与高效，.net类库里面有很多动态集合都采用这种牺牲空间换取时间的方式，一般来说效果还是不错的。

# 3.string.Format的方式

它的底层是StringBuilder，所以其效率与StringBuiler相似。

#
4.List<string>它可以转换为string[]后使用string.Concat或string.Join，很多时候效率比StringBuiler更高效。

List与StringBuilder采用的是同样的动态集合算法，时间复杂度也是O(n)，与StringBuilder不同的是：List的n是字符串的数量，复制的是字符串的引用；StringBuilder的n是字符串的长度，复制的数据。不同的特性决定的它们各自的适应环境，当子串比较大时建议使用List<string>，因为复制引用比复制数据划算。而当子串比较小，比如平均长度小于8，特别是一个一个的字符，建议使用StringBuilder。

# 总结：

1>固定数量的字符串连接+的效率是最高的；

2>当字符串的数量不固定，并且子串的长度小于8，用StringBuiler的效率高些。

3>当字符串的数量不固定，并且子串的长度大于8，用List<string>的效率高些。

