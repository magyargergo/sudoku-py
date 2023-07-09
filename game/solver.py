"""
This module provides functions for solving Sudoku puzzles.

The module includes functions for solving Sudoku grids, finding empty cells, determining valid choices for cells,
and checking the validity of a number in a specific cell.

Functions:
- solve(grid): Recursively solves the Sudoku grid.
- find_empty_cell(grid): Finds an empty cell in the Sudoku grid.
- get_choices(grid, row, col): Returns a list of possible choices for a given cell in the Sudoku grid.
- is_valid(grid, row, col, num): Checks if a given number is valid in a specific cell of the Sudoku grid.
"""


def solve(grid):
    """
    Recursively solves the Sudoku grid.

    Args:
        grid (List[List[int]]): The Sudoku grid to be solved.

    Returns:
        bool: True if the grid is solvable, False otherwise.
    """
    empty_cell = find_empty_cell(grid)
    if not empty_cell:
        return True
    row, col = empty_cell
    choices = get_choices(grid, row, col)
    for num in choices:
        if is_valid(grid, row, col, num):
            grid[row][col] = num
            if solve(grid):
                return True
            grid[row][col] = 0
    return False


def find_empty_cell(grid):
    """
    Finds an empty cell in the Sudoku grid.

    Args:
        grid (List[List[int]]): The Sudoku grid.

    Returns:
        Tuple[int, int] or None: The coordinates of the empty cell (row, col), or None if no empty cells are found.
    """
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                return row, col
    return None


def get_choices(grid, row, col):
    """
    Returns a list of possible choices for a given cell in the Sudoku grid.

    Args:
        grid (List[List[int]]): The Sudoku grid.
        row (int): The row index of the cell.
        col (int): The column index of the cell.

    Returns:
        List[int]: A list of possible choices for the cell.
    """
    choices = set(range(1, 10))

    # Eliminate choices that appear in the same row
    choices -= set(grid[row])

    # Eliminate choices that appear in the same column
    choices -= {grid[i][col] for i in range(9)}

    # Eliminate choices that appear in the same 3x3 block
    block_row = row // 3
    block_col = col // 3
    choices -= {
        grid[block_row * 3 + i][block_col * 3 + j]
        for i in range(3)
        for j in range(3)
    }

    return list(choices)


def is_valid(grid, row, col, num):
    """
    Checks if a given number is valid in a specific cell of the Sudoku grid.

    Args:
        grid (List[List[int]]): The Sudoku grid.
        row (int): The row index of the cell.
        col (int): The column index of the cell.
        num (int): The number to be checked.

    Returns:
        bool: True if the number is valid in the cell, False otherwise.
    """
    # Check if num appears in the same row, column, or 3x3 block
    for i in range(9):
        if (
            num in (
                grid[row][i],  # row
                grid[i][col],  # column
                grid[row // 3 * 3 + i // 3][col // 3 * 3 + i % 3]  # cell
            )
        ):
            return False
    return True
