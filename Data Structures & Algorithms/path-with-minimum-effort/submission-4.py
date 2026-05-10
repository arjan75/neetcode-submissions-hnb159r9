import heapq
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        heap = []
        heapq.heappush(heap, [0, 0, 0])
        visited = set()
        length = len(heights)
        breath = len(heights[0])

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        while heap:
            cell = heapq.heappop(heap)
            cellDiff = cell[0]
            cellRow = cell[1]
            cellCol = cell[2]

            if cellRow == length - 1 and cellCol == breath - 1:
                return cellDiff

            if (cellRow, cellCol) in visited:
                continue
            
            visited.add((cellRow, cellCol))

            for direction in directions:
                newRow = cellRow + direction[0]
                newCol = cellCol + direction[1]

                if newRow >= 0 and newRow < length and newCol >= 0 and newCol < breath:
                    maxDiff = max(cellDiff, abs(heights[newRow][newCol] - heights[cellRow][cellCol]))
                    heapq.heappush(heap, [maxDiff, newRow, newCol])
            







        