from collections import Counter
from math import comb
from typing import List


class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        count = Counter(s)
        half_counts = {}
        middle = ""

        for ch, cnt in count.items():
            if cnt % 2 == 1:
                middle = ch
            if cnt // 2 > 0:
                half_counts[ch] = cnt // 2

        def count_perms(counts, limit):
            result = 1
            n = sum(counts.values())
            for cnt in counts.values():
                result *= comb(n, cnt)
                n -= cnt
                if result >= limit:
                    return limit
            return result

        if k > count_perms(half_counts, k + 1):
            return ""

        half = []
        remaining = dict(half_counts)

        for _ in range(sum(half_counts.values())):
            for ch in sorted(remaining.keys()):
                remaining[ch] -= 1
                if remaining[ch] == 0:
                    del remaining[ch]

                perms = count_perms(remaining, k) if remaining else 1

                if k <= perms:
                    half.append(ch)
                    break
                else:
                    k -= perms
                    remaining[ch] = remaining.get(ch, 0) + 1

        half_str = "".join(half)
        return half_str + middle + half_str[::-1]
