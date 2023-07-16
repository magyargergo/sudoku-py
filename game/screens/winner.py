"""
The `winner` module defines the WinnerScreen class responsible for displaying the winner screen in the Sudoku game.

Classes:
    WinnerScreen: Represents the winner screen with menu options.

"""
import pygame

from game.screens.menu import MenuScreen
from game.utils import formatted_time


class WinnerScreen(MenuScreen):
    """
    Represents the winner screen.

    This class inherits from the MenuScreen class and adds functionality specific to the winner screen.
    It displays the winner screen with a congratulatory message, elapsed time, and menu options to restart or exit the game.

    Attributes:
        elapsed_time (str): The elapsed time for the win screen.
        menu_items (List[str]): The list of menu items.
        selected_item (int): The index of the currently selected menu item.
        header_text (str): The header text to display on the winner screen.

    Methods:
        display() -> None: Draws the winner screen on the game window.
        set_elapsed_time(timer: float) -> None: Sets the elapsed time for the win screen.
        handle_item_selection() -> int | None: Handles the menu item selection logic based on user input.

    """

    def __init__(self) -> None:
        """
        Initializes the WinnerScreen instance.
        """
        super().__init__()

        self.elapsed_time = None
        self.menu_items = ["Restart", "Exit"]
        self.selected_item = 0
        self.header_text = "Congratulations!"

    def display(self) -> None:
        """
        Draws the winner screen on the game window.

        This method calls the parent's display method to draw the menu on the window.
        It sets the window caption to "Sudoku - Winner Menu" to provide a descriptive title.

        Returns:
            None
        """
        super().display()

        pygame.display.set_caption("Sudoku - Winner Menu")

    def set_elapsed_time(self, timer: float) -> None:
        """
        Sets the elapsed time for the win screen.

        Args:
            timer (float): The elapsed time in seconds.

        Returns:
            None
        """
        if self.elapsed_time is None:
            self.elapsed_time = formatted_time(timer)
            self.sub_header_text = f"Your time was {self.elapsed_time}"

    def handle_item_selection(self) -> int | None:
        """
        Handles the menu item selection logic based on user input.

        This method overrides the parent's handle_item_selection method to handle the selection of menu items.
        It checks if the selected menu item is "Exit" and performs the quit action if so.
        Otherwise, it returns the selected item index as the result.

        Returns:
            int | None: The updated index of the selected menu item after handling the user input,
                       or None if no valid selection is made.
        """
        selected_item = super().handle_item_selection()
        if selected_item == self.menu_items.index("Exit"):
            self.quit()
        return selected_item
