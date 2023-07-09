import sys
import pygame
from consts import WHITE, BLACK


class WinnerScreen:
    def __init__(
        self, window: pygame.Surface, font: pygame.font.Font, elapsed_time_str: str
    ) -> None:
        self.window = window
        self.font = font
        self.elapsed_time_str = elapsed_time_str

    def draw(self) -> None:
        self.window.fill(WHITE)
        top_left_x = (self.window.get_size()[0] - 200) // 2
        top_left_y = (self.window.get_size()[1] - 50) // 2
        text = self.font.render("You won!", True, BLACK)
        self.window.blit(text, (top_left_x, top_left_y))
        text = self.font.render(self.elapsed_time_str, True, BLACK)
        self.window.blit(text, (top_left_x, top_left_y + 20))
        pygame.display.update()

    def handle_events(self) -> bool:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                return True
        return False
