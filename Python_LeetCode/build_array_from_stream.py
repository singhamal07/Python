from typing import List


class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        ops, i = [], 0
        for num in range(1, n + 1):
            if i == len(target):
                break
            ops.append("Push")
            if num != target[i]:
                ops.append("Pop")
            else:
                i += 1
        return ops
