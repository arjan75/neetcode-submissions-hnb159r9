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
        keys = list(freqMap.keys())
        # print (keys)

        for i in range(k):
            heapq.heappush(heap, [freqMap[keys[i]], keys[i]])
        
        
        for j in range(k, len(keys)):
            if freqMap[keys[j]] > heap[0][0]:
                heapq.heappush(heap, [freqMap[keys[j]], keys[j]])
                heapq.heappop(heap)
        
        output = []

        while heap:
            item = heapq.heappop(heap)
            output.append(item[1])
        return output[::-1]




            


        