import heapq

class MedianFinder:

    def __init__(self):
        self.max_heap = []
        self.min_heap = []

    def addNum(self, num: int) -> None:
        if self.max_heap and num < -self.max_heap[0]:
            heapq.heappush(self.max_heap, -num)
        else:
            heapq.heappush(self.min_heap, num)
        if len(self.min_heap) - len(self.max_heap) == 2:
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))
        elif len(self.max_heap) - len(self.min_heap) == 2:
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
    def findMedian(self) -> float:
        if len(self.min_heap) > len(self.max_heap):
            return self.min_heap[0]
        elif len(self.min_heap) < len(self.max_heap):
            return -self.max_heap[0]
        else:
            return (self.min_heap[0] + -self.max_heap[0]) / 2



#2
class MedianFinder2:

    def __init__(self):
        self.big = []
        self.small = []

    def addNum(self, num: int) -> None:
        if not self.big or num >= self.big[0]:
            heapq.heappush(self.big, num)
        else:
            heapq.heappush(self.small, -num)
        if abs(len(self.big) - len(self.small)) == 2:
            if len(self.big) > len(self.small):
                heapq.heappush(self.small, -heapq.heappop(self.big))
            else:
                heapq.heappush(self.big, -heapq.heappop(self.small))

    def findMedian(self) -> float:
        if len(self.big) > len(self.small):
            return self.big[0]
        elif len(self.big) < len(self.small):
            return -self.small[0]
        else:
            return (self.big[0] - self.small[0]) / 2



f = MedianFinder2()
f.addNum(-1)
f.addNum(-2)
print(f.findMedian())
f.addNum(-3)
print(f.findMedian())