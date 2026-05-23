from typing import List

class Solution:
    def check(self, nums: List[int]) -> bool:
        drops = sum(nums[i] > nums[(i+1) % len(nums)] for i in range(len(nums)))
        return drops <= 1
