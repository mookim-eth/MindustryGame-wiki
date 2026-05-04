# 编写和编辑代码

编写 Mindustry 逻辑主要有两种方法：可视化编辑器和手动编辑。它们各有优势，因此请选择最适合你的方式。

## 可视化编辑器

可视化编辑器是处理器的“编辑”界面（当你按下“铅笔”按钮时）。**这是推荐给初学者的方法**，因为它被设计得易于理解和使用。

与手动编辑相比，以这种方式编辑的优点包括：

* 基于块、颜色编码、可拖放的界面
* 简单的参数选择器，会显示所有所需参数
* 可视化、易于设置的跳转关系
* 适合移动端

<img src="/wiki/images/misc/logic-editing-visualEditor-overview.png">

你也可以将代码导出为文本形式，或从文本形式导入代码。

## 手动编辑

手动编辑是指使用 Notepad++、Vim 或 Visual Studio Code 等文本编辑器来编辑你的代码。**对于更高级的用户和更长的代码，手动编辑才是合适的方式**。

与可视化编辑器相比，手动编辑代码的优点包括：

* 比可视化编辑器更紧凑；一次可以看到更多代码
* 在很长的代码中，打字比拖放更快
* 不打开 Mindustry 也能快速编写用于演示的代码片段
* 一些编辑器支持语法高亮，例如 [VS Code（插件）](https://marketplace.visualstudio.com/items/?itemName=JeanJPNM.mlogls-vscode)、[Emacs（包）](https://github.com/vednoc/masm-mode)、[Vim（插件）](https://github.com/purofle/vim-mindustry-logic) 和 [Sublime Text（包）](https://github.com/gigamicro/Mindustry4Sublime)
* 文本块不会遮挡部分参数文本
* 能够在 Mindustry 之外保存和访问代码

不过，对于初学者或不习惯编辑代码的人来说，它可能会有些困难，因为变量必须明确键入，而且跳转在没有可视化指引时可能会变得非常混乱，除此之外还有其他问题。
