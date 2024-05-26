class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        def safe(board: List[List[str]],row : int,col : int,digit:str):
            for i in range(9):
                if board[row][i]==digit or board[i][col]==digit:
                    return False
            srow=floor(row/3)*3
            scol=floor(col/3)*3
            for i in range(srow,srow+3):
                for j in range(scol,scol+3):
                    if board[i][j]==digit: return False
            return True
        def solve(board: List[List[str]],row : int,col : int):
            if row==8 and col==9:
                print("complete")
                return True
            else:
                if col==9:
                    row+=1
                    col=0
                if(board[row][col]=="."):
                    #digits=['1','2','3','4','5','6','7','8','9']
                    for i in range(1,10):
                        if safe(board,row,col,str(i)):
                            board[row][col]=str(i)
                            #print(board[row][col])
                            if solve(board,row,col+1):
                                return True
                            else:
                                board[row][col]="."
                    return False
                else:
                    return solve(board,row,col+1)
        solve(board,0,0)

        