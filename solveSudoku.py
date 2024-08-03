
def isvaild(board,row,col,c):
    for i in range(9):
        if board[i][col]==c:
            return False
        if board[row][i]==c:
            return False
        if board[3*(row//3)+i//3][3*(col//3)+i%3]==c:
            return False
    return True

def solveSudoku(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j]==0:
                for c in range(1,10):
                    if isvaild(board,i,j,c):
                        board[i][j]=c
                        if solveSudoku(board):
                            return True
                        else:
                            board[i][j]=0
                return False
    return True