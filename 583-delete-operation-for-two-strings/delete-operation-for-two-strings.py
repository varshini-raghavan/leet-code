class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        l1=len(word1)+1
        l2=len(word2)+1
        dp = [[0] * l2 for _ in range(l1)]
        for r in range(l1):
            for c in range(l2):
                if r==0 or c==0:
                    dp[r][c]=0
                elif word1[r-1]==word2[c-1]:
                    dp[r][c]=1+dp[r-1][c-1]
                else:
                    dp[r][c]=max(dp[r][c-1],dp[r-1][c])
        return l1+l2-2-2*dp[l1-1][l2-1]