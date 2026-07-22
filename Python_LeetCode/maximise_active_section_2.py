class Solution:
    def maxActiveSectionsAfterTrade(
        self, 
        s: str, 
        queries: List[List[int]]
    ) -> List[int]:
        totalOnes = s.count('1')
        def bestTrade(sub: str) -> int:
            ones = sub.count('1')
            t = "1" + sub + "1"
            runs = []
            i = 0
            while i < len(t):
                j = i
                while j < len(t) and t[j] == t[i]:
                    j += 1
                runs.append((t[i], j - i))
                i = j
            ans = ones
            for i in range(1, len(runs) - 1):
                if (
                    runs[i][0] == '1'
                    and runs[i - 1][0] == '0'
                    and runs[i + 1][0] == '0'
                ):
                    gain = runs[i - 1][1] + runs[i + 1][1]
                    ans = max(ans, ones + gain)
            return ans
        result = []
        for l, r in queries:
            sub = s[l:r + 1]
            inside = bestTrade(sub)
            outside = totalOnes - s[l:r + 1].count('1')
            result.append(inside + outside)
        return result
