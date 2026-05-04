# 绘制贴图

绘制贴图是 Mindustry 模组制作中必不可少的一环；如果没有贴图，你制作的任何内容都会显示为缩放很差的“oh no”图片。

Mindustry 的贴图风格简单，但限制很强；在其他游戏里可行的画法，在 Mindustry 中会显得格格不入。

你可以在[这里](https://github.com/Anuken/Mindustry/tree/master/core/assets-raw/sprites)找到所有原版贴图。

**请注意，未经其他模组作者许可使用他们的贴图是不允许的，但你可以将其用作灵感或参考。**

**诸如“这个模组是开源的，所以我想怎么用就怎么用”之类的理由不会被接受或容忍，你的模组也会被模组浏览器列入黑名单。**

## **贴图绘制软件**
强烈建议使用支持透明度并能导出 `.PNG` 格式图片的贴图绘制软件。下面是推荐软件列表。

### **桌面端**

  1. **[Aseprite](https://www.aseprite.org/)**
    - 黄金标准。它有一点学习曲线，但一旦习惯就非常简单。
    - 它是**付费**软件，但你可以**[自行编译源代码](https://github.com/aseprite/aseprite/blob/main/INSTALL.md#compiling)**。请购买许可证以支持其开发者。
      - 它有许多对绘制 Mindustry 贴图有用的功能，例如：
         - 镜像
         - 调色板控制
         - 动画
         - 图层（也可以导出单独图层）
  
  2. **[LibreSprite](https://libresprite.github.io/#!/)**
      - Aseprite 仓库的一个分支，没有 Aseprite 那么新、那么强大，但用于绘制 Mindustry 风格贴图应该足够。
  
  3. **[Piskel](https://www.piskelapp.com/)**
      - 一款简单直接的像素画软件，不如 Aseprite 或 LibreSprite 强大，但已经够用。它有在线版本和可下载的离线版本，二者功能相同。
      - 无法导出单独图层

  4. **[Pixilart](https://www.pixilart.com/)**
      - 一个在线贴图绘制工具，功能比 Piskel 更多，但缺少镜像工具。如果你更熟悉 Pixilart，就用它而不是 Piskel。
      - 对于绘制 Mindustry 风格贴图来说有些臃肿。

  5. **[Paint.NET](https://www.getpaint.net/)**
      - 非常基础的绘图软件，不要与 Paint 3D 混淆。Paint&#46;NET 可以使用，但不如上面提到的软件方便。
      - Paint&#46;NET 缺少绘制 Mindustry 风格贴图所需的一些基础功能。你可以通过插件补足其中一部分缺失功能。
      - 话虽如此，出于便利性考虑，不建议使用它。如果你能下载 Paint&#46;NET，那么你大概也能下载更适合像素画的 Piskel 或 LibreSprite。

### **移动端**
1. **[Novix Pixel Editor](https://play.google.com/store/apps/details?id=io.anuke.novix)**
     - 古老但可靠，由 Anuke 制作后放弃维护。它很简单、没有广告；虽然有些老，但作为移动用户的贴图绘制工具仍然可靠，并且支持镜像工具。
     - 绘制较大的贴图时偶尔会出问题。
  
2.  **[Pixel Studio](https://play.google.com/store/apps/details?id=com.PixelStudio)**
    - 最受欢迎的像素画软件之一。
    - 拥有你所需的大多数功能，并且还可以与它的 PC 版本联动。
    - 有广告

3. **[Ibispaint X](https://play.google.com/store/apps/details?id=jp.ne.ibis.ibispaintx.app)**
    - 并非专为绘制贴图而设计，使用前需要调整一些设置。
    - 支持八向镜像、泛光、渐变等多种工具，也有区域选择和图层等基础功能。
    - 可以轻松绘制复杂贴图，但对简单贴图来说可能过于臃肿。
    - 也有广告

## **尺寸**
### 方块
你能制作的最小方块贴图是 `32px × 32px`，也就是 1×1 方块。制作更大的方块意味着贴图尺寸每次额外增加 `32px`，所以 2×2 方块是 `64 × 64`，以此类推。这同时适用于炮塔和方块。

- `1×1` : `32px × 32px`
- `2×2` : `64px × 64px`
- `3×3` : `96px × 96px`
- `4×4` : `128px × 128px`
- `5×5` : `160px × 160px`

你并不局限于这些尺寸；游戏仍会加载比推荐尺寸更大或更小的贴图，这可能会产生外观独特的贴图，也可能会产生惨不忍睹的结果。

### 物品、液体、状态
对于这些内容类型，最小贴图尺寸是 `32px`；你可以使用更大的图片，但游戏会把它们压缩到 `32px`。游戏不会放大小于该尺寸的图片，因此 `32px` 是最小值。

### 单位
单位贴图的尺寸要求比其他内容宽松一些，不过尽量不要低于 `48px`。单位越大，你就越需要调整它们的 `hitSize`（碰撞箱大小）。

## **存放贴图**
如果你的模组是 hJSON 模组，贴图可以放到模组的 `sprites/` 子目录；如果是 Java 模组，则放到 `src/assets/sprites/`。内容解析器会递归查找其中的文件。

图片会被打包进一个“图集”（atlas）以便高效渲染。sprites/ 下的第一个目录，例如 `sprites/blocks`，决定贴图会被放入图集中的哪个页面。把方块贴图放进 units 文件夹很可能导致大量卡顿；因此，你应该尽量像原版游戏那样组织文件。

游戏会根据内容名称查找贴图。`content/blocks/test-turret.json` 的名称是 `test-turret`，同样地，`sprites/test-turret.png` 的名称也是 `test-turret`，因此它会被该内容使用。
- 方块应存放在 `sprites/blocks`
- 单位应存放在 `sprites/units`
- 物品应存放在 `sprites/items`

游戏会修改某些贴图。炮塔和单位会被添加 `3-4px` 的灰色描边，因此你在制作贴图时必须预留这部分空间，在炮塔周围留出空隙。默认描边半径和颜色可以通过修改 `outlineRadius` / `outlineColor` 字段来自定义，这些字段位于 `Block` 和 `UnitType` 类中。

### 覆盖

可以覆盖已有贴图；为此，贴图必须放在 `sprites-override/`。

<a id="suffixes"></a>

## **后缀**
游戏也可以为单个方块查找多个贴图。

对于炮塔，游戏可能会查找后缀 `<name>-heat`（`test-turret-heat.png`）。

对于方块和制作器/冶炼器，游戏可能会查找 `<name>-top` 和 `<name>-liquid`，这些会在对应章节中说明。

你可以阅读各个方块类的源代码，了解它们能加载哪些贴图的更多细节。请查看带有 `@Load` 的行。
对于模组中的贴图，如果方块类中有此方法，请检查方块类中的每个 `load()` 方法。

## **调色板**

和每个游戏一样，Mindustry 也有自己的调色板。对于初学者，强烈建议你的贴图坚持使用这些特定颜色，否则最好也会显得不协调，最坏甚至会变得异端。这可能会给 Discord 的 #spriting 频道带来巨大困扰。

方块调色板：

<img src="/wiki/images/modding/spriting/pal-mindustry.png">

环境调色板

<img src="/wiki/images/modding/spriting/pal-mindustry-evn.png">

假设你已经正确获得了合适的贴图绘制软件，你应该能够下载这些图片并将它们用作调色板。

## **风格和阴影**

Mindustry 的美术风格简单但限制很强。对其他游戏可行的画法，在 Mindustry 中会显得格格不入。因此，下面建立了一些准则，帮助模组作者创建能融入游戏的贴图。

Mindustry 是 2D 游戏，因此为了添加高度和凹陷等深度，我们需要使用一种叫作“阴影”的技巧。尽管实际资源是一张 2D 图片，这个技巧会让它在游戏中看起来像 3D。

根据光照方向，**凸起**用**较亮色调**表示，**平坦区域**用**中间调**表示，**凹陷**用**较暗色调**表示。先在脑海中想象某个物体的 3D 形态，再将它画成 2D，通常是在 Mindustry 中绘制贴图的好方法。

不过这只是一份准则；如果你还没有成功绘制过 Mindustry 贴图就试图打破它，你很可能会创造出怪物，而 #spriting 频道也不会高兴。

---

### **方块阴影**
![](https://raw.githubusercontent.com/Anuken/Mindustry/master/core/assets-raw/sprites/blocks/production/surge-smelter.png)

我们将以合金冶炼厂（Surge Smelter）为例。

对于方块，光源位于接近**右上**角的位置，阴影在**左下**。右上方靠近光源的像素应使用浅色；同样，右下方的像素应使用深色。最好让一条穿过中间的对角线把它们分开。

大多数方块有 3 种颜色类型：

  - 基础色，有 3 种明暗：
    
    - ![](https://via.placeholder.com/15/B0BAC0/000000?text=+) `B0BAC0` | 亮色调
    - ![](https://via.placeholder.com/15/989AA4/000000?text=+) `989AA4` | 中间调
    - ![](https://via.placeholder.com/15/6E7080/000000?text=+) `6E7080` | 暗色调
  
  - 贴花色，也有 3 种明暗：
    
    - ![](https://via.placeholder.com/15/feb380/000000?text=+) `FEB380` | 亮色调
    - ![](https://via.placeholder.com/15/ea8878/000000?text=+) `EA8878` | 中间调
    - ![](https://via.placeholder.com/15/bc5452/000000?text=+) `BC5452` | 暗色调
   
  - 底部颜色
    
    - ![](https://via.placeholder.com/15/4a4b53/000000?text=+) `4a4b53`

**基础色**代表方块的主要颜色。建议制作器只使用灰色的不同明暗，因为所有原版制作器都是如此。

**贴花色**是方块上的强调色。它代表方块的**作用**或**用途**，也是区分不同方块的一种方式。要选择方块应使用什么贴花色，你应该思考方块的用途。例如：

**塑钢压缩机（Plastanium Compressor）**

![Plast-Comp](https://raw.githubusercontent.com/Anuken/Mindustry/master/core/assets-raw/sprites/blocks/production/plastanium-compressor.png) 

塑钢压缩机（Plastanium Compressor）有绿色贴花。这个绿色贴花与塑钢（Plastanium）的颜色相同。因此，只要看一眼，你就能知道这个方块与塑钢有关。

**底部颜色**代表方块内部，即没有光照到的地方，因此它应当非常暗。例如，它可以表示像合金冶炼厂（Surge Smelter）这样带烟囱方块的底部。

请注意，不同方块根据类型不同需要不同数量的图层；例如，墙只需要 1 个图层，也就是贴图本身，而像重构器这样的方块可能需要多达 4 个图层。请参见 [#suffixes](#suffixes)。

模组示例：

  - [DiverseTech](https://github.com/FlinTyX/DiverseTech) 中 Flin#8261 制作的 Unit Bunker
  
    - <img src="/wiki/images/modding/spriting/sprite-examples/flintyx-unit-bunker.png" draggable="false">
  
  - [Unlimited Armament Works](https://github.com/Eschatologue/Unlimited-Armament-Works) 中 Geschiedenis #4783 制作的 Surge Mixer
    
    - ![](https://raw.githubusercontent.com/Eschatologue/Unlimited-Armament-Works/master/assets/sprites/blocks/production/surge-mixer.png)


---

### **炮塔阴影**

对于炮塔阴影，光源在**右侧**，阴影在**左侧**。

![浪涌（Ripple）](https://raw.githubusercontent.com/Anuken/Mindustry/master/core/assets-raw/sprites/blocks/turrets/ripple.png)

这一部分我们将以“**浪涌（Ripple）**”为例。

一般来说，炮塔有 2 到 3 种颜色类型，每种有 2 种色调：

- 基础色

  - ![](https://via.placeholder.com/15/7b7b7b/000000?text=+) `7B7B7B` | 亮色调
  - ![](https://via.placeholder.com/15/4d4e58/000000?text=+) `4D4E58` | 暗色调
  
- 贴花色
  
  - ![](https://via.placeholder.com/15/feb380/000000?text=+) `FEB380` | 亮色调
  - ![](https://via.placeholder.com/15/ea8878/000000?text=+) `EA8878` | 暗色调
  
- [可选] 炮口孔颜色
  
  - ![](https://via.placeholder.com/15/2c2d38/000000?text=+) `2C2D38` 

**基础色**或主体色，是炮塔的主要颜色。它可以是经典的铜棕色、白色、深灰色，或自定义颜色（来自调色板！）。

  - 铜棕色
    - ![](https://raw.githubusercontent.com/Anuken/Mindustry/master/core/assets-raw/sprites/blocks/turrets/duo.png) ![](https://raw.githubusercontent.com/Anuken/Mindustry/master/core/assets-raw/sprites/blocks/turrets/scorch.png) ![](https://raw.githubusercontent.com/Anuken/Mindustry/master/core/assets-raw/sprites/blocks/turrets/hail.png)
    - 通常代表低阶炮塔，例如 **双管（Duo）**、**火焰（Scorch）**、**冰雹（Hail）** 等。
      
      - ![](https://via.placeholder.com/15/c9a58f/000000?text=+) `C9A58F` 
      - ![](https://via.placeholder.com/15/8f665b/000000?text=+) `8F665B` 
  
  - 白色
    
    - ![电弧（Arc）](https://raw.githubusercontent.com/Anuken/Mindustry/master/core/assets-raw/sprites/blocks/turrets/arc.png) ![蓝瑟（Lancer）](https://raw.githubusercontent.com/Anuken/Mindustry/master/core/assets-raw/sprites/blocks/turrets/lancer.png) ![差扰（Parallax）](https://raw.githubusercontent.com/Anuken/Mindustry/master/core/assets-raw/sprites/blocks/defense/parallax.png) ![裂解（Segment）](https://raw.githubusercontent.com/Anuken/Mindustry/master/core/assets-raw/sprites/blocks/defense/segment.png)
    - 通常代表使用电力而不是物品射击的炮塔，例如 **电弧（Arc）**、**蓝瑟（Lancer）**、**差扰（Parallax）**、**裂解（Segment）**。
  
      - ![](https://via.placeholder.com/15/f4f4f4/000000?text=+) `F4F4F4` 
      - ![](https://via.placeholder.com/15/c1c3d4/000000?text=+) `C1C3D4`
  
  - 深灰色
    
    - ![蜂群（Swarmer）](https://raw.githubusercontent.com/Anuken/Mindustry/master/core/assets-raw/sprites/blocks/turrets/swarmer.png) ![气旋（Cyclone）](https://raw.githubusercontent.com/Anuken/Mindustry/master/core/assets-raw/sprites/blocks/turrets/cyclone.png) ![熔毁（Meltdown）](https://raw.githubusercontent.com/Anuken/Mindustry/master/core/assets-raw/sprites/blocks/turrets/meltdown.png)
    - 在大多数情况下，深灰色代表中高阶炮塔。
      
      - ![](https://via.placeholder.com/15/7b7b7b/000000?text=+) `7B7B7B` 
      - ![](https://via.placeholder.com/15/4d4e58/000000?text=+) `4D4E58` 

炮塔中的**贴花色**与普通方块相同；它是一种强调色，可以代表炮塔的作用、用途或原型。例如，如果你想把炮塔分成不同类别，就可以通过贴花色来区分它们。

**炮口孔**是炮塔的一种可选颜色，用来表示炮塔的炮口孔；这通常用于火炮炮塔或导弹发射器。

![蜂群（Swarmer）](https://raw.githubusercontent.com/Anuken/Mindustry/master/core/assets-raw/sprites/blocks/turrets/swarmer.png) 
![浪涌（Ripple）](https://raw.githubusercontent.com/Anuken/Mindustry/master/core/assets-raw/sprites/blocks/turrets/ripple.png)

  - ![](https://via.placeholder.com/15/2c2d38/000000?text=+) `2C2D38` 

#### 非常规方法

  - **炮塔中间调**
    
    - 一种仍然相对较新的非常规方法，是在炮塔贴图中加入中间调，让它看起来有平坦表面，而不只是亮色调和暗色调。
    
    - 其中一个例子是 [Unlimited Armament Works](https://github.com/Eschatologue/Unlimited-Armament-Works) 中的“Skyhammer”
      
      - ![Skyhammer](https://github.com/Eschatologue/Unlimited-Armament-Works/blob/master/assets/sprites/blocks/turrets/artillery/skyhammer/skyhammer-preview.png?raw=true)

---

### **资源阴影**
资源阴影相当简单，光照可以来自**顶部角落**、**从上到下**或**从右到左**。

资源贴图只应使用同一种颜色的 2 或 3 种明暗。确保贴图看起来是 3D 而不是扁平的，否则它会像纸片一样突兀。

示例：

![](https://raw.githubusercontent.com/Anuken/Mindustry/master/core/assets-raw/sprites/items/item-copper.png)
![](https://raw.githubusercontent.com/Anuken/Mindustry/master/core/assets-raw/sprites/items/item-plastanium.png)
![](https://raw.githubusercontent.com/Anuken/Mindustry/master/core/assets-raw/sprites/items/item-graphite.png)
![](https://raw.githubusercontent.com/Anuken/Mindustry/master/core/assets-raw/sprites/items/item-coal.png)
![](https://raw.githubusercontent.com/Anuken/Mindustry/master/core/assets-raw/sprites/items/item-surge-alloy.png)
![](https://raw.githubusercontent.com/Anuken/Mindustry/master/core/assets-raw/sprites/items/item-scrap.png)
![](https://raw.githubusercontent.com/Anuken/Mindustry/master/core/assets-raw/sprites/items/item-pyratite.png)
![](https://raw.githubusercontent.com/Anuken/Mindustry/master/core/assets-raw/sprites/items/liquid-cryofluid.png)

### **单位阴影**
单位通常是最难上阴影的。

对于更大的单位，单位阴影会变得相当复杂。在单位阴影中，光线来自**从上到下**或**从前到后**的方向。亮色调和暗色调的强度会根据你正在处理的单位部位而变化。

对于单位，亮色调代表**凸起**，中间调代表**平坦区域**，暗色调代表**凹陷**。

#### **单位基础色**

<img src="/wiki/images/modding/spriting/spriting-unit-shading.png" draggable="false">

这里使用日蚀（Eclipse）作为示例，因为它是最复杂的原版单位。随着你不断向背面处理，亮色调会越来越少，中间调和暗色调会越来越多。

被光照到的部分会有较亮色调，而没有被照到的部分会有较暗色调；平坦区域则是中间调。

<img src="/wiki/images/modding/spriting/spriting-unit-shading-illustration.png" draggable="false">

上图是把单位想象成 3D 时的粗略示意。

- 基础色，照常有 3 种色调：
  
  - ![](https://via.placeholder.com/15/B0BAC0/000000?text=+) `B0BAC0` | 亮色调
  - ![](https://via.placeholder.com/15/989AA4/000000?text=+) `989AA4` | 中间调
  - ![](https://via.placeholder.com/15/6E7080/000000?text=+) `6E7080` | 暗色调

#### **单位贴花色**

单位贴花色只有 2 种色调：亮色调和暗色调。颜色代表该单位在游戏中的作用。
 
- 黄色代表由核心生产的**核心**单位。
  
  - ![](https://raw.githubusercontent.com/Anuken/Mindustry/master/core/assets-raw/sprites/units/gamma.png) ![](https://raw.githubusercontent.com/Anuken/Mindustry/master/core/assets-raw/sprites/units/beta.png)
    
    - ![](https://via.placeholder.com/15/ffd37f/000000?text=+) `FFD37F` | 亮色调
    - ![](https://via.placeholder.com/15/d4816b/000000?text=+) `D4816B` | 暗色调

- 橙色代表**突击**单位，它们承担攻击对手的角色。
  
  - ![](https://raw.githubusercontent.com/Anuken/Mindustry/master/core/assets-raw/sprites/units/fortress.png) ![](https://raw.githubusercontent.com/Anuken/Mindustry/master/core/assets-raw/sprites/units/horizon.png)
    
    - ![](https://via.placeholder.com/15/ffa665/000000?text=+) `FFA665` | 亮色调
    - ![](https://via.placeholder.com/15/d06b53/000000?text=+) `D06B53` | 暗色调

- 绿色代表可以建造、治疗并保护你的单位的**支援**单位。
  
  - ![](https://raw.githubusercontent.com/Anuken/Mindustry/master/core/assets-raw/sprites/units/poly.png) ![](https://raw.githubusercontent.com/Anuken/Mindustry/master/core/assets-raw/sprites/units/retusa.png)

    - ![](https://via.placeholder.com/15/84f491/000000?text=+) `84F491` | 亮色调
    - ![](https://via.placeholder.com/15/62ae7f/000000?text=+) `62AE7F` | 暗色调

- 紫色代表做其他事情的~~蜘蛛~~**特种**单位。
  
  - ![](https://raw.githubusercontent.com/Anuken/Mindustry/master/core/assets-raw/sprites/units/crawler.png) ![](https://raw.githubusercontent.com/Anuken/Mindustry/master/core/assets-raw/sprites/units/arkyid.png)
    
    - ![](https://via.placeholder.com/15/bf92f9/000000?text=+) `BF92F9` | 亮色调
    - ![](https://via.placeholder.com/15/665c9f/000000?text=+) `665C9F` | 暗色调

你可以自由选择任何喜欢的颜色，只要它出现在多个单位上，并且与调色板中的其他颜色相协调。

#### **单位 Cell/队伍颜色**
单位 Cell 是用于区分不同队伍单位的贴图；它们是单独的贴图，会被加载到单位上方。

<img src="/wiki/images/modding/spriting/spriting-unit-cell.png" draggable="false">

![](https://raw.githubusercontent.com/Anuken/Mindustry/master/core/assets-raw/sprites/units/fortress.png) ![](https://raw.githubusercontent.com/Anuken/Mindustry/master/core/assets-raw/sprites/units/fortress-cell.png)

上图是带有 Cell 的堡垒（Fortress）。游戏会自动把**白色**(#FFFFF) 和**棕褐色**(#DCC6C6) 替换为队伍颜色的不同明暗。你的 Cell 贴图只应包含下面两种明暗：

  - ![](https://via.placeholder.com/15/ffffff/000000?text=+) `FFFFFF` | 亮色调
  - ![](https://via.placeholder.com/15/dcc6c6/000000?text=+) `DCC6C6` | 暗色调

强烈建议使用能够使用图层并分别导出图层的贴图绘制软件，因为你可以在一个文件中把单位本体和 Cell 分别绘制在不同图层上。

#### **单位武器**
单位武器遵循与炮塔和单位阴影相同的规则；它们可以按**从上到下**或**从右到左**来绘制阴影。


![](https://raw.githubusercontent.com/Anuken/Mindustry/master/core/assets-raw/sprites/units/weapons/zenith-missiles.png) 
![](https://raw.githubusercontent.com/Anuken/Mindustry/master/core/assets-raw/sprites/units/weapons/large-artillery.png) 
![](https://raw.githubusercontent.com/Anuken/Mindustry/master/core/assets-raw/sprites/units/weapons/large-laser-mount.png)

武器的旋转基于贴图的中心；如果你想移动武器的旋转点，就必须移动贴图本身。


#### **单位贴图绘制阶段**

<img src="/wiki/images/modding/spriting/spriting-unit-stepbystep.png" draggable="false">
 
绘制单位的过程大致可以分为 5 个阶段：

1. 草绘出总体形状。选择带暗色调的粗画笔来绘制，慢慢叠加线条并形成基本形状，不必太精确。尽量让它们稍微变形或弯曲，并确保形状好看——在大多数情况下，你无法从糟糕的形状做出好的贴图，所以在继续之前请确保自己满意。

2. 细化形状，并用 45 度角的线条构成它。你可能需要调整边缘，而且不要太严格地照着已经画好的草图走。

3. 添加贴花。这一步很棘手，因为贴花很难做好。我展示了 3 个可行的例子——不过你应该自己尝试，看看什么最适合你。最好现在就添加贴花，是因为之后你可以围绕贴花“构建阴影”，让第 5 阶段更容易进行。

4. 粗略标出较亮和较暗的部分。由于光来自上方，你可以而且应该立刻帮自己标出哪些形状最少或最多受到照亮，以免反复纠结。不要覆盖太大面积，因为贴图大约 30-40% 应该是暗色阴影。另外，请注意在贴花周围保留较暗区域，以增强对比度并让它看起来更有吸引力。

5. 迄今为止最复杂的部分——“添加细节”。可用的技巧不多；你必须真正练好。不过我有一个方法：当不确定该添加什么时，就在那里添加 Cell。它们可以像额外贴花一样发挥作用，你也可以围绕它们构建形状。不要添加太多细节，并利用任何方便的角落或板块来雕刻出新的形状。

> 由 Zhenьkotron#9493 编写，Geschiedenis#4783 校对，BalaM314#4781 修正语法。

### **描边**
在炮塔贴图和单位贴图边缘周围留出 4 像素空间，因为游戏会用这部分空间自动添加描边。

---

### **环境贴图**
环境贴图与 Mindustry 其余贴图风格略有不同，其区别在于**不适用 45° 增量规则**。

环境贴图会构成 Mindustry 游戏的大部分甚至绝大多数画面，因此你最好确保自己制作的贴图足够低调，并且即使反复平铺也仍然好看。

#### **地板**
地板只有 2 种色调，变体数量由你决定。

  - 原版示例：
    
    - ![](https://raw.githubusercontent.com/Anuken/Mindustry/master/core/assets-raw/sprites/blocks/environment/basalt1.png) ![](https://raw.githubusercontent.com/Anuken/Mindustry/master/core/assets-raw/sprites/blocks/environment/basalt2.png) ![](https://raw.githubusercontent.com/Anuken/Mindustry/master/core/assets-raw/sprites/blocks/environment/basalt3.png)
    - ![](https://raw.githubusercontent.com/Anuken/Mindustry/master/core/assets-raw/sprites/blocks/environment/dirt1.png) ![](https://raw.githubusercontent.com/Anuken/Mindustry/master/core/assets-raw/sprites/blocks/environment/dirt2.png) ![](https://raw.githubusercontent.com/Anuken/Mindustry/master/core/assets-raw/sprites/blocks/environment/dirt3.png)
  
  - 模组示例：
    
    - ![](https://raw.githubusercontent.com/Sh1penfire/Endless-Rusting/master/assets/sprites/blocks/environment/classem-stolnene1.png) ![](https://raw.githubusercontent.com/Sh1penfire/Endless-Rusting/master/assets/sprites/blocks/environment/classem-stolnene2.png) ![](https://raw.githubusercontent.com/Sh1penfire/Endless-Rusting/master/assets/sprites/blocks/environment/classem-stolnene3.png) 
    - ![](https://raw.githubusercontent.com/Sh1penfire/Endless-Rusting/master/assets/sprites/blocks/environment/ebrin-drylon1.png) ![](https://raw.githubusercontent.com/Sh1penfire/Endless-Rusting/master/assets/sprites/blocks/environment/ebrin-drylon2.png) ![](https://raw.githubusercontent.com/Sh1penfire/Endless-Rusting/master/assets/sprites/blocks/environment/ebrin-drylon3.png) ![](https://raw.githubusercontent.com/Sh1penfire/Endless-Rusting/master/assets/sprites/blocks/environment/ebrin-drylon4.png) ![](https://raw.githubusercontent.com/Sh1penfire/Endless-Rusting/master/assets/sprites/blocks/environment/ebrin-drylon5.png) ![](https://raw.githubusercontent.com/Sh1penfire/Endless-Rusting/master/assets/sprites/blocks/environment/ebrin-drylon6.png) 

> 贴图由 Sh1penfire#0868 制作，来自 [Endless-Rusting](https://github.com/Sh1penfire/Endless-Rusting)
  
#### **静态墙**
不要与可建造的防御墙混淆，环境墙有 **3 种色调**，并且和地板一样，变体数量由你决定。

墙还有可选的 2x2 版本，会随机混入 1x1 墙中。

  - 原版示例：
    - ![](https://raw.githubusercontent.com/Anuken/Mindustry/master/core/assets-raw/sprites/blocks/environment/dacite-wall1.png) ![](https://raw.githubusercontent.com/Anuken/Mindustry/master/core/assets-raw/sprites/blocks/environment/dacite-wall2.png) ![](https://raw.githubusercontent.com/Anuken/Mindustry/master/core/assets-raw/sprites/blocks/environment/dacite-wall-large.png)
  - 模组示例：
    - ![](https://raw.githubusercontent.com/Sh1penfire/Endless-Rusting/master/assets/sprites/blocks/environment/classem-wallen1.png) ![](https://raw.githubusercontent.com/Sh1penfire/Endless-Rusting/master/assets/sprites/blocks/environment/classem-wallen2.png)

> 贴图由 Sh1penfire#0868 制作，来自 [Endless-Rusting](https://github.com/Sh1penfire/Endless-Rusting)

#### **矿石**
矿石会叠加在地板上方，因此它们在可能放置其上的所有地板纹理上都应该看起来不错。

  - 原版示例：
    - ![](https://raw.githubusercontent.com/Anuken/Mindustry/master/core/assets-raw/sprites/blocks/environment/ore-thorium1.png) ![](https://raw.githubusercontent.com/Anuken/Mindustry/master/core/assets-raw/sprites/blocks/environment/ore-thorium2.png) ![](https://raw.githubusercontent.com/Anuken/Mindustry/master/core/assets-raw/sprites/blocks/environment/ore-thorium3.png)
    - ![](https://raw.githubusercontent.com/Anuken/Mindustry/master/core/assets-raw/sprites/blocks/environment/ore-scrap1.png) ![](https://raw.githubusercontent.com/Anuken/Mindustry/master/core/assets-raw/sprites/blocks/environment/ore-scrap2.png) ![](https://raw.githubusercontent.com/Anuken/Mindustry/master/core/assets-raw/sprites/blocks/environment/ore-scrap3.png)
  - 模组示例：
    - ![](https://raw.githubusercontent.com/Sh1penfire/Endless-Rusting/master/assets/sprites/blocks/environment/melonaleum1.png) ![](https://raw.githubusercontent.com/Sh1penfire/Endless-Rusting/master/assets/sprites/blocks/environment/melonaleum2.png) 
    - ![](https://raw.githubusercontent.com/Sh1penfire/Endless-Rusting/master/assets/sprites/blocks/environment/taconite1.png) ![](https://raw.githubusercontent.com/Sh1penfire/Endless-Rusting/master/assets/sprites/blocks/environment/taconite2.png) ![](https://raw.githubusercontent.com/Sh1penfire/Endless-Rusting/master/assets/sprites/blocks/environment/taconite3.png)  

> 贴图由 Sh1penfire 制作，来自 [Endless-Rusting](https://github.com/Sh1penfire/Endless-Rusting)

#### **装饰物**
装饰物（或巨石）是玩家可破坏的环境方块，会随机出现在地板上方；它们有自己的文件，与环境贴图分开。

  - 示例：

    - ![](https://raw.githubusercontent.com/Anuken/Mindustry/master/core/assets-raw/sprites/blocks/props/boulder1.png) ![](https://raw.githubusercontent.com/Anuken/Mindustry/master/core/assets-raw/sprites/blocks/props/boulder2.png)      
    - ![](https://raw.githubusercontent.com/Anuken/Mindustry/master/core/assets-raw/sprites/blocks/props/sand-boulder1.png) ![](https://raw.githubusercontent.com/Anuken/Mindustry/master/core/assets-raw/sprites/blocks/props/sand-boulder2.png)


#### **树木**

<img src="/wiki/images/modding/spriting/spriting-props-white-tree-screenshot.png" draggable="false">

树木绘制在大多数类型方块上方，单位也可以穿过它们；它们只作为地图的额外植被。

请记住，树木尤其有阴影贴图，你必须手动制作这些贴图。

  - 示例：
  
    - <img src="/wiki/images/modding/spriting/spriting-props-white-tree.png" draggable="false">
  
      - ![](https://raw.githubusercontent.com/Anuken/Mindustry/master/core/assets-raw/sprites/blocks/props/white-tree-shadow.png)

---
