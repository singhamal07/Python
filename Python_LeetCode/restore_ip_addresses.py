from typing import List
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        n = len(s)
        result = []
        path = []
        def backtrack(start):
            if len(path) == 4:
                if start == n:
                    result.append(".".join(path))
                return
            for length in range(1, 4):
                if start + length > n:
                    break
                segment = s[start:start + length]
                if (segment[0] == '0' and len(segment) > 1) or int(segment) > 255:
                    continue
                path.append(segment)
                backtrack(start + length)
                path.pop()
        backtrack(0)
        return result