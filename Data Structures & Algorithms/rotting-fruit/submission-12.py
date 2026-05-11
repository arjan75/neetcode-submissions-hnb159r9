from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        length = len(grid)
        breath = len(grid[0])
        queue = deque()
        fresh = 0
        rottenn = 0

        visited = set()

        for i in range(length):
            for j in range(breath):
                if grid[i][j] == 2:
                    queue.append((i, j))
                    visited.add((i, j))
                
                if grid[i][j] == 1:
                    fresh += 1
        
        if fresh == 0:
            return 0
                

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        distance = 0

        while queue:
            for _ in range(len(queue)):
                cell = queue.popleft()
                cellRow = cell[0]
                cellCol = cell[1]

                for direction in directions:
                    newRow = cellRow + direction[0]
                    newCol = cellCol + direction[1]

                    if newRow >= 0 and  newRow < length and newCol >= 0 and newCol < breath and (newRow, newCol) not in visited and grid[newRow][newCol] == 1:
                        visited.add((newRow, newCol))
                        queue.append((newRow, newCol))
                        fresh -= 1
                        grid[newRow][newCol] = 2

            distance += 1
        
        if fresh > 0:
            return -1
        return distance-1
        

        