from typing import List
from collections import defaultdict
class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        count = defaultdict(int)
        n = len(nums)
        for i in range(n - k + 1):
            for x in set(nums[i:i + k]):
                count[x] += 1
        best = -1
        for x, c in count.items():
            if c == 1:
                best = max(best, x)
        return best
