# IP 地址无效化

# 给你一个有效的 IPv4 地址 address，返回这个 IP 地址的无效化版本。
# 所谓无效化 IP 地址，其实就是用 "[.]" 代替了每个 "."。


from typing import List
class Solution:
    def defangIPaddr(self, address: str) -> str:
        return str.replace(str, '.', "[.]")



c = Solution()
print(c.defangIPaddr(address = "1.1.1.1"))
