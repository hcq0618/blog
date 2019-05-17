---
title: Unity-Profiler-window分析器窗口
thumbnail: http://upload-images.jianshu.io/upload_images/17266280-ba26d77bcc40cd59.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240
categories: Unity优化
tags: [Unity优化]
---

![](http://upload-images.jianshu.io/upload_images/17266280-ba26d77bcc40cd59.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

# Attaching to Unity players 附加到Unity播放器

To profile your game running on an other device or a player running on another
computer, it is possible to connect the editor to that other player. The
dropdown  **Active Profiler**  will show all players running on the local
network. These players are identified by player type and the host name running
the player "iPhonePlayer (Toms iPhone)". To be able to connect to a player,
the player must be launched with the  **Development Build** checkbox found in
the  **Build Settings**  dialog. From here it is also possible to tick a
checkbox to make the Editor and Player Autoconnect at startup.

要分析你的游戏运行在其他设备上或者在另一台计算机上运行的播放器，可以连接编辑器到其他播放器。Active
Profiler下拉菜单显示在本地网络上运行的所有播放器。这些播放器通过播放器的类型和运行播放器的主机名"iPhonePlayer（Toms
iPhone）"被识别。要能够连接到一个播放器，播放器必须在 Build Settings对话框中找到Development Build
复选框勾上的情况下打包生成。从这里也可以勾选一个复选框，使编辑器和播放器在启动时自动连接。

# Profiler Controls 分析器控件

  

![](http://upload-images.jianshu.io/upload_images/17266280-98c2d5c194654e46.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

Profiler controls are in the toolbar at the top of the window. Use these to
turn profiling on and off, navigate through profiled frames and so on. The
transport controls are at the far right end of the toolbar. Note that when the
game is running and the profiler is collecting data clicking on any of these
transport controls will pause the game. The controls go to the first recorded
frame, step one frame back, step one frame forward and go to the last frame
respectively. The profiler does not keep all recorded frames, so the notion of
the  _first_  frame should really be though of as the oldest frame that is
still kept in memory. The "current" transport button causes the profile
statistics window to display data collected in real-time. The Active Profiler
popup menu allows you to select whether profiling should be done in the editor
or a separate player (for example, a game running on an attached iOS device).

分析器控件在窗口顶部的工具栏。使用这些控件打开和关闭分析，浏览分析好的帧等。传输控件在工具栏的最右端。请注意，当游戏运行、分析器收集数据时，点击任何这些传输控件（那两个小箭头）将暂停游戏。控件转到记录的第一帧，一步一帧向前(左箭头)，一步一帧向后（右箭头），分别去到最后一帧。分析器不保留所有记录的帧，因此第一帧的概念，事实上应该是仍然保存在内存中的最旧的一帧。
"current"按钮会使得分析统计窗口显示实时采集的数据。激活分析器（Active
Profiler）弹出菜单让你选择是否应在编辑器或一个或独立播放器进行分析（例如，一个游戏运行在iOS设备）。

# Deep Profiling 深度分析

When you turn on Deep Profile,  _all_  your script code is profiled - that is,
all function calls are recorded. This is useful to know where exactly time is
spent in your game code.

当你打开深度分析（Deep Profile），所有脚本代码将被分析 - 也就是说，所有的函数调用被记录。知道确切在你的游戏代码中花费的时间，这是有用的。

Note that Deep Profiling incurs a  **very large overhead**  and uses a lot of
memory, and as a result your game will run significantly slower while
profiling. If you are using complex script code, Deep Profiling might not be
possible at all. Deep profiling should work fast enough for small games with
simple scripting. If you find that Deep Profiling for your entire game causes
the frame rate to drop so much that the game barely runs, you should consider
not using this approach, and instead use the approach described below. You may
find deep profiling more helpful as you are designing your game and deciding
how to best implement key features. Note that for large games deep profiling
may cause Unity to run out of memory and so for this reason deep profiling may
not be possible.

注意深度分析（Deep
Profiling）会造成非常大的开销，并使用大量的内存，结果你的游戏在分析同时运行明显变慢。如果您使用的是复杂的脚本代码，深度分析可能不会完全有效。深度分析为使用简单的脚本的小游戏工作足够快。如果您发现您的整个游戏在深度分析时运行，导致帧速率下降很多，以至于游戏几乎不能运行，你应该考虑不采用这种方法，而是使用下面描述的方法。您可能会发现深度分析更有利于设计你的游戏，并确定如何最好地实现关键特性。注意深度分析，对于大型游戏可能会导致Unity耗尽内存，基于这个原因，深度分析未必有效。

Manually profiling blocks of your script code will have a smaller overhead
than using Deep Profiling. Use
[Profiler.BeginSample](http://www.ceeger.com/Script/Profiler/Profiler.BeginSample.html)
and
[Profiler.EndSample](http://www.ceeger.com/Script/Profiler/Profiler.EndSample.html)
scripting functions to enable and disable profiling around sections of code.

手动分析脚本代码块比使用深度分析产生更小的开销。使用Profiler.BeginSample和Profiler.EndSample函数，启用和禁用分析代码段（从Profiler.BeginSample
到Profiler.EndSample间的代码）。

# View SyncTime 查看同步时间

When running at a fixed framerate or running in sync with the vertical blank,
Unity records the waiting time in "Wait For Target FPS". By default this
amount of time is not shown in the profiler. To view how much time is spent
waiting, you can toggle "View SyncTime". This is also a measure of how much
headroom you have before losing frames.

当运行在一个固定的帧率或带垂直空白同步运行，Unity在"Wait For Target
FPS"记录等待时间，默认情况下，该段时间没有显示在分析器。要查看等待花费多少时间，您可以切换"View
SyncTime"。这也是衡量多少余量你之前丢失帧。

# Profiler Timeline 分析器时间轴

  

![](http://upload-images.jianshu.io/upload_images/17266280-b1a78ceaed08ae09.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

The upper part of the Profiler window displays performance data over time.
When you run a game, data is recorded each frame, and the history of the last
several hundred frames is displayed. Clicking on a particular frame will
display it's details in the lower part of the window. Different details are
displayed depending on which timeline area is currently selected.

分析器窗口的上部显示随着时间的推移的性能数据。当您运行游戏，每一帧数据被记录，最后则会显示几百帧的历史。点击一个特定的帧上，该帧的细节将显示在窗口的下部。具体取决于当前选定的时间轴区域显示不同的细节。

The vertical scale of the timeline is managed automatically and will attempt
to fill the vertical space of the window. Note that to get more detail in say
the CPU Usage area you can remove the Memory and Rendering areas. Also, the
splitter between the timeline and the statistics area can be selected and
dragged downward to increase the screen area used for the timeline chart.

时间轴的垂直刻度是自动管理，并尝试填补窗口的垂直空间。请注意，要获得更多关于CPU的使用率(CPU Usage)的细节，您可以删除内存（Memory
）和渲染（Rendering ）区域。此外，时间轴和统计区域之间的分离器能被选择和向下拖动，为时间轴图表增加屏幕面积。

The timeline consists of several areas: CPU Usage, Rendering and Memory. These
areas can be removed by clicking the close button in the panel, and re-added
again using the  _Add Area_  drop down in the Profile Controls bar.

时间轴包括几个方面：CPU使用率，渲染和内存。这些区域可以在面板上按一下关闭按钮删除和 在分析控件（Profile Controls）工具栏中使用Add
Area 下拉菜单再次重新添加。

[CPU Usage Area](http://www.ceeger.com/Manual/ProfilerCPU.html)CPU使用率区域

[Rendering Area](http://www.ceeger.com/Manual/ProfilerRendering.html)渲染区域

[Memory Area](http://www.ceeger.com/Manual/ProfilerMemory.html)内存区域

[Audio Area](http://www.ceeger.com/Manual/ProfilerAudio.html)音频区域

[Physics Area](http://www.ceeger.com/Manual/ProfilerPhysics.html)物理学区域

[GPU Area](http://www.ceeger.com/Manual/ProfilerGPU.html)GPU区域

