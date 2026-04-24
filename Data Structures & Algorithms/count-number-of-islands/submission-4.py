class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        length = len(grid)
        breath = len(grid[0])
        countIslands = 0
        visited = set()


        def visitIsland(i, j):
            if i < 0 or j < 0 or i >= length or j >= breath or (i, j) in visited or grid[i][j] != "1":
                return
            
            visited.add((i, j))

            visitIsland(i+1, j)
            visitIsland(i-1, j)
            visitIsland(i, j+1)
            visitIsland(i, j-1)

        for i in range(length):
            for j in range(breath):
                if (i, j) not in visited and grid[i][j] == "1":
                    visitIsland(i, j)
                    countIslands += 1
        return countIslands

            
        