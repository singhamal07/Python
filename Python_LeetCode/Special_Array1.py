#An array is considered special if every pair of its adjacent elements contains two numbers with different parity.
#You are given an array of integers nums. Return true if nums is a special array, otherwise, return false.

class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        n = len(nums)
        is_special_adjacent = [0] * (n - 1)
        for i in range(n - 1):
            is_special_adjacent[i] = (nums[i] % 2) != (nums[i + 1] % 2)

        prefix_sum = [0] * n
        for i in range(1, n):
            prefix_sum[i] = prefix_sum[i - 1] + is_special_adjacent[i - 1]

        answer = []
        for from_i, to_i in queries:
            count_different_parity = prefix_sum[to_i] - prefix_sum[from_i]
            if count_different_parity == (to_i - from_i):
                answer.append(True)
            else:
                answer.append(False)

        return answer
