class Solution:
    def subsequencePairCount(self, nums: list[int]) -> int:
        MOD = 10**9 + 7
        dp = {(0, 0): 1}
        for x in nums:
            new_dp = {}
            for (g1, g2), ways in dp.items():
                key = (g1, g2)
                new_dp[key] = (new_dp.get(key, 0) + ways) % MOD
                ng1 = gcd(g1, x) if g1 != 0 else x
                key = (ng1, g2)
                new_dp[key] = (new_dp.get(key, 0) + ways) % MOD
                ng2 = gcd(g2, x) if g2 != 0 else x
                key = (g1, ng2)
                new_dp[key] = (new_dp.get(key, 0) + ways) % MOD
            dp = new_dp
        return sum(
            ways for (g1, g2), ways in dp.items()
            if g1 != 0 and g2 != 0 and g1 == g2
        ) % MOD