class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        length = len(grid)
        breath = len(grid[0])

        def shortestPath(i, j):
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

            queue = [[i, j]]
            distance = 0
            visited = set()
            visited.add((i, j))
            while queue:
                for _ in range(len(queue)):
                    current = queue.pop(0)
                    curX = current[0]
                    curY = current[1]

                    if grid[curX][curY] == 0:
                        return distance

                    for direction in directions:
                        newX = curX + direction[0]
                        newY = curY + direction[1]

                        if (newX, newY) in visited or newX < 0 or newX >= length or newY < 0 or newY >= breath or grid[newX][newY] == -1:
                            continue
                        
                        visited.add((newX, newY))
                        queue.append([newX, newY])
                distance += 1
            return -1   


        for i in range(length):
            for j in range(breath):
                if grid[i][j] == 2147483647:
                    shortestDistance = shortestPath(i, j)
                    if shortestDistance != -1:
                        grid[i][j] = shortestDistance

        
        
        