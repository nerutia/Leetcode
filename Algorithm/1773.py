# 统计匹配检索规则的物品数量

# 给你一个数组 items ，其中 items[i] = [typei, colori, namei] ，描述第 i 件物品的类型、颜色以及名称。

# 另给你一条由两个字符串 ruleKey 和 ruleValue 表示的检索规则。

# 如果第 i 件物品能满足下述条件之一，则认为该物品与给定的检索规则 匹配 ：

# ruleKey == "type" 且 ruleValue == typei 。
# ruleKey == "color" 且 ruleValue == colori 。
# ruleKey == "name" 且 ruleValue == namei 。
# 统计并返回 匹配检索规则的物品数量 。

from typing import List

class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        r = 0
        if ruleKey == 'type':
            for i in items:
                if i[0] == ruleValue:
                    r += 1
        if ruleKey == 'color':
            for i in items:
                if i[1] == ruleValue:
                    r += 1
        if ruleKey == 'name':
            for i in items:
                if i[2] == ruleValue:
                    r += 1
        return r


c = Solution()
print(c.countMatches(items = [["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]], ruleKey = "color", ruleValue = "silver"))



