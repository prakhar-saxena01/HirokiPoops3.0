import pygame
from .menu import Menu
from utils.load_image import load_image
import os


class CrashMenu(Menu):
    def __init__(self, game):
        super(CrashMenu, self).__init__(game)

    def display_menu(self):
        self.run_display = True
        image = load_image("img/tmp/screenshot.png").convert()

        while self.run_display:
            self.game.check_events()
            if self.game.start_key or self.game.back_key:
                self.game.current_menu = self.game.main_menu
                pygame.mixer.music.load(f"{os.getcwd()}/sounds/he'll_take_care_of_the_rest.mp3")
                pygame.mixer.music.play(loops=-1)
                self.run_display = False

            self.game.display.fill("black")
            self.game.display.blit(image, (0, 0))
            self.game.draw_text("You crashed.", 60, self.game.display_width / 2, self.game.display_height / 2 - 50,
                                color="black")
            self.game.draw_text("Press enter to", 40, self.game.display_width / 2, self.game.display_height / 2,
                                color="black")
            self.game.draw_text("return to main menu", 40, self.game.display_width / 2, self.game.display_height / 2 +
                                40, color="black")
            self.blit_screen()
            # Add character select, main menu, and quit menu options here

        if os.path.exists(f"{os.getcwd()}/img/tmp/screenshot.png"):
            os.remove(f"{os.getcwd()}/img/tmp/screenshot.png")
