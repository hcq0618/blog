---
title: Prefab里面的Prefab关联问题
thumbnail: http://upload-images.jianshu.io/upload_images/17266280-96725fd31f44b3f7.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240
categories: Unity
tags: [Unity]
---

最近造了个轮子可以批量替换prefab里的prefab，欢迎大家测试～<https://bitbucket.org/xuanyusong/prefab-
replace>

最近在做UI部分中遇到了这样的问题，就是Prefab里面预制了Prefab。可是在Unity里面一旦Prefab预制了Prefab那么内部的Prefab就失去关联。导致与如果要改内部的Prefab需要把所有引用的地方全部改一遍。今天在逛国外网站看到了一个老外的思路，原文在这里<http://framebunker.com/blog
/poor-mans-nested-prefabs/>

下面直接上代码
```
using UnityEngine;

#if UNITY_EDITOR
 using UnityEditor;
 using UnityEditor.Callbacks;
#endif

using System.Collections.Generic;

[ExecuteInEditMode]
public class PrefabInstance : MonoBehaviour
{

    public GameObject prefab;

#if UNITY_EDITOR
 // Struct of all components. Used for edit-time visualization and gizmo drawing
 public struct Thingy {
 public Mesh mesh;
 public Matrix4x4 matrix;
 public List<Material materials;
 }

 [System.NonSerializedAttribute] public List<Thingy things = new
List<Thingy ();

 void OnValidate () {

 things.Clear();

 if (enabled)
 Rebuild (prefab, Matrix4x4.identity);
 }


 void OnEnable () {
 things.Clear();
 if (enabled)
 Rebuild (prefab, Matrix4x4.identity);
 }

 void Rebuild (GameObject source, Matrix4x4 inMatrix) {

 if (!source)
 return;

 Matrix4x4 baseMat = inMatrix * Matrix4x4.TRS (-source.transform.position,
Quaternion.identity, Vector3.one);
 foreach (MeshRenderer mr in source.GetComponentsInChildren(typeof
(Renderer), true))
 {

 things.Add(new Thingy () {
 mesh = mr.GetComponent<MeshFilter().sharedMesh,
 matrix = baseMat * mr.transform.localToWorldMatrix,
 materials = new List<Material (mr.sharedMaterials)
 });

 }

 foreach (PrefabInstance pi in source.GetComponentsInChildren(typeof
(PrefabInstance), true))
 {
 if (pi.enabled && pi.gameObject.activeSelf)
 Rebuild (pi.prefab, baseMat * pi.transform.localToWorldMatrix);
 }
 }
 // Editor-time-only update: Draw the meshes so we can see the objects in the
scene view
 void Update () {
 if (EditorApplication.isPlaying)
 return;
 Matrix4x4 mat = transform.localToWorldMatrix;
 foreach (Thingy t in things)
 for (int i = 0; i < t.materials.Count; i++)
 Graphics.DrawMesh (t.mesh, mat * t.matrix, t.materials[i], gameObject.layer,
null, i);
 }

 // Picking logic: Since we don't have gizmos.drawmesh, draw a bounding cube
around each thingy
 void OnDrawGizmos () { DrawGizmos (new Color (0,0,0,0)); }
 void OnDrawGizmosSelected () { DrawGizmos (new Color (0,0,1,.2f)); }
 void DrawGizmos (Color col) {

 if (EditorApplication.isPlaying)
 return;

 Gizmos.color = col;
 Matrix4x4 mat = transform.localToWorldMatrix;
 foreach (Thingy t in things)
 {
 Gizmos.matrix = mat * t.matrix;
 Gizmos.DrawCube(t.mesh.bounds.center, t.mesh.bounds.size);
 }
 }

 // Baking stuff: Copy in all the referenced objects into the scene on play
or build
 [PostProcessScene(-2)]
 public static void OnPostprocessScene() {
 foreach (PrefabInstance pi in UnityEngine.Object.FindObjectsOfType (typeof
(PrefabInstance)))
      BakeInstance (pi);
 }

 public static void BakeInstance (PrefabInstance pi) {
 if(!pi.prefab || !pi.enabled)
 return;

 pi.enabled = false;
 GameObject go = PrefabUtility.InstantiatePrefab(pi.prefab) as GameObject;
 Quaternion rot = go.transform.localRotation;
 Vector3 scale = go.transform.localScale;
 go.transform.parent = pi.transform;
 go.transform.localPosition = Vector3.zero;
 go.transform.localScale = scale;
 go.transform.localRotation = rot;
 pi.prefab = null;

 foreach (PrefabInstance childPi in
go.GetComponentsInChildren<PrefabInstance())
 BakeInstance (childPi);
 }
#endif
}
```

用法比较简单，比如我有两个Prefab，inside嵌入在Big里面。如下图所示，把PrefabInstance脚本挂在Big上，然后把inside拖入下方。

  

![](http://upload-images.jianshu.io/upload_images/17266280-96725fd31f44b3f7.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

OK 无论怎么修改inside这个Prefab，当实例化Big的时候都能得到最新修改的Inside这个Prefab。

持续思考：

界面预览问题，就是我在布界面的时候，我需要把子集Prefab界面控件拖进来预览效果。如果用上述思路UI的Prefab就必须通过脚本自动生成。一份是预览用的也就是不需要脚本的，一份是只带脚本运行时动态生成的。在处理自动生成UIPrefab的时候可以利用tag
比如像这种需要内嵌的Prefab标记一个特殊的tag，在Editor下完成Prefab的导出。另外布界面的时候不需要绑定脚本，而上述脚本的绑定也应该由Editor导出Prefab的时候完成。

总之一切布界面的时候只操作Prefab不操作脚本。

最近造了个轮子可以批量替换prefab里的prefab，欢迎大家测试～<https://bitbucket.org/xuanyusong/prefab-
replace>

如果有更好的方法欢迎各位朋友在下面给我留言，谢谢。

本文固定链接: <https://www.xuanyusong.com/archives/3042>

转载请注明: [雨松MOMO](https://www.xuanyusong.com/archives/author/xuanyusong)
2014年07月31日 于 [雨松MOMO程序研究院](https://www.xuanyusong.com/) 发表

