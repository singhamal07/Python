from functools import lru_cache
class Solution:
    def beautifulArray(self, n: int) -> list[int]:
        @lru_cache(None)
        def build(n):
            if n == 1:
                return [1]
            odds  = [2 * x - 1 for x in build((n + 1) // 2)]
            evens = [2 * x     for x in build(n // 2)]
            return odds + evens
        return [x for x in build(n) if x <= n]