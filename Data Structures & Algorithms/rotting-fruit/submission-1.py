class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        length = len(grid)
        breadth = len(grid[0])

    

        queue = []
        fresh = 0
        for i in range(length):
            for j in range(breadth):
                if grid[i][j] == 2:
                    queue.append([i, j])
                if grid[i][j] == 1:
                    fresh += 1
        
        directions = [[0,1], [0, -1], [1, 0], [-1, 0]]

        time = 0
        while queue and fresh > 0:
            for i in range(len(queue)):
                orange = queue.pop(0)
                for direction in directions:
                    newX = orange[0] + direction[0]
                    newY = orange[1] + direction[1]
                    
                    if newX < 0 or newY < 0 or newX >= length or newY >= breadth or grid[newX][newY] != 1:
                        continue
                    
                    # Landed on a clean fruit 
                    
                    grid[newX][newY] = 2
                    queue.append([newX, newY])
                    fresh -= 1
            time += 1
        
        if fresh == 0:
            return time
        return -1

        


        