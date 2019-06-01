import tcod

class TileMap():
    def __init__(self, blocked, sight = None):
        self.blocked = blocked

        if sight == None: sight = blocked
        self.sight = sight

class Rect():
    def __init__(self, x, y, w, h):
        self.x1 = x
        self.y1 = y
        self.x2 = x + w
        self.y2 = y + h

class Map():
    def __init__(self, con):
        self.map_width = 60
        self.map_height = 45
        self.grass_color = tcod.Color(100, 160, 20)
        self.tree_color = tcod.Color(80, 185, 0)
        self.con = con

        self.current_map = [[TileMap(False)
            for y in range(self.map_height)]
                for x in range(self.map_width)]

        #self.current_map[30][22].blocked = True
        #self.current_map[30][22].sight = True
        #self.current_map[50][22].blocked = True
        #self.current_map[50][22].sight = True

    def create_room(self, room):
        pass

    def render_map(self):
        for y in range(self.map_height):
            for x in range(self.map_width):
                wall = self.current_map[x][y].sight
                if wall:
                    tcod.console_put_char_ex(self.con, x, y, '#', self.tree_color, tcod.black)
                else:
                    tcod.console_put_char_ex(self.con, x, y, '.', self.grass_color, tcod.black)