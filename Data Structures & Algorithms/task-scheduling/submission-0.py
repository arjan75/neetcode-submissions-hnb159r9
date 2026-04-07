
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        heap = []
        frequencies = {}
        for task in tasks:
            if task in frequencies:
                frequencies[task] += 1
            else:
                frequencies[task] = 1
        
        queue = []

        for item in frequencies:
            heapq.heappush(heap, -frequencies[item])

        time = 0
        while heap or queue:
            if heap:
                item = heapq.heappop(heap) + 1
                if not item == 0:
                    queue.append((item, time+n))
            
            if queue:
                if queue[0][1] <= time:
                    item = queue.pop(0)
                    heapq.heappush(heap, item[0])
            time += 1
        
        return time






        