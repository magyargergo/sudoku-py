"""
Defines the Grid class responsible for drawing and generating the Sudoku grid.
"""
import numpy
import pygame

from game import BLACK, CELL_SIZE, WINDOW_BLUE
from game.solver import solve


class Grid:
    """
    Represents the Sudoku grid.

    Args:
        window (pygame.Surface): The Pygame window surface.
        font (pygame.font.Font): The font used for rendering text.

    Attributes:
        window (pygame.Surface): The Pygame window surface.
        grid_size (int): The size of the grid.
        cell_size (int): The size of each cell in the grid.
        top_left_x (int): The x-coordinate of the top-left corner of the grid.
        top_left_y (int): The y-coordinate of the top-left corner of the grid.
        font (pygame.font.Font): The font used for rendering text.
        table (numpy.ndarray): The Sudoku grid table.
        original_table (numpy.ndarray): The original Sudoku grid table.
        solution_table (numpy.ndarray): The solution table for the Sudoku grid.

    Methods:
        draw(selected_col: int, selected_row: int) -> None: Draws the grid on the window.
        draw_lines() -> None: Draws the grid lines on the window.
        draw_numbers() -> None: Draws the numbers on the grid.
        draw_selected_cell(selected_col: int, selected_row: int) -> None: Draws the selected cell.
        generate_puzzle(difficulty: int) -> None: Generates a Sudoku puzzle.
        is_solved() -> bool: Checks if the puzzle has been solved.
    """
    def __init__(self, window: pygame.Surface, font: pygame.font.Font) -> None:
        """
        Initializes the Grid instance.

        Args:
            window (pygame.Surface): The Pygame surface representing the game window.
            font (pygame.font.Font): The Pygame font used for rendering text.
        """
        self.window = window
        self.grid_size = min(window.get_size())
        self.cell_size = self.grid_size // 9
        self.top_left_x = (window.get_size()[0] - self.grid_size) // 2
        self.top_left_y = (window.get_size()[1] - self.grid_size) // 2
        self.font = font
        self.table = None
        self.original_table = None
        self.solution_table = None

    def draw(self, selected_col: int, selected_row: int) -> None:
        """
        Draws the grid on the game window.

        Args:
            selected_col (int): The column index of the currently selected cell.
            selected_row (int): The row index of the currently selected cell.
        """
        self.draw_lines()
        self.draw_numbers()
        self.draw_selected_cell(selected_col, selected_row)
        pygame.display.update()

    def draw_lines(self) -> None:
        """
        Draws the grid lines on the game window.
        """
        for i in range(10):
            # Determine line width (3 for every 3rd line, 1 for others)
            line_width = 3 if i % 3 == 0 else 1

            # Vertical lines
            vertical_start_pos = (self.top_left_x + i * self.cell_size, self.top_left_y)
            vertical_end_pos = (self.top_left_x + i * self.cell_size, self.top_left_y + self.grid_size)
            pygame.draw.line(self.window, BLACK, vertical_start_pos, vertical_end_pos, line_width)

            # Horizontal lines
            horizontal_start_pos = (self.top_left_x, self.top_left_y + i * self.cell_size)
            horizontal_end_pos = (self.top_left_x + self.grid_size, self.top_left_y + i * self.cell_size)
            pygame.draw.line(self.window, BLACK, horizontal_start_pos, horizontal_end_pos, line_width)

    def draw_numbers(self) -> None:
        """
        Draws the numbers on the grid.

        The original numbers are displayed in blue, while the user-entered numbers are displayed in black.
        """
        for i, row in enumerate(self.table):
            for j, cell in enumerate(row):
                if cell:
                    color = BLACK if self.original_table[i][j] != 0 else WINDOW_BLUE
                    text = self.font.render(str(cell), True, color)
                    text_rect = text.get_rect(
                        center=(
                            self.top_left_x + j * self.cell_size + self.cell_size // 2,
                            self.top_left_y + i * self.cell_size + self.cell_size // 2,
                        ),
                    )
                    self.window.blit(text, text_rect)

    def draw_selected_cell(self, selected_col: int, selected_row: int) -> None:
        """
        Draws a highlight around the currently selected cell.

        Args:
            selected_col (int): The column index of the currently selected cell.
            selected_row (int): The row index of the currently selected cell.
        """
        pos_x = selected_col * CELL_SIZE
        pos_y = selected_row * CELL_SIZE
        pygame.draw.rect(
            self.window, WINDOW_BLUE, (pos_x, pos_y, CELL_SIZE, CELL_SIZE), 4
        )

    def generate_puzzle(self, difficulty: int) -> None:
        """
        Generates a Sudoku puzzle of the specified difficulty level.

        Args:
            difficulty (int): The difficulty level of the puzzle (1 = Easy, 2 = Medium, 3 = Hard, 4 = Expert).

        Returns:
            None
        """
        # Create an empty Sudoku grid
        self.table = numpy.zeros((9, 9), dtype=numpy.uint)

        # Fill in values for the first row
        self.table[0] = numpy.arange(1, 10)
        numpy.random.shuffle(self.table[0])

        solve(self.table)
        self.solution_table = self.table.copy()

        difficulty_ranges = {4: (40, 50), 3: (30, 40), 2: (20, 30), 1: (10, 20)}
        num_removed = numpy.random.randint(*difficulty_ranges[difficulty])

        indices = numpy.random.choice(81, num_removed, replace=False)
        self.table.flat[indices] = 0

        self.original_table = self.table.copy()

    def is_solved(self) -> bool:
        """
        Checks if the Sudoku puzzle has been solved.

        Returns:
            bool: True if the puzzle is solved, False otherwise.
        """
        return (
            self.table is not None
            and numpy.all(self.table != 0)
            and numpy.array_equal(self.table, self.solution_table)
        )
