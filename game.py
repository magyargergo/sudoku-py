import sys

import pygame

from consts import CELL_SIZE, DIFFICULTIES
from grid import Grid
from solver import solve


class Game:
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

    def start(self, difficulty: int) -> None:
        """
        Starts a new game with the specified difficulty level.

        Args:
            difficulty: The difficulty level of the game (1 = Easy, 2 = Medium, 3 = Hard, 4 = Expert).
        """
        self.difficulty = difficulty
        self.grid.generate_puzzle(self.difficulty)

    def update(self) -> None:
        """
        Updates the game state and redraws the grid.
        """
        self.grid.draw(self.selected_col, self.selected_row)

    def handle_events(self) -> None:
        """
        Handles the events (keyboard and mouse) to update the game state accordingly.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
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
                    dx, dy = direction[event.key]
                    self.selected_row = max(0, min(8, self.selected_row + dy))
                    self.selected_col = max(0, min(8, self.selected_col + dx))
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
        return all(all(cell != 0 for cell in row) for row in self.grid.table) and solve(
            self.grid.table
        )

    def handle_difficulty_selection(self, selected_difficulty: int) -> int:
        """
        Handles the difficulty selection logic based on user input.

        Args:
            selected_difficulty: The index of the currently selected difficulty.

        Returns:
            The updated index of the selected difficulty after handling the user input.
        """
        self.difficulty = None

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:  # Up arrow key
                    return max(0, selected_difficulty - 1)
                elif event.key == pygame.K_DOWN:  # Down arrow key
                    return min(len(DIFFICULTIES) - 1, selected_difficulty + 1)
                elif (
                    event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER
                ):  # Enter key
                    if 0 <= selected_difficulty < len(DIFFICULTIES):
                        self.difficulty = (
                            selected_difficulty + 1
                        )  # Convert index to difficulty level
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Get mouse position
                pos = pygame.mouse.get_pos()
                # Calculate selected difficulty
                calculated_difficulty = (pos[1] - CELL_SIZE) // CELL_SIZE
                # Set difficulty based on selected difficulty
                if 1 <= calculated_difficulty <= len(DIFFICULTIES):
                    self.difficulty = calculated_difficulty

        return selected_difficulty
