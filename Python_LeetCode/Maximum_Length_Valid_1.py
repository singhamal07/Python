class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        n = len(nums)
        
        even_count = 0
        odd_count = 0
        for num in nums:
            if num % 2 == 0:
                even_count += 1
            else:
                odd_count += 1
        max_same_parity = max(even_count, odd_count)
        
        even_ending = 0
        odd_ending = 0
        max_alternating = 0
        
        for num in nums:
            parity = num % 2
            if parity == 0:
                even_ending = odd_ending + 1
            else:
                odd_ending = even_ending + 1
            max_alternating = max(max_alternating, even_ending, odd_ending)
        
        return max(max_same_parity, max_alternating)
