import heapq
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        if not heights:
            return 0

        length = len(heights)
        breath = len(heights[0])
        heap = []

        heapq.heappush(heap, [0, 0, 0])
        visited = set()

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        while heap:
            cell = heapq.heappop(heap)
            diff = cell[0]
            cellX = cell[1]
            cellY = cell[2]
        
            if cellX == length-1 and cellY == breath-1:
                return diff
            
            if (cellX, cellY) in visited:
                continue

            visited.add((cellX, cellY))
            
            for direction in directions:
                newX = cellX + direction[0]
                newY = cellY + direction[1]

                if newX < 0 or newY < 0 or newX >= length or newY >= breath or (newX, newY) in visited:
                    continue
                
                newDiff = max(diff, abs(heights[newX][newY]-heights[cellX][cellY]))
                heapq.heappush(heap, [newDiff, newX, newY])
                


            

            
            



        