class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        n = len(apples)
        heap = []
        eaten = 0
        day = 0
        while day < n or heap:
            if day < n and apples[day] > 0:
                heapq.heappush(heap, (day + days[day], apples[day]))
            while heap and heap[0][0] <= day:
                heapq.heappop(heap)
            if heap:
                expiry, count = heapq.heappop(heap)
                eaten += 1
                if count - 1 > 0:
                    heapq.heappush(heap, (expiry, count - 1))
            day += 1
        return eaten