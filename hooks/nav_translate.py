"""Translate top-level MkDocs navigation section titles for the Chinese site.

This only changes displayed navigation labels. Source directories and URLs stay
unchanged so existing generated links keep working.
"""

NAV_TRANSLATIONS = {
    # Official/near-official game terms from bundle_zh_CN.properties:
    # database-category.block = 建筑
    # database-category.item = 物品
    # database-category.liquid = 流体
    # database-category.unit = 单位
    # database-category.status = 状态效果
    # planets = 星球
    # rules.title.environment = 环境; lenum.getblock mentions 环境块/环境墙体
    "Environment Blocks": "环境块",
    "Blocks": "建筑",
    "Items": "物品",
    "Liquids": "流体",
    "Units": "单位",
    "Statuses": "状态效果",
    "Planets": "星球",
    "Logic": "逻辑",
    "Guides": "攻略",
    "guides": "攻略",
    # Wiki-specific sections; no exact in-game category exists.
    "Modding": "模组制作",
    "Modding Classes": "模组类参考",
}


def on_nav(nav, config, files):
    def translate(items):
        for item in items:
            if getattr(item, "is_section", False):
                item.title = NAV_TRANSLATIONS.get(item.title, item.title)
                translate(item.children)

    translate(nav.items)
    return nav
