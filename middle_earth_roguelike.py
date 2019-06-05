import tcod
import sys
from entity.entity import Creature
from entity.entity import Player
from game_map.map import Map
from layers.console_layers import MainConsole, NewConsole

root_layer = MainConsole()
npc_layer = NewConsole(root_layer.screen_width, root_layer.screen_height)

player = Player(int(root_layer.screen_width/2), int(root_layer.screen_height/2), '@', tcod.green, npc_layer)
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

	key_press = player.handle_keys()
	if key_press:
		break