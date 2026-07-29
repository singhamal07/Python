from collections import Counter
from typing import List
class Solution:
    def smallestPalindrome(self, s: str) -> str:
        count = Counter(s)
        half = []
        middle = ""
        for ch in sorted(count.keys()):
            if count[ch] % 2 == 1:
                middle = ch
            half.extend([ch] * (count[ch] // 2))
        half_str = "".join(half)
        return half_str + middle + half_str[::-1]