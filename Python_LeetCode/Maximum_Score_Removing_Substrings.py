class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def remove_substring(s: str, target: str, points: int) -> tuple[str, int]:
            stack = []
            score = 0
            for char in s:
                if stack and stack[-1] + char == target:
                    stack.pop()
                    score += points
                else:
                    stack.append(char)
            return ''.join(stack), score
        s1, score1 = remove_substring(s, "ab", x)
        _, score2 = remove_substring(s1, "ba", y)
        total1 = score1 + score2
        s2, score3 = remove_substring(s, "ba", y)
        _, score4 = remove_substring(s2, "ab", x)
        total2 = score3 + score4
        return max(total1, total2)
