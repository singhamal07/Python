class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total = sum(nums)
        need = total % p
        if need == 0:
            return 0
        prefix = 0
        seen = {0: -1}
        best = len(nums)
        for i, num in enumerate(nums):
            prefix = (prefix + num) % p
            target = (prefix - need) % p
            if target in seen:
                best = min(best, i - seen[target])
            seen[prefix] = i
        return best if best < len(nums) else -1
