"""
Defines the DifficultyMenu class for displaying and handling the difficulty menu.
"""
import sys

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
       handle_difficulty_selection() -> int | None: The updated index of the selected difficulty after handling the user input,
                                                    or None if no valid selection is made.
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

    def get_selected_difficulty(self) -> int:
        """
        Returns the index of the selected difficulty level.

        Returns:
            The index of the selected difficulty level.
        """
        return self.selected_difficulty

    def handle_difficulty_selection(self) -> int | None:
        """
        Handles the difficulty selection logic based on user input.

        Returns:
            int | None: The updated index of the selected difficulty after handling the user input,
                       or None if no valid selection is made.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:  # Up arrow key
                    self.selected_difficulty = max(0, self.selected_difficulty - 1)

                elif event.key == pygame.K_DOWN:  # Down arrow key
                    self.selected_difficulty = min(len(DIFFICULTIES) - 1, self.selected_difficulty + 1)

                elif (
                    event.key in (pygame.K_RETURN, pygame.K_KP_ENTER)
                    and 0 <= self.selected_difficulty < len(DIFFICULTIES)
                ):
                    # Convert index to difficulty level
                    return self.selected_difficulty + 1
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Get mouse position
                pos = pygame.mouse.get_pos()
                # Calculate selected difficulty
                calculated_difficulty = (pos[1] - CELL_SIZE) // CELL_SIZE
                # Set difficulty based on selected difficulty
                if 1 <= calculated_difficulty <= len(DIFFICULTIES):
                    return calculated_difficulty

        return None
