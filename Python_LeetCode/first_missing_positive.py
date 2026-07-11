from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)

        # Step 1: Place each number in its correct index position
        # nums[i] = x should be at index x-1
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                # Swap nums[i] to its correct position
                correct = nums[i] - 1
                nums[i], nums[correct] = nums[correct], nums[i]

        # Step 2: Find the first index where nums[i] != i+1
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        # All positions 1..n are filled, answer is n+1
        return n + 1


# Test cases
if __name__ == "__main__":
    s = Solution()

    result1 = s.firstMissingPositive([1, 2, 0])
    print(f"Test 1: nums=[1,2,0] => {result1} | Expected: 3")

    result2 = s.firstMissingPositive([3, 4, -1, 1])
    print(f"Test 2: nums=[3,4,-1,1] => {result2} | Expected: 2")

    result3 = s.firstMissingPositive([7, 8, 9, 11, 12])
    print(f"Test 3: nums=[7,8,9,11,12] => {result3} | Expected: 1")

    result4 = s.firstMissingPositive([1])
    print(f"Test 4: nums=[1] => {result4} | Expected: 2")
