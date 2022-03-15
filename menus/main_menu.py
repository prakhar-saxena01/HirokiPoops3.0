from .menu import Menu


class MainMenu(Menu):
    def __init__(self, game):
        super(MainMenu, self).__init__(game)
        self.state = "Start"
        self.start_x, self.start_y, = self.mid_width, self.mid_height - 120
        self.options_x, self.options_y, = self.mid_width, self.mid_height - 70
        self.credits_x, self.credits_y, = self.mid_width, self.mid_height - 20
        self.cursor_rect.midtop = (self.start_x + self.offset, self.start_y)

    def display_menu(self):
        self.run_display = True

        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill("black")
            self.game.draw_text("Main Menu", 40, self.game.display_width / 2, self.game.display_height / 2 - 80)
            self.game.draw_text("Play!", 40, self.start_x, self.start_y)
            self.game.draw_text("Options", 40, self.options_x, self.options_y)
            self.game.draw_text("Credits", 40, self.credits_x, self.credits_y)
            self.draw_cursor()
            self.blit_screen()

    def move_cursor(self):
        if self.game.down_key:
            if self.state == 'Start':
                self.cursor_rect.midtop = (self.options_x + self.offset, self.options_y)
                self.state = 'Options'
            elif self.state == 'Options':
                self.cursor_rect.midtop = (self.credits_x + self.offset, self.credits_y)
                self.state = 'Credits'
            elif self.state == 'Credits':
                self.cursor_rect.midtop = (self.start_x + self.offset, self.start_y)
                self.state = 'Start'
        elif self.game.up_key:
            if self.state == 'Start':
                self.cursor_rect.midtop = (self.credits_x + self.offset, self.credits_y)
                self.state = 'Credits'
            elif self.state == 'Options':
                self.cursor_rect.midtop = (self.start_x + self.offset, self.start_y)
                self.state = 'Start'
            elif self.state == 'Credits':
                self.cursor_rect.midtop = (self.options_x + self.offset, self.options_y)
                self.state = 'Options'

    def check_input(self):
        self.move_cursor()
        if self.game.start_key:
            if self.state == "Start":
                self.game.playing = True
            elif self.state == "Options":
                self.game.current_menu = self.game.options
            elif self.state == "Credits":
                self.game.current_menu = self.game.credits

            self.run_display = False
