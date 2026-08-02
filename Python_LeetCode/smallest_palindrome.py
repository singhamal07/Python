class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if not s:
            return s
        t = s + "#" + s[::-1]
        fail = [0] * len(t)
        j = 0
        for i in range(1, len(t)):
            while j > 0 and t[i] != t[j]:
                j = fail[j - 1]
            if t[i] == t[j]:
                j += 1
            fail[i] = j
        longest_prefix = fail[-1]
        return s[longest_prefix:][::-1] + s