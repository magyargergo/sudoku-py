"""
Main script for Sudoku Game with difficulty menu, game logic, and winner screen.
"""
import logging

import pygame

from game.screens.difficulty_menu import DifficultyMenuScreen
from game.screens.sudoku import SudokuScreen
from game.screens.winner import WinnerScreen

# Set the logging configuration
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler(),
    ],
)

# Initialize Pygame
pygame.init()

while True:
    difficulty_menu = DifficultyMenuScreen()
    sudoku_screen = SudokuScreen()
    winner_screen = WinnerScreen()

    while True:
        if sudoku_screen.check_win():
            winner_screen.display()
            winner_screen.handle_events()
            selected_item = winner_screen.handle_item_selection()
            if selected_item is not None:
                break
        elif sudoku_screen.is_started():
            sudoku_screen.display()
            sudoku_screen.handle_events()
            if sudoku_screen.check_win():
                winner_screen.set_elapsed_time(sudoku_screen.timer)
        else:
            difficulty_menu.display()
            difficulty_menu.handle_events()
            selected_item = difficulty_menu.handle_item_selection()
            if selected_item is not None:
                sudoku_screen.start(selected_item)
