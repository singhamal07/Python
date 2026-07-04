class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)
        for a, b, dist in roads:
            graph[a].append((b, dist))
            graph[b].append((a, dist))
        visited = set()
        min_score = float('inf')
        queue = deque([1])
        visited.add(1)
        while queue:
            node = queue.popleft()
            for neighbor, dist in graph[node]:
                min_score = min(min_score, dist)
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        return min_score
