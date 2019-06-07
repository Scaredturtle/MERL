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

class Player(Creature):
    def __init__(self, x, y, char, color, console):
        Creature.__init__(self, x, y, char, color, console)

    def handle_keys(self):
        key = tcod.console_wait_for_keypress(True)

        if key.vk == tcod.KEY_ENTER and key.lalt:
            tcod.console_set_fullscreen(not tcod.console_is_fullscreen())
        elif key.vk == tcod.KEY_ESCAPE:
            return True

        if key.vk == tcod.KEY_UP:
            self.movement(0, -1)
        elif key.vk == tcod.KEY_DOWN:
            self.movement(0, 1)
        elif key.vk == tcod.KEY_LEFT:
            self.movement(-1, 0)
        elif key.vk == tcod.KEY_RIGHT:
            self.movement(1, 0)