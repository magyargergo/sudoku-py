import copy
import random
import pygame
from typing import List
from consts import WHITE, BLACK, CELL_SIZE, WINDOW_BLUE
from solver import solve


class Grid:
    def __init__(self, window: pygame.Surface, font: pygame.font.Font) -> None:
        self.window = window
        self.grid_size = min(window.get_size())
        self.cell_size = self.grid_size // 9
        self.top_left_x = (window.get_size()[0] - self.grid_size) // 2
        self.top_left_y = (window.get_size()[1] - self.grid_size) // 2
        self.font = font
        self.table = None
        self.original_table = None

    def draw(self, selected_col: int, selected_row: int) -> None:
        self.window.fill(WHITE)
        self.draw_lines()
        self.draw_numbers()
        self.draw_selected_cell(selected_col, selected_row)
        pygame.display.update()

    def draw_lines(self) -> None:
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
        pos_x = selected_col * CELL_SIZE
        pos_y = selected_row * CELL_SIZE
        pygame.draw.rect(
            self.window, WINDOW_BLUE, (pos_x, pos_y, CELL_SIZE, CELL_SIZE), 4
        )

    def generate_puzzle(self, difficulty: int) -> List[List[int]]:
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
