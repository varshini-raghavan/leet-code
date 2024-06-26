class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        total=0
        n=len(mat)
        for i in range(n):
            total=total+mat[i][i]
            print(total)
        for i in range(n):
            total=total+mat[i][n-1-i]
            print(total)
        if n%2==1:
            j=n//2
            total-=mat[j][j]
        return total