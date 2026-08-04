from typing import List
class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        n = len(stones)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + stones[i]
        def rangeSum(i, j):
            return prefix[j + 1] - prefix[i]
        dp = [[0] * n for _ in range(n)]
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                dp[i][j] = max(
                    rangeSum(i + 1, j) - dp[i + 1][j],
                    rangeSum(i, j - 1) - dp[i][j - 1]
                )
        return dp[0][n - 1]