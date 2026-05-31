from typing import List
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []
        ans = prices[:]
        for i, p in enumerate(prices):
            while stack and prices[stack[-1]] >= p:
                ans[stack.pop()] -= p
            stack.append(i)
        return ans
