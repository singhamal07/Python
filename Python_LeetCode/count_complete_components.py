class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
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
        for a, b in edges:
            union(a, b)
        vertex_count = defaultdict(int)
        edge_count = defaultdict(int)
        for v in range(n):
            vertex_count[find(v)] += 1
        for a, b in edges:
            edge_count[find(a)] += 1
        result = 0
        for root in vertex_count:
            k = vertex_count[root]
            if edge_count[root] == k * (k - 1) // 2:
                result += 1
        return result
