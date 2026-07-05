class Solution:
    def isPossible(self, target: List[int]) -> bool:
        total = sum(target)
        heap = [-x for x in target]
        heapq.heapify(heap)
        while True:
            largest = -heapq.heappop(heap)
            if largest == 1:
                return True
            rest = total - largest
            if rest == 0:
                return False
            prev = largest % rest
            if prev == 0:
                prev = rest
            if prev == largest:
                return False
            total = rest + prev
            heapq.heappush(heap, -prev)