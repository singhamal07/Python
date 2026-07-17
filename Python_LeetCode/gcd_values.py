class Solution:
    def gcdValues(self, nums: list[int], queries: list[int]) -> list[int]:
        max_val = max(nums)
        freq = Counter(nums)
        cnt = [0] * (max_val + 1)
        for g in range(1, max_val + 1):
            for multiple in range(g, max_val + 1, g):
                cnt[g] += freq[multiple]
        exact_gcd = [0] * (max_val + 1)
        for g in range(max_val, 0, -1):
            c = cnt[g]
            exact_gcd[g] = c * (c - 1) // 2
            for multiple in range(2 * g, max_val + 1, g):
                exact_gcd[g] -= exact_gcd[multiple]
        prefix = [0] * (max_val + 1)
        for g in range(1, max_val + 1):
            prefix[g] = prefix[g - 1] + exact_gcd[g]
        answer = []
        for q in queries:
            lo, hi = 1, max_val
            while lo < hi:
                mid = (lo + hi) // 2
                if prefix[mid] > q:
                    hi = mid
                else:
                    lo = mid + 1
            answer.append(lo)
        return answer