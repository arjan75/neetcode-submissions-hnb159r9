class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        length = len(grid)
        breadth = len(grid[0])
    
        def traverseIsland(i, j):
            if (i, j) in visited or i < 0 or j < 0 or i >= length or j >= breadth or grid[i][j] != 1:
                return 0
            visited.add((i, j))
            return 1 + traverseIsland(i+1, j) + traverseIsland(i-1, j) + traverseIsland(i, j+1) + traverseIsland(i, j-1)

        
        maxArea = 0
        for i in range(length):
            for j in range(breadth):
                area = traverseIsland(i, j)
                maxArea = max(maxArea, area)
        return maxArea
                

            

        
        