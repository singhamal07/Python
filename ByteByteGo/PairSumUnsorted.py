from typing import List

def pair_sum_unsorted(nums: List[int], target: int) -> List[int]:
    num_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i] 
        num_map[num] = i
    return [] 
