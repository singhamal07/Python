import bisect
class Solution:
    def findRightInterval(self, intervals: list[list[int]]) -> list[int]:
        start_map = {start: i for i, (start, end) in enumerate(intervals)}
        sorted_starts = sorted(start_map.keys())
        result = []
        for start, end in intervals:
            pos = bisect.bisect_left(sorted_starts, end)
            if pos < len(sorted_starts):
                result.append(start_map[sorted_starts[pos]])
            else:
                result.append(-1)
        return result