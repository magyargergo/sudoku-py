"""
Defines the Game class responsible for managing the Sudoku game logic.
"""
import sys
import time

import pygame

from game import CELL_SIZE, DIFFICULTIES
from game.grid import Grid


class SudokuGame:
    """
    Represents the Sudoku game.

    Args:
        window (pygame.Surface): The Pygame window surface.
        font (pygame.font.Font): The font used for rendering text.

    Attributes:
        window (pygame.Surface): The Pygame window surface.
        selected_row (int): The index of the selected row.
        selected_col (int): The index of the selected column.
        difficulty (Optional[int]): The selected difficulty level.
        grid (Grid): The Sudoku grid.

    Methods:
        start(difficulty: int): Starts the game with the specified difficulty.
        update(): Updates the game state.
        handle_events(): Handles Pygame events.
        check_win() -> bool: Checks if the game is won.
    """
    def __init__(self, window: pygame.Surface, font: pygame.font.Font) -> None:
        """
        Initializes the Game instance.

        Args:
            window: The Pygame Surface representing the game window.
            font: The Pygame font used for rendering text.
        """
        self.window = window
        self.selected_row = 0
        self.selected_col = 0
        self.difficulty = None
        self.grid = Grid(window, font)
        self.timer = None
        self.formatted_timer = None

    def start(self, difficulty: int) -> None:
        """
        Starts a new game with the specified difficulty level.

        Args:
            difficulty: The difficulty level of the game (1 = Easy, 2 = Medium, 3 = Hard, 4 = Expert).
        """
        self.difficulty = difficulty
        self.grid.generate_puzzle(self.difficulty)
        self.timer = time.perf_counter()

    def update(self) -> None:
        """
        Updates the game state and redraws the grid.
        """
        self.grid.draw(self.selected_col, self.selected_row)
        elapsed_time = time.perf_counter() - self.timer
        self.formatted_timer = time.strftime("%M:%S", time.gmtime(elapsed_time))
        pygame.display.set_caption(
            f"Sudoku ({DIFFICULTIES[self.difficulty - 1]}) - {self.formatted_timer}"
        )

    def handle_events(self) -> None:
        """
        Handles the events (keyboard and mouse) to update the game state accordingly.
        """
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key in (
                    pygame.K_UP,
                    pygame.K_DOWN,
                    pygame.K_LEFT,
                    pygame.K_RIGHT,
                ):
                    direction = {
                        pygame.K_UP: (0, -1),
                        pygame.K_DOWN: (0, 1),
                        pygame.K_LEFT: (-1, 0),
                        pygame.K_RIGHT: (1, 0),
                    }
                    d_x, d_y = direction[event.key]
                    self.selected_row = max(0, min(8, self.selected_row + d_y))
                    self.selected_col = max(0, min(8, self.selected_col + d_x))
                elif (
                    pygame.K_1 <= event.key <= pygame.K_9
                    or pygame.K_KP1 <= event.key <= pygame.K_KP9
                ):
                    if (
                        self.grid.original_table[self.selected_row][self.selected_col]
                        == 0
                    ):
                        self.grid.table[self.selected_row][self.selected_col] = int(
                            event.unicode
                        )
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                self.selected_col = pos[0] // CELL_SIZE
                self.selected_row = pos[1] // CELL_SIZE

    def check_win(self) -> bool:
        """
        Checks if the player has won the game.

        Returns:
            True if the game is solved correctly, False otherwise.
        """
        return (
            self.grid.table is not None
            and all(all(cell != 0 for cell in row) for row in self.grid.table)
            and self.grid.is_solved()
        )

    def is_started(self) -> None:
        """
        Checks if the game has been started.

        Returns:
            bool: True if the game has been started, False otherwise.
        """
        return self.difficulty is not None

    def finish(self) -> None:
        """
        Finish the game by resetting the difficulty.

        This method sets the difficulty of the game to None, indicating that the game has finished.

        Returns:
            None
        """
        self.difficulty = None
