class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        m, n = len(grid), len(grid[0])
        start_health = health - grid[0][0]
        if start_health <= 0:
            return False
        best_health = [[-1] * n for _ in range(m)]
        best_health[0][0] = start_health
        queue = deque([(0, 0, start_health)])
        while queue:
            r, c, hp = queue.popleft()
            if r == m - 1 and c == n - 1:
                return True
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n:
                    new_hp = hp - grid[nr][nc]
                    if new_hp > 0 and new_hp > best_health[nr][nc]:
                        best_health[nr][nc] = new_hp
                        queue.append((nr, nc, new_hp))
        return False
