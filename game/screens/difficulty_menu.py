"""
The `difficulty_menu` module defines the DifficultyMenuScreen class for
displaying and handling the difficulty menu in the Sudoku game.

Classes:
    DifficultyMenuScreen: Represents the difficulty menu screen.

"""
import pygame

from game import DIFFICULTIES
from game.screens.menu import MenuScreen


class DifficultyMenuScreen(MenuScreen):
    """
    Represents a difficulty menu for the Sudoku game.

    Methods:
        display() -> None: Draws the difficulty menu on the window.
        handle_events() -> None: Handles Pygame events.
        handle_item_selection() -> int | None: The updated index of the selected difficulty after handling the user input,
                                                or None if no valid selection is made.
    """

    def __init__(self) -> None:
        """
        Initializes the DifficultyMenuScreen instance.
        """
        super().__init__()

        self.menu_items = DIFFICULTIES
        self.header_text = "Difficulty"

    def display(self) -> None:
        """
        Draws the difficulty menu on the game window.
        """
        super().display()

        pygame.display.set_caption("Sudoku - Difficulty Menu")
