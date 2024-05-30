class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        l1=len(nums1)+1
        l2=len(nums2)+1
        dp=[[0]*l2 for _ in range(l1)]
        for i in range(l1):
            for j in range(l2):
                if i==0 or j==0:
                    dp[i][j]=0
                elif nums1[i-1]==nums2[j-1]:
                    dp[i][j]=1+dp[i-1][j-1]
                else:
                    dp[i][j]=max(dp[i][j-1],dp[i-1][j])
        return dp[l1-1][l2-1]            