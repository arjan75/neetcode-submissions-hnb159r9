class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        length = len(grid)
        breadth = len(grid[0])

        def bfs(i, j):
            queue = [[i, j]]
            distance = 0
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            visited = set()
            while queue:
                for _ in range(len(queue)):
                    current = queue.pop(0)
                    currentX = current[0]
                    currentY = current[1]

                    if grid[currentX][currentY] == 0:
                        return distance
                    
                    for direction in directions:
                        newX = currentX + direction[0]
                        newY = currentY + direction[1]

                        if newX >= 0 and newX < length and newY >= 0 and newY < breadth:
                            if (newX, newY) not in visited and grid[newX][newY] != -1:
                                queue.append([newX, newY])
                                visited.add((newX, newY))
                distance += 1
            
            return 2147483647

        for i in range(length):
            for j in range(breadth):
                if grid[i][j] == 2147483647:
                    minDistance = bfs(i, j)
                    grid[i][j] = minDistance
        
        