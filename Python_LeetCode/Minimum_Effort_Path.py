import heapq
from typing import List


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        effort = [[float('inf')] * cols for _ in range(rows)]
        effort[0][0] = 0

        heap = [(0, 0, 0)]  # (effort, row, col)

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


# Test cases
if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        ([[1, 2, 2], [3, 8, 2], [5, 3, 5]], 2),
        ([[1, 2, 3], [3, 8, 4], [5, 3, 5]], 1),
        ([[1, 2, 1, 1, 1], [1, 2, 1, 2, 1], [1, 2, 1, 2, 1], [1, 2, 1, 2, 1], [1, 1, 1, 2, 1]], 0),
    ]

    for i, (heights, expected) in enumerate(test_cases, 1):
        result = sol.minimumEffortPath(heights)
        status = "PASS" if result == expected else "FAIL"
        print(f"Example {i}: Output = {result}, Expected = {expected} → {status}")
