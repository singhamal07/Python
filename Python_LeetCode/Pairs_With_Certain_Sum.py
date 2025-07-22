class FindSumPairs:
    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums2 = nums2
        self.freq1 = {}
        self.freq2 = {}
        for num in nums1:
            self.freq1[num] = self.freq1.get(num, 0) + 1
        for num in nums2:
            self.freq2[num] = self.freq2.get(num, 0) + 1
    def add(self, index: int, val: int) -> None:
        old_val = self.nums2[index]
        self.nums2[index] += val
        new_val = self.nums2[index]
        self.freq2[old_val] -= 1
        if self.freq2[old_val] == 0:
            del self.freq2[old_val]
        self.freq2[new_val] = self.freq2.get(new_val, 0) + 1
    def count(self, tot: int) -> int:
        result = 0
        for val1 in self.freq1:
            val2 = tot - val1
            if val2 in self.freq2:
                result += self.freq1[val1] * self.freq2[val2]
        return result
