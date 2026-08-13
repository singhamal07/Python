from typing import List
class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        n = len(s)
        arr = list(s)
        tree = [None] * (4 * n)
        def merge(left, right):
            l_len, l_lc, l_rc, l_lrun, l_rrun, l_max = left
            r_len, r_lc, r_rc, r_lrun, r_rrun, r_max = right

            length = l_len + r_len
            lrun = l_lrun + r_lrun if l_lrun == l_len and l_rc == r_lc else l_lrun
            rrun = r_rrun + l_rrun if r_rrun == r_len and r_lc == l_rc else r_rrun
            max_run = max(l_max, r_max)
            if l_rc == r_lc:
                max_run = max(max_run, l_rrun + r_lrun)
            return (length, l_lc, r_rc, lrun, rrun, max_run)
        def build(node, start, end):
            if start == end:
                tree[node] = (1, arr[start], arr[start], 1, 1, 1)
                return
            mid = (start + end) // 2
            build(2 * node, start, mid)
            build(2 * node + 1, mid + 1, end)
            tree[node] = merge(tree[2 * node], tree[2 * node + 1])
        def update(node, start, end, idx, ch):
            if start == end:
                tree[node] = (1, ch, ch, 1, 1, 1)
                return
            mid = (start + end) // 2
            if idx <= mid:
                update(2 * node, start, mid, idx, ch)
            else:
                update(2 * node + 1, mid + 1, end, idx, ch)
            tree[node] = merge(tree[2 * node], tree[2 * node + 1])
        build(1, 0, n - 1)
        result = []
        for ch, idx in zip(queryCharacters, queryIndices):
            arr[idx] = ch
            update(1, 0, n - 1, idx, ch)
            result.append(tree[1][5])
        return result