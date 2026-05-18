class Solution:
    def minJumps(self, arr: list[int]) -> int:
        n = len(arr)
        if n == 1:
            return 0

        graph = defaultdict(list)
        for i, v in enumerate(arr):
            graph[v].append(i)

        visited = {0}
        queue = deque([(0, 0)])

        while queue:
            i, steps = queue.popleft()
            for ni in [i + 1, i - 1] + graph.pop(arr[i], []):
                if ni == n - 1:
                    return steps + 1
                if 0 <= ni < n and ni not in visited:
                    visited.add(ni)
                    queue.append((ni, steps + 1))
