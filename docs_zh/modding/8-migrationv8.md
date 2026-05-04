# 8.0 迁移指南

本指南尚不完整。由于 v8 尚未完全发布，它会持续变化，直到 v8 完全稳定。

## JSON 模组

如果你有一个 JSON 模组，你*大概*不需要做任何事。所有现有 JSON 模组应该仍能正常工作，尽管某些星球上的内容显示方式会有一些变化。请参见下面的“星球”章节。

## Java/JS 模组

## 杂项

- `Binding` 键位绑定值现在使用 camelCase。
- 旧的键位绑定系统已完全重做，以允许自定义模组键位绑定——请参见 `arc.input.KeyBind#add`。`Core.keybinds` 已移除，请改用 `Keybind` 类。
- 调用 `Core.atlas.getPixmap` 时，如果位于 `createIcons` 之外，则不再被允许。如果你的内容需要生成图标，请通过重写 `createIcons` 来完成。否则，你不能访问已打包数据的图片数据；它曾是一个巨大的内存泄漏。

## 方块

- 大多数不必要的“getter”方法（例如 `void tile(Tile), Tile tile(), block()`）已从 `Building` 移除。本来就没有理由使用这些方法，但如果你的模组恰好这样做了，你需要改为直接访问字段。
- 方块现在有一个单独的 `lightClipSize` 字段，用于 `drawLight()` 尺寸裁剪。现在必须将 `emitLight` 设为 true，才会调用此方法。
- `loopSound` 已移除；循环音效必须在每个方块的 `Building` 中手动创建和更新。示例请参见 `Turret` 源代码。

## 单位

- `Player#unit()` **现在可以为 null。** 在访问单位之前，请确保检查 `!player.dead()`。
- `Units.null` 已移除。
- 指令现在是内容。`UnitCommand.all` 已移除。
- 单位指令现在是 `Seq`，而不是数组。

## 星球

- 所有与物品可见性相关的字段（`itemWhitelist`、`hiddenItems`、`Rules.hiddenBuildItems`）都已移除。要让内容在星球上显示，请修改其 `shownPlanets` 字段。如果你已经为某个星球设置了科技树，这会自动完成。
