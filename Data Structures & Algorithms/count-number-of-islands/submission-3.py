class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        length = len(grid)
        breadth = len(grid[0])
        numberOfIslands = 0

        visited = set()

        def markIsland(i, j):
            if i < 0 or j < 0 or i >= length or j >= breadth or grid[i][j] != "1":
                return
            
            grid[i][j] = "X"
            markIsland(i+1, j)
            markIsland(i-1, j)
            markIsland(i, j+1)
            markIsland(i, j-1)
        
        for i in range(length):
            for j in range(breadth):
                if grid[i][j] == "1":
                    if (i, j) not in visited:
                        markIsland(i, j)
                        numberOfIslands += 1
        return numberOfIslands

        


        