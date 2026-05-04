# 6.0 迁移指南

如果你是 5.0 的插件或模组开发者，你可能已经注意到你的内容在 6.0 中不再能正常工作。
这是由于大量内部变更和新增内容造成的，本文会对其进行说明。

## 常规变更

### 最低游戏版本

现在所有模组都必须指定值为 "105" 或以上的 `minGameVersion` 才能被加载。这是为了确保过时模组不会被加载。
只需添加 `minGameVersion: "$latestRelease"` 到你的 `mod.hjson` 文件中。

## 名称变更

### 变量和类名变更

`ItemTurret`：

- `ammo` -> `ammoTypes`
- `reload` -> `reloadTime`

`ArtilleryTurret`、`BurstTurret`、`ChargeTurret`：

- 已移除。请改用 `ItemTurret` 或 `PowerTurret`；所有功能都已合并进基类。

`BasicBulletType`：

- `bulletWidth` -> `width`
- `bulletHeight` -> `height`
- `bulletSprite` -> `sprite`

### TileEntity -> Building

`TileEntity` 现在是 `Building`。
因此，以前 `TileEntity` 的函数，以及任何与其相关的函数（包含或提到 "entity"）都已重命名；现在它们会把 `TileEntity` 称为 "building" 或 "build"。`Tile.entity` 已重命名为 `Tile.build`，所有 `TileEntity` 实例（例如 `RouterEntity`、`ConveyorEntity`）都被重命名为以 "Build" 后缀结尾（例如 `RouterBuild`、`ConveyorBuild`），这里只举几例。

许多函数，如 `draw()` 或 `placed()`，已经从在 `Block` 中声明移动到在 `Building` 中声明。这意味着这些函数不再传入 `Tile`，也让方块专属行为不那么复杂。特别是，`update(Tile tile)` 已被移动到 `Building` 并重命名为（严格来说并非完全如此，但移植时可以忽略这个细节）`updateTile()`。

### `Array<T>` -> `Seq<T>`

`arc.struct.Array` 已重命名为 `arc.struct.Seq`，这是 `Sequence` 的缩写。

为什么？

- 这样更准确。这个数据结构不是数组，而是类似 `ArrayList` 的列表。
- 它不会与其他名为 `Array` 的类冲突，例如 Java 反射 API 中的类或 Javascript 的数组。
- 名字更短，这很好。

### mindustry.plugin.Plugin -> mindustry.mod.Plugin

`Plugin` 类已移动到 `mod` 包中，因为旧包本来也只包含一个类。

### 移除 Call 方法的 "on" 前缀

`Call` 中所有远程调用方法都移除了 "on" 前缀。例如：

- `onSnapshot` -> `snapshot`
- `onSetRules` -> `setRules`
- `onLabel` -> `label`

### 新玩家系统

现在玩家控制单位，他们不再作为有形实体存在于游戏中——也就是说，他们没有生命值或武器。所有动作都由 `Unit` 执行。不再有 `Mech` 类，只有 `UnitType`。

- 每个单位都有一个 `UnitController`，它可以是 AI、逻辑或玩家。
- 要检查某个单位是否由玩家控制，请使用 `unit.isPlayer()`
- 要获取某个单位的玩家（如果有），请使用 `unit.getPlayer()`
- 设置玩家的位置不会产生任何效果。请改为设置单位的位置。
