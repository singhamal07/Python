class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        n = len(online)
        def can_achieve(min_edge: int) -> bool:
            graph = defaultdict(list)
            for u, v, cost in edges:
                if cost >= min_edge:
                    graph[u].append((v, cost))
            dist = [float('inf')] * n
            dist[0] = 0
            heap = [(0, 0)]
            while heap:
                total_cost, u = heapq.heappop(heap)
                if total_cost > dist[u]:
                    continue
                if u == n - 1:
                    return total_cost <= k
                for v, cost in graph[u]:
                    if v != n - 1 and not online[v]:
                        continue
                    new_cost = total_cost + cost
                    if new_cost < dist[v]:
                        dist[v] = new_cost
                        heapq.heappush(heap, (new_cost, v))
            return dist[n - 1] <= k
        candidates = sorted(set(cost for _, _, cost in edges))
        if not candidates or not can_achieve(candidates[0]):
            return -1
        lo, hi = 0, len(candidates) - 1
        result = -1
        while lo <= hi:
            mid = (lo + hi) // 2
            if can_achieve(candidates[mid]):
                result = candidates[mid]
                lo = mid + 1
            else:
                hi = mid - 1
        return result