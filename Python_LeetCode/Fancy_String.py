class Solution:
    def makeFancyString(self, s: str) -> str:
        result = []
        count = 1
        prev = None
        for char in s:
            if char == prev:
                count += 1
                if count <= 2:
                    result.append(char)
            else:
                count = 1
                prev = char
                result.append(char)
        return ''.join(result)
