import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for point in points:
            distance = (point[0]*point[0]) + (point[1]*point[1])
            heapq.heappush(heap, (distance, point))
        
        i = 0
        output = []
        while i < k:
            item = heapq.heappop(heap)
            output.append(item[1])
            i += 1
        return output


        