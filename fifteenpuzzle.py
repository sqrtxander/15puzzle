import random
from tile import Tile
from constants import *

def init_colour(x, y):
    if y == 0:
        return RED, WHITE
    elif x == 0:
        return ORANGE, WHITE
    elif y == 1:
        return YELLOW, WHITE
    elif x == 1:
        return GREEN, WHITE
    elif y == 2:
        return BLUE, WHITE
    elif x == 2:
        return PURPLE, WHITE
    else:
        return WHITE, BLACK

class FifteenPuzzle:
    def __init__(self):
        self.tiles = []
        for y in range(ROWS):
            self.tiles.append([])
            for x in range(COLS):
                self.tiles[y].append(Tile(*init_colour(x, y), y * 4 + x + 1, x, y))

        self.empty_x, self.empty_y = COLS - 1, ROWS - 1
        self.tiles[self.empty_y][self.empty_x].colour = WHITE
        self.tiles[self.empty_y][self.empty_x].num = None

    def draw(self):
        for row in self.tiles:
            for tile in row:
                tile.draw()

    def move_tile(self, direction):

        new_x = self.empty_x - direction[0]
        new_y = self.empty_y - direction[1]

        if new_x < 0 or new_x >= COLS or new_y < 0 or new_y >= ROWS:
            return


        self.tiles[self.empty_y][self.empty_x].x -= direction[0]
        self.tiles[self.empty_y][self.empty_x].y -= direction[1] 
        self.tiles[new_y][new_x].x += direction[0]
        self.tiles[new_y][new_x].y += direction[1]

        self.tiles[self.empty_y][self.empty_x], self.tiles[new_y][new_x] = self.tiles[new_y][new_x], self.tiles[self.empty_y][self.empty_x]
                
        self.tiles[self.empty_y][self.empty_x].update_rect()
        self.tiles[new_y][new_x].update_rect()

        self.empty_x -= direction[0]
        self.empty_y -= direction[1]

    def scramble(self):
        directions = ((1, 0), (0, 1), (-1, 0), (0, -1))
        for _ in range(1000):

            direction = random.choice(directions)
            
            self.move_tile(direction)

    def handle_hover(self, mouse_pos):
        x = mouse_pos[0] // TILE_WIDTH
        y = mouse_pos[1] // TILE_WIDTH - 1

        if x < 0 or x >= COLS or y < 0 or y >= ROWS:
            return
        if self.tiles[y][x].num is None:
            return
        if abs(self.empty_x - x) + abs(self.empty_y - y) != 1:
            return
        
        dx = self.empty_x - x
        dy = self.empty_y - y
        self.move_tile((dx, dy))


    def is_solved(self):
        for row in self.tiles:
            for tile in row:
                if tile.num is not None and tile.num != tile.y * 4 + tile.x + 1:
                    return False
        return True
