import heapq
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        heap = []
        length = len(heights)
        breath = len(heights[0])

        if heights == []:
            return 0

        heapq.heappush(heap, [0, 0, 0])
        visited = set()
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while heap:
            currentItem = heapq.heappop(heap)
            currentItemDiff = currentItem[0]
            currentItemRow = currentItem[1]
            currentItemCol = currentItem[2]

            if currentItemRow == length-1 and currentItemCol == breath-1:
                return currentItemDiff
            
            if (currentItemRow, currentItemCol) in visited:
                continue
            
            visited.add((currentItemRow, currentItemCol))

            for direction in directions:
                newRow = currentItemRow + direction[0]
                newCol = currentItemCol + direction[1]
            
                if newRow < 0 or newCol < 0 or newRow >= length or newCol >= breath or (newRow, newCol) in visited:
                    continue
                
                diff = abs(heights[newRow][newCol]-heights[currentItemRow][currentItemCol])
                maxDiffSoFar = max(diff, currentItemDiff)
                heapq.heappush(heap, [maxDiffSoFar, newRow, newCol])
            


                

            






        