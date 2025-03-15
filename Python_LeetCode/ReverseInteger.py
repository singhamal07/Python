class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        sign = -1 if x < 0 else 1
        x_abs = abs(x)
        reversed_str = str(x_abs)[::-1]
        reversed_int = int(reversed_str)
        result = sign * reversed_int
        if result < INT_MIN or result > INT_MAX:
            return 0     
        return result
