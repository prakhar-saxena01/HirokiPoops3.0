import pygame
import sys
from menus.options_menu import OptionsMenu
from menus.main_menu import MainMenu
from menus.credits_menu import CreditsMenu
from main_game import main


class Game:
    def __init__(self, window: pygame.Surface):
        pygame.init()
        self.running, self.playing = True, False
        self.up_key, self.down_key, self.start_key, self.back_key = False, False, False, False
        self.display_width, self.display_height =  window.get_width(), window.get_height()
        self.display = pygame.Surface((self.display_width, self.display_height))
        self.window = window
        # self.font_name = "8BitWonder/8-BIT WONDER.TTF"
        self.font_name = "clearsans"
        self.main_menu = MainMenu(self)
        self.options = OptionsMenu(self)
        self.credits = CreditsMenu(self)
        self.current_menu = self.main_menu

    def game_loop(self):
        main(self.window, self)

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing, self.running = False, False
                self.current_menu.run_display = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT or event.key == pygame.K_RETURN:
                    self.start_key = True
                if event.key == pygame.K_LEFT or event.key == pygame.K_BACKSPACE:
                    self.back_key = True
                if event.key == pygame.K_DOWN:
                    self.down_key = True
                if event.key == pygame.K_UP:
                    self.up_key = True

    def reset_keys(self):
        self.up_key, self.down_key, self.start_key, self.back_key = False, False, False, False

    def draw_text(self, text, size, x, y):
        # font = pygame.font.Font(self.font_name, size)
        font = pygame.font.SysFont(self.font_name, size)
        text_surface = font.render(text, True, "white")
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        self.display.blit(text_surface, text_rect)
