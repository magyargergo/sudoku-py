"""
Defines the WinnerScreen class responsible for displaying the winner screen.
"""
import pygame

from game import WHITE, BLACK
from game.screens.screen import Screen
from game.utils import formatted_time


class WinnerScreen(Screen):
    """
    Represents the winner screen.

    Methods:
        draw(): Draws the winner screen on the window.
        set_elapsed_time(timer: float): Sets the elapsed time for the win screen.
        handle_events() -> bool: Handles Pygame events and returns True if the game should restart.
    """
    def __init__(self) -> None:
        """
        Initializes the WinnerScreen instance.
        """
        super().__init__()

        self.elapsed_time = None
        self.restart = False

    def display(self) -> None:
        """
        Draws the winner screen on the game window.
        """
        super().display()

        # Calculate the center coordinates of the window
        window_width, window_height = self.window.get_size()
        center_x = window_width // 2
        center_y = window_height // 2

        # Define fonts
        heading_font = pygame.font.Font(None, 40)
        time_font = pygame.font.Font(None, 30)

        # Render and position the congratulatory message
        congrats_text = heading_font.render("Congratulations!", True, BLACK)
        congrats_text_rect = congrats_text.get_rect(center=(center_x, center_y - 40))

        # Render and position the elapsed time
        elapsed_time_text = time_font.render(self.elapsed_time, True, BLACK)
        elapsed_time_text_rect = elapsed_time_text.get_rect(center=(center_x, center_y))

        # Render and position the instruction message
        instruction_text = time_font.render("Press SPACE to play again", True, BLACK)
        instruction_text_rect = instruction_text.get_rect(center=(center_x, center_y + 40))

        # Draw the background and text on the window
        self.window.fill(WHITE)
        self.window.blit(congrats_text, congrats_text_rect)
        self.window.blit(elapsed_time_text, elapsed_time_text_rect)
        self.window.blit(instruction_text, instruction_text_rect)

        pygame.display.update()

    def set_elapsed_time(self, timer: float):
        """
        Sets the elapsed time for the win screen.

        Args:
            timer (float): The elapsed time in seconds.

        Returns:
            None
        """
        if self.elapsed_time is None:
            self.elapsed_time = formatted_time(timer)

    def handle_events(self) -> None:
        """
        Handles events on the winner screen.

        Returns:
            A boolean indicating if the user pressed the return key to restart the game.
        """
        super().handle_events()

        for event in self.pygame_events:
            self.restart = event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE
