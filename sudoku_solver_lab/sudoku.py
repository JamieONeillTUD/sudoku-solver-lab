def solve_sudoku(board):
    """
    Solves a Sudoku puzzle using backtracking.
    Args:
        board (list): A 9x9 list representing the Sudoku board. 
                      Empty cells should be filled with 0.
    Returns:
        list: Solved board as a 9x9 list, or None if the board is unsolvable.
    Raises:
        ValueError: If the board is not a valid 9x9 list.
    """

    def is_valid_move(board, row, col, num):
        """Checks if placing 'num' in (row, col) is valid."""
        for i in range(9):
            if board[row][i] == num or board[i][col] == num:
                return False

        subgrid_row, subgrid_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(subgrid_row, subgrid_row + 3):
            for j in range(subgrid_col, subgrid_col + 3):
                if board[i][j] == num:
                    return False

        return True

    def solve(board):
        """Recursively solves the board using backtracking."""
        for row in range(9):
            for col in range(9):
                if board[row][col] == 0:
                    for num in range(1, 10):
                        if is_valid_move(board, row, col, num):
                            board[row][col] = num
                            if solve(board):
                                return True
                            board[row][col] = 0
                    return False
        return True

    if not isinstance(board, list) or len(board) != 9 or any(len(row) != 9 for row in board):
        raise ValueError("Invalid board format. Must be a 9x9 list.")

    if not solve(board):
        return None

    return board
