class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def safe(board: List[List[str]],row : int,col : int,digit:str):
            for i in range(9):
                if board[row][i]==digit and i != col:
                    return False
            for i in range(9):
                if board[i][col]==digit and i!= row:
                    return False
            srow=floor(row/3)*3
            scol=floor(col/3)*3
            for i in range(srow,srow+3):
                for j in range(scol,scol+3):
                    if board[i][j]==digit and i!=row and j!=col: return False
            return True
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    if(safe(board,i,j,board[i][j])==False):
                        return False
        return True

