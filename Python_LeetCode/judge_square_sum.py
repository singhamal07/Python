class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        lo, hi = 0, isqrt(c)

        while lo <= hi:
            total = lo * lo + hi * hi
            if total == c:
                return True
            elif total < c:
                lo += 1
            else:
                hi -= 1
        return False