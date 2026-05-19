class Solution:
    def getCommon(self, nums1: list[int], nums2: list[int]) -> int:
        s = set(nums1)
        for n in nums2:
            if n in s:
                return n
        return -1
