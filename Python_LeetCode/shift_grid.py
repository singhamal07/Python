class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        flat = [v for row in grid for v in row]
        k %= m * n
        flat = flat[-k:] + flat[:-k]
        return [flat[i*n:(i+1)*n] for i in range(m)]