# 数据包

数据包（Data Patches；单个文件在游戏内称为“补丁集”）是一种强大的工具，可按地图或按服务器修改建筑（block）、单位和物品的属性。此功能的一些用途包括平衡性补丁、自定义游戏模式，或不同的游戏进度设计。

数据包**可以**做的一些事情：

- 让工厂消耗更多或更少的资源
- 更改建筑的资源需求
- 完全更改单位的武器和子弹
- 更改单位工厂可用的配方
- 将建筑或单位显示的贴图改为其他游戏内纹理
- 更改任意建筑或单位的建造速度、生命值、护甲等
- 更改单位的类型（例如从地面改为飞行）

数据包**不能**做的一些事情：

- 向游戏中引入新的纹理或资产
- 引入原版中不存在的新机制
- 更改建筑的类型（例如把墙改成炮塔）
- 添加新内容（物品、建筑、单位等）

平衡性补丁*不能*替代模组；它们只能调整现有内容。

# 编写一个简单的数据包

数据包使用 JSON 或 HJSON（JSON 的超集）编写。你需要一个文本编辑器来编写它们；目前没有用于补丁的游戏内编辑器。

为简洁起见，本指南只会展示如何用 HJSON 编写补丁。

首先，创建一个名为 `mypatch.hjson` 的文本文件，内容如下：

```json5
//为补丁命名是可选的，但有助于在 UI 中识别它
name: My Patch

//使所有传送带的最大生命值为 50
block.conveyor.health: 50
```

# 应用数据包

## 在地图上应用补丁

在地图编辑器中打开你的地图，然后打开左上角菜单（或在桌面端按 ESC）。进入*地图信息（Map Info） -> 数据包（Data Patches） -> 添加（Add）*，然后指定你在上一步保存的补丁文件。你可以点击 ⚠️ 图标查看补丁生成的任何错误，或使用 🔁 按钮重新加载文件。

## 在专用服务器上应用补丁

打开你的服务器目录（其中应已包含 plugins、maps、saves 等文件夹），找到 `patches` 目录，然后直接把补丁文件放进去。补丁文件必须具有 `hjson/json/json5` 扩展名才会被加载。
它们会在地图已包含的任何其他数据包*之后*，自动应用到任何地图上。

如果一切操作正确，服务器应会在启动时记录已加载的补丁文件数量。任何警告或错误也会输出到控制台。
要在服务器仍在运行时重新加载补丁，请使用 `reloadpatches` 命令。

# 数据包基础

数据包遵循层级结构。在第一层，你定义要更改的内容类型：建筑 `block`、流体 `liquid`、物品 `item`、单位 `unit`、天气 `weather` 等。

在*第二*层，你定义要编辑的内容名称，例如 `conveyor`、`copper`、`copper-wall-large`。这些名称*区分大小写*；如果你启用了控制台，它们会显示在核心数据库中内容名称的下方。

在*第三*层，你定义将要更改的属性及其对应的值。例如：

```json5
block: {
  conveyor: {
    health: 50
    //传送带的其他属性写在这里...
  }
  //其他建筑写在这里...
}
//其他内容类型写在这里...

```

或者，如果你只修改单个属性，使用简写语法可能更方便：

```json5
block.conveyor.health: 50
```

## 查看内容的所有字段

如果你熟悉 Java，可以查看相关内容的源文件，例如建筑/方块对应的 [Block.java](https://github.com/Anuken/Mindustry/blob/master/core/src/mindustry/world/Block.java)。

如果不熟悉，可以在游戏设置中启用控制台，然后在特定建筑、单位或流体的数据库中点击“查看内容字段（View Content Fields）”按钮。

请注意，这只会显示*该特定类*的字段——如果你想查看父类的字段，请点击该页面上 “extends” 后紧跟的页面链接。

例如，[传送带（Conveyors）](https://mindustrygame.github.io/wiki/Modding%20Classes/Conveyor/) 会在其页面上显示所有字段，以及 [Block](https://mindustrygame.github.io/wiki/Modding%20Classes/Block/) 父类中的所有内容。

## 访问数组/序列

当需要访问数组（`T[]`）或序列（`Seq<T>`）时，你可能需要像这样操作：

```json5
//大幅偏移尖刀（dagger）的两个武器之一
unit.dagger.weapons.0.x: 100
```

请注意，修改*镜像*武器的子弹会影响两侧，因为它们共享同一种子弹类型：

```json5
//这个写法会让尖刀（dagger）的*两个*武器都造成 55 伤害
unit.dagger.weapons.0.bullet.damage: 55
```

## 向数组/序列添加与覆写数组/序列

有时可能需要向序列中*添加*内容，而不是覆写它，如下所示：

```json5
//给星辉（flare）的武器添加一把离谱强的激光，同时保留其他武器
//注意字段赋值前的 .+；这会添加元素
//还要注意，它可以是单个元素，而不是数组！
unit.flare.weapons.+: {
  x: 0
  y: 0
  reload: 10
  bullet: {
    type: LaserBulletType
    damage: 100
  }
}
```

或者，你可以覆写数组：

```json5
//星辉（flare）现在将*只有*这把武器；旧武器会被覆盖
//还要注意，覆写时*必须*使用数组括号 []，因为你是在赋予一个新值
unit.flare.weapons: [
  {
    x: 0
    y: 0
    reload: 10
    bullet: {
      type: LaserBulletType
      damage: 100
    }
  }
]
```

此语法适用于类型为 `T[]`、`Seq<T>` 和 `ObjectSet` 的字段。

# 一般信息

- 时间值通常以 *ticks*（有时称为“帧”）计量，即 1/60 秒（60 ticks = 1 秒）。如果某个字段描述的是持续时间，它很可能以 ticks 为单位。如果某个字段描述的是消耗速率，它很可能以“每 tick 单位数”为单位。
- 距离、位置和大小通常以“世界单位”计量，即图块的 1/8。这是因为 Mindustry 过去使用 8x8 贴图，而 1 个世界单位过去等于 1 像素。这*确实*很糟糕且不直观，但出于历史原因被保留了下来。
- 当你通过逻辑处理器与坐标交互时，它们会在*内部*与世界单位相互转换。补丁会直接修改字段，没有这种便利。
- 物品和液体堆叠可以定义为“name/amount”。例如，`ItemStack` 字段的值可以是 `thorium/100`。

# 注意事项与限制

- 创建或分配带有 `mirror: true` 的单位武器不会生效，因为不会为单位重新运行初始化。你必须手动创建镜像版本，并分配 `x/shootX/flipSprite`。
- 即使你增加了单位子弹的 lifetime 或 speed，单位的 `range` 和 `maxRange` 也不会更新。这些值必须手动分配。
- 同样，如果你重新分配单位的类型，单位字段也不会更新。例如，重新分配后的海军单位仍然会溺水。
- 即使你让方块或单位绘制更大的贴图，`clipSize` 也不会更新。请手动分配它。
- 许多 consumer 类型无法用于并非为支持它们而设计的方块。一般来说，如果它没有在原版中使用，很可能就没有得到良好支持。
- 建筑大小不能被重新分配，因为这会灾难性地破坏存档，而且对大多数运输方块完全不起作用。
- 依赖其他值的值不会被重新分配。例如，更改方块的物品建造需求*不会*像在模组中那样更改其建造时间。
- 环境（静态）方块不能使用环境图集页之外的纹理。换句话说，你可以让草使用雪的贴图，但不能让草使用路由器的贴图；它会在游戏内显示错误纹理。
- 应用补丁后不会重新加载纹理。例如，如果你更改 `suffix` 或 `name` 等 `DrawRegion` 属性，它不会产生任何效果，因为 `load` 不会再次被调用。请改为创建一个全新的对象。
- 重新分配单位/建筑的生命值不会更新任何现有单位/建筑的当前生命值。如果你提高某个方块的最大生命值，地图上所有*现有*的该类型建筑都会看起来受损。
- 补丁很可能导致游戏崩溃或冻结。如果发生这种情况，请报告它，但请记住，我可能无法修复*所有*这类问题——请保持合理。形如“我让这个单位生成 9 万亿发子弹，然后我的游戏卡死了”的错误报告会被忽略。

# 更多示例

## 'Duoification（双管化）'

```json5
//再次说明，名称是可选的，但有助于在列表中识别补丁集
name: Duofication

item: {
  //裂变产物（fissile-matter）是一个未使用的物品，因此用它来演示
  fissile-matter: {
    //将物品的显示名称改为 'Duo'（双管的英文名）
    localizedName: Duo
    //取消隐藏它
    hidden: false
    //将游戏内图标改为 'duo-preview'，它由双管（duo）炮塔使用
    fullIcon: duo-preview
    //将 UI 中的图标改为 'block-duo-ui'，它也由 UI 中的双管（duo）炮塔使用
    uiIcon: block-duo-ui
  }
}

block: {
  //编辑粉碎机（pulverizer）
  pulverizer: {
    //更改其名称
    localizedName: Duo Factory
    //重写它消耗的内容
    consumes: {
      //移除所有先前的消耗项——如果没有这一行，它会保留旧的废料（scrap）消耗
      //你也可以通过写入 `remove: items` 来*仅*移除物品消耗项
      remove: all
      //每次制作消耗 1 个铜（copper）物品
      item: copper
    }
    //更改 UI 显示图标
    uiIcon: block-duo-ui
    //更改 region
    region: block-duo-full
    //输出 1 个裂变产物（fissile-matter），它之前已被补丁改为名称 'Duo'
    //注意 outputItems 是数组，因此其内容必须写为带 [ 和 ] 的列表
    outputItems: [fissile-matter/1]
    //定义 drawers，它们决定方块如何渲染。它们可以定义为带 [] 的数组
    drawer: [
      {
        //第一个 drawer 是简单的 DrawRegion，它绘制贴图 'block-1'，即 1x1 塞普罗（Serpulo）炮塔的底座
        type: DrawRegion
        name: block-1
      }
      {
        //第二个 drawer 绘制 'duo-preview' region，并以速度 1 旋转它
        type: DrawRegion
        rotateSpeed: 1
        name: duo-preview
      }
    ]
  }

}

unit: {
  //为尖刀（dagger）单位打补丁
  dagger: {
    //将其 body region 改为 duo-preview
    region: duo-preview
    //重新定义 weapon 数组（注意：这会清除所有先前武器）
    weapons: [
      //数组中的所有武器都是自己的对象，因此需要用 {} 花括号包裹
      {
        //武器位于单位中心
        x: 0
        y: 0
        //20 ticks 的 reload（1 秒 = 60 ticks）
        reload: 20
        //以 3.5 世界单位的散布在左右之间交替（1 个图块 = 8 世界单位）
        shoot: {
          type: ShootAlternate
          spread: 3.5
        }

        //定义该武器发射的子弹
        bullet: {
          //贴图在世界单位中的宽度和高度
          width: 7
          height: 9
          //以 ticks 计的 lifetime（1 秒）
          lifetime: 60
          //以十六进制代码表示的子弹颜色
          frontColor: eac1a8
          backColor: d39169
        }
      }
    ]
  }
}
```

## 修改炮塔弹药

```json5
block.fuse.ammoTypes: {
  //使用特殊值 "-" 从 ammo map 中移除钛（titanium）弹药
  titanium: "-"
  //添加会发射激光的巨浪合金（surge alloy）弹药
  surge-alloy: {
    type: LaserBulletType
    //让它每个弹药物品产生 1 次射击
    ammoMultiplier: 1
    //让它的射击速度减半
    reloadMultiplier: 0.5
    damage: 100
    //让它看起来很糟糕！
    colors: ["000000", "ff0000", "ffffff"]
  }
}
```

## 添加单位能力

```json5
//向恒星（pulsar）添加一个新能力（注意 .+）
unit.pulsar.abilities.+: [
  {
    type: ForceFieldAbility
    //将力场的最大生命值设为 1000
    max: 1000
  }
]

```

## 添加单位计划

```json5
//让陆军工厂（ground factory）生产星辉（flare）
block.ground-factory.plans.+: {
  unit: flare
  //需要 10 个巨浪合金（surge alloy）来建造
  requirements: [surge-alloy/10]
  //需要 100 ticks 来建造
  time: 100
}
```

## 修改单位工厂计划

```json5
//让尖刀（dagger，陆军工厂的第一个计划，也就是索引 0）需要 60 ticks 来建造，即 1 秒
block.ground-factory.plans.0.time: 60
```

## 修改建筑需求

```json5
//让双管（duo）消耗 5 个钛（titanium）和 20 个巨浪合金（surge alloy）
block.duo.requirements: [titanium/5, surge-alloy/20]
```
