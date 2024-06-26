import heapq

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        prj = [(capital[i], profits[i]) for i in range(len(profits))]
        prj.sort()
        max_heap = []
        i = 0

        for _ in range(k):
            while i < len(profits) and prj[i][0] <= w:
                heapq.heappush(max_heap, -prj[i][1])
                i += 1
            if not max_heap:
                break
            w -= heapq.heappop(max_heap)

        return w