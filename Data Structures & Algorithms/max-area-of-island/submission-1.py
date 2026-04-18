class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        length = len(grid)
        breath = len(grid[0])
        maxArea = 0

        visited = set()
        def getIslandSize(i, j):
            if i < 0 or j < 0 or i >= length or j >= breath or (i, j) in visited or grid[i][j] != 1:
                return 0
            
            visited.add((i, j))
            return 1 + getIslandSize(i+1, j) + getIslandSize(i-1, j) + getIslandSize(i, j+1) + getIslandSize(i, j-1)
        

        for i in range(length):
            for j in range(breath):
                if grid[i][j] == 1 and (i, j) not in visited:
                    area = getIslandSize(i, j)
                    maxArea = max(area, maxArea)
        return maxArea
        