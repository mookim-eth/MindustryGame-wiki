# 脚本

Mindustry 使用 JavaScript 进行模组脚本编写。脚本使用 `js` 扩展名，并放在 `scripts/` 子目录中。

执行从名为 `main.js` 的文件开始。任何其他脚本文件都可以由主文件通过 `require("script_name")` 导入。
典型设置如下：

*scripts/main.js*:
```js

require("blocks");
require("items");

```

*scripts/blocks.js*:
```js
const myBlock = extend(Conveyor, "terrible-conveyor", {
  // various overrides...
  size: 3,
  health: 200
  //...
});
```

*scripts/items.js*:
```js

const terribleium = Item("terribleium");
terribleium.color = Color.valueOf("ff0000");
//...

```

# 示例

## 监听事件

<img src="/wiki/images/misc/modding-pathetic.gif">

```js

// listen for the event where a unit is destroyed
Events.on(UnitDestroyEvent, event => {
  // display toast on top of screen when the unit was a player
  if(event.unit.isPlayer()){
    Vars.ui.hudfrag.showToast("Pathetic.");
  }
})

```

查找可以监听哪些事件，最简单的方法是查看源文件：[Mindustry/blob/master/core/src/mindustry/game/EventType.java](https://github.com/Anuken/Mindustry/blob/master/core/src/mindustry/game/EventType.java)

## 显示对话框

```js
const myDialog = new BaseDialog("Dialog Title");
// Add "go back" button
myDialog.addCloseButton();
// Add text to the main content
myDialog.cont.add("Goodbye.");
// Show dialog
myDialog.show();
```

## 播放一些自定义音效

播放自定义音频很简单，前提是你将声音片段作为 `.mp3` 或 `.ogg` 文件存放在 `/sounds` 目录中。

在此示例中，我们已将 `example.mp3` 存放在 `/sounds/example.mp3`。

### 使用库加载声音

*scripts/alib.js*:
```js
exports.loadSound = (() => {
    const cache = {};
    return (path) => {
        const c = cache[path];
        if (c === undefined) {
            return cache[path] = loadSound(path);
        }
        return c;
    }
})();

```

*scripts/main.js*:

```js
const lib = require("alib");

Events.on(WaveEvent, event => {
    // loads example.mp3
    const mySound = lib.loadSound("example");
    // engine will spawn this sound at this location (X,Y)
    mySound.at(1, 1);
})
```

//TODO 测试这些示例并添加更多示例
