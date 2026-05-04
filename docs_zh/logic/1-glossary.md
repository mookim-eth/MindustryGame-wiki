# 术语表

本术语表对本手册中使用的许多术语提供更详细的解释。

## 数据类型

Mindustry 中有两种主要数据类型：数字和对象。

### number

十进制数字。可以为负数或正数，也可以表示 true（任何不等于 0 的值）或 false（0）值。Null 也会表示为 0。

某些指令只能接受整数，因此本手册会相应说明。

在内部，数字以 64 位浮点值（`double`）存储；涉及位移时，则以 64 位有符号整数（`long`）参与运算。

### String

表示用引号括起来的文本的对象，例如 `"hello mindustry"`

### Building

表示世界中一个实体建筑的对象。

**这不同于方块（Block）**；Block 只是 Building 的一种类型，而 Building 是一个有形的 Block——也就是说，它有生命值，会与电力和物品等交互。

本质上，**Building 是物理存在于世界中的方块（Block）。**

例如，`getlink` 指令会返回一个 *Building* 对象，你可以使用 `sensor` 获取它的信息。

### Unit

表示世界中的一个单位（包括玩家）的对象。

例如，`ubind` 指令会将处理器变量 `@unit` 设为一个表示已绑定单位的 Unit 对象。

## 参数类型

这些类似于数据类型，但只作为指令的参数使用，不会由任何指令返回。

### BuildingType `content`

一种 Building 类型。以 `@` 开头。

在游戏代码中，它更适合被称为“Block”。不过，为了本手册的可读性，我们会称它为 BuildingType。*关于 Building 与 Block 的解释，请参见 [###Building]。*

与物品和液体不同，你不能在 `sensor` 中使用它。不过，你可以使用 `@type` 于 `sensor` 中，并在 `jump` 中与它进行比较。

示例：`@scatter`

### UnitType `content`

一种 Unit 类型。以 `@` 开头。

示例：`@toxopid`

*完整列表显示在“Unit Bind”指令块中铅笔按钮下。*

<img src="/wiki/images/misc/logic-glossary-unitType-unitBind.png">

### Senseable

可由 `sensor` “感测”的物品、液体、建筑或单位属性。以 `@` 开头。

示例：`@scrap`、`@slag`、`@totalAmmo`

*完整列表显示在“Sensor”指令块中铅笔按钮下。*

<img src="/wiki/images/misc/logic-glossary-senseable-sensor.png">

### Target

用于按特征筛选单位或方块目标的条件。主要用于 `radar`、`uradar` 和 `ulocate`。`radar` 和 `uradar` 拥有相同的 Target，但 `ulocate` 不同，因为它会寻找建筑。

*完整列表可通过按下 `radar` 和 `uradar` 中“target”后的参数，或 `uradar` 中的“find”和“type”来显示。*

<img src="/wiki/images/misc/logic-glossary-target-radar.png">

### Op

一种数学运算。*这不同于 `op` 指令。*

*完整列表显示在“Operation”指令块中“+”按钮下。*

<img src="/wiki/images/misc/logic-glossary-op-operation.png">

对于较复杂的运算，你可以 Google “<operation name\> Java math”。

### Comp

一种比较。主要用于 `jump` 指令中比较两个值。`always` 无论如何都会返回 true，因此它总会导致跳转。

*完整列表显示在“Jump”指令块中的比较按钮下。*

<img src="/wiki/images/misc/logic-glossary-comp-jump.png">
