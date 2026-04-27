class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        length = len(grid)
        breath = len(grid[0])
        islands = 0
        visited = set()

        def markIsland(i, j):
            if i <0 or j <0 or i >= length or j >= breath or grid[i][j] != "1" or (i, j) in visited:
                return
            
            visited.add((i, j))
            markIsland(i+1, j)
            markIsland(i-1, j)
            markIsland(i, j+1)
            markIsland(i, j-1)
        

        for i in range(length):
            for j in range(breath):
                if grid[i][j] == "1" and (i, j) not in visited:
                    markIsland(i, j)
                    islands += 1
        return islands

        