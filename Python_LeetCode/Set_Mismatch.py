from typing import List

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        dup = (sum(nums) - sum(set(nums)))
        missing = n * (n + 1) // 2 - sum(set(nums))
        return [dup, missing]
