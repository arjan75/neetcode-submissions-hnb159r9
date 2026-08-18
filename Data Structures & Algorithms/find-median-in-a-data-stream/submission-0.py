import heapq 

class MedianFinder:

    def __init__(self):
        self.higher = []
        self.lower = []
        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.lower, -num)

        if self.lower and self.higher and -self.lower[0] > self.higher[0]:
            heapq.heappush(self.higher, -heapq.heappop(self.lower))
        
        if len(self.higher) - len(self.lower) > 1:
            heapq.heappush(self.lower, -heapq.heappop(self.higher))
        
        if len(self.lower) - len(self.higher) > 1:
            heapq.heappush(self.higher, -heapq.heappop(self.lower))
        
        
    def findMedian(self) -> float:
        higherlength = len(self.higher)
        lowerlength = len(self.lower)

        if higherlength > lowerlength:
            return self.higher[0]
        
        if higherlength < lowerlength:
            return -self.lower[0]
        

        return (-self.lower[0] + self.higher[0])/2
            
        
        