from typing import Tuple

import numpy


def solve(board: numpy.ndarray) -> bool:
    """
    Solve a Sudoku puzzle using backtracking.

    Args:
        board (numpy.ndarray): A 9x9 NumPy array representing the Sudoku puzzle.
                               Empty cells are represented by zeros, and filled cells
                               contain integers from 1 to 9.

    Returns:
        bool: True if a solution is found, False otherwise.
    """
    # Find the next empty cell
    row, col = find_empty_cell(board)

    # If there are no empty cells, the puzzle is solved
    if row is None or col is None:
        return True

    # Try filling the empty cell with a valid number
    for num in range(1, 10):
        if is_valid_move(board, row, col, num):
            # Place the number in the cell
            board[row, col] = num

            # Recursively solve the puzzle
            if solve(board):
                return True

            # If the puzzle cannot be solved, backtrack and try a different number
            board[row, col] = 0

    # If no number can be placed in the current cell, the puzzle is unsolvable
    return False


def is_valid_board(board: numpy.ndarray) -> bool:
    """
    Check if the given Sudoku board is valid.

    Args:
        board (numpy.ndarray): A 9x9 NumPy array representing the Sudoku puzzle.

    Returns:
        bool: True if the board is valid, False otherwise.
    """
    # Check rows for duplicates
    for i in range(9):
        nums = [num for num in board[i, :] if num != 0]
        if len(nums) != len(set(nums)):
            return False

    # Check columns for duplicates
    for j in range(9):
        nums = [num for num in board[:, j] if num != 0]
        if len(nums) != len(set(nums)):
            return False

    # Check 3x3 subgrids for duplicates
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            subgrid = board[i:i + 3, j:j + 3].flatten()
            nums = [num for num in subgrid if num != 0]
            if len(nums) != len(set(nums)):
                return False

    return True


def find_empty_cell(board: numpy.ndarray) -> Tuple[int | None, int | None]:
    """
    Find the next empty cell (cell with value 0) in the Sudoku board.

    Args:
        board (numpy.ndarray): A 9x9 NumPy array representing the Sudoku puzzle.

    Returns:
        tuple: The (row, col) indices of the empty cell, or (None, None) if no empty cell is found.
    """
    for i in range(9):
        for j in range(9):
            if board[i, j] == 0:
                return i, j
    return None, None


def is_valid_move(board: numpy.ndarray, row: int, col: int, num: int) -> bool:
    """
    Check if placing a number in a cell is a valid move.

    Args:
        board (numpy.ndarray): A 9x9 NumPy array representing the Sudoku puzzle.
        row (int): The row index of the cell.
        col (int): The column index of the cell.
        num (int): The number to be placed in the cell.

    Returns:
        bool: True if the move is valid, False otherwise.
    """
    # Check if the number already exists in the row or column
    if num in board[row, :] or num in board[:, col]:
        return False

    # Check if the number already exists in the 3x3 subgrid
    subgrid_row = 3 * (row // 3)
    subgrid_col = 3 * (col // 3)
    subgrid = board[subgrid_row:subgrid_row+3, subgrid_col:subgrid_col+3]
    return num in subgrid
