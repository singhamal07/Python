class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        MOD = 10**9 + 7
        n = len(board)
        UNREACHABLE = (-1, 0)
        dp = [[UNREACHABLE] * n for _ in range(n)]
        dp[n-1][n-1] = (0, 1)
        def cell_value(i, j):
            c = board[i][j]
            return 0 if c in ('S', 'E') else int(c)
        def merge(best, candidate_sum, candidate_count):
            best_sum, best_count = best
            if best_sum < candidate_sum:
                return (candidate_sum, candidate_count % MOD)
            elif best_sum == candidate_sum:
                return (best_sum, (best_count + candidate_count) % MOD)
            return best
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if i == n - 1 and j == n - 1:
                    continue
                if board[i][j] == 'X':
                    continue
                best = UNREACHABLE
                val = cell_value(i, j)
                for di, dj in [(1, 0), (0, 1), (1, 1)]:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < n and 0 <= nj < n:
                        src_sum, src_count = dp[ni][nj]
                        if src_sum != -1:
                            best = merge(best, src_sum + val, src_count)
                dp[i][j] = best
        top_sum, top_count = dp[0][0]
        return [0, 0] if top_sum == -1 else [top_sum, top_count % MOD]