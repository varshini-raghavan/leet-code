class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        nums2=list(set(nums))
        nums2.sort()
        m=len(nums)+1
        n=len(nums2)+1
        dp=[[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i==0 or j==0:
                    dp[i][j]=0
                elif nums[i-1]==nums2[j-1]:
                    dp[i][j]=1+dp[i-1][j-1]
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])
        #print(dp)
        return dp[m-1][n-1]
        