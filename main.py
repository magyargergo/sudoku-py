"""
Main script for Sudoku Game with difficulty menu, game logic, and winner screen.
"""
import pygame

from game.screens.difficulty_menu_screen import DifficultyMenuScreen
from game.screens.sudoku_screen import SudokuScreen
from game.screens.winner_screen import WinnerScreen

# Initialize Pygame
pygame.init()

while True:
    difficulty_menu = DifficultyMenuScreen()
    sudoku_screen = SudokuScreen()
    winner_screen = WinnerScreen()

    while not winner_screen.restart:
        if sudoku_screen.check_win():
            winner_screen.display()
            winner_screen.handle_events()
        elif sudoku_screen.is_started():
            sudoku_screen.display()
            sudoku_screen.handle_events()
            if sudoku_screen.check_win():
                winner_screen.set_elapsed_time(sudoku_screen.timer)
        else:
            difficulty_menu.display()
            difficulty_menu.handle_events()
            difficulty = difficulty_menu.handle_difficulty_selection()
            if difficulty is not None:
                sudoku_screen.start(difficulty)
