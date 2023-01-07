def solve(grid):
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
    min_remaining_values = 10
    empty_cell = None
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                choices = get_choices(grid, row, col)
                if len(choices) < min_remaining_values:
                    min_remaining_values = len(choices)
                    empty_cell = (row, col)
    return empty_cell


def get_choices(grid, row, col):
    choices = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    # Eliminate choices that appear in the same row
    choices -= set(grid[row])
    # Eliminate choices that appear in the same column
    for r in range(9):
        choices.discard(grid[r][col])
    # Eliminate choices that appear in the same 3x3 block
    block_row = row // 3
    block_col = col // 3
    for r in range(block_row * 3, block_row * 3 + 3):
        for c in range(block_col * 3, block_col * 3 + 3):
            choices.discard(grid[r][c])
    return list(choices)


def is_valid(grid, row, col, num):
    # Check if num appears in the same row
    if num in grid[row]:
        return False
    # Check if num appears in the same column
    for r in range(9):
        if grid[r][col] == num:
            return False
    # Check if num appears in the same 3x3 block
    block_row = row // 3
    block_col = col // 3
    for r in range(block_row * 3, block_row * 3 + 3):
        for c in range(block_col * 3, block_col * 3 + 3):
            if grid[r][c] == num:
                return False
    return True
