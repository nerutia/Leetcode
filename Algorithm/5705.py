# 判断国际象棋棋盘中一个格子的颜色

# 给你一个坐标 coordinates ，它是一个字符串，表示国际象棋棋盘中一个格子的坐标。
# 左下角是a1黑色。右下角是h1白色。左上角是a8白色。右上角是h8黑色。

# 如果所给格子的颜色是白色，请你返回 true，如果是黑色，请返回 false 。

# 给定坐标一定代表国际象棋棋盘上一个存在的格子。坐标第一个字符是字母，第二个字符是数字。


class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        return (ord(coordinates[0]) - ord('a') + ord(coordinates[1]) + 1) % 2 == 1


c = Solution()
print(c.squareIsWhite(
    coordinates = "a1"
))