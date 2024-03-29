# 解码异或后的数组

# 未知 整数数组 arr 由 n 个非负整数组成。
# 经编码后变为长度为 n - 1 的另一个整数数组 encoded ，其中 encoded[i] = arr[i] XOR arr[i + 1] 。例如，arr = [1,0,2,1] 经编码后得到 encoded = [1,2,3] 。
# 给你编码后的数组 encoded 和原数组 arr 的第一个元素 first（arr[0]）。
# 请解码返回原数组 arr 。可以证明答案存在并且是唯一的。

from typing import List

class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        r = [first]
        for i in encoded:
            r.append(r[-1] ^ i)
        return r

c = Solution()
print(c.decode(
    encoded = [1,2,3], first = 1
))