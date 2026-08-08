from typing import List
class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        n, m = len(word1), len(word2)
        suf = [0] * (n + 1)
        p = m
        for i in range(n - 1, -1, -1):
            if p > 0 and word1[i] == word2[p - 1]:
                p -= 1
            suf[i] = m - p
        result = []
        i = j = 0
        used_change = False
        while i < n and j < m:
            if word1[i] == word2[j]:
                result.append(i)
                i += 1
                j += 1
            elif not used_change and suf[i + 1] >= m - j - 1:
                used_change = True
                result.append(i)
                i += 1
                j += 1
            else:
                i += 1
        return result if j == m else []