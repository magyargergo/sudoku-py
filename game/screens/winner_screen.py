"""
Defines the WinnerScreen class responsible for displaying the winner screen.
"""
import pygame

from game import BLACK
from game.screens.screen import Screen


class WinnerScreen(Screen):
    """
    Represents the winner screen.

    Args:
        elapsed_time_str (str): The string representation of the elapsed time.

    Methods:
        draw(): Draws the winner screen on the window.
        handle_events() -> bool: Handles Pygame events and returns True if the game should restart.
    """
    def __init__(self, elapsed_time_str: str) -> None:
        """
        Initializes the WinnerScreen instance.

        Args:
            window: The Pygame surface representing the game window.
            font: The Pygame font used for rendering text.
            elapsed_time_str: The string representation of the elapsed time.
        """
        super().__init__()

        self.elapsed_time_str = elapsed_time_str

    def display(self) -> None:
        """
        Draws the winner screen on the game window.
        """
        super().display()

        top_left_x = (self.window.get_size()[0] - 200) // 2
        top_left_y = (self.window.get_size()[1] - 50) // 2
        text = self.font.render("You won!", True, BLACK)
        self.window.blit(text, (top_left_x, top_left_y))
        text = self.font.render(self.elapsed_time_str, True, BLACK)
        self.window.blit(text, (top_left_x, top_left_y + 20))
        pygame.display.update()

    def handle_events(self) -> None:
        """
        Handles events on the winner screen.

        Returns:
            A boolean indicating if the user pressed the return key to restart the game.
        """
        super().handle_events()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                pass
