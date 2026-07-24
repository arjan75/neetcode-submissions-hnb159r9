import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for i in range(k):
            point = points[i]
            distance = (point[0]*point[0]) + (point[1]*point[1])
            heapq.heappush(heap, (-distance, point))

        
        for j in range(k, len(points)):
            point = points[j]
            distance = (point[0]*point[0]) + (point[1]*point[1])
            if -heap[0][0] > distance:
                heapq.heappop(heap)
                heapq.heappush(heap, (-distance, point))

        
        output = []
        while heap:
            item = heapq.heappop(heap)
            output.append(item[1])
        return output


        