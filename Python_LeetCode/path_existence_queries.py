class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        parent = list(range(n))
        rank = [0] * n
        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        def union(x, y):
            px, py = find(x), find(y)
            if px == py:
                return
            if rank[px] < rank[py]:
                px, py = py, px
            parent[py] = px
            if rank[px] == rank[py]:
                rank[px] += 1
        right = 0
        for left in range(n):
            if right < left:
                right = left
            while right + 1 < n and nums[right + 1] - nums[left] <= maxDiff:
                right += 1
            if left + 1 <= right:
                union(left, left + 1)
        return [find(u) == find(v) for u, v in queries]
