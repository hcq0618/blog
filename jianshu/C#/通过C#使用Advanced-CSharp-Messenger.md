---
title: 通过C#使用Advanced-CSharp-Messenger
thumbnail: 
categories: C#
tags: [C#]
---

**Advanced CSharp Messenger 属于C#事件的一种。
维基百科中由详细的说明<http://wiki.unity3d.com/index.php?title=Advanced_CSharp_Messenger>上周的一天刚巧有朋友问到我这一块的知识，那么我研究出来将它贴在博客中，帮助了他也帮助我自己！哇咔咔。**

 **Advanced CSharp Messenger的特点可以将游戏对象做为参数发送。到底Advanced CSharp
Messenger有什么用呢？先创建一个立方体对象，然后把Script脚本绑定在这个对象中。脚本中有一个方法叫DoSomething()。**
**写一段简单的代码，通常我们在调用方法的时候需要这样来写。**

C#

> private Script script;

>

> void Awake()

>

> {

>

> GameObject cube = GameObject.Find("Cube");

>

> script = cube.GetComponent<Script>();

>

> }

>

>  
>

>

> void Update()

>

> {

>

> if(Input.GetMouseButtonDown(0))

>

> {

>

> script.DoSomething();

>

> }

>

> }

  

**代码比较简单，我就不注释了。
原理就是先获取游戏对象，接着获取脚本组件对象，最后通过脚本组件对象去调用对应脚本中的方法，这样的调用方法我们称之为直接调用。**

**这个例子中我只调用了一个对象的方法，如果说有成千上万个对象，那么这样调用是不是感觉自己的代码非常的丑？因为你需要一个一个的获取对象然后获取脚本组件然后在调用方法。。。。。
（想想都恐怖！！）**

 **下面我们在用Advanced CSharp Messenger来实现事件的调用。按照维基百科中首先把Message.cs
和Callback.cs拷贝在你的工程中。**

 **CallBack.cs**

C#

> public delegate void Callback();

>

> public delegate void Callback<T>(T arg1);

>

> public delegate void Callback<T, U>(T arg1, U arg2);

>

> public delegate void Callback<T, U, V>(T arg1, U arg2, V arg3);

**Message.cs**

C#

> /*

>

> * Advanced C# messenger by Ilya Suzdalnitski. V1.0

>

> *

>

> * Based on Rod Hyde's "CSharpMessenger" and Magnus Wolffelt's
"CSharpMessenger Extended".

>

> *

>

> * Features:

>

> * Prevents a MissingReferenceException because of a reference to a destroyed
message handler.

>

> * Option to log all messages

>

> * Extensive error detection, preventing silent bugs

>

> *

>

> * Usage examples:

>

> 1\. Messenger.AddListener<GameObject>("prop collected", PropCollected);

>

>    Messenger.Broadcast<GameObject>("prop collected", prop);

>

> 2\. Messenger.AddListener<float>("speed changed", SpeedChanged);

>

>    Messenger.Broadcast<float>("speed changed", 0.5f);

>

> *

>

> * Messenger cleans up its evenTable automatically upon loading of a new
level.

>

> *

>

> * Don't forget that the messages that should survive the cleanup, should be
marked with Messenger.MarkAsPermanent(string)

>

> *

>

> */

>

>  
>

>

> //#define LOG_ALL_MESSAGES

>

> //#define LOG_ADD_LISTENER

>

> //#define LOG_BROADCAST_MESSAGE

>

> #define REQUIRE_LISTENER

>

>  
>

>

> using System;

>

> using System.Collections.Generic;

>

> using UnityEngine;

>

>  
>

>

> static internal class Messenger {

>

> #region Internal variables

>

>  
>

>

> //Disable the unused variable warning

>

> #pragma warning disable 0414

>

> //Ensures that the MessengerHelper will be created automatically upon start
of the game.

>

> static private MessengerHelper messengerHelper = ( new
GameObject("MessengerHelper") ).AddComponent< MessengerHelper >();

>

> #pragma warning restore 0414

>

>  
>

>

> static public Dictionary<string, Delegate> eventTable = new
Dictionary<string, Delegate>();

>

>  
>

>

> //Message handlers that should never be removed, regardless of calling
Cleanup

>

> static public List< string > permanentMessages = new List< string > ();

>

> #endregion

>

> #region Helper methods

>

> //Marks a certain message as permanent.

>

> static public void MarkAsPermanent(string eventType) {

>

> #if LOG_ALL_MESSAGES

>

> Debug.Log("Messenger MarkAsPermanent \t\"" + eventType + "\"");

>

> #endif

>

>  
>

>

> permanentMessages.Add( eventType );

>

> }

>

>  
>

>

> static public void Cleanup()

>

> {

>

> #if LOG_ALL_MESSAGES

>

> Debug.Log("MESSENGER Cleanup. Make sure that none of necessary listeners are
removed.");

>

> #endif

>

>  
>

>

> List< string > messagesToRemove = new List<string>();

>

>  
>

>

> foreach (KeyValuePair<string, Delegate> pair in eventTable) {

>

> bool wasFound = false;

>

>  
>

>

> foreach (string message in permanentMessages) {

>

> if (pair.Key == message) {

>

> wasFound = true;

>

> break;

>

> }

>

> }

>

>  
>

>

> if (!wasFound)

>

> messagesToRemove.Add( pair.Key );

>

> }

>

>  
>

>

> foreach (string message in messagesToRemove) {

>

> eventTable.Remove( message );

>

> }

>

> }

>

>  
>

>

> static public void PrintEventTable()

>

> {

>

> Debug.Log("\t\t\t=== MESSENGER PrintEventTable ===");

>

>  
>

>

> foreach (KeyValuePair<string, Delegate> pair in eventTable) {

>

> Debug.Log("\t\t\t" + pair.Key + "\t\t" + pair.Value);

>

> }

>

>  
>

>

> Debug.Log("\n");

>

> }

>

> #endregion

>

>  
>

>

> #region Message logging and exception throwing

>

>     static public void OnListenerAdding(string eventType, Delegate
listenerBeingAdded) {

>

> #if LOG_ALL_MESSAGES || LOG_ADD_LISTENER

>

> Debug.Log("MESSENGER OnListenerAdding \t\"" + eventType + "\"\t{" +
listenerBeingAdded.Target + " -> " + listenerBeingAdded.Method + "}");

>

> #endif

>

>  
>

>

>         if (!eventTable.ContainsKey(eventType)) {

>

>             eventTable.Add(eventType, null );

>

>         }

>

>  
>

>

>         Delegate d = eventTable[eventType];

>

>         if (d != null && d.GetType() != listenerBeingAdded.GetType()) {

>

>             throw new ListenerException(string.Format("Attempting to add
listener with inconsistent signature for event type {0}. Current listeners
have type {1} and listener being added has type {2}", eventType,
d.GetType().Name, listenerBeingAdded.GetType().Name));

>

>         }

>

>     }

>

>  
>

>

>     static public void OnListenerRemoving(string eventType, Delegate
listenerBeingRemoved) {

>

> #if LOG_ALL_MESSAGES

>

> Debug.Log("MESSENGER OnListenerRemoving \t\"" + eventType + "\"\t{" +
listenerBeingRemoved.Target + " -> " + listenerBeingRemoved.Method + "}");

>

> #endif

>

>  
>

>

>         if (eventTable.ContainsKey(eventType)) {

>

>             Delegate d = eventTable[eventType];

>

>  
>

>

>             if (d == null) {

>

>                 throw new ListenerException(string.Format("Attempting to
remove listener with for event type \"{0}\" but current listener is null.",
eventType));

>

>             } else if (d.GetType() != listenerBeingRemoved.GetType()) {

>

>                 throw new ListenerException(string.Format("Attempting to
remove listener with inconsistent signature for event type {0}. Current
listeners have type {1} and listener being removed has type {2}", eventType,
d.GetType().Name, listenerBeingRemoved.GetType().Name));

>

>             }

>

>         } else {

>

>             throw new ListenerException(string.Format("Attempting to remove
listener for type \"{0}\" but Messenger doesn't know about this event type.",
eventType));

>

>         }

>

>     }

>

>  
>

>

>     static public void OnListenerRemoved(string eventType) {

>

>         if (eventTable[eventType] == null) {

>

>             eventTable.Remove(eventType);

>

>         }

>

>     }

>

>  
>

>

>     static public void OnBroadcasting(string eventType) {

>

> #if REQUIRE_LISTENER

>

>         if (!eventTable.ContainsKey(eventType)) {

>

>             throw new BroadcastException(string.Format("Broadcasting message
\"{0}\" but no listener found. Try marking the message with
Messenger.MarkAsPermanent.", eventType));

>

>         }

>

> #endif

>

>     }

>

>  
>

>

>     static public BroadcastException
CreateBroadcastSignatureException(string eventType) {

>

>         return new BroadcastException(string.Format("Broadcasting message
\"{0}\" but listeners have a different signature than the broadcaster.",
eventType));

>

>     }

>

>  
>

>

>     public class BroadcastException : Exception {

>

>         public BroadcastException(string msg)

>

>             : base(msg) {

>

>         }

>

>     }

>

>  
>

>

>     public class ListenerException : Exception {

>

>         public ListenerException(string msg)

>

>             : base(msg) {

>

>         }

>

>     }

>

> #endregion

>

>  
>

>

> #region AddListener

>

> //No parameters

>

>     static public void AddListener(string eventType, Callback handler) {

>

>         OnListenerAdding(eventType, handler);

>

>         eventTable[eventType] = (Callback)eventTable[eventType] + handler;

>

>     }

>

>  
>

>

> //Single parameter

>

> static public void AddListener<T>(string eventType, Callback<T> handler) {

>

>         OnListenerAdding(eventType, handler);

>

>         eventTable[eventType] = (Callback<T>)eventTable[eventType] +
handler;

>

>     }

>

>  
>

>

> //Two parameters

>

> static public void AddListener<T, U>(string eventType, Callback<T, U>
handler) {

>

>         OnListenerAdding(eventType, handler);

>

>         eventTable[eventType] = (Callback<T, U>)eventTable[eventType] +
handler;

>

>     }

>

>  
>

>

> //Three parameters

>

> static public void AddListener<T, U, V>(string eventType, Callback<T, U, V>
handler) {

>

>         OnListenerAdding(eventType, handler);

>

>         eventTable[eventType] = (Callback<T, U, V>)eventTable[eventType] +
handler;

>

>     }

>

> #endregion

>

>  
>

>

> #region RemoveListener

>

> //No parameters

>

>     static public void RemoveListener(string eventType, Callback handler) {

>

>         OnListenerRemoving(eventType, handler);

>

>         eventTable[eventType] = (Callback)eventTable[eventType] - handler;

>

>         OnListenerRemoved(eventType);

>

>     }

>

>  
>

>

> //Single parameter

>

> static public void RemoveListener<T>(string eventType, Callback<T> handler)
{

>

>         OnListenerRemoving(eventType, handler);

>

>         eventTable[eventType] = (Callback<T>)eventTable[eventType] -
handler;

>

>         OnListenerRemoved(eventType);

>

>     }

>

>  
>

>

> //Two parameters

>

> static public void RemoveListener<T, U>(string eventType, Callback<T, U>
handler) {

>

>         OnListenerRemoving(eventType, handler);

>

>         eventTable[eventType] = (Callback<T, U>)eventTable[eventType] -
handler;

>

>         OnListenerRemoved(eventType);

>

>     }

>

>  
>

>

> //Three parameters

>

> static public void RemoveListener<T, U, V>(string eventType, Callback<T, U,
V> handler) {

>

>         OnListenerRemoving(eventType, handler);

>

>         eventTable[eventType] = (Callback<T, U, V>)eventTable[eventType] -
handler;

>

>         OnListenerRemoved(eventType);

>

>     }

>

> #endregion

>

>  
>

>

> #region Broadcast

>

> //No parameters

>

>     static public void Broadcast(string eventType) {

>

> #if LOG_ALL_MESSAGES || LOG_BROADCAST_MESSAGE

>

> Debug.Log("MESSENGER\t" + System.DateTime.Now.ToString("hh:mm:ss.fff") +
"\t\t\tInvoking \t\"" + eventType + "\"");

>

> #endif

>

>         OnBroadcasting(eventType);

>

>  
>

>

>         Delegate d;

>

>         if (eventTable.TryGetValue(eventType, out d)) {

>

>             Callback callback = d as Callback;

>

>  
>

>

>             if (callback != null) {

>

>                 callback();

>

>             } else {

>

>                 throw CreateBroadcastSignatureException(eventType);

>

>             }

>

>         }

>

>     }

>

>  
>

>

> //Single parameter

>

>     static public void Broadcast<T>(string eventType, T arg1) {

>

> #if LOG_ALL_MESSAGES || LOG_BROADCAST_MESSAGE

>

> Debug.Log("MESSENGER\t" + System.DateTime.Now.ToString("hh:mm:ss.fff") +
"\t\t\tInvoking \t\"" + eventType + "\"");

>

> #endif

>

>         OnBroadcasting(eventType);

>

>  
>

>

>         Delegate d;

>

>         if (eventTable.TryGetValue(eventType, out d)) {

>

>             Callback<T> callback = d as Callback<T>;

>

>  
>

>

>             if (callback != null) {

>

>                 callback(arg1);

>

>             } else {

>

>                 throw CreateBroadcastSignatureException(eventType);

>

>             }

>

>         }

>

> }

>

>  
>

>

> //Two parameters

>

>     static public void Broadcast<T, U>(string eventType, T arg1, U arg2) {

>

> #if LOG_ALL_MESSAGES || LOG_BROADCAST_MESSAGE

>

> Debug.Log("MESSENGER\t" + System.DateTime.Now.ToString("hh:mm:ss.fff") +
"\t\t\tInvoking \t\"" + eventType + "\"");

>

> #endif

>

>         OnBroadcasting(eventType);

>

>  
>

>

>         Delegate d;

>

>         if (eventTable.TryGetValue(eventType, out d)) {

>

>             Callback<T, U> callback = d as Callback<T, U>;

>

>  
>

>

>             if (callback != null) {

>

>                 callback(arg1, arg2);

>

>             } else {

>

>                 throw CreateBroadcastSignatureException(eventType);

>

>             }

>

>         }

>

>     }

>

>  
>

>

> //Three parameters

>

>     static public void Broadcast<T, U, V>(string eventType, T arg1, U arg2,
V arg3) {

>

> #if LOG_ALL_MESSAGES || LOG_BROADCAST_MESSAGE

>

> Debug.Log("MESSENGER\t" + System.DateTime.Now.ToString("hh:mm:ss.fff") +
"\t\t\tInvoking \t\"" + eventType + "\"");

>

> #endif

>

>         OnBroadcasting(eventType);

>

>  
>

>

>         Delegate d;

>

>         if (eventTable.TryGetValue(eventType, out d)) {

>

>             Callback<T, U, V> callback = d as Callback<T, U, V>;

>

>  
>

>

>             if (callback != null) {

>

>                 callback(arg1, arg2, arg3);

>

>             } else {

>

>                 throw CreateBroadcastSignatureException(eventType);

>

>             }

>

>         }

>

>     }

>

> #endregion

>

> }

>

>  
>

>

> //This manager will ensure that the messenger's eventTable will be cleaned
up upon loading of a new level.

>

> public sealed class MessengerHelper : MonoBehaviour {

>

> void Awake ()

>

> {

>

> DontDestroyOnLoad(gameObject);

>

> }

>

>  
>

>

> //Clean up eventTable every time a new level loads.

>

> public void OnDisable() {

>

> Messenger.Cleanup();

>

> }

>

> }

**然后就可以开始使用了，Messager.Broadcast()这样就好比我们发送了一条广播。**

C#

> void Update()

>

> {

>

> if(Input.GetMouseButtonDown(0))

>

> {

>

> Messenger.Broadcast("Send");

>

> }

>

> }

**在需要这条广播的类中来接受它，同样是刚刚说的Script类。接受广播的标志是
Messager.AddListener()参数1表示广播的名称，参数2表示广播所调用的方法。**

C#

> using UnityEngine;

>

> using System.Collections;

>

>  
>

>

> public class Script : MonoBehaviour {

>

>  
>

>

> void Awake()

>

> {

>

> Messenger.AddListener( "Send", DoSomething );

>

> }

>

> public void DoSomething()

>

> {

>

> Debug.Log("DoSomething");

>

> }

>

> }

**这样一来，只要发送名称为”Send”的方法，就可以在别的类中接收它了。**

**我们在说说如何通过广播来传递参数,这也是那天那个哥们主要问我的问题。（其实是维基百科上写的不是特别特别的清楚，那哥们误解了）在Callback中可以看出参数最多可以是三个，参数的类型是任意类型，也就是说我们不仅能传递
int float bool 还能传递gameObject类型。**

 **如下所示，发送广播的时候传递了两个参数，参数1是一个游戏对象，参数2是一个int数值。**

C#

> void Update()

>

> {

>

> if(Input.GetMouseButtonDown(0))

>

> {

>

> GameObject cube = GameObject.Find("Cube");

>

> Messenger.Broadcast<GameObject,int>("Send",cube,1980);

>

> }

>

> }

**然后是接受的地方 参数用 <>存在一起。游戏对象也可以完美的传递。**

C#

> using UnityEngine;

>

> using System.Collections;

>

>  
>

>

> public class Script : MonoBehaviour {

>

>  
>

>

> void Awake()

>

> {

>

> Messenger.AddListener<GameObject,int>( "Send", DoSomething );

>

> }

>

> public void DoSomething(GameObject obj,int i)

>

> {

>

> Debug.Log("name " + obj.name + " id =" + i);

>

> }

>

> }

**如果传递一个参数 <T>**

 **两个参数 <T,T>**

 **三个参数 <T,T,T>   **

 **怎么样使用起来还是挺简单的吧？**

**我觉得项目中最好不要大量的使用代理事件这类的方法（根据需求而定），虽然可以让你的代码非常的简洁，但是它的效率不高大概比直接调用慢5-倍左右吧，就好比美好的东西一定都有瑕疵一样。
还记得Unity自身也提供了一种发送消息的方法吗？，用过的都知道效率也非常低下，虽然我们看不到它具体实现的源码是如何实现的，但是我觉得原理可能也是这样的。
欢迎和大家一起讨论与学习。**

