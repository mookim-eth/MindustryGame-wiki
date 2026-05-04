# 标记

文本渲染器使用一种简单的标记语言为文本着色。

-   `[name]` 按名称设置颜色，有一些[内置颜色](#built-in-colors)；
-   `[#rrggbb]` / `[#rrggbbaa]` 按十六进制值设置颜色，每个值可以是从 `00` 到 `ff` 的任意值：
    -   `rr` 是红色值，
    -   `gg` 是绿色值，
    -   `bb` 是蓝色值，
    -   `aa` 是 alpha 值；
-   `[]` 将颜色设置回上一个颜色；
-   `[[` 转义左方括号，因此你可以写 `[[red]`，它会渲染为 `[red]`。

说明：

-   错误/未知颜色会被静默忽略。

示例：

    [red]red
    [#ff0000]full-red
    [#ff000066]half-red
    [#ff000033]half-half-red
    [#00ff00]green
    []half-half-red



<a id="built-in-colors"></a>

### 内置颜色

    [clear]clear (#00000000)
    [black]black (#000000FF)
    [white]white (#FFFFFFFF)
    [lightgray]lightgray (#BFBFBFFF)
    [gray]gray (#7F7F7FFF)
    [darkgray]darkgray (#3F3F3FFF)
    [blue]blue (#0000FFFF)
    [navy]navy (#00007FFF)
    [royal]royal (#4169E1FF)
    [slate]slate (#700090FF)
    [sky]sky (#87CEEBFF)
    [cyan]cyan (#00FFFFFF)
    [teal]teal (#007F7FFF)
    [green]green (#00FF00FF)
    [acid]acid (#7FFF00FF)
    [lime]lime (#32CD32FF)
    [forest]forest (#228B22FF)
    [olive]olive (#6B8E23FF)
    [yellow]yellow (#FFFF00FF)
    [gold]gold (#FFD700FF)
    [goldenrod]goldenrod (#DAA520FF)
    [orange]orange (#FFA500FF)
    [brown]brown (#8B4513FF)
    [tan]tan (#D2B48CFF)
    [brick]brick (#B22222FF)
    [red]red (#FF0000FF)
    [scarlet]scarlet (#FF341CFF)
    [coral]coral (#FF7F50FF)
    [salmon]salmon (#FA8072FF)
    [pink]pink (#FF69B4FF)
    [magenta]magenta (#FF00FFFF)
    [purple]purple (#8000FFFF)
    [violet]violet (#EE82EEFF)
    [maroon]maroon (#B03060FF)
