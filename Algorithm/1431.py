class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        a=len(candies)
        m=max(candies)
        b=[0]*a
        for i in range(a):
            if candies[i]+extraCandies < m:
                b[i]=False
            else:
                b[i]=True
        return b
