# To change the sudoku board for this file, change this
board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]

def solve(board: list) -> bool:
    """Solves the board using backtracking algorithm and recursion.

    Args:
        board (list): Main sudoku board.

    Returns:
        bool: True if there's no empty spaces left (board has been solved), otherwise False.
    """
    # uncomment this to see step by step
    # print(board)

    find = find_empty(board)
    if not find:  # base case for recursion
        return True
    else:
        row, col = find

    for num in range(1,10):
        if valid(board, num, (row, col)):
            board[row][col] = num

            if solve(board):
                return True

            board[row][col] = 0

    return False


def valid(board: list, num: int, position: tuple) -> bool:
    """Checks if the game is still valid after inserting the number.

    Args:
        board (list): Main sudoku board.
        num (int): Number that was inserted recently.
        position (tuple): [description]

    Returns:
        bool: True if valid, otherwise False.
    """
    # Check row
    for i in range(len(board[0])):
        if board[position[0]][i] == num and position[1] != i:
            return False

    # Check column
    for i in range(len(board)):
        if board[i][position[1]] == num and position[0] != i:
            return False

    # Check box
    box_x = position[1] // 3
    box_y = position[0] // 3
    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if board[i][j] == num and (i,j) != position:
                return False

    return True


def print_board(board: list):
    """Prints the sudoku board in a more readable form.

    Args:
        board (list): Main Sudoku board.
    """
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")


def find_empty(board: list) -> tuple:
    """Finds an empty space on the sudoku board.

    Args:
        board (list): Main Sudoku board.

    Returns:
        tuple: Indexes (row, column) of the empty space.
    """
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)  # row, col

    return None


if __name__ == '__main__':
    print_board(board)
    print("-------------------------")
    print("Solving...")
    print("-------------------------")
    solve(board)
    print_board(board)
