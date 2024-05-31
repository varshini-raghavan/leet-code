class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        m+=1
        n+=1
        dp=[[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i==1 and j==1:
                    dp[i][j]=1
                elif i==0 or j==0:
                    dp[i][j]=0
                else:
                    dp[i][j]=dp[i-1][j]+dp[i][j-1]
        return dp[m-1][n-1]