class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        total_even = sum(nums[i] for i in range(0, len(nums), 2))
        total_odd = sum(nums[i] for i in range(1, len(nums), 2))    
        result = 0
        prefix_even = prefix_odd = 0      
        for i, num in enumerate(nums):
            if i % 2 == 0:
                total_even -= num
            else:
                total_odd -= num
            new_even = prefix_even + total_odd
            new_odd = prefix_odd + total_even 
            if new_even == new_odd:
                result += 1 
            if i % 2 == 0:
                prefix_even += num
            else:
                prefix_odd += num
        return result
