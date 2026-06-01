from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        length = len(grid)
        breath = len(grid[0])

        queue = deque()
        numberOfFreshFruits = 0
        visited = set()
        for i in range(length):
            for j in range(breath):
                if grid[i][j] == 1:
                    numberOfFreshFruits += 1
                
                if grid[i][j] == 2:
                    queue.append((i, j))
                    visited.add((i, j))

        if numberOfFreshFruits == 0:
            return 0
        
        directions = [[0,1], [0,-1], [1, 0], [-1, 0]]
        time = 0
        while queue:
            for _ in range(len(queue)):
                cell = queue.popleft()
                cellX = cell[0]
                cellY = cell[1]
                
                for direction in directions:
                    newX = cellX + direction[0]
                    newY = cellY + direction[1]

                    if newX >= 0 and newX < length and newY >= 0 and newY < breath and (newX, newY) not in visited and grid[newX][newY] == 1:
                        queue.append((newX, newY))
                        visited.add((newX, newY))
                        numberOfFreshFruits -= 1
                        grid[newX][newY] = 2
            time += 1
        
        if numberOfFreshFruits == 0:
            return time-1
        return -1



        

        

        