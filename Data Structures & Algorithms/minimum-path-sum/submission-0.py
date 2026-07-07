class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        length = len(grid)
        breath = len(grid[0])

        dp = [[0]* breath for _ in range(length)]
        dp[0][0] = grid[0][0]

        for i in range(1, length):
            dp[i][0] = dp[i-1][0] + grid[i][0]

        for j in range(1, breath):
            dp[0][j] = dp[0][j-1] + grid[0][j]

        for i in range(1, length):
            for j in range(1, breath):
                dp[i][j] = min(dp[i-1][j]+grid[i][j], dp[i][j-1]+grid[i][j])
        return dp[-1][-1]   