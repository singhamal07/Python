class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        effort = [[float('inf')] * cols for _ in range(rows)]
        effort[0][0] = 0
        heap = [(0, 0, 0)]
        while heap:
            eff, r, c = heapq.heappop(heap)
            if r == rows - 1 and c == cols - 1:
                return eff
            if eff > effort[r][c]:
                continue
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    new_eff = max(eff, abs(heights[nr][nc] - heights[r][c]))
                    if new_eff < effort[nr][nc]:
                        effort[nr][nc] = new_eff
                        heapq.heappush(heap, (new_eff, nr, nc))
        return effort[rows - 1][cols - 1]
