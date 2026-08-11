from typing import List
class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        n = len(nums)
        total = nums[0]
        for i in range(1, n):
            if nums[i] == nums[i - 1] + 1:
                total += nums[i]
            else:
                break
        num_set = set(nums)
        x = total
        while x in num_set:
            x += 1
        return x