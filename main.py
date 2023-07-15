"""
Main script for Sudoku Game with difficulty menu, game logic, and winner screen.
"""
import pygame

from game.screens.difficulty_menu_screen import DifficultyMenuScreen
from game.screens.sudoku_screen import SudokuScreen
from game.screens.winner_screen import WinnerScreen

# Initialize Pygame
pygame.init()

# Set window size and title
size = width, height = 540, 540
window = pygame.display.set_mode(size)
pygame.display.set_caption("Sudoku")

# Set font
font = pygame.font.Font(None, 36)

difficulty_menu = DifficultyMenuScreen(window, font)
sudoku_screen = SudokuScreen(window, font)

while True:
    if sudoku_screen.is_started():
        sudoku_screen.display()
        sudoku_screen.handle_events()
        if sudoku_screen.check_win():
            winner_screen = WinnerScreen(window, font, sudoku_screen.formatted_timer)
            winner_screen.display()
            winner_screen.handle_events()
    else:
        difficulty_menu.display()
        difficulty_menu.handle_events()
        difficulty = difficulty_menu.handle_difficulty_selection()
        if difficulty is not None:
            sudoku_screen.start(difficulty)
