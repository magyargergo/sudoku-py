"""
Defines the DifficultyMenu class for displaying and handling the difficulty menu.
"""

import pygame

from game import WINDOW_BLUE, CELL_SIZE, DIFFICULTIES, BLACK, WHITE


class DifficultyMenu:
    """
    Represents a difficulty menu for the Sudoku game.

    Args:
       window (pygame.Surface): The Pygame window surface.
       font (pygame.font.Font): The font used for rendering text.

    Attributes:
       window (pygame.Surface): The Pygame window surface.
       selected_difficulty (int): The index of the selected difficulty.
       font (pygame.font.Font): The font used for rendering text.

    Methods:
       draw(): Draws the difficulty menu on the window.
       set_selected_difficulty(selected_difficulty: int): Sets the selected difficulty.
       get_selected_difficulty() -> int: Returns the index of the selected difficulty.
    """
    def __init__(self, window: pygame.Surface, font: pygame.font.Font) -> None:
        """
        Initializes the DifficultyMenu instance.

        Args:
            window: The Pygame Surface representing the game window.
            font: The Pygame font used for rendering text.
        """
        self.window = window
        self.selected_difficulty = 0
        self.font = font

    def draw(self) -> None:
        """
        Draws the difficulty menu on the game window.
        """
        self.window.fill(WHITE)

        top_left_x = (self.window.get_size()[0] - 5 * CELL_SIZE) // 2
        top_left_y = (self.window.get_size()[1] - 5 * CELL_SIZE) // 2

        pygame.draw.rect(
            self.window, WHITE, (top_left_x, top_left_y, 5 * CELL_SIZE, 5 * CELL_SIZE)
        )

        for i, difficulty in enumerate(DIFFICULTIES):
            text = self.font.render(difficulty, True, BLACK)
            text_rect = text.get_rect(
                center=(top_left_x + 150, top_left_y + CELL_SIZE // 2 + i * CELL_SIZE)
            )

            mouse_pos = pygame.mouse.get_pos()
            if text_rect.collidepoint(mouse_pos):
                self.selected_difficulty = i

            if self.selected_difficulty == i:
                pygame.draw.rect(
                    self.window,
                    WINDOW_BLUE,
                    (top_left_x, top_left_y + i * CELL_SIZE, 5 * CELL_SIZE, CELL_SIZE),
                )

            self.window.blit(text, text_rect)

        pygame.display.update()

    def update(self, selected_difficulty: int) -> None:
        """
        Sets the selected difficulty level.

        Args:
            selected_difficulty: The index of the selected difficulty level.
        """
        self.selected_difficulty = selected_difficulty

    def get_selected_difficulty(self) -> int:
        """
        Returns the index of the selected difficulty level.

        Returns:
            The index of the selected difficulty level.
        """
        return self.selected_difficulty
