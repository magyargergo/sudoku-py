"""
The `menu` module defines the MenuScreen class for displaying and handling a menu screen in the game.

Classes:
    MenuScreen: Represents a menu screen.

"""
import pygame

from game import BLACK, WHITE, WINDOW_BLUE
from game.screens.screen import Screen


class MenuScreen(Screen):
    """
    Represents a menu screen.

    Attributes:
        selected_item (int): The index of the currently selected menu item.
        menu_items (List[str]): The list of menu items.
        text_rects (List[pygame.Rect]): The rectangles for displaying the menu item texts.

    Methods:
        display() -> None: Draws the menu on the window.
        handle_events() -> None: Handles Pygame events.
        handle_item_selection() -> int | None: Handles the menu item selection logic based on user input.

    """

    def __init__(self) -> None:
        """
        Initializes the MenuScreen instance.
        """
        super().__init__()

        self.selected_item = 0
        self.menu_items = []
        self.text_rects = []
        self.header_text = None
        self.sub_header_text = None

    def display(self) -> None:
        """
        Draws the menu on the game window.

        This method calculates the necessary coordinates and dimensions to draw the menu items centered on the window.
        It then iterates over the menu items, renders each item as text, and draws it on the window surface.
        The selected item is highlighted with a colored rectangle.

        Returns:
            None
        """
        super().display()

        # Calculate the grid and cell sizes based on the window dimensions
        cell_size = min(self.window.get_size()) // 9

        # Calculate the center coordinates of the window
        center_x = self.window.get_width() // 2
        center_y = self.window.get_height() // 2

        # Calculate the top-left coordinates for drawing the menu
        menu_width = 5 * cell_size
        menu_height = len(self.menu_items) * cell_size
        menu_top_left_x = center_x - menu_width // 2
        menu_top_left_y = center_y - menu_height // 2

        # Draw the welcome text if available
        if self.header_text is not None:
            # Render and position the welcome text
            welcome_font = pygame.font.Font(None, 60)
            welcome_text = welcome_font.render(self.header_text, True, BLACK)
            welcome_text_rect = welcome_text.get_rect(
                center=(
                    center_x,
                    menu_top_left_y
                    - (1.25 if self.sub_header_text is None else 2) * cell_size,
                )
            )
            self.window.blit(welcome_text, welcome_text_rect)

        # Draw the sub-header text if available
        if self.sub_header_text is not None:
            # Render and position the welcome text
            welcome_font = pygame.font.Font(None, 45)
            welcome_text = welcome_font.render(self.sub_header_text, True, BLACK)
            welcome_text_rect = welcome_text.get_rect(
                center=(center_x, menu_top_left_y - 1.25 * cell_size)
            )
            self.window.blit(welcome_text, welcome_text_rect)

        # Draw the background rectangle for the menu
        pygame.draw.rect(
            self.window,
            WHITE,
            (menu_top_left_x, menu_top_left_y, menu_width, menu_height),
        )

        # Clear the list of text rectangles for menu items
        self.text_rects.clear()

        # Iterate over menu items and draw each item on the window
        for i, menu_item in enumerate(self.menu_items):
            # Render the menu item text
            text = self.font.render(menu_item, True, BLACK)

            # Calculate the center coordinates of the text rectangle
            text_rect = text.get_rect(
                center=(center_x, menu_top_left_y + cell_size // 2 + i * cell_size)
            )

            # Add the text rectangle to the list
            self.text_rects.append(text_rect)

            # Highlight the selected item with a colored rectangle
            if self.selected_item == i:
                pygame.draw.rect(
                    self.window,
                    WINDOW_BLUE,
                    (
                        menu_top_left_x,
                        menu_top_left_y + i * cell_size,
                        menu_width,
                        cell_size,
                    ),
                )

            # Draw the text on the window surface
            self.window.blit(text, text_rect)

        # Update the display to show the menu
        pygame.display.update()

    def handle_events(self) -> None:
        """
        Handles Pygame events to update the selected item accordingly.

        This method iterates over the Pygame events received and updates the selected item based on user input.
        If the up arrow key is pressed, the selected item is decremented by 1 (unless it's already at the minimum index).
        If the down arrow key is pressed, the selected item is incremented by 1 (unless it's already at the maximum index).
        If the mouse is moved, the selected item is updated based on the collision of the mouse position with text rectangles.

        Returns:
            None
        """
        super().handle_events()

        for event in self.pygame_events:
            if event.type == pygame.KEYDOWN and event.key in (
                pygame.K_UP,
                pygame.K_DOWN,
            ):
                # Increment or decrement the selected item based on the key direction
                self.selected_item += 1 if event.key == pygame.K_DOWN else -1

                # Clamp the selected item between the minimum and maximum indices
                self.selected_item = max(
                    0, min(len(self.menu_items) - 1, self.selected_item)
                )

            elif event.type == pygame.MOUSEMOTION:
                # Check collision of mouse position with text rectangles
                for i, text_rect in enumerate(self.text_rects):
                    if text_rect.collidepoint(event.pos):
                        # Update selected item based on collision
                        self.selected_item = i

    def handle_item_selection(self) -> int | None:
        """
        Handles the menu item selection logic based on user input.

        This method checks for keyboard input of the return key (Enter) or keypad enter key, and also checks for a mouse button
        press event. If any of these events occur and the selected item is within the valid range of menu items, it returns
        the updated index of the selected item. Otherwise, it returns None.

        Returns:
            int | None: The updated index of the selected menu item after handling the user input,
                       or None if no valid selection is made.
        """
        for event in self.pygame_events:
            if (
                event.type == pygame.KEYDOWN
                and event.key in (pygame.K_RETURN, pygame.K_KP_ENTER)
                and 0 <= self.selected_item < len(self.menu_items)
            ) or event.type == pygame.MOUSEBUTTONDOWN:
                # Return the updated index of the selected item if return key is pressed or mouse button is pressed
                return self.selected_item

        # Return None if no valid selection is made
        return None
