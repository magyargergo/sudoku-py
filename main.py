import time

import pygame

from consts import DIFFICULTIES
from difficulty_menu import DifficultyMenu
from game import Game
from winner_screen import WinnerScreen

# Initialize Pygame
pygame.init()

# Set window size and title
size = width, height = 540, 540
window = pygame.display.set_mode(size)
pygame.display.set_caption("Sudoku")

# Set font
font = pygame.font.Font(None, 36)


class SudokuGame:
    def __init__(self):
        self.difficulty_menu = DifficultyMenu(window, font)
        self.game = Game(window, font)

    def play(self):
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
                self.difficulty_menu.set_selected_difficulty(selected_difficulty)
                self.difficulty_menu.draw()
                selected_difficulty = self.game.handle_difficulty_selection(
                    self.difficulty_menu.get_selected_difficulty()
                )
                if self.game.difficulty is not None:
                    game_state = "game"
                    self.game.start(self.game.difficulty)

            elif game_state == "game":
                self.game.update()
                self.game.handle_events()

                if self.game.check_win():
                    winner_screen = WinnerScreen(window, font, elapsed_time_str)
                else:
                    winner_screen = None

                difficulty_str = DIFFICULTIES[self.game.difficulty - 1]
                pygame.display.set_caption(
                    f"Sudoku ({difficulty_str}) - {elapsed_time_str}"
                )

            elif winner_screen is not None:
                winner_screen.draw()
                if winner_screen.handle_events():
                    game_state = "difficulty_menu"
                    self.game.selected_row = 0
                    self.game.selected_col = 0


# Create and play the game
sudoku_game = SudokuGame()
sudoku_game.play()
