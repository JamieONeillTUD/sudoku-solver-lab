import unittest
from sudoku import solve_sudoku

class TestSudokuSolver(unittest.TestCase):
    """
    Unit tests for the solve_sudoku function.
    """

    def test_valid_board(self):
        """Test solving a valid Sudoku board."""
        board = [
            [5, 3, 0, 0, 7, 0, 0, 0, 0],
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 9]
        ]
        solution = solve_sudoku(board)
        self.assertIsNotNone(solution)  # The board should be solvable

    def test_invalid_board_format(self):
        """Test that invalid board formats raise a ValueError."""
        invalid_board = [
            [1] * 8,  # Only 8 columns instead of 9
            [0] * 9,
            [0] * 9,
            [0] * 9,
            [0] * 9,
            [0] * 9,
            [0] * 9,
            [0] * 9,
            [0] * 9
        ]
        with self.assertRaises(ValueError):
            solve_sudoku(invalid_board)

    def test_unsolvable_board(self):
        """Test that an unsolvable board returns None."""
        unsolvable_board = [
            [1, 1, 0, 0, 7, 0, 0, 0, 0],  # Invalid board (two 1s in row 0)
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 9]
        ]
        result = solve_sudoku(unsolvable_board)
        self.assertIsNone(result)  # The board should be unsolvable

    def test_completed_board(self):
        """Test a completed Sudoku board to ensure it remains unchanged."""
        completed_board = [
            [5, 3, 4, 6, 7, 8, 9, 1, 2],
            [6, 7, 2, 1, 9, 5, 3, 4, 8],
            [1, 9, 8, 3, 4, 2, 5, 6, 7],
            [8, 5, 9, 7, 6, 1, 4, 2, 3],
            [4, 2, 6, 8, 5, 3, 7, 9, 1],
            [7, 1, 3, 9, 2, 4, 8, 5, 6],
            [9, 6, 1, 5, 3, 7, 2, 8, 4],
            [2, 8, 7, 4, 1, 9, 6, 3, 5],
            [3, 4, 5, 2, 8, 6, 1, 7, 9]
        ]
        solution = solve_sudoku(completed_board)
        self.assertEqual(solution, completed_board)  # The solution should match the input

    def test_multiple_solutions(self):
        """Test a board with multiple solutions (ensure one valid solution is returned)."""
        multiple_solution_board = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 9]
        ]
        solution = solve_sudoku(multiple_solution_board)
        self.assertIsNotNone(solution)  # A solution should exist

    def test_empty_board(self):
        """Test an empty board to ensure it is solved correctly."""
        empty_board = [
            [0] * 9,
            [0] * 9,
            [0] * 9,
            [0] * 9,
            [0] * 9,
            [0] * 9,
            [0] * 9,
            [0] * 9,
            [0] * 9
        ]
        solution = solve_sudoku(empty_board)
        self.assertIsNotNone(solution)  # The board should be solvable

if __name__ == '__main__':
    unittest.main()
