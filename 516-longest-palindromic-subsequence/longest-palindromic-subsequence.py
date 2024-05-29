class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        rev=s[::-1]
        l1=len(s)+1
        l2=len(rev)+1
        dp = [[-1] * l2 for _ in range(l1)]
        for r in range(l1):
            for c in range(l2):
                if r==0 or c==0:
                    dp[r][c]=0
                elif s[r-1]==rev[c-1]:
                    dp[r][c]=1+dp[r-1][c-1]
                else:
                    dp[r][c]=max(dp[r][c-1],dp[r-1][c])
        return dp[l1-1][l2-1]