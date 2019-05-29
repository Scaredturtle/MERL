import tdl
import tcod
import sys

def game():
	sw = 80
	sh = 60
	player_posx = sw/2
	player_posy = sh/2

	tcod.console_set_custom_font('arial10x10.png', tcod.FONT_TYPE_GRAYSCALE | tcod.FONT_LAYOUT_TCOD)

	tcod.console_init_root(sw, sh, 'Middle Earth RL', False)

	while not tcod.console_is_window_closed():
		tcod.console_set_default_foreground(0, tcod.green)

		tcod.console_put_char(0, 1, 1, '@', tcod.BKGND_NONE)

		tcod.console_flush()

if __name__ == '__main__':
	game()
	sys.exit