"""
Defines the Screen class representing a screen in the game.
"""
import sys

import pygame

from game import WHITE
from game.logger import Logger


class Screen(Logger):
    """
    Represents a screen in the game.

    Attributes:
        window (pygame.Surface): The Pygame window surface.
        font (pygame.font.Font): The font used for rendering text.
        pygame_events (List[pygame.event.Event]): The list of Pygame events.

    Methods:
        display() -> None: Displays the screen.
        handle_events() -> None: Handles Pygame events.
        quit() -> None: Quits the game and exits the program.

    """

    def __init__(self) -> None:
        """
        Initializes the Screen instance.
        """
        super().__init__()
        self.window = pygame.display.set_mode((540, 540))
        self.font = pygame.font.Font(None, 36)
        self.pygame_events = []

    def display(self) -> None:
        """
        Displays the screen by filling the window with the background color.
        """
        self.window.fill(WHITE)

    def handle_events(self) -> None:
        """
        Handles Pygame events.

        This method retrieves Pygame events, stores them in the `pygame_events` list, and checks for the QUIT event
        to exit the game.

        """
        self.pygame_events.clear()
        for event in pygame.event.get():
            self.pygame_events.append(event)
            if event.type == pygame.QUIT:
                self.quit()

    def quit(self) -> None:
        """
        Quits the game and exits the program.

        This method calls the `pygame.quit()` function to quit the Pygame framework,
        and then calls the `sys.exit()` function to exit the program.

        Returns:
            None
        """
        pygame.quit()
        sys.exit()
