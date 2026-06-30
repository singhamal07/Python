class Solution:
    def countVowels(self, word: str) -> int:
        n = len(word)
        result = 0
        vowels = set("aeiou")

        for i, ch in enumerate(word):
            if ch in vowels:
                result += (i + 1) * (n - i)

        return result
