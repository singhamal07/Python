from typing import List
class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        base = sum(c for c, g in zip(customers, grumpy) if g == 0)
        extra = sum(customers[i] * grumpy[i] for i in range(minutes))
        best_extra = extra
        for i in range(minutes, len(customers)):
            extra += customers[i] * grumpy[i] - customers[i - minutes] * grumpy[i - minutes]
            best_extra = max(best_extra, extra)
        return base + best_extra