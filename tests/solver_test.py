"""
Unit tests for the solver.py
"""
import unittest
import numpy as np

import game.solver


class SudokuSolverTestCase(unittest.TestCase):
    """
    Unit TestCase for the solver.py
    """

    def test_solve_sudoku(self):
        """
        Valid case 1
        """
        # Unsolved Sudoku board
        board = np.array(
            [
                [0, 0, 0, 2, 6, 0, 7, 0, 1],
                [6, 8, 0, 0, 7, 0, 0, 9, 0],
                [1, 9, 0, 0, 0, 4, 5, 0, 0],
                [8, 2, 0, 1, 0, 0, 0, 4, 0],
                [0, 0, 4, 6, 0, 2, 9, 0, 0],
                [0, 5, 0, 0, 0, 3, 0, 2, 8],
                [0, 0, 9, 3, 0, 0, 0, 7, 4],
                [0, 4, 0, 0, 5, 0, 0, 3, 6],
                [7, 0, 3, 0, 1, 8, 0, 0, 0],
            ]
        )

        # Solve the Sudoku board
        game.solver.solve(board)

        # Expected solution
        expected_solution = np.array(
            [
                [4, 3, 5, 2, 6, 9, 7, 8, 1],
                [6, 8, 2, 5, 7, 1, 4, 9, 3],
                [1, 9, 7, 8, 3, 4, 5, 6, 2],
                [8, 2, 6, 1, 9, 5, 3, 4, 7],
                [3, 7, 4, 6, 8, 2, 9, 1, 5],
                [9, 5, 1, 7, 4, 3, 6, 2, 8],
                [5, 1, 9, 3, 2, 6, 8, 7, 4],
                [2, 4, 8, 9, 5, 7, 1, 3, 6],
                [7, 6, 3, 4, 1, 8, 2, 5, 9],
            ]
        )

        # Compare the solved board with the expected solution
        self.assertTrue(np.array_equal(board, expected_solution))

    def test_solve_sudoku_1(self):
        """
        Valid case 2
        """
        # Unsolved Sudoku board
        board = np.array(
            [
                [5, 3, 0, 0, 7, 0, 0, 0, 0],
                [6, 0, 0, 1, 9, 5, 0, 0, 0],
                [0, 9, 8, 0, 0, 0, 0, 6, 0],
                [8, 0, 0, 0, 6, 0, 0, 0, 3],
                [4, 0, 0, 8, 0, 3, 0, 0, 1],
                [7, 0, 0, 0, 2, 0, 0, 0, 6],
                [0, 6, 0, 0, 0, 0, 2, 8, 0],
                [0, 0, 0, 4, 1, 9, 0, 0, 5],
                [0, 0, 0, 0, 8, 0, 0, 7, 9],
            ]
        )

        # Solve the Sudoku board
        game.solver.solve(board)

        # Expected solution
        expected_solution = np.array(
            [
                [5, 3, 4, 6, 7, 8, 9, 1, 2],
                [6, 7, 2, 1, 9, 5, 3, 4, 8],
                [1, 9, 8, 3, 4, 2, 5, 6, 7],
                [8, 5, 9, 7, 6, 1, 4, 2, 3],
                [4, 2, 6, 8, 5, 3, 7, 9, 1],
                [7, 1, 3, 9, 2, 4, 8, 5, 6],
                [9, 6, 1, 5, 3, 7, 2, 8, 4],
                [2, 8, 7, 4, 1, 9, 6, 3, 5],
                [3, 4, 5, 2, 8, 6, 1, 7, 9],
            ]
        )

        # Compare the solved board with the expected solution
        self.assertTrue(np.array_equal(board, expected_solution))

    # The following test cases are two slow
    #
    # def test_duplicate_given_column(self):
    #     """
    #     This puzzle cannot be solved, because the middle column (c5) has the value ‘1’ twice.
    #     """
    #     board = np.array([
    #       [6, 0, 1, 5, 9, 0, 0, 0, 0],
    #       [0, 9, 0, 0, 1, 0, 0, 0, 0],
    #       [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #       [4, 0, 7, 0, 3, 1, 4, 0, 0],
    #       [0, 6, 0, 2, 4, 0, 0, 0, 5],
    #       [0, 0, 3, 0, 0, 0, 1, 0, 0],
    #       [0, 0, 0, 6, 0, 0, 0, 0, 3],
    #       [0, 0, 9, 0, 2, 0, 4, 0, 0],
    #       [0, 0, 0, 0, 0, 0, 1, 6, 0]
    #     ])
    #
    #     # Ensure solve returns False for an invalid board
    #     self.assertFalse(solve(board))

    # def test_duplicate_given_row(self):
    #     """
    #     This puzzle cannot be solved, because the middle row (r5) has the value ‘2’ twice.
    #     """
    #     board = np.array([
    #       [0, 4, 0, 1, 0, 0, 3, 5, 0],
    #       [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #       [2, 0, 5, 0, 0, 0, 0, 0, 0],
    #       [0, 0, 4, 8, 9, 0, 0, 2, 6],
    #       [0, 0, 0, 0, 1, 2, 0, 5, 0],
    #       [3, 0, 0, 0, 0, 7, 0, 0, 4],
    #       [0, 0, 0, 1, 6, 0, 6, 0, 0],
    #       [0, 7, 0, 0, 0, 0, 0, 1, 0],
    #       [0, 8, 0, 0, 2, 0, 0, 0, 0]
    #     ])
    #
    #     # Ensure solve returns False for an invalid board
    #     self.assertFalse(solve(board))

    def test_unsolvable_square(self):
        """
        This puzzle cannot be solved, because the left-most square of the middle row (r5c1) has no possible candidates.
        """
        board = np.array(
            [
                [0, 0, 9, 0, 2, 8, 7, 0, 0],
                [0, 8, 0, 6, 0, 0, 4, 0, 0],
                [5, 0, 0, 3, 0, 0, 0, 0, 0],
                [0, 4, 6, 0, 0, 0, 0, 2, 0],
                [7, 1, 3, 4, 5, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 2, 3, 0, 0],
                [0, 0, 5, 0, 9, 0, 0, 4, 0],
                [0, 0, 8, 0, 7, 0, 0, 1, 2],
                [5, 0, 3, 0, 0, 1, 2, 5, 0],
            ]
        )

        # Ensure solve returns False for an unsolvable board
        self.assertFalse(game.solver.solve(board))

    def test_unsolvable_box(self):
        """
        This puzzle cannot be solved, because the center box (b5) has no possible candidates for the value ‘4’.
        """
        board = np.array(
            [
                [0, 9, 0, 3, 0, 0, 0, 0, 1],
                [0, 0, 0, 3, 0, 0, 0, 0, 8],
                [0, 0, 4, 6, 0, 0, 0, 0, 8],
                [0, 0, 4, 0, 5, 0, 6, 0, 0],
                [0, 3, 2, 7, 5, 6, 0, 0, 0],
                [0, 0, 6, 0, 1, 0, 9, 0, 4],
                [0, 0, 1, 0, 0, 0, 0, 5, 8],
                [0, 0, 0, 0, 2, 0, 0, 0, 0],
                [0, 0, 0, 0, 7, 0, 6, 0, 0],
            ]
        )

        # Ensure solve returns False for an unsolvable board
        self.assertFalse(game.solver.solve(board))
