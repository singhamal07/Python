class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        direction_map = {1: 0, 2: 1, 3: 2, 4: 3}
        
        pq = [(0, 0, 0)]
        
        cost_matrix = [[float('inf')] * n for _ in range(m)]
        cost_matrix[0][0] = 0
        
        while pq:
            cost, x, y = heapq.heappop(pq)
            
            if x == m - 1 and y == n - 1:
                return cost
            
            for i, (dx, dy) in enumerate(directions):
                nx, ny = x + dx, y + dy
                
                if 0 <= nx < m and 0 <= ny < n:

                    new_cost = cost if i == direction_map[grid[x][y]] else cost + 1
                    
                    if new_cost < cost_matrix[nx][ny]:
                        cost_matrix[nx][ny] = new_cost
                        heapq.heappush(pq, (new_cost, nx, ny))
        
        return -1
