"""
Main script for Sudoku Game with difficulty menu, game logic, and winner screen.
"""
import time

import pygame

from game import DIFFICULTIES
from game.difficulty_menu import DifficultyMenu
from game.sudoku_game import SudokuGame
from game.winner_screen import WinnerScreen

# Initialize Pygame
pygame.init()

# Set window size and title
size = width, height = 540, 540
window = pygame.display.set_mode(size)
pygame.display.set_caption("Sudoku")

# Set font
font = pygame.font.Font(None, 36)


difficulty_menu = DifficultyMenu(window, font)
sudoku_game = SudokuGame(window, font)
start_time = time.perf_counter()

elapsed_time_str = ""
selected_difficulty = 0

while not sudoku_game.check_win():
    elapsed_time = time.perf_counter() - start_time
    elapsed_time_str = time.strftime("%M:%S", time.gmtime(elapsed_time))

    if sudoku_game.is_started():
        sudoku_game.update()
        sudoku_game.handle_events()
        difficulty_str = DIFFICULTIES[sudoku_game.difficulty - 1]
        pygame.display.set_caption(f"Sudoku ({difficulty_str}) - {elapsed_time_str}")
    else:
        difficulty_menu.update(selected_difficulty)
        difficulty_menu.draw()
        selected_difficulty = sudoku_game.handle_difficulty_selection(
            difficulty_menu.get_selected_difficulty()
        )
        if sudoku_game.difficulty is not None:
            sudoku_game.start(sudoku_game.difficulty)

winner_screen = WinnerScreen(window, font, elapsed_time_str)
winner_screen.draw()
