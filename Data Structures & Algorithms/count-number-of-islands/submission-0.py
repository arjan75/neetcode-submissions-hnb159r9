class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        visited = set()
        def traverseIsland(i, j):
            if i < 0 or j < 0 or i >= rows or j >= cols or (i, j) in visited or grid[i][j] != "1":
                return 
            
            grid[i][j] = "X"
            visited.add((i, j))
            traverseIsland(i+1, j)
            traverseIsland(i-1, j)
            traverseIsland(i, j+1)
            traverseIsland(i, j-1)


        countIslands = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and (i, j) not in visited:
                    traverseIsland(i, j)
                    countIslands += 1
        return countIslands

        