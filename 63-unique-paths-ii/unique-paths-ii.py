class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m=len(obstacleGrid)
        n=len(obstacleGrid[0])
        m+=1
        n+=1
        dp=[[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i-1][j-1]==1:
                    dp[i][j]=0
                elif i==0 or j==0:
                    dp[i][j]=0
                elif i==1 and j==1:
                    dp[i][j]=1
                else:
                    dp[i][j]=dp[i-1][j]+dp[i][j-1]
        return dp[m-1][n-1]