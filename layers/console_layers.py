import tcod

class MainConsole():
    def __init__(self):
        self.screen_width = 80
        self.screen_height = 60

        tcod.console_set_custom_font('arial10x10.png', tcod.FONT_TYPE_GRAYSCALE | tcod.FONT_LAYOUT_TCOD)
        tcod.console_init_root(self.screen_width, self.screen_height, 'Middle Earth RL', False)

    def add_layer(self, new_layer):
        tcod.console_blit(new_layer, 0, 0, self.screen_width, self.screen_height, 0, 0, 0)

    def update(self):
        tcod.console_flush()

class NewConsole():
    def __init__(self, width, height):
        self.width = width
        self.height = height

        tcod.console_new(self.width, self.height)
