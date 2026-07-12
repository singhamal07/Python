class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        ranks = {val: rank for rank, val in enumerate(sorted(set(arr)), 1)}
        return [ranks[val] for val in arr]
