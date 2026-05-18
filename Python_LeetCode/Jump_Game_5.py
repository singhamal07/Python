class Solution:
    def maxJumps(self, arr: list[int], d: int) -> int:
        n = len(arr)
        memo = {}

        def dp(i):
            if i in memo:
                return memo[i]
            best = 1
            for dx in (1, -1):
                for x in range(1, d + 1):
                    j = i + dx * x
                    if not (0 <= j < n):
                        break
                    if arr[j] >= arr[i]:  # blocked
                        break
                    best = max(best, 1 + dp(j))
            memo[i] = best
            return best

        return max(dp(i) for i in range(n))
