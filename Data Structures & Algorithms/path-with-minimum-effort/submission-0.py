import heapq

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        length = len(heights)
        breath = len(heights[0])
        if heights == []:
            return 0

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        minHeap = []
        heapq.heappush(minHeap, [0, 0, 0])
        visited = set()

        while minHeap:
            item = heapq.heappop(minHeap)
            diff = item[0]
            itemRow = item[1]
            itemCol = item[2]
            
            if itemRow == length-1 and itemCol == breath-1:
                return diff
            
            if (itemRow, itemCol) in visited:
                continue

            visited.add((itemRow, itemCol))
            
            for direction in directions:
                newRow = itemRow + direction[0]
                newCol = itemCol + direction[1]

                if (newRow < 0 or newCol < 0 or newRow == length or newCol == breath or (newRow, newCol) in visited):
                    continue

                effortDiff = abs(heights[newRow][newCol] - heights[itemRow][itemCol])
                maxDiff = max(effortDiff, diff)
            
                heapq.heappush(minHeap, [maxDiff, newRow, newCol])
             
        
            
            






        


        