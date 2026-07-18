from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        length = len(grid)
        breath = len(grid[0])

        fresh = 0
        queue = deque()
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
        minutes = 0 

        while queue:
            for _ in range(len(queue)):
                cell = queue.popleft()
                cellX = cell[0]
                cellY = cell[1]

                for direction in directions:
                    newX = cellX + direction[0]
                    newY = cellY + direction[1]

                    if newX >= 0 and newY >= 0 and newX < length and newY < breath and (newX, newY) not in visited and grid[newX][newY] == 1:
                        if grid[newX][newY] == 1:
                            grid[newX][newY] = 2
                            fresh -= 1

                        queue.append((newX, newY))
                        visited.add((newX, newY))
    
            minutes += 1
        if fresh == 0:
            return minutes-1
        return -1


                

                
        