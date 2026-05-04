# 类型

*注意：* 此处未列出已弃用的内容类，并且强烈不建议使用它们。请尽快迁移到未弃用的等效项。

在 [Mindustry Javadoc](https://mindustrygame.github.io/docs/deprecated-list.html) 中查看所有已弃用类和方法的列表。

所有 JSON 示例都会自动取自 *BlueWolf3682* 的 [Exotic Mod](https://github.com/BlueWolf3682/Exotic-Mod)。这些示例应*仅*用作字段参考——不要直接将它们复制粘贴到你的模组中，它们**不会**工作！

$allTypes


## BuildVisibility

游戏使用的标志，用于改变少数特殊情况行为。它可以是以下字符串之一：

$buildVisibilities


## BlockGroup

用于在方块上方建造其他方块的组：

$blockGroups


<a id="item"></a>

## ItemStack

`ItemStack` 可以是字符串或对象。它用于描述机器所需物品的类型和数量。

作为 `string`：

    copper/5

作为 `object`：

    item: copper
    amount: 5

|字段|类型|说明|
|---|---|---|
|item|string|[Item](#item) 的名称。|
|amount|int|该物品的数量。|



<a id="liquid"></a>

## LiquidStack

`LiquidStack` 可以是字符串或对象。它用于描述机器所需流体/液体的类型和数量。

作为 `string`：

    water/0.5

作为 `object`：

    liquid: water
    amount: 0.5

|字段|类型|说明|
|---|---|---|
|liquid|string|[Liquid](#liquid) 的名称。|
|amount|float|该流体/液体的数量。|


## Category

建造菜单的分类：

-   `turret` 进攻型炮塔；
-   `production` 生产原始资源的方块，例如钻头；
-   `distribution` 移动物品的方块；
-   `liquid` 移动流体/液体的方块；
-   `power` 生成或传输电力的方块；
-   `defense` 墙和其他防御结构；
-   `crafting` 制造物品的方块；
-   `units` 创建单位的方块；
-   `logic` 与逻辑运算相关的方块；
-   `effect` 用于储存或被动效果的内容。


## Color

颜色是十六进制字符串，例如 `<rr><gg><bb>`：

-   `ff0000` 是红色，
-   `00ff00` 是绿色，
-   `0000ff` 是蓝色，
-   `ffff00` 是黄色，
-   `00ffff` 是青色，
-   等等。



## CacheLayer

用于缓存渲染的标志：

-   `normal` 普通层；
-   `walls` 墙层；
-   `water` 水层，会添加图格水着色器并提供波浪反射；
-   `tar`（石油）层，会添加石油/油面着色器，使其更暗并提供一些气泡反射；

## TargetPriority

更高的序号表示更高的优先级。无论距离如何，较高优先级的方块总会优先于较低优先级的方块被作为目标。

1.  `base`
2.  `turret`
