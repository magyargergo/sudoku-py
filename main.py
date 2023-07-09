import sys
import time

import pygame
import random

from solver import solve

# Initialize Pygame
pygame.init()

# Set window size and title
size = width, height = 540, 540
window = pygame.display.set_mode(size)
pygame.display.set_caption("Sudoku")

CELL_SIZE = 60
DIFFICULTIES = ["Easy", "Medium", "Hard", "Expert"]

# Set colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
WINDOW_BLUE = (100, 162, 216)

# Set font
font = pygame.font.Font(None, 36)


def draw_grid(window, grid):
    # Calculate grid size
    grid_size = min(window.get_size())
    # Calculate cell size
    cell_size = grid_size // 9
    # Calculate top left corner of grid
    top_left_x = (window.get_size()[0] - grid_size) // 2
    top_left_y = (window.get_size()[1] - grid_size) // 2

    # Draw lines
    for i in range(10):
        # Horizontal lines
        start_pos = (top_left_x, top_left_y + i * cell_size)
        end_pos = (top_left_x + grid_size, top_left_y + i * cell_size)
        if i % 3 == 0:
            # Thick line
            pygame.draw.line(window, BLACK, start_pos, end_pos, 3)
        else:
            # Thin line
            pygame.draw.line(window, BLACK, start_pos, end_pos)
        # Vertical lines
        start_pos = (top_left_x + i * cell_size, top_left_y)
        end_pos = (top_left_x + i * cell_size, top_left_y + grid_size)
        if i % 3 == 0:
            # Thick line
            pygame.draw.line(window, BLACK, start_pos, end_pos, 3)
        else:
            # Thin line
            pygame.draw.line(window, BLACK, start_pos, end_pos)

    # Draw numbers
    for i in range(9):
        for j in range(9):
            if grid[i][j]:
                text = font.render(str(grid[i][j]), True, BLACK)
                window.blit(
                    text,
                    (
                        top_left_x + j * cell_size + cell_size // 3,
                        top_left_y + i * cell_size + cell_size // 3,
                    ),
                )


def is_solved(grid):
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                return False
    return solve(grid)


def generate_puzzle(difficulty):
    grid = [[0 for _ in range(9)] for _ in range(9)]
    solve(grid)

    # Choose a random number of cells to remove based on difficulty
    if difficulty == 1:
        num_removed = random.randint(40, 50)
    elif difficulty == 2:
        num_removed = random.randint(30, 40)
    elif difficulty == 3:
        num_removed = random.randint(20, 30)
    else:
        num_removed = random.randint(10, 20)

    for _ in range(num_removed):
        # Choose a random cell to remove
        row = random.randint(0, 8)
        col = random.randint(0, 8)
        while grid[row][col] == 0:
            row = random.randint(0, 8)
            col = random.randint(0, 8)
        grid[row][col] = 0
    return grid


def draw_difficulty_menu(window, selected_difficulty):
    # Calculate top left corner of menu
    top_left_x = (window.get_size()[0] - 300) // 2
    top_left_y = (window.get_size()[1] - 300) // 2

    # Draw menu background
    pygame.draw.rect(window, WHITE, (top_left_x, top_left_y, 300, 300))

    # Draw menu items
    for i, difficulty in enumerate(DIFFICULTIES):
        text = font.render(difficulty, True, BLACK)
        text_rect = text.get_rect(center=(top_left_x + 150, top_left_y + 30 + i * 60))

        # Check if mouse is hovering over menu item
        mouse_pos = pygame.mouse.get_pos()
        if text_rect.collidepoint(mouse_pos):
            # Highlight menu item
            pygame.draw.rect(
                window, WINDOW_BLUE, (top_left_x, top_left_y + i * 60, 300, 60)
            )
            text_rect = text.get_rect(
                center=(top_left_x + 150, top_left_y + 30 + i * 60)
            )
            selected_difficulty = i  # Update the selected difficulty

        # Highlight selected difficulty
        if selected_difficulty == i:
            pygame.draw.rect(
                window, WINDOW_BLUE, (top_left_x, top_left_y + i * 60, 300, 60)
            )

        window.blit(text, text_rect)

    # Update display
    pygame.display.update()

    return selected_difficulty


def get_difficulty_from_events(selected_difficulty):
    difficulty = None

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:  # Up arrow key
                selected_difficulty = max(0, selected_difficulty - 1)
            elif event.key == pygame.K_DOWN:  # Down arrow key
                selected_difficulty = min(
                    len(DIFFICULTIES) - 1, selected_difficulty + 1
                )
            elif (
                event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER
            ):  # Enter key
                if 0 <= selected_difficulty < len(DIFFICULTIES):
                    difficulty = (
                        selected_difficulty + 1
                    )  # Convert index to difficulty level
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Get mouse position
            pos = pygame.mouse.get_pos()
            # Calculate selected difficulty
            _selected_difficulty = (pos[1] - CELL_SIZE) // CELL_SIZE
            # Set difficulty based on selected difficulty
            if 1 <= _selected_difficulty <= len(DIFFICULTIES):
                difficulty = _selected_difficulty

    return difficulty, selected_difficulty


def draw_selected_cell(window, selected_row, selected_col):
    # Calculate top-left position of cell
    pos_x = selected_col * CELL_SIZE
    pos_y = selected_row * CELL_SIZE
    # Draw selected cell
    pygame.draw.rect(window, WINDOW_BLUE, (pos_x, pos_y, CELL_SIZE, CELL_SIZE), 4)
    # Update display
    pygame.display.update()


def handle_game_events(selected_row, selected_col, grid):
    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key in (pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT):
                selected_row += int(event.key == pygame.K_DOWN) - int(
                    event.key == pygame.K_UP
                )
                selected_col += int(event.key == pygame.K_RIGHT) - int(
                    event.key == pygame.K_LEFT
                )
                selected_row = max(0, min(8, selected_row))
                selected_col = max(0, min(8, selected_col))
            elif (
                event.key
                in (
                    pygame.K_1,
                    pygame.K_2,
                    pygame.K_3,
                    pygame.K_4,
                    pygame.K_5,
                    pygame.K_6,
                    pygame.K_7,
                    pygame.K_8,
                    pygame.K_9,
                )
                and grid[selected_row][selected_col] == 0
            ):
                grid[selected_row][selected_col] = int(chr(event.key))
            elif (
                event.key
                in (
                    pygame.K_KP1,
                    pygame.K_KP2,
                    pygame.K_KP3,
                    pygame.K_KP4,
                    pygame.K_KP5,
                    pygame.K_KP6,
                    pygame.K_KP7,
                    pygame.K_KP8,
                    pygame.K_KP9,
                )
                and grid[selected_row][selected_col] == 0
            ):
                grid[selected_row][selected_col] = int(event.unicode)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Get mouse position
            pos = pygame.mouse.get_pos()
            # Calculate selected cell
            selected_col = pos[0] // CELL_SIZE
            selected_row = pos[1] // CELL_SIZE

    return selected_row, selected_col


def draw_win_screen(elapsed_time_str):
    # Draw background
    window.fill(WHITE)
    # Calculate top left corner of text
    top_left_x = (window.get_size()[0] - 200) // 2
    top_left_y = (window.get_size()[1] - 50) // 2
    # Display win message
    text = font.render("You won!", True, BLACK)
    window.blit(text, (top_left_x, top_left_y))
    # Display elapsed time
    text = font.render(elapsed_time_str, True, BLACK)
    window.blit(text, (top_left_x, top_left_y + 20))
    # Update display
    pygame.display.update()


def handle_win_screen_events():
    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            # Restart game
            return True


def play():
    grid = None
    difficulty = None
    selected_difficulty = 0  # Initialize selected difficulty to 0
    # Set initial selected cell
    selected_row = 0
    selected_col = 0
    # Set initial game state
    game_state = "difficulty_menu"
    # Set initial time
    start_time = time.perf_counter()
    while True:
        elapsed_time = time.perf_counter() - start_time
        elapsed_time_str = time.strftime("%M:%S", time.gmtime(elapsed_time))

        # Draw background
        window.fill(WHITE)
        if game_state == "difficulty_menu":
            selected_difficulty = draw_difficulty_menu(
                window, selected_difficulty
            )  # Store the selected difficulty
            difficulty, selected_difficulty = get_difficulty_from_events(
                selected_difficulty
            )
            if difficulty is not None:
                game_state = "game"
                grid = generate_puzzle(difficulty)
        elif game_state == "game":
            draw_grid(window, grid)
            draw_selected_cell(window, selected_row, selected_col)
            selected_row, selected_col = handle_game_events(
                selected_row, selected_col, grid
            )
            game_state = "win" if is_solved(grid) else "game"

            difficulty_str = ""
            if difficulty == 1:
                difficulty_str = "Easy"
            elif difficulty == 2:
                difficulty_str = "Medium"
            elif difficulty == 3:
                difficulty_str = "Hard"
            elif difficulty == 4:
                difficulty_str = "Expert"

            pygame.display.set_caption(
                f"Sudoku ({difficulty_str}) - {elapsed_time_str}"
            )
        elif game_state == "win":
            draw_win_screen(elapsed_time_str)
            if handle_win_screen_events():
                game_state = "difficulty_menu"
                selected_row = 0
                selected_col = 0


play()
