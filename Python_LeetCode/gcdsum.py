class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        n = len(nums)
        prefixGcd = []
        max_so_far = 0
        for num in nums:
            max_so_far = max(max_so_far, num)
            prefixGcd.append(gcd(num, max_so_far))
        prefixGcd.sort()
        result = 0
        left, right = 0, n - 1
        while left < right:
            result += gcd(prefixGcd[left], prefixGcd[right])
            left += 1
            right -= 1
        return result