class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        if m == 1 and n == 1:
            return 0
        best = [[-1] * n for _ in range(m)]
        best[0][0] = k
        queue = deque([(0, 0, 0, k)])
        while queue:
            steps, r, c, remaining = queue.popleft()
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n:
                    new_remaining = remaining - grid[nr][nc]
                    if new_remaining < 0 or new_remaining <= best[nr][nc]:
                        continue
                    if nr == m - 1 and nc == n - 1:
                        return steps + 1
                    best[nr][nc] = new_remaining
                    queue.append((steps + 1, nr, nc, new_remaining))
        return -1