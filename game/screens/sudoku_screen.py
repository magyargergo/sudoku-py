"""
Defines the SudokuGame class responsible for managing the Sudoku game logic.
"""
import time

import pygame

from game import CELL_SIZE, DIFFICULTIES
from game.grid import Grid
from game.screens.screen import Screen


class SudokuScreen(Screen):
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
        timer (float): The start time of the game.
        formatted_timer (str): The formatted timer string.

    Methods:
        start(difficulty: int) -> None: Starts the game with the specified difficulty.
        display() -> None: Updates the game state and redraws the grid.
        handle_events() -> None: Handles Pygame events.
        is_valid() -> bool: Checks if the selected cell is valid for input.
        check_win() -> bool: Checks if the game is won.
        is_started() -> bool: Checks if the game has been started.
        finish() -> None: Finishes the game by resetting the difficulty.
    """

    def __init__(self, window: pygame.Surface, font: pygame.font.Font) -> None:
        """
        Initializes the SudokuGame instance.

        Args:
            window (pygame.Surface): The Pygame surface representing the game window.
            font (pygame.font.Font): The Pygame font used for rendering text.
        """
        super().__init__(window, font)
        self.grid = Grid(window, font)
        self.selected_row = 0
        self.selected_col = 0
        self.difficulty = None
        self.timer = None
        self.formatted_timer = None

    def start(self, difficulty: int) -> None:
        """
        Starts a new game with the specified difficulty level.

        Args:
            difficulty (int): The difficulty level of the game (1 = Easy, 2 = Medium, 3 = Hard, 4 = Expert).
        """
        self.difficulty = difficulty
        self.grid.generate_puzzle(self.difficulty)
        self.timer = time.perf_counter()

    def display(self) -> None:
        """
        Updates the game state and redraws the grid.
        """
        super().display()
        self.grid.draw(self.selected_col, self.selected_row)
        elapsed_time = time.gmtime(time.perf_counter() - self.timer)
        self.formatted_timer = time.strftime("%M:%S", elapsed_time)
        pygame.display.set_caption(
            f"Sudoku ({DIFFICULTIES[self.difficulty - 1]}) - {self.formatted_timer}"
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
                    if self.is_valid():
                        self.grid.table[self.selected_row][self.selected_col] = int(
                            event.unicode
                        )
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                self.selected_col = pos[0] // CELL_SIZE
                self.selected_row = pos[1] // CELL_SIZE

    def is_valid(self) -> bool:
        """
        Checks if the selected cell is valid for input.

        Returns:
            bool: True if the selected cell is valid for input, False otherwise.
        """
        return self.grid.original_table[self.selected_row][self.selected_col] == 0

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

    def finish(self) -> None:
        """
        Finishes the game by resetting the difficulty.

        This method sets the difficulty of the game to None, indicating that the game has finished.

        Returns:
            None
        """
        self.difficulty = None
