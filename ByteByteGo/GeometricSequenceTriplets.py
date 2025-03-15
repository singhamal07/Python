from typing import List
from collections import defaultdict

def geometric_sequence_triplets(nums: List[int], r: int) -> int:
    count_2nd = defaultdict(int)
    count_3rd = defaultdict(int)
    triplet_count = 0
    
    for num in nums:

        if num in count_3rd:
            triplet_count += count_3rd[num]

        if num in count_2nd:
            count_3rd[num * r] += count_2nd[num]

        count_2nd[num * r] += 1

    return triplet_count
