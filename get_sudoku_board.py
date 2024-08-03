def get_sudoku_board():
    board = []
    print("Enter the Sudoku board row by row. Use '0' for empty cells.")
    for i in range(9):
        while True:
            row = input(f"Enter row {i + 1} (9 digits):")
            if len(row) == 9 and all(c.isdigit() for c in row):
                board.append([int(c) for c in row])
                break
            else:
                print("Invalid input. Please enter exactly 9 digits(0-9).")
    return board