class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = {}
        max_len_per_rem = [0] * k
        max_length = 1    
        for i in range(n):
            dp[(i, -1)] = 1
            max_length = max(max_length, 1)    
            for j in range(i):
                r = (nums[j] + nums[i]) % k
                if (j, r) in dp:
                    dp[(i, r)] = max(dp.get((i, r), 0), dp[(j, r)] + 1)
                    max_length = max(max_length, dp[(i, r)])
                dp[(i, r)] = max(dp.get((i, r), 0), 2)
                max_length = max(max_length, 2)      
            for r in range(k):
                if (i, r) in dp:
                    max_len_per_rem[r] = max(max_len_per_rem[r], dp[(i, r)])
        return max_length
