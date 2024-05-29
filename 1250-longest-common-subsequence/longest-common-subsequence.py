class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        l1=len(text1)+1
        l2=len(text2)+1
        dp = [[-1] * l2 for _ in range(l1)]
        for r in range(l1):
            for c in range(l2):
                if r==0 or c==0:
                    dp[r][c]=0
                elif text1[r-1]==text2[c-1]:
                    dp[r][c]=1+dp[r-1][c-1]
                else:
                    dp[r][c]=max(dp[r][c-1],dp[r-1][c])
            #print(dp)
        print(dp)
        return dp[l1-1][l2-1]