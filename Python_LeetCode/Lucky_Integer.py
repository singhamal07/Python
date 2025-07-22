class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freq = {}
        for num in arr:
            freq[num] = freq.get(num, 0) + 1
        lucky = -1
        for num in freq:
            if num == freq[num]:
                lucky = max(lucky, num) 
        return lucky
