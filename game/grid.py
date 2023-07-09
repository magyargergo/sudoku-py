import copy
import random
from typing import List

import pygame

from consts import WHITE, BLACK, CELL_SIZE, WINDOW_BLUE
from solver import solve


class Grid:
    def __init__(self, window: pygame.Surface, font: pygame.font.Font) -> None:
        """
        Initializes the Grid instance.

        Args:
            window: The Pygame Surface representing the game window.
            font: The Pygame font used for rendering text.
        """
        self.window = window
        self.grid_size = min(window.get_size())
        self.cell_size = self.grid_size // 9
        self.top_left_x = (window.get_size()[0] - self.grid_size) // 2
        self.top_left_y = (window.get_size()[1] - self.grid_size) // 2
        self.font = font
        self.table = None
        self.original_table = None

    def draw(self, selected_col: int, selected_row: int) -> None:
        """
        Draws the grid on the game window.

        Args:
            selected_col: The column index of the currently selected cell.
            selected_row: The row index of the currently selected cell.
        """
        self.window.fill(WHITE)
        self.draw_lines()
        self.draw_numbers()
        self.draw_selected_cell(selected_col, selected_row)
        pygame.display.update()

    def draw_lines(self) -> None:
        """
        Draws the grid lines on the game window.
        """
        for i in range(10):
            start_pos = (self.top_left_x, self.top_left_y + i * self.cell_size)
            end_pos = (
                self.top_left_x + self.grid_size,
                self.top_left_y + i * self.cell_size,
            )
            line_width = 3 if i % 3 == 0 else 1
            pygame.draw.line(self.window, BLACK, start_pos, end_pos, line_width)

            start_pos = (self.top_left_x + i * self.cell_size, self.top_left_y)
            end_pos = (
                self.top_left_x + i * self.cell_size,
                self.top_left_y + self.grid_size,
            )
            pygame.draw.line(self.window, BLACK, start_pos, end_pos, line_width)

    def draw_numbers(self) -> None:
        """
        Draws the numbers on the grid.

        The original numbers are displayed in blue, while the user-entered numbers are displayed in black.
        """
        for i in range(9):
            for j in range(9):
                if self.table[i][j]:
                    text = self.font.render(
                        str(self.table[i][j]),
                        True,
                        BLACK if self.original_table[i][j] != 0 else WINDOW_BLUE,
                    )
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
            selected_col: The column index of the currently selected cell.
            selected_row: The row index of the currently selected cell.
        """
        pos_x = selected_col * CELL_SIZE
        pos_y = selected_row * CELL_SIZE
        pygame.draw.rect(
            self.window, WINDOW_BLUE, (pos_x, pos_y, CELL_SIZE, CELL_SIZE), 4
        )

    def generate_puzzle(self, difficulty: int) -> List[List[int]]:
        """
        Generates a Sudoku puzzle of the specified difficulty level.

        Args:
            difficulty: The difficulty level of the puzzle (1 = Easy, 2 = Medium, 3 = Hard, 4 = Expert).

        Returns:
            The generated Sudoku puzzle as a 2D list representing the grid.
        """
        self.table = [[0 for _ in range(9)] for _ in range(9)]
        solve(self.table)

        difficulty_ranges = {1: (40, 50), 2: (30, 40), 3: (20, 30), 4: (10, 20)}
        num_removed = random.randint(*difficulty_ranges[difficulty])

        for _ in range(num_removed):
            row = random.randint(0, 8)
            col = random.randint(0, 8)
            while self.table[row][col] == 0:
                row = random.randint(0, 8)
                col = random.randint(0, 8)
            self.table[row][col] = 0

        self.original_table = copy.deepcopy(self.table)

        return self.table
