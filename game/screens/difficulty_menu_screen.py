"""
Defines the DifficultyMenu class for displaying and handling the difficulty menu.
"""
import pygame

from game import WINDOW_BLUE, DIFFICULTIES, BLACK, WHITE
from game.screens.screen import Screen


class DifficultyMenuScreen(Screen):
    """
    Represents a difficulty menu for the Sudoku game.

    Attributes:
       selected_difficulty (int): The index of the selected difficulty.
       text_rects (List[pygame.Rect]): The rectangles for displaying the difficulty text.

    Methods:
       display() -> None: Draws the difficulty menu on the window.
       set_selected_difficulty(selected_difficulty: int) -> None: Sets the selected difficulty.
       get_selected_difficulty() -> int: Returns the index of the selected difficulty.
       handle_difficulty_selection() -> int | None: The updated index of the selected difficulty after handling the user input,
                                                    or None if no valid selection is made.
    """

    def __init__(self) -> None:
        """
        Initializes the DifficultyMenuScreen instance.
        """
        super().__init__()

        self.selected_difficulty = 0
        self.text_rects = []

    def display(self) -> None:
        """
        Draws the difficulty menu on the game window.
        """
        super().display()

        grid_size = min(self.window.get_size())
        cell_size = grid_size // 9

        top_left_x = (self.window.get_size()[0] - 5 * cell_size) // 2
        top_left_y = (self.window.get_size()[1] - 5 * cell_size) // 2

        pygame.draw.rect(
            self.window, WHITE, (top_left_x, top_left_y, 5 * cell_size, 5 * cell_size)
        )

        self.text_rects.clear()

        for i, difficulty in enumerate(DIFFICULTIES):
            text = self.font.render(difficulty, True, BLACK)
            text_rect = text.get_rect(
                center=(top_left_x + 150, top_left_y + cell_size // 2 + i * cell_size)
            )

            self.text_rects.append(text_rect)

            if self.selected_difficulty == i:
                pygame.draw.rect(
                    self.window,
                    WINDOW_BLUE,
                    (top_left_x, top_left_y + i * cell_size, 5 * cell_size, cell_size),
                )

            self.window.blit(text, text_rect)

        pygame.display.update()
        pygame.display.set_caption("Sudoku")

    def get_selected_difficulty(self) -> int:
        """
        Returns the index of the selected difficulty level.

        Returns:
            int: The index of the selected difficulty level.
        """
        return self.selected_difficulty

    def handle_events(self) -> None:
        """
        Handles Pygame events to update the selected difficulty accordingly.
        """
        super().handle_events()

        for event in self.pygame_events:
            if (
                event.type == pygame.KEYDOWN
                and event.key == pygame.K_UP  # Up arrow key
            ):
                self.selected_difficulty = max(0, self.selected_difficulty - 1)

            elif (
                event.type == pygame.KEYDOWN
                and event.key == pygame.K_DOWN  # Down arrow key
            ):
                self.selected_difficulty = min(
                    len(DIFFICULTIES) - 1, self.selected_difficulty + 1
                )

            elif event.type == pygame.MOUSEMOTION:
                for i, text_rect in enumerate(self.text_rects):
                    if text_rect.collidepoint(pygame.mouse.get_pos()):
                        self.selected_difficulty = i

    def handle_difficulty_selection(self) -> int | None:
        """
        Handles the difficulty selection logic based on user input.

        Returns:
            int | None: The updated index of the selected difficulty after handling the user input,
                       or None if no valid selection is made.
        """
        for event in self.pygame_events:
            if (
                (event.type == pygame.KEYDOWN
                 and event.key in (pygame.K_RETURN, pygame.K_KP_ENTER)
                 and 0 <= self.selected_difficulty < len(DIFFICULTIES))
                or event.type == pygame.MOUSEBUTTONDOWN
            ):
                # Convert index to difficulty level
                return self.selected_difficulty + 1

        return None
