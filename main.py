from  get_sudoku_board import get_sudoku_board
from solveSudoku import solveSudoku
if __name__ == "__main__":
    board=get_sudoku_board()
    print('Given board:')
    for row in board:
        print(' '.join(map(str,row)))

    if solveSudoku(board):
        print('The resultant sudoku is:')
        for i in range(9):
            for j in range(9):
                print(board[i][j],end=' ')
            print()
    else:
        print('NO SOLUTION IS EXISTS FOR THE GIVEN SUDOKU')
