from itertools import combinations
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        LO, HI = -10**5, 10**5
        def maxProduct3(arr):
            arr = sorted(arr)
            return max(arr[-1] * arr[-2] * arr[-3], arr[-1] * arr[0] * arr[1])
        n = len(nums)
        best = float('-inf')

        if n <= 5:
            for i in range(n):
                rest = nums[:i] + nums[i+1:]
                for v in (LO, HI):
                    best = max(best, maxProduct3(rest + [v]))
        else:
            s = sorted(nums)
            candidates_base = s[-3:] + s[:2]  # top3 largest + bottom2 smallest
            for v in (LO, HI):
                pool = candidates_base + [v]
                for combo in combinations(pool, 3):
                    best = max(best, combo[0] * combo[1] * combo[2])
        return best