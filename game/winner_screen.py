"""
Defines the WinnerScreen class responsible for displaying the winner screen.
"""
import sys

import pygame

from game import BLACK, WHITE


class WinnerScreen:
    """
    Represents the winner screen.

    Args:
        window (pygame.Surface): The Pygame window surface.
        font (pygame.font.Font): The font used for rendering text.
        elapsed_time_str (str): The string representation of the elapsed time.

    Methods:
        draw(): Draws the winner screen on the window.
        handle_events() -> bool: Handles Pygame events and returns True if the game should restart.
    """
    def __init__(
        self, window: pygame.Surface, font: pygame.font.Font, elapsed_time_str: str
    ) -> None:
        """
        Initializes the WinnerScreen instance.

        Args:
            window: The Pygame surface representing the game window.
            font: The Pygame font used for rendering text.
            elapsed_time_str: The string representation of the elapsed time.
        """
        self.window = window
        self.font = font
        self.elapsed_time_str = elapsed_time_str

    def draw(self) -> None:
        """
        Draws the winner screen on the game window.
        """
        self.window.fill(WHITE)
        top_left_x = (self.window.get_size()[0] - 200) // 2
        top_left_y = (self.window.get_size()[1] - 50) // 2
        text = self.font.render("You won!", True, BLACK)
        self.window.blit(text, (top_left_x, top_left_y))
        text = self.font.render(self.elapsed_time_str, True, BLACK)
        self.window.blit(text, (top_left_x, top_left_y + 20))
        pygame.display.update()

    def handle_events(self) -> bool:
        """
        Handles events on the winner screen.

        Returns:
            A boolean indicating if the user pressed the return key to restart the game.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                return True
        return False
