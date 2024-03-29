"""
The `sudoku` module defines the SudokuScreen class for managing the Sudoku game logic.

Classes:
    SudokuScreen: Represents the Sudoku game.

"""
import time

import pygame

from game import DIFFICULTIES
from game.grid import Grid
from game.screens.screen import Screen
from game.utils import formatted_time


class SudokuScreen(Screen):
    """
    Represents the Sudoku game.

    Attributes:
        selected_row (int): The index of the selected row.
        selected_col (int): The index of the selected column.
        difficulty (Optional[int]): The selected difficulty level.
        grid (Grid): The Sudoku grid.
        timer (float): The start time of the game.

    Methods:
        start(difficulty: int) -> None: Starts the game with the specified difficulty.
        display() -> None: Updates the game state and redraws the grid.
        handle_events() -> None: Handles Pygame events.
        check_win() -> bool: Checks if the game is won.
        is_started() -> bool: Checks if the game has been started.
    """

    def __init__(self) -> None:
        """
        Initializes the SudokuGame instance.
        """
        super().__init__()

        self.grid = Grid(self.window, self.font)
        self.selected_row = 0
        self.selected_col = 0
        self.difficulty = None
        self.timer = None

    def start(self, difficulty: int) -> None:
        """
        Starts a new game with the specified difficulty level.

        Args:
            difficulty (int): The difficulty level of the game (0 = Easy, 1 = Medium, 2 = Hard, 3 = Expert).
        """
        self.difficulty = difficulty
        self.grid.generate_puzzle(self.difficulty)
        self.timer = time.perf_counter()
        self.log_info(f"Game started with difficulty: {DIFFICULTIES[self.difficulty]}")

    def display(self) -> None:
        """
        Updates the game state and redraws the grid.
        """
        super().display()
        self.grid.draw(self.selected_col, self.selected_row)
        pygame.display.set_caption(
            f"Sudoku ({DIFFICULTIES[self.difficulty]}) - {formatted_time(self.timer)}"
        )

    def handle_events(self) -> None:
        """
        Handles the events (keyboard and mouse) to update the game state accordingly.
        """
        super().handle_events()

        for event in self.pygame_events:
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
                    self.grid.update(
                        self.selected_row, self.selected_col, int(event.unicode)
                    )
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                self.selected_col = pos[0] // self.grid.cell_size
                self.selected_row = pos[1] // self.grid.cell_size

    def check_win(self) -> bool:
        """
        Checks if the player has won the game.

        Returns:
            bool: True if the game is solved correctly, False otherwise.
        """
        return self.grid.is_solved()

    def is_started(self) -> bool:
        """
        Checks if the game has been started.

        Returns:
            bool: True if the game has been started, False otherwise.
        """
        return self.difficulty is not None
