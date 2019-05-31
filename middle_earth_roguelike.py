import pygame
import tcod
import sys
from entity.entity import Creature
from game_map.map import Map
from layers.console_layers import MainConsole, NewConsole

def handle_keys():
	key = tcod.console_wait_for_keypress(True)

	if key.vk == tcod.KEY_ENTER and key.lalt:
		tcod.console_set_fullscreen(not tcod.console_is_fullscreen())

	elif key.vk == tcod.KEY_ESCAPE:
		return True

	if tcod.console_is_key_pressed(tcod.KEY_UP):
		player.movement(0, -1)

	elif tcod.console_is_key_pressed(tcod.KEY_DOWN):
		player.movement(0, 1)

	elif tcod.console_is_key_pressed(tcod.KEY_LEFT):
		player.movement(-1, 0)

	elif tcod.console_is_key_pressed(tcod.KEY_RIGHT):
		player.movement(1, 0)

pygame.init()

root_layer = MainConsole()
npc_layer = NewConsole(root_layer.screen_width, root_layer.screen_height)

player = Creature(int(root_layer.screen_width/2), int(root_layer.screen_height/2), '@', tcod.green, npc_layer)
npc = Creature(int(root_layer.screen_width/2 - 5), int(root_layer.screen_height/2), '@', tcod.yellow, npc_layer)
creatures = [player, npc]

current_map = Map(root_layer)

while not tcod.console_is_window_closed():
	current_map.render_map()

	for entity in creatures:
		entity.draw()

	root_layer.add_layer(npc_layer)

	root_layer.update()

	for entity in creatures:
		entity.clear()

	#key = pygame.event.poll()

	key_press = handle_keys()
	if key_press:
		break