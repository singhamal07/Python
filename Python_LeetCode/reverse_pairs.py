class Solution:
    def reversePairs(self, nums: list[int]) -> int:    
        def merge_sort(arr):
            if len(arr) <= 1:
                return arr, 0    
            mid = len(arr) // 2
            left,  left_count  = merge_sort(arr[:mid])
            right, right_count = merge_sort(arr[mid:])
            count = left_count + right_count
            j = 0
            for i in range(len(left)):
                while j < len(right) and left[i] > 2 * right[j]:
                    j += 1
                count += j
            merged = []
            l, r = 0, 0
            while l < len(left) and r < len(right):
                if left[l] <= right[r]:
                    merged.append(left[l]); l += 1
                else:
                    merged.append(right[r]); r += 1
            merged.extend(left[l:])
            merged.extend(right[r:])
            return merged, count
        _, result = merge_sort(nums)
        return result