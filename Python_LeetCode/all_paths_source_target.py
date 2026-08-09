from typing import List
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        target = len(graph) - 1
        result = []
        path = [0]
        def backtrack(node):
            if node == target:
                result.append(path[:])
                return
            for nxt in graph[node]:
                path.append(nxt)
                backtrack(nxt)
                path.pop()
        backtrack(0)
        return result