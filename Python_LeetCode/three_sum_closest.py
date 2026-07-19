class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        closest_sum = float('inf')
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left, right = i + 1, n - 1
            while left < right:
                current = nums[i] + nums[left] + nums[right]
                if abs(current - target) < abs(closest_sum - target):
                    closest_sum = current
                if current < target:
                    left += 1
                elif current > target:
                    right -= 1
                else:
                    return current
        return closest_sum
