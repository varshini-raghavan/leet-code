class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n=len(board)
        m=len(board[0])
        def solve(board,word,wi,n,m,i,j):
            if i==-1 or j==-1 or i==n or j==m or board[i][j]=="*":
                return False
            if wi<len(word) and board[i][j]!=word[wi]:
                return False
            if wi==len(word)-1:
                print("found")
                return True 
            else:
                temp= board[i][j]
                board[i][j]="*"
                res=(solve(board,word,wi+1,n,m,i+1,j)
                or solve(board,word,wi+1,n,m,i,j+1)
                or solve(board,word,wi+1,n,m,i-1,j)
                or solve(board,word,wi+1,n,m,i,j-1))
                board[i][j]=temp
                return res   
        for i in range(n):
            for j in range(m):
                if board[i][j]==word[0]:
                    flag=solve(board,word,0,n,m,i,j)
                    if flag == True:
                        return True
        return False