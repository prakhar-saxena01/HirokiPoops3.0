from .menu import Menu


class CrashMenu(Menu):
    def __init__(self, game):
        super(CrashMenu, self).__init__(game)

    def display_menu(self):
        self.run_display = True

        while self.run_display:
            self.game.check_events()
            if self.game.start_key or self.game.back_key:
                self.game.current_menu = self.game.main_menu
                self.run_display = False

            self.game.display.fill("black")
            self.game.draw_text("You Crashed.", 60, self.game.display_width / 2, self.game.display_height / 2)
            self.blit_screen()
            # Add character select, main menu, and quit menu options here
