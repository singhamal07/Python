class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:
        sorted_nodes = sorted(range(n), key=lambda x: nums[x])
        sorted_vals = [nums[x] for x in sorted_nodes]
        rank = [0] * n
        for pos, node in enumerate(sorted_nodes):
            rank[node] = pos
        LOG = 17
        jump = [[0] * n for _ in range(LOG)]
        for pos in range(n):
            val = sorted_vals[pos]
            hi = bisect.bisect_right(sorted_vals, val + maxDiff) - 1
            jump[0][pos] = hi
        for k in range(1, LOG):
            for pos in range(n):
                jump[k][pos] = jump[k - 1][jump[k - 1][pos]]
        def min_dist(src, dst):
            if src == dst:
                return 0
            sp = rank[src]
            dp = rank[dst]
            if sp > dp:
                sp, dp = dp, sp
            cur = sp
            dist = 0
            for k in range(LOG - 1, -1, -1):
                if jump[k][cur] < dp:
                    cur = jump[k][cur]
                    dist += (1 << k)
            if jump[0][cur] >= dp:
                return dist + 1
            else:
                return -1
        return [min_dist(u, v) for u, v in queries]