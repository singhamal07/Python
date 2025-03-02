from typing import List
def largest_container(heights: List[int]) -> int:
    left, right = 0, len(heights) - 1
    max_area = 0  
    while left < right:
        width = right - left
        min_height = min(heights[left], heights[right])
        area = width * min_height
        max_area = max(max_area, area)
        if heights[left] < heights[right]:
            left += 1
        else:
            right -= 1
    return max_area
