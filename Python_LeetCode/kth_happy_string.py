class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        letters = ['a', 'b', 'c']
        result = []
        def backtrack(pos):
            nonlocal k
            if pos == n:
                k -= 1
                if k == 0:
                    return True
                return False
            for ch in letters:
                if result and result[-1] == ch:
                    continue
                result.append(ch)
                if backtrack(pos + 1):
                    return True
                result.pop()
            return False
        if backtrack(0):
            return "".join(result)
        return ""