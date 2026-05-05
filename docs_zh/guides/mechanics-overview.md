# Mindustry 当前源码机制总览

> 适用版本：当前 Wiki 生成流程使用的 Mindustry 源码。本文件不是泛泛而谈的百科，而是把源码里的关键规则翻译成玩家可操作的理解框架。

## 1. 战役有两个实际主战场：Serpulo 与 Erekir

源码中 `Planets.load()` 定义了多个天体，但当前实际可作为战役推进主体的是：

- **Serpulo**：`alwaysUnlocked = true`，`allowWaves = true`，允许扇区入侵、允许发射蓝图与发射资源、允许传统发射台/发射物流，并允许自星球编号区块发射；默认敌队为 `Team.crux`。见 `Planets.java` 中 Serpulo 配置（`allowWaves`、`allowSectorInvasion`、`allowLaunchSchematics`、`allowLaunchLoadout`、`allowSelfSectorLaunch` 等）。
- **Erekir**：`alwaysUnlocked = true`，默认核心为 **城堡核心**，默认环境是灼热陆地，开启雾、静态雾、显示出生点、RTS AI；规则里 `onlyDepositCore = true`，且 `allowLaunchToNumbered = false`，所以它更像一组线性/半线性攻坚谜题，而不是 Serpulo 式的大规模编号区块扩张。见 `Planets.java` 的 Erekir 配置。
- **Tantros** 当前 `accessible = false` 且 `visible = false`；若玩家问“通关后去 Tantros 吗”，按当前代码不能把它当作可玩战役内容。几个小行星也是 `accessible = false`。

**攻略含义**：新手优先从 Serpulo 的零号地区建立基本自动化；Erekir 虽然一开始也可进入，但雾、玩家手动投放限制、热量/气体链条让它更适合已懂物流后再推进。

## 2. 区块胜利条件：波次、防守、攻坚、混合

区块不是只有一种胜利方式。源码里的判断集中在 `Sector`、`SectorPreset`、`Logic.checkGameState()` 和 `Logic.sectorCapture()`：

- **有 `captureWave` 的命名区块**：到达指定波次且场上没有剩余敌人后会占领。例：零号地区 10 波，冰冻森林 15 波，陨坑战场 20 波，焦油田 40 波。
- **没有 `captureWave` 的命名区块**：`Sector.hasEnemyBase()` 会把它视作敌方基地攻坚；需要摧毁敌方核心/使敌队不再存活。
- **混合区块**：如 Erekir 的交错丘陵 `intersect` 有 `captureWave = 9` 且 `attackAfterWaves = true`，波次结束后会切到攻坚模式。
- **战役占领事件**：`sectorCapture()` 会关闭 waves/attackMode、标记 `wasCaptured`、保存区块；若该区块是本星球 `isLastSector` 且初次占领，会弹出通关对话。

**攻略含义**：

- 波次图要“守到 winWave”；攻坚图要“摧毁核心”。不要用纯防守思维打 Salt Flats/Frontier 这类攻坚图。
- 有敌核的图里，破核心后代码会按星球规则处理清场/占领，因此突击核心是有效目标。

## 3. 难度不是一句话，而是多层叠加

源码里至少有三种“难度相关”概念：

1. **区块显示难度**：`SectorPreset.difficulty`，范围 0–10。本文把 4–6 称为“中级难度关卡”。Serpulo 的风吹群岛/工业区 32M/边陲哨站/盐碱荒滩/焦油田等处在这个区间；Erekir 的岩浆湖/交错丘陵/风化山脉/风蚀盆地等也处在这个区间。
2. **战役规则难度**：`Difficulty` 枚举影响敌人血量、敌人生成速度、波次时间倍率：casual、easy、normal、hard、eradication 分别设置不同倍率。
3. **程序生成威胁**：Serpulo 生成器按区块威胁计算 winWave 与 waveSpacing；敌基邻近还会提高威胁。

**攻略含义**：当你卡关时，不只看“区块难度 7/10”；还要看是否被敌基包围、是否开了高战役难度、是否是攻坚图。

## 4. 科技树/研究树实际由“父节点 + 额外目标 + 产出解锁”组成

`TechTree.TechNode` 把研究拆成几层约束：

- 必须研究父节点。
- 额外目标可能要求 `SectorComplete`（占领某区块）、`OnSector`（在某区块有基地）、`OnPlanet`（在某星球有基地）、`Produce`（产出某资源）或 `Research`（先研究某内容）。
- 如果科技节点挂在一个区块节点下面，代码会自动插入“完成该区块”的要求。

**Serpulo 的关键科技门槛示例**：

- 冰冻森林后解锁气动钻头和硅冶炼相关路线。
- 陨坑战场后解锁钛传送带、火成玻璃链、火力/水强化、冰雹等中期要件。
- 风吹群岛后推进塑钢压缩机、脉冲导管、海军支线。
- 萃取前哨后解锁高级发射台；行星发射终端后才接到行星际加速器研究节点。

**Erekir 的关键科技门槛示例**：

- Erekir 根节点是城堡核心，且根节点要求进入该星球后才能有效展开。
- 庇护前哨后能拿到冲击钻头、通风冷凝器、强化管线、溢流管道等。
- 风化山脉/风蚀盆地后开始电解、重构与更完整的液体链。
- 贫瘠峡谷、破碎火山、平行岭谷、岩溶洞穴逐步打开热量、氰气、碳化物、相织物、五级炮塔与 T4/T5 单位链。

## 5. 资源经济：核心容量、区块后台、发射物流

源码里的资源系统不是“当前地图唯一仓库”：

- **核心容量**：Serpulo 初代/次代/终代核心分别是 4000/9000/13000 物品容量；Erekir 的城堡/堡垒/卫城核心分别是 2000/3000/4000 物品容量，但血量与护甲明显更高。
- **离线区块生产**：`Universe.runTurn()` 每个战役 turn 会把未受攻击、未被当前游玩的区块的生产统计加入该区块库存；受攻击的区块会被冻结。
- **Serpulo 传统发射物流**：旧发射台或高级发射台会把物品送往 `sector.info.destination`，后台按生产/出口统计导入目标区块。
- **新式高级发射台 + 着陆台**：高级发射台需要装满 100 物品并消耗油和电；着陆台按指定物品、导入速率和冷却接收，每次填满 100 物品，需要大量水冷却。
- **发射载荷**：Serpulo 的发射资源容量由 `planet.launchCapacityMultiplier * core.itemCapacity` 决定；Serpulo 将倍率设为 0.5，因此次代核心/终代核心可以携带更多开局资源。

**攻略含义**：中后期不应每张图从零开始。你应该把安全区块变成“后勤省”，用高级发射台把硅、钛、钍、巨浪合金、相织物、塑钢发往前线。

## 6. Serpulo 的编号区块扩张有“次代核心门槛”

`SerpuloPlanetGenerator.allowNumberedLaunch()` 要求发射来源有基地、未受攻击，并且最佳核心尺寸至少 4；次代核心 `coreFoundation` 的 `size = 4`，因此 UI 才会提示“需要次代核心”。

**攻略含义**：占领周边编号区块前，不要只靠初代核心硬扩张；先研究并建造/携带次代核心级别载荷，才能可靠展开编号区块网络。

## 7. 单位体系：Serpulo 是工厂 + 重构，Erekir 是制造 + 重构 + 装配

- **Serpulo**：地面、空军、海军工厂产 T1；数增/倍乘/指数/迭代重构工厂把单位从 T1 升到 T5。每级重构需要大量硅、钛、塑钢、相织物、巨浪合金和冷冻液。
- **Erekir**：坦克/飞船/机甲制造厂先产 Stell/Elude/Merui；再用对应重构厂升级；后期单位装配厂要吃若干基础单位与墙块 payload，并消耗氰气。
- **单位上限**：`Units.getCap()` 使用规则基础上限 + 队伍建筑给的 `unitCapModifier`。核心给单位上限；敌波队在战役/非 PvP 下没有普通玩家单位上限。

**攻略含义**：攻坚图不要只堆炮塔。Serpulo 需要用单位拆核心；Erekir 许多关卡地图空间和雾设计就是鼓励边侦察边生产合适兵种。

## 8. 电力/液体/热量是三套不同的瓶颈

- Serpulo 早期是煤电、蒸汽、热能、差分、钍反应堆、冲击反应堆逐层升级。冷冻液与水既能给钻头/炮塔加速，也支撑反应堆和重构。
- Erekir 早期依靠涡轮冷凝器和蒸汽 vent；中期进入电解水产氢/臭氧、氧化、热量传导、炉类；后期有氰气、碳化物、相织物和高热炮塔。
- Erekir 的热量不是普通液体：热源、热导向器、热路由器等按相邻方向传递；高阶炮塔如魔灵需要大量热量才能满效率。

**攻略含义**：

- Serpulo 防线缺电时先稳电网，再加炮塔；不然蓝瑟、厄兆等高耗电炮塔会“摆着不开火”。
- Erekir 后期别把热量链当电线拉，热量布局要短、直、少分叉；热源生产点应贴近耗热点。

## 9. 本攻略集的读者分层

- **新手**：重点学会“矿 → 传送带/管道 → 加工 → 核心/炮塔/研究”的闭环，完成 Serpulo 早期命名区块，并能进入 Erekir 起步。
- **已完成中级难度关卡**：重点学会后勤、跨区、攻坚单位、区块选择、冷却/电力冗余、Erekir 热量链。
- **剧情通关玩家**：重点转向全图征服、隐藏区块、规则挑战、蓝图标准化、极限难度与自定义玩法。

## 源码索引

- 星球可访问性与规则：`core/src/mindustry/content/Planets.java`
- 区块难度/最终区块：`core/src/mindustry/content/SectorPresets.java`
- 胜负判断：`core/src/mindustry/core/Logic.java`
- 区块状态/敌基判断：`core/src/mindustry/type/Sector.java`
- 研究目标：`core/src/mindustry/game/Objectives.java`、`core/src/mindustry/content/TechTree.java`
- 战役 turn、入侵、离线生产：`core/src/mindustry/game/Universe.java`、`core/src/mindustry/Vars.java`
- 发射台/着陆台：`core/src/mindustry/world/blocks/campaign/LaunchPad.java`、`LandingPad.java`
- 方块数值：`core/src/mindustry/content/Blocks.java`
