class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last = {c: i for i, c in enumerate(s)}  # last occurrence of each char
        stack = []
        seen = set()

        for i, c in enumerate(s):
            if c in seen:
                continue
            # Pop if current char is smaller and the top char appears later
            while stack and c < stack[-1] and last[stack[-1]] > i:
                seen.discard(stack.pop())
            stack.append(c)
            seen.add(c)

        return ''.join(stack)
