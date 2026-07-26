class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_so_far = min_so_far = result = nums[0]
        for num in nums[1:]:
            if num < 0:
                max_so_far, min_so_far = min_so_far, max_so_far
            max_so_far = max(num, max_so_far * num)
            min_so_far = min(num, min_so_far * num)
            result = max(result, max_so_far)
        return result