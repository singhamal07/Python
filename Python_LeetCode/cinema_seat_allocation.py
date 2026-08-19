from typing import List
from collections import defaultdict
class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        row_mask = defaultdict(int)
        for row, seat in reservedSeats:
            if 2 <= seat <= 9:
                row_mask[row] |= 1 << (seat - 2)
        left = 0b00001111
        mid = 0b00111100
        right = 0b11110000
        total = 2 * (n - len(row_mask))
        for mask in row_mask.values():
            if mask & left == 0 and mask & right == 0:
                total += 2
            elif mask & left == 0 or mask & mid == 0 or mask & right == 0:
                total += 1
        return total