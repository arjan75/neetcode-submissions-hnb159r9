from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        length = len(grid)
        breath = len(grid[0])

        queue = deque()
        visited = set()
        for i in range(length):
            for j in range(breath):
                if grid[i][j] == 0:
                    queue.append((i, j))
                    visited.add((i, j))
                
        directions = [[0,1], [0, -1], [1, 0], [-1, 0]]
        distance = 0
        while queue:
            for _ in range(len(queue)):
                cell = queue.popleft()
                cellRow = cell[0]
                cellCol = cell[1]

                if grid[cellRow][cellCol] == 2147483647:
                    grid[cellRow][cellCol] = distance

                for direction in directions:
                    newRow = cellRow + direction[0]
                    newCol = cellCol + direction[1]

                    if newRow < 0 or newRow >= length or newCol < 0 or newCol >= breath or (newRow, newCol) in visited or grid[newRow][newCol] == -1:
                        continue
                    
                    queue.append((newRow, newCol))
                    visited.add((newRow, newCol))
            distance += 1
            






        