# 变量和常量

变量和常量本质上都是值的“容器”。每一个都有名称和值。Mindustry 中既有可以由用户及其代码设置的变量，也有只由处理器设置、用户无法更改的常量。

*若要了解变量或常量可能具有的数据类型或参数类型，请参见术语表。*

## 变量

### 创建和更改变量

变量顾名思义，是可以改变的值。

例如，在这段代码中：`set myVariable 3`，`set` 指令会创建一个名为 `myVariable` 的变量，并赋予它值 `3`。

稍后，可以这样将它的值改为 `9`：`set myVariable 9`。

请注意，我们在创建和更改变量时使用了同一条指令。这是因为**如果某条指令要更改的变量尚不存在，它会先创建该变量。**如果你懂 Python，你可能已经意识到它的工作方式相同。

另一个例子是使用 `sensor`：`sensor playerX playerUnit @x`（或在可视化编辑器中写作 Sensor playerX = @x in playerUnit）。

假设玩家的位置是 `141, 20`，那么会先创建一个名为 `playerX` 的变量，然后把值 `141` 赋给它。

不过，示例中还有另一个名为 `playerUnit` 的变量。这个变量是一个**参数**。参数是传给指令的输入值。在这种情况下，我们很可能先前已经得到了 `playerUnit`，而它来自 `radar` 指令。如果没有提供参数，或参数无效，该指令将不会执行。

### 数据类型和隐式转换

变量中的值当然具有不同类型，这些类型对应不同的来源和用途，例如用于单位的 `Unit`、用于任意数字的 `number` 等。你可以在术语表中找到它们的完整列表。

Mindustry 逻辑中的变量还有一个称为**隐式转换**的机制。这意味着如果需要，它会将变量的值从一种类型转换为另一种类型。

如果某条指令得到的是 `number`，但它需要 `Object`，该值会被转换为 `null`。如果某条指令需要 `number`，但得到的是 `Object`，那么当该对象不是 `null` 时会被转换为 1，否则转换为 0。

示例：

* `53` -> `null`
* `null` -> 0,
* `Object`（例如热能坩埚（Silicon Crucible）） -> 1

`print` 指令是唯一需要 `String` 作为输入的指令，因此它的规则会在本手册中对应的部分说明。

### 变量命名

在一般编程中，正确命名变量是一项重要技能。它有助于让代码更易读、更容易理解。因此，这也能让别人更容易从你的代码中学习，或修复你的代码。

变量名可以包含任何可输入字符。不过，它们不能完全由数字组成，因为那样会改为使用实际的数字。

大多数 mlog 代码中常见的命名约定是 camelCase，它本身就是一个例子。使用 camelCase 命名的变量示例包括：`playerX`、`coreFound`、`vertexAngle`。

**命名变量时，请确保它们具有描述性但又简短。**它们必须描述所保存的值或其用途。同时，它们不应该是完整句子、不应该横跨整个页面，也不应该短到令人困惑。你可以使用缩写、首字母缩略词或更短的术语，让它们更简洁。

每个人都有自己的具体风格和偏好，但请尝试学习 mlog 和其他语言中的优秀代码示例，同时尽量贴近通用风格。

## 处理器变量和常量

常量也保存值，但不能被更改。每个处理器都内置了这些常量和变量：

### 处理器

#### @this `constant` `Building`

表示处理器自身的 `Building` 对象。你可以将它与 `sensor` 搭配使用，来查找处理器的各种属性。

#### @thisx `constant` `number`

处理器的 x 坐标。

#### @thisy `constant` `number`

处理器的 y 坐标。

#### @ipt `constant` `number`

每 tick 执行的指令数量（每秒 60 tick）。

* 微型处理器（Micro Processor） -> 2
* 逻辑处理器（Logic Processor） -> 8
* 超核处理器（Hyper Processor） -> 25 

#### @counter `variable` `number`

表示处理器下一步将从哪一行读取代码的变量，等价于 x86 中的 `%IP`。它可以像其他变量一样被更改，从而作为另一种执行跳转的方法。

一个（进阶）示例：设置 `@counter` 以跳转到函数，然后再跳回调用者：

```
op add retAddr @counter 1 # Save where we will continue after the function returns by adding 1 to the counter
set @counter myFunc       # Jump to the line representing myFunc
...
set @counter retAddr      # Return to the line set earlier after the function is called
```
### 链接

#### @links `constant` `number`

一个等于链接到处理器的建筑数量的常量。当方块被链接到处理器或取消链接时，它会由处理器更改。

你可以将它与 `getlink` 一起使用，循环遍历所有已链接建筑，如下所示：

```
set linkIter 0                  # 创建迭代变量
getlink block linkIter          # 获取第 linkIter 个已链接建筑
# 在这里处理该建筑
op add linkIter linkIter 1      # 移动到下一个链接
jump 1 lessThan linkIter @links # 继续循环
```

#### `<buildingName><n>` `constant` `Building`

这实际上是多个常量，每个链接到处理器的建筑各有一个。当某个建筑与处理器取消链接或链接到处理器时，它们会被移除或添加。

`buildingName` 表示该建筑的**内部名称**，你可以在 Wiki 的其他部分找到它。

`n` 从 1 开始，并随着该类型的每个建筑被链接而递增。它有点类似于某个类型的第 `n` 个建筑。

这可能有点难以理解，所以这里有一些示例：

* 第一个链接到处理器的分裂（Scatter）：`scatter1`
* 第三个链接的浪涌（Ripple）：`ripple3`
* 第二个链接的激光钻头（Laser Drill）：`drill2`
* 第十一个链接的孢子压缩机（Spore Press）：`press11`

当处理器被选中时，你也可以在每个已链接建筑上方查看它们的“常量名”。

<img src="/wiki/images/misc/logic-variables-constants-links-linkedBuilding.png">

### 其他

#### @unit `constant` `Unit`

表示当前已绑定单位的常量。它只会在处理器解绑单位或绑定另一个单位时改变。你可以使用 `ucontrol`、`ulocate` 和 `uradar` 等单位指令访问它。由于它是一个 Unit 对象，你也可以将它与 `sensor` 一起使用。

这体现了 mlog 中单位控制的核心部分：**一次只能绑定一个单位。**不过，你可以在变量中引用它，例如 `set unitReference @unit`。然而，该变量不能用于控制被引用的单位。它只能用于和其他单位进行比较，或获取关于它的信息。因此，你可以把它看作一个“单位身份”。

#### @time `constant` `number`

表示当前 UNIX 时间戳，*单位为毫秒*。

#### @tick `constant` `float`

表示地图开始以来经过的 tick 数量（每秒 60 tick）。

#### @mapw `constant` `number`

地图宽度，以图格为单位。

#### @maph `constant` `number`

地图高度，以图格为单位。
