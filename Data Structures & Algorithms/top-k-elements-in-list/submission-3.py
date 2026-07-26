import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap = {}
        for num in nums:
            if num in freqMap:
                freqMap[num] += 1
            else:
                freqMap[num] = 1
        

        heap = []
        for key in freqMap:
            heapq.heappush(heap, (freqMap[key], key))
            if len(heap) > k:
                heapq.heappop(heap)
        
        output = []
        while heap:
            item = heapq.heappop(heap)
            output.append(item[1])
        return output[::-1]




            


        