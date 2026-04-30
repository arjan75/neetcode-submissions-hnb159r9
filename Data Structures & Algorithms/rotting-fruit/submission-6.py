class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        length = len(grid)
        breath = len(grid[0])

        queue = []
        numberOfRottenOranges = 0
        numberOfFreshOranges = 0
        for i in range(length):
            for j in range(breath):
                if grid[i][j] == 2:
                    queue.append([i, j])
                    numberOfRottenOranges += 1
                
                if grid[i][j] == 1:
                    numberOfFreshOranges += 1

        if numberOfFreshOranges == 0:
            return 0
        
        countOrangesFound = 0
        directions = [[0,1], [0, -1], [1, 0], [-1, 0]]
        distance = 0
        while queue:
            for _ in range(len(queue)):
                cell = queue.pop(0)
                cellX = cell[0]
                cellY = cell[1]

                for direction in directions:
                    newX = cellX + direction[0]
                    newY = cellY + direction[1]


                    if newX < 0 or newY < 0 or newX >= length or newY >= breath or grid[newX][newY] != 1:
                        continue
                    
                    grid[newX][newY] = 2
                    queue.append([newX, newY])
                    countOrangesFound += 1
            distance += 1

        if countOrangesFound == numberOfFreshOranges:
            return distance-1
        return -1


            



                

        