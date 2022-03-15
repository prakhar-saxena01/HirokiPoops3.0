from .menu import Menu


class CreditsMenu(Menu):
    def __init__(self, game):
        super(CreditsMenu, self).__init__(game)

    def display_menu(self):
        self.run_display = True

        while self.run_display:
            self.game.check_events()
            if self.game.start_key or self.game.back_key:
                self.game.current_menu = self.game.main_menu
                self.run_display = False

            self.game.display.fill("black")
            self.game.draw_text("Credits", 40, self.game.display_width / 2, self.game.display_height / 2 - 100)
            self.game.draw_text("Menu made by Cristian Duenas,", 25, self.game.display_width / 2, self.game.
                                display_height / 2 - 50)
            self.game.draw_text("modified by me :)", 25, self.game.display_width / 2, self.game.display_height /
                                2 - 20)
            self.game.draw_text("Artwork made by my brothers", 25, self.game.display_width / 2, self.game.display_height
                                / 2 + 10)
            self.game.draw_text("© mak448a 2022", 25, self.game.display_width / 2, self.game.display_height /
                                2 + 70)
            self.blit_screen()
