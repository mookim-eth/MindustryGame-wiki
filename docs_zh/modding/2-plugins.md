# 插件与 JVM 模组

Mindustry 支持在桌面端和 Android 上加载包含 Java 字节码的 `jar` 文件。它们的功能类似 JS 模组，并且必须提供一个在创建模组时实例化的单一主类。

理论上，所有 JVM 语言都应受到支持。

Jar/JVM 模组使用与标准模组相同的 `mod.hjson` 元文件，但有一个额外项：可以用 `main: "mypackage.MyMod"` 指定*完全限定主类*。这个类应扩展 `mindustry.mod.Mod`。


如果未指定主类，它默认会是 `modnameinlowercase.ModName + "Mod".`

一个简单的 Java 模组 `mod.hjson` 可以如下所示：

```hjson
name: "Nothing"
author: "Yourself"
main: "nothing.NothingMod"
description: "..."
version: "99.99"
```

更多说明请参阅[示例 Java 模组仓库](https://github.com/Anuken/MindustryJavaModTemplate)或[示例 Kotlin 模组仓库](https://github.com/Anuken/MindustryKotlinModTemplate)。

## 插件

插件是仅打算在服务器上运行的 Java 模组。通常，它们会添加*新命令*或*新游戏模式*。
所有插件主类都应扩展 `mindustry.mod.Plugin`。这会使它们隐式地变为*隐藏*——客户端不需要下载插件也能加入服务器。它们仅在服务器端运行。要安装插件，请将 JAR 放入 `<server directory>/config/mods/`。

插件将其元文件命名为 `plugin.[h]json`。文件结构与其他 Java 模组相同——详情见上文。

你可以在[这里](https://github.com/Anuken/MindustryPluginTemplate)查看示例插件。若要查看可用于真实服务器的更实用示例，请参阅[这个仓库](https://github.com/Anuken/AuthorizePlugin)。

## 导入

与 JS 或 JSON 模组不同，JAR 模组需要编译。这意味着它们不能直接从 GitHub 导入；取而代之的是使用 *GitHub Releases*。

当用户尝试安装 JAR 模组时，Mindustry 会检查最新（且*只有*最新）的 GitHub release 中是否有 `.jar` 构件。找到第一个构件后，它会被下载到客户端。请注意，预发布版本会被忽略。

我建议使用 GitHub Actions（或任何其他 CI）自动构建 jar 构件，并上传到新的 releases。

## 多线程

除非另有说明，**没有任何 Mindustry 代码是线程安全的**。从主线程以外的线程执行任何操作（例如发送数据包、改变图格）都会导致随机崩溃或网络错误。要在主线程上运行某些内容，请使用 `Core.app.post(() -> { /* code */ })`。

## 能力与安全性

由于 jar 模组会通过没有沙盒的 `URLClassLoader` 直接加载，它们没有任何安全限制。这意味着：

- 可以访问所有 Java API。
- 可以使用反射访问 private/hidden 属性。
- 模组拥有对客户端电脑的完全访问权限，可能打开潜在恶意行为的大门。
- 模组可以更改游戏文件或重写核心字节码。

因此，你应*永远不要从不受信任的来源导入 jar 模组。* 现在，你可能会疑惑：为什么不对 jar 模组使用沙盒？这难道不是巨大的安全风险吗？

答案是：*是的*，确实如此。然而，没有好的替代方案。即使我实现 `SecurityManager` 来限制模组能力，也无济于事——Java 本质上并不安全，任何足够“安全”的沙盒实现（*如果甚至存在的话*）都需要在模组中禁用反射，而这是不可接受的。

作为比较，Forge（*一个流行的 Minecraft Java 模组加载器*）也不会对模组使用沙盒。
