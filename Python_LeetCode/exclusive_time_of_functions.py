from typing import List
class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        res = [0] * n
        stack = []
        for log in logs:
            fid, typ, t = log.split(':')
            fid, t = int(fid), int(t)
            if typ == 'start':
                if stack:
                    res[stack[-1][0]] += t - stack[-1][1]
                stack.append((fid, t))
            else:
                res[fid] += t - stack.pop()[1] + 1
                if stack:
                    stack[-1] = (stack[-1][0], t + 1)
        return res
