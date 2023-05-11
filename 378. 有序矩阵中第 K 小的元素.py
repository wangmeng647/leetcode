import heapq

class Solution:
    def kthSmallest(self, matrix, k: int) -> int:
        l = []
        for row in matrix:
            l += row
        heapq.heapify(l)
        for _ in range(k - 1):
            heapq.heappop(l)

        return heapq.heappop(l)