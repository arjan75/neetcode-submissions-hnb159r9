from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        length = len(grid)
        breath = len(grid[0])
        numberOfFresh = 0
        queue = deque()
        visited = set()
        for i in range(length):
            for j in range(breath):
                if grid[i][j] == 1:
                    numberOfFresh += 1
                
                if grid[i][j] == 2:
                    queue.append((i, j))
                    visited.add((i, j))

        if numberOfFresh == 0:
            return 0

        time = 0
        directions = [[0,1], [0, -1], [1, 0], [-1, 0]]
        while queue:
            for _ in range(len(queue)):
                rotten = queue.popleft()
                rottenX = rotten[0]
                rottenY = rotten[1]

                for direction in directions:
                    newX = rottenX + direction[0]
                    newY = rottenY + direction[1]

                    if newX >= 0 and newX < length and newY >= 0 and newY < breath and (newX, newY) not in visited and grid[newX][newY] == 1:
                        queue.append((newX, newY))
                        visited.add((newX, newY))

                        grid[rottenX][rottenY] = 2
                        numberOfFresh -= 1
            time += 1

        if numberOfFresh == 0:
            return time-1
        return -1


        

                
            
                


        