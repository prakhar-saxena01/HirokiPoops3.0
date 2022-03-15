from .menu import Menu


class OptionsMenu(Menu):
    def __init__(self, game):
        super(OptionsMenu, self).__init__(game)
        self.state = "Volume"
        self.volume_x, self.volume_y = self.mid_width, self.mid_height - 80
        self.controls_x, self.controls_y = self.mid_width, self.mid_height - 30
        self.cursor_rect.midtop = (self.volume_x + self.offset, self.volume_y)

    def display_menu(self):
        self.run_display = True

        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill("black")
            self.game.draw_text("Options", 40, self.game.display_width / 2, self.game.display_height / 2 - 50)
            self.game.draw_text("Volume", 40, self.volume_x, self.volume_y)
            self.game.draw_text("Controls", 40, self.controls_x, self.controls_y)

            self.draw_cursor()
            self.blit_screen()

    def check_input(self):
        if self.game.back_key:
            self.game.current_menu = self.game.main_menu
            self.run_display = False
        elif self.game.up_key or self.game.down_key:
            if self.state == "Volume":
                self.state = "Controls"
                self.cursor_rect.midtop = (self.controls_x + self.offset, self.controls_y)
            elif self.state == "Controls":
                self.state = "Volume"
                self.cursor_rect.midtop = (self.volume_x + self.offset, self.volume_y)
        elif self.game.start_key:
            # Volume menu?
            # Options menu?
            pass
