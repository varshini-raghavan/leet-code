class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        def value(board,row,col,i,j):
            if i<0 or j<0 or i>row or j>col or board[i][j]==0 or board[i][j]==3:
                return 0
            return 1
        row=len(board)-1
        col=len(board[0])-1
        for i in range(0,row+1):
            for j in range(0,col+1):
                sum=0
                sum+=value(board,row,col,i-1,j)+value(board,row,col,i+1,j)
                sum+=value(board,row,col,i,j-1)+value(board,row,col,i,j+1)
                sum+=value(board,row,col,i-1,j-1)+value(board,row,col,i+1,j+1)
                sum+=value(board,row,col,i-1,j+1)+value(board,row,col,i+1,j-1)
                if board[i][j]==1:
                    if sum!=2 and sum!=3:
                        board[i][j]=2
                if board[i][j]==0:
                    if sum==3:
                        board[i][j]=3
        for i in range(0,row+1):
            for j in range(0,col+1):
                if board[i][j]==2:
                    board[i][j]=0
                if board[i][j]==3:
                    board[i][j]=1



        