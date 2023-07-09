"""
Main script for Sudoku Game with difficulty menu, game logic, and winner screen.
"""
import pygame

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

while True:
    if sudoku_game.is_started():
        sudoku_game.update()
        sudoku_game.handle_events()
        if sudoku_game.check_win():
            winner_screen = WinnerScreen(window, font, sudoku_game.formatted_timer)
            winner_screen.draw()
    else:
        difficulty_menu.draw()
        difficulty = difficulty_menu.handle_difficulty_selection()
        if difficulty is not None:
            sudoku_game.start(difficulty)
