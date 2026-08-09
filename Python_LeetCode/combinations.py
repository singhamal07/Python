from typing import List
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        path = []
        def backtrack(start):
            if len(path) == k:
                result.append(path[:])
                return
            for num in range(start, n + 1):
                if n - num + 1 < k - len(path):
                    break
                path.append(num)
                backtrack(num + 1)
                path.pop()
        backtrack(1)
        return result