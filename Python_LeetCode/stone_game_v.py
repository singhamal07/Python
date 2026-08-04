from typing import List
class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        n = len(stoneValue)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + stoneValue[i]
        dp = [[0] * n for _ in range(n)]
        leftMax = [[0] * n for _ in range(n)]
        rightMax = [[0] * n for _ in range(n)]
        for i in range(n):
            leftMax[i][i] = stoneValue[i]
            rightMax[i][i] = stoneValue[i]
        for length in range(1, n):
            for i in range(n - length):
                j = i + length
                total = prefix[j + 1] - prefix[i]
                lo, hi, pos = i, j - 1, i - 1
                while lo <= hi:
                    mid = (lo + hi) // 2
                    if 2 * (prefix[mid + 1] - prefix[i]) <= total:
                        pos = mid
                        lo = mid + 1
                    else:
                        hi = mid - 1
                best = 0
                if pos >= i:
                    best = max(best, leftMax[i][pos])
                if pos + 2 <= j:
                    best = max(best, rightMax[pos + 2][j])
                if pos >= i and 2 * (prefix[pos + 1] - prefix[i]) == total:
                    best = max(best, (prefix[pos + 1] - prefix[i]) + dp[pos + 1][j])
                dp[i][j] = best
                leftMax[i][j] = max(leftMax[i][j - 1], (prefix[j + 1] - prefix[i]) + dp[i][j])
                rightMax[i][j] = max(rightMax[i + 1][j], (prefix[j + 1] - prefix[i]) + dp[i][j])
        return dp[0][n - 1]