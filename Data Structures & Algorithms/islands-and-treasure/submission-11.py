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


                
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        distance = 0
        while queue:
            for _ in range(len(queue)):
                cell = queue.popleft()
                cellX = cell[0]
                cellY = cell[1]

                if grid[cellX][cellY] == 2147483647:
                    grid[cellX][cellY] = distance

                for direction in directions:
                    newX = cellX + direction[0]
                    newY = cellY + direction[1]

                    if newX >= 0 and newX < length and newY >= 0 and newY < breath and grid[newX][newY] != -1 and (newX, newY) not in visited:
                        visited.add((newX, newY))
                        queue.append((newX, newY))

            distance += 1





                    
            

        