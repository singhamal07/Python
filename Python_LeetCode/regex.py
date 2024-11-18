class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # Dynamic programming table
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        
        # Base case: empty string matches empty pattern
        dp[0][0] = True
        
        # Handle patterns like "a*", "a*b*", ".*", etc., which can match an empty string
        for j in range(2, len(p) + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]
        
        # Fill the DP table
        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if p[j - 1] == s[i - 1] or p[j - 1] == '.':
                    # Characters match, or '.' matches any character
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':
                    # '*' can mean zero or more of the preceding character
                    dp[i][j] = dp[i][j - 2]  # Case 1: '*' matches zero occurrences
                    if p[j - 2] == s[i - 1] or p[j - 2] == '.':
                        dp[i][j] = dp[i][j] or dp[i - 1][j]  # Case 2: '*' matches one or more occurrences
        
        return dp[len(s)][len(p)]

solution = Solution()
print(solution.isMatch("aa", "a*"))  # True
print(solution.isMatch("mississippi", "mis*is*p*."))  # False
print(solution.isMatch("ab", ".*"))  # True