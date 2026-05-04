# 模组制作简介

Mindustry 模组本质上只是资源目录。根据你具体想做什么，以及愿意为此深入到什么程度，模组 API 有许多使用方式。

你可以只为现有游戏内容重绘贴图，也可以用更简单的 JSON API（这是本文档的主要重点）创建新的游戏内容，还可以添加自定义音效（或复用现有效果）。你可以向战役模式添加地图，也可以向模组中添加脚本，以编写特殊行为，例如自定义特效。

分享模组就像把你的项目目录交给别人一样简单；模组也能在任何支持模组的平台之间跨平台使用。你会希望使用 [GitHub](#github)（*或类似服务*）来托管源代码。
制作模组真正需要的只是任意一台带文本编辑器的电脑。


## 目录结构

你的项目目录应大致如下：

    project
    ├── mod.hjson
    ├── content
    │   ├── items
    │   ├── blocks
    │   ├── liquids
    │   └── units
    ├── maps
    ├── bundles
    ├── sounds
    ├── schematics
    ├── scripts
    ├── sprites-override
    └── sprites

-   `mod.hjson`（必需）你的模组元数据文件，
-   `content/*` 用于游戏[内容](#content)的目录，
-   `maps/` 用于游戏内地图的目录，
-   `bundles/` 用于[语言包/Bundle](#bundles)的目录，
-   `sounds/` 用于[音效](#sound)文件的目录，
<a id="schematic"></a>
-   `schematics/` 用于[蓝图](#schematic)文件的目录，
<a id="scripts"></a>
-   `scripts/` 用于[脚本](#scripts)的目录，
-   `sprites-override/` 用于覆盖游戏内内容的[贴图](#sprites)目录，
-   `sprites/` 用于你的内容的[贴图](#sprites)目录，

每个平台都有不同的用户应用数据目录，你的模组应放在这里：

-   Linux: `~/.local/share/Mindustry/mods/`
-   Steam: `steam/steamapps/common/Mindustry/saves/mods/`
-   Windows: `%appdata%/Mindustry/mods/`
-   MacOS: `~/Library/Application Support/Mindustry/mods/`

*请注意，文件名应使用小写并以连字符分隔：*

-   正确：`my-custom-block.json`
-   错误：`My Custom Block.json`


## Hjson

Mindustry 使用 [Hjson](https://hjson.github.io/)。对于熟悉 JSON 的人来说，它只是非常流行的序列化语言 [JSON](https://en.wikipedia.org/wiki/JSON) 的一个超集。&#x2013; 这意味着任何有效的 JSON 都能使用，同时还能获得一些额外的实用功能：

    # single line comment
    
    // single line comment
    
    /* multiline
    comment */
    
    key1: single line string
    
    key2:
    '''
    multiline
    string
    '''
    
    key3: [ value 1
            value 2
            value 3 ]
    
    key4: { key1: string
            key2: 0 }

如果你不认识这些词。&#x2013; 序列化语言就是一种为程序编码信息的语言，而 *encode* 指把信息从一种形式转换为另一种形式；在这里，就是把文本转换为 Java 数据结构。



## `mod.hjson`

在项目目录根部，必须有一个 `mod.json`，用于定义项目的基本元数据。这个文件也可以（可选地）命名为 `mod.hjson`，这样可能有助于文本编辑器选择更好的语法高亮。

    name: "mod-name"
    displayName: "This isn't a mod."
    author: Yourself
    description: "Bbfashbjhcbabfhsbafbhajbf"
    version: "1.0"
    minGameVersion: "$latestRelease"
    dependencies: [ ]
    hidden: false

-   `name` 会用于引用你的模组，因此请谨慎命名。它应使用 kebab-case（没有大写字母，空格用连字符填充），并且不应包含任何颜色格式。
-   `displayName` 会用作 UI 中显示的名称，你可以为该名称添加格式。
-   `description` 是模组说明，会在游戏内模组管理器中渲染，因此请保持简短并切中要点。
-   `dependencies` 是可选项；如果想了解更多，请前往[依赖项](#dependencies)一节。
-   `minGameVersion` 是模组要求的最低游戏构建版本；请设置为你的模组实际支持的最低版本。v6 迁移模组通常至少应为 `105`。
-   `hidden` 表示此模组是否隐藏并且不参与多人游戏模组同步检查，默认值为 `false`。仅材质包、纯客户端脚本、服务器插件等不创建新内容，且不要求所有玩家共同安装的模组才应使用 `hidden: true`。如果你的模组会创建物品、方块、单位等内容，就不应将其隐藏。



<a id="content"></a>

<a id="item"></a>
<a id="block"></a>
<a id="liquid"></a>
<a id="unittype"></a>

## 内容

在项目目录根部可以有一个 `content/` 目录，所有 Hjson/JSON 数据都放在这里。在 `content/` 内部，你可以为各种内容类型设置子目录；以下是目前常见的几种：

-   `content/items/` 用于[物品](#item)，例如铜（`copper`）和巨浪合金（`surge-alloy`）；
-   `content/blocks/` 用于[方块](#block)，例如炮塔和地板；
-   `content/liquids/` 用于[流体/液体](#liquid)，例如水（`water`）和矿渣（`slag`）；
-   `content/units/` 用于飞行或地面[单位](#unittype)，例如日蚀（`eclipse`）和尖刀（`dagger`）；

请注意，每个子目录都需要特定的内容类型。这些文件的文件名很重要，因为路径的主干名（*不含扩展名的文件名*）会用于引用它。

此外，这些 `content/<content-type>/*` 目录中的文件可以任意嵌套到任何名称的其他子目录中，以便进一步组织，例如：

-   `content/items/metals/iron.hjson`，它会相应地创建一个名为 `iron` 的物品。

这些文件的内容通常会大致如下：

    type: TypeOfThing
    name: Name Of Thing
    description: Description of thing.
    # ... more fields here ...

|字段|类型|说明|
|---|---|---|
|type|String|具体实现类型或类名，例如方块的 `GenericCrafter`、单位的 `flying`；内容类型由所在目录（如 `content/blocks/`）决定。|
|name|String|内容显示名称。|
|description|String|内容显示说明。|

包含的其他字段将是该类型本身的字段。

顺带一提，`name` 和 `description` 并不要求出现在 JSON 结构中。你可以通过[语言包/Bundle](#bundles)为任意语言定义它们。不过，如果两处都不存在，那么名称将分别为 `<type>.<modname>-<stemname>.name`，说明则为空。


## 类型

类型有许多字段，但重要的是 `type`；这是内容解析器使用的特殊字段，用来选择具体实现类或单位实体构造方式。*`Router` 不能当作 `Turret` 使用*，因为它们完全不同。

类型会相互 *extend*，因此如果 `MissileBulletType` 扩展了 `BasicBulletType`，那么你就能在 `MissileBulletType` 中访问 `BasicBulletType` 的所有字段，例如 `damage`、`lifetime` 和 `speed`。字段区分大小写：`hitSize =/= hitsize`。

字段实际会做什么取决于具体类型；有些类型完全不会使用自己的字段，主要作为其他类型扩展的基础类型。`Block` 就是这样的类型之一。

在这个单位示例中，该单位的类型是 `flying`。`bullet` 的类型是 `BulletType`，因此你可以使用 `MissileBulletType`，因为 `MissileBulletType` 扩展了 `BulletType`。

这里也可以使用 `mech`、`legs`、`naval`、`payload`、`missile`、`tank`、`hover`、`tether` 或 `crawl` 作为单位类型。

```hjson
type: flying
weapons: [
  {
    bullet: {
      type: MissileBulletType
      damage: 9000
    }
  }
]
```

从构建版本 `125.1` 开始，类型也可以是 Java 类的*完全限定类名*。

例如，要将一个方块指定为 `MendProjector`，你可以写
`type: mindustry.world.blocks.defense.MendProjector`，而不是 `type: MendProjector`。

虽然这对原版类型并不是特别有用，但它可以用于从*其他 Java 模组*加载方块类型作为依赖项。

## 科技树

与 `type` 类似，还存在另一个名为 `research` 的神奇字段；它可以放在任意方块对象的根部，用于将其放入科技树。

    research: duo

这会把你的方块放在科技树中的双管（`duo`）之后；如果要把它放在你自己的模组方块之后，则写入你的 `<block-name>`。只有在使用其他模组的内容时，才需要加上模组名前缀。

研究花费：

|类型|花费|说明|
|---|---|---|
|blocks|`requirements ^ 1.1 * 20 * researchCostMultiplier`|`researchCostMultiplier` 是一个可以在方块上设置的属性|
|units|`requirements ^ 1.1 * 50`|---|

随后会根据花费的高低，将花费向下取整到最接近的 10、100、1k、10k 或 100k。

`requirements` 是方块或单位的花费。单位会使用其建造花费/升级花费进行计算。

如果你想设置自定义研究需求，请使用这个对象来替代单纯的名称：

    research: {
      parent: duo
      requirements: [
        copper/100
      ]
    }

这可用于覆盖方块或单位花费，或让资源需要先被研究，而不只是生产出来即可。

<a id="sprites"></a>

## 贴图

制作贴图所需的一切，只是一个支持透明度的图像编辑器（*也就是：不是画图*）。方块贴图应为 `32 * size`，因此一个 `2x2` 方块需要 `64x64` 图像。图像必须是 32 位 RGBA 像素格式的 PNG 文件。
**任何其他像素格式，例如 16 位 RGBA，都可能导致 Mindustry 因 “Pixmap decode error” 而崩溃。** 你可以使用命令行工具 `file` 打印贴图信息：

    file sprites/**.png

如果其中有任何贴图不是 32 位 RGBA 格式，请修正它们。

贴图可以直接放入 `sprites/` 子目录。内容解析器会递归遍历它。
图像会被打包进一个“图集”（atlas），以便高效渲染。`sprites/` 中的第一个目录，例如 `sprites/blocks`，决定贴图会被放入该图集的哪一页。把方块贴图放进 `units` 页很可能导致大量卡顿；因此，你应尽量按[原版游戏的组织方式](https://github.com/Anuken/Mindustry/tree/master/core/assets-raw/sprites)来整理内容。

内容会根据自身名称查找贴图。`content/blocks/my-hail.json` 的名称是 `my-hail`，类似地，`sprites/my-hail.png` 的名称也是 `my-hail`，因此它会被此内容使用。

内容可能会查找多张贴图。`my-hail` 可能是炮塔，并且它可能会查找后缀 `<name>-heat`；这意味着它会查找 `my-hail-heat`。

你可以在这里找到所有原版贴图：

-   <https://github.com/Anuken/Mindustry/tree/master/core/assets-raw/sprites>

关于贴图还需要知道的一点是，其中一些会被游戏修改。具体来说，炮塔和单位会被添加深灰/灰色描边，因此制作贴图时必须考虑这一点，例如在炮塔周围留出透明空间：[浪涌（Ripple）](https://raw.githubusercontent.com/Anuken/Mindustry/master/core/assets-raw/sprites/blocks/turrets/ripple.png)

要覆盖游戏内内容贴图，只需把它们放入 `sprites-override/`。
这会移除其 id 中的 `<modname>-` 前缀，使它们能够覆盖原版甚至其他模组的贴图。
你也可以用它创建像 `cat` 这样简短好用的贴图名称，便于在脚本中使用；只是要注意与其他模组发生名称冲突。



<a id="sound"></a>

## 音效

可以通过模组系统添加自定义音效，只需把它们放入 `sounds/` 子目录即可。之后放在哪里都无所谓。支持两种格式：`ogg` 和 `mp3`。请注意，`mp3` 文件无法无缝循环，因此请尽可能使用 `ogg`。

和其他任何资源一样，你通过文件名的主干名引用它们，因此 `pewpew.ogg` 和 `pewpew.mp3` 可以在 `Sound` 类型的字段中用 `pewpew` 引用。

内置音效列表：

$sounds

<a id="dependencies"></a>

## 依赖项

你可以通过简单地在 `mod.json` 中添加其他模组名称，向你的模组添加依赖项：

    dependencies: [
      other-mod-name
      not-a-mod
    ]

依赖项名称会转换为小写，并把空格替换为 `-` 连字符，例如 `Other MOD NamE` 会变成 `other-mod-name`。

要引用其他模组的资源，必须给资源加上其他模组的名称作为前缀：

-   `other-mod-name-not-copper` 会引用 `other-mod-name` 中的 `not-copper`
-   `other-mod-name-angry-dagger` 会引用 `other-mod-name` 中的 `angry-dagger`
-   `not-a-mod-angry-dagger` 会引用 `not-a-mod` 中的 `angry-dagger`



<a id="bundles"></a>

## 语言包/Bundle

你的模组还可以选择添加称为语言包/Bundle 的内容。Bundle 的主要用途是为你的内容提供翻译，但你当然也可以在英文中使用它们。它们是放在 `bundles/` 子目录中的纯文本文件，命名方式应类似 `bundle_ru.properties`（用于俄语）。

这个文件的内容非常简单：

    block.example-mod-silver-wall.name = Серебряная Стена
    block.example-mod-silver-wall.description = Стена из серебра.

如果你读过本指南前几节，就会立刻看出来：

-   `<content type>.<mod name>-<content name>.name`
-   `<content type>.<mod name>-<content name>.description`

对于脚本中使用的自定义 Bundle 条目，你可以使用任何喜欢的键：

-    `message.egg = Eat your eggs`
-    `randomline = Random Line`

说明：

-   模组/内容名称为小写，并以连字符分隔。

内容类型列表：

$contentTypes

语言对应的 Bundle 后缀列表：

$bundles


<a id="github"></a>

## GitHub

一旦你有了某种模组，就会想要真正分享它，甚至可能想与其他人一起开发；为此可以使用 [GitHub](https://github.com/)。如果你完全不知道 Git（或 GitHub）是什么，那么应了解一下 [GitHub Desktop](https://desktop.github.com/)；否则，直接使用你喜欢的命令行工具或文本编辑器插件即可。

你只需要了解如何在 GitHub 上打开仓库、在本地仓库中暂存并提交更改，以及将更改推送到 GitHub 仓库。项目放到 GitHub 后，有三种分享方式：

-   使用端点，例如 `Anuken/MindustryJavaModTemplate`，随后可以在游戏内 GitHub 界面中输入它并下载；
-   使用 zip 文件，例如 `https://github.com/Anuken/MindustryJavaModTemplate/archive/master.zip`，这会以 zip 文件下载仓库，并放入模组目录（不需要解压）；
-   在你的仓库上添加主题/标签 `mindustry-mod`，这应会把它加入主题搜索和 [Mod scraper](https://github.com/Anuken/MindustryMods)。



## FAQ

-   游戏中的 `time` 通过 `ticks` 计算；
-   `ticks`（*有时称为 `frames`*）被视为 1/60 秒；
-   `tilesize` 在内部为 8 单位；
-   要通过 `lifetime` 和 `speed` 计算射程，可以使用 `lifetime * speed = range`；
-   *Abstract* 什么是 `abstract`？关于抽象类型，你只需要知道它们不能自行实例化/初始化。如果这么做，你会遇到某种 *“initialization exception”*；
-   什么是 `NullPointerException`？这是一条错误信息，表示某个字段为 null，而它不应为 null，这意味着可能缺少某个必填字段；
-   *bleeding-edge* 什么是 `bleeding-edge`？这是 Mindustry 的开发版本，具体指 GitHub master 分支。bleeding-edge 上的更改通常会进入 Mindustry 的下一个版本。

