import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        for num in nums:
            if num in frequency:
                frequency[num] += 1
            else:
                frequency[num] = 1
        
        freqHeap = []
        for key in frequency:
            heapq.heappush(freqHeap, (-frequency[key], key))
        
        i = 0
        output = []
        while i < k:
            item = heapq.heappop(freqHeap)
            output.append(item[1])
            i += 1
        return output

        