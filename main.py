"""
Main script for Sudoku Game with difficulty menu, game logic, and winner screen.
"""
import time

import pygame

from game import DIFFICULTIES
from game.difficulty_menu import DifficultyMenu
from game.game import Game
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
game = Game(window, font)
game_state = "difficulty_menu"
start_time = time.perf_counter()

elapsed_time_str = ""
winner_screen = None
selected_difficulty = 0

while True:
    if winner_screen is not None:
        elapsed_time = time.perf_counter() - start_time
        elapsed_time_str = time.strftime("%M:%S", time.gmtime(elapsed_time))

    if game_state == "difficulty_menu":
        difficulty_menu.set_selected_difficulty(selected_difficulty)
        difficulty_menu.draw()
        selected_difficulty = game.handle_difficulty_selection(
            difficulty_menu.get_selected_difficulty()
        )
        if game.difficulty is not None:
            game_state = "game"
            game.start(game.difficulty)

    elif game_state == "game":
        game.update()
        game.handle_events()

        if game.check_win():
            winner_screen = WinnerScreen(window, font, elapsed_time_str)
        else:
            winner_screen = None

        difficulty_str = DIFFICULTIES[game.difficulty - 1]
        pygame.display.set_caption(
            f"Sudoku ({difficulty_str}) - {elapsed_time_str}"
        )

    elif winner_screen is not None:
        winner_screen.draw()
        if winner_screen.handle_events():
            game_state = "difficulty_menu"
            game.selected_row = 0
            game.selected_col = 0
