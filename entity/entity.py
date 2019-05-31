import tcod

class Creature():
    def __init__(self, x, y, char, color, console):
        self.x = x
        self.y = y
        self.char = char
        self.color = color
        self.con = console

    def movement(self, dx, dy):
        self.x += dx
        self.y += dy

    def draw(self):
        tcod.console_set_default_foreground(self.con, self.color)
        tcod.console_put_char(self.con, self.x, self.y, self.char, tcod.BKGND_NONE)

    def clear(self):
        tcod.console_put_char(self.con, self.x, self.y, ' ', tcod.BKGND_NONE)