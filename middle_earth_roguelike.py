import tcod
import sys

screen_width = 80
screen_height = 60
playerx = int(screen_width/2)
playery = int(screen_height/2)

tcod.console_set_custom_font('arial10x10.png', tcod.FONT_TYPE_GRAYSCALE | tcod.FONT_LAYOUT_TCOD)

tcod.console_init_root(screen_width, screen_height, 'Middle Earth RL', False)

while not tcod.console_is_window_closed():
	tcod.console_set_default_foreground(0, tcod.green)

	tcod.console_put_char(0, playerx, playery, '@', tcod.BKGND_NONE)

	tcod.console_flush()
