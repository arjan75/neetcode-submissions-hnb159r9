class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        length = len(grid)
        breath = len(grid[0])

        queue = []
        fresh = 0
        for i in range(length):
            for j in range(breath):
                if grid[i][j] == 2:
                    queue.append([i, j])
                
                if grid[i][j] == 1:
                    fresh += 1
                
        time = 0
        directions = [[0,1], [0, -1], [1, 0], [-1, 0]]
        while queue and fresh > 0:
            for i in range(len(queue)):
                rotten = queue.pop(0)
                rottenX = rotten[0]
                rottenY = rotten[1]


                for direction in directions:
                    newX = rottenX + direction[0]
                    newY = rottenY + direction[1]

                    if newX < 0 or newY < 0 or newX >= length or newY >= breath or grid[newX][newY] != 1:
                        continue
                    
                    queue.append([newX, newY])
                    grid[newX][newY] = 2
                    fresh -= 1

            time += 1
        if fresh == 0:
             return time
        return -1






        