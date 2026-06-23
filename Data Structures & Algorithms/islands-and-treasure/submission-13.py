from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        queue = deque()
        length = len(grid)
        breath = len(grid[0])
        visited = set()
        for i in range(length):
            for j in range(breath):
                if grid[i][j] == 0:
                    queue.append([i, j])
                    visited.add((i, j))


        distance = 0
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while queue:
            for _ in range(len(queue)):
                current = queue.popleft()
                currentX = current[0]
                currentY = current[1]

                if grid[currentX][currentY] == 2147483647:
                    grid[currentX][currentY] = distance
                
                for direction in directions:
                    newX = currentX + direction[0]
                    newY = currentY + direction[1]

                    if newX >= 0 and newX < length and newY >= 0 and newY < breath and (newX, newY) not in visited and grid[newX][newY] != -1:
                        queue.append((newX, newY))
                        visited.add((newX, newY))
            distance += 1
        
                


                
        