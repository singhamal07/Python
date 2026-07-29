from typing import List


class Solution:
    def longestPrefix(self, s: str) -> str:
        fail = [0] * len(s)
        j = 0

        for i in range(1, len(s)):
            while j > 0 and s[i] != s[j]:
                j = fail[j - 1]
            if s[i] == s[j]:
                j += 1
            fail[i] = j

        return s[:fail[-1]]
