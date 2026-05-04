# 7.0 迁移指南

## 方块

- `Block#expanded` 现在已弃用且不执行任何操作，请改用 `Block#clipSize`。该字段被保留以确保兼容性，但最终会被移除。
- 所有 `mindustry.world.meta.values.*` 类都已替换为 lambda。请参见 `StatValues` 类。
- `BlockForge` 已从 experimental 包移出，并且很可能会经历重大变更。如果你在 Java 模组中使用了这个类，我建议把它复制粘贴到你的模组中，这样你就可以继续使用旧版本。其他实验性方块也可能会被移动。
- `CacheLayer` 现在是一个带有可重写方法的类，而不是枚举。可以使用 `CacheLayer#add` 注册新图层。
- `variants` 和 `attributes` 等多个字段已从 `Floor` 移动到 `Block`。
- `Iconc` 和相关方法已移除；请使用 `UnlockableContent.uiIcon/fullIcon`。
- `Smelter` 和 `AttributeSmelter` 已弃用。这些类有硬编码的绘制功能。请尽快迁移到 `GenericCrafter`，并为其使用 `DrawSmelter`。若需要属性支持，请使用 `AttributeCrafter`。
- `Cultivator` 出于与 `Smelter` 相同的原因已弃用，请改用 `AttributeCrafter`。
- `ExtendingItemBridge` 和 `LiquidExtendingBridge` 已与 `ItemBridge` / `LiquidBridge` 合并，请改用后者。
- `PayloadAcceptor` 是一个位于错误包中的误导性名称，请改用 `PayloadBlock`。
- 生成的图标现在**必须**在 `createIcons` 中创建；尝试使用 `Core.atlas.addRegion` 根本不会生效。
- `LiquidModule#total()` 已弃用；请改用 `currentAmount()`。

## 弹药

- 任何处理单位弹药的模组代码现在都已损坏。
- `ResupplyPoint` 类已移除。
- `AmmoType` 现在是接口，而不是类。
- `AmmoTypes` 已移除，请改为创建新实例。
- 弹药类型类已移动到 `mindustry.type.ammo` 包中。
- `ContentType.ammo` 已被“移除”，因为弹药不再是内容。

## Arc

- `Pixmap` 的 API 已完全改变。大多数方法现在默认禁用混合，颜色/混合/缩放参数也不再是 `Pixmap` 状态机的一部分。大多数与图片相关的方法现在都是纯 Java 实现，而不是 JNI + C。
- `SettingsDialog`（`Vars.ui.settings`）已移动到 Mindustry 的代码库中。从技术上说这不会改变 API；然而，用 6.0 源码编译的 Java 模组会尝试访问一个不存在类中的不存在字段，从而导致崩溃。使用 v7 Mindustry/arc 依赖重新编译应该足以修复此问题。
- TextureAtlas 现在使用更小、更快的 `aatls` 二进制格式。请更新你的 Arc 依赖以读取它。
- `Core.net` 已移除，请改用 `arc.util.Http` 中的静态方法。
- `RidgedPerlin` 已重命名为 `Ridged`。
- `Simplex` 和 `Ridged` 现在是无状态的；现在请使用静态方法生成噪声。种子是一个参数。

## 网络

- 数据包的 `Registrator` 已移动到 `Net`，注册方法也已公开，以便 Java 模组潜在使用。
- `InvokePacket` 已移除，并替换为直接处理事件的生成数据包类。
- `RemoteRead{Server, Client}` 也已移除。
- `Packet` 现在是抽象类，而不是接口。

## 杂项

- `BulletType#despawned` 在许多情况下不再被调用；如果你需要监听所有移除事件，请使用 `#removed`
- `Attribute` 现在是标准类，而不是枚举。请使用 `Attribute.add` 注册新的属性。
- `Vars.miningRange` 已移动到 `UnitType`。
- `Tex` 中的所有字段现在都是 `Drawable`，而不是 `NinePatchDrawable` 或 `TextureRegionDrawable`。为什么？这些字段从图集中加载，这意味着修改 UI 贴图的模组或过时图集过去可能会导致 `ClassCastException` 崩溃。

## 贴图

- 现在会自动为单位和武器贴图生成描边。腿部区域目前例外。
- 启用线性过滤时，现在所有模组贴图都会在加载时自动进行 alpha bleed，因此不需要手动处理。
