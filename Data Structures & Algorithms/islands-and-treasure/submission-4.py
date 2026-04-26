class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid:
            return grid

        
        length = len(grid)
        breath = len(grid[0])
        queue = []
        for i in range(length):
            for j in range(breath):
                if grid[i][j] == 0:
                    queue.append([i, j])
        
        visited = set()
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        distance = 0

        while queue:
            for _ in range(len(queue)):
                current = queue.pop(0)
                currentX = current[0]
                currentY = current[1]

                visited.add((currentX, currentY))

                if grid[currentX][currentY] == 2147483647:
                    grid[currentX][currentY] = distance

                for direction in directions:
                    newX = currentX + direction[0]
                    newY = currentY + direction[1]

                    if newX < 0 or newY < 0 or newX >= length or newY >= breath or (newX, newY) in visited or grid[newX][newY] == -1:
                        continue
                    
                    queue.append([newX, newY])
            distance += 1
        



        