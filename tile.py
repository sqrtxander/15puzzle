import pygame
from constants import *


class Tile:
    def __init__(self, colour, text_colour, num, x, y):
        self.colour = colour
        self.text_colour = text_colour
        self.num = num
        self.x = x
        self.y = y
        self.rect = pygame.Rect(x * TILE_WIDTH + GAP / 2,
                                (y + 1) * TILE_WIDTH + GAP / 2,
                                TILE_WIDTH - GAP,
                                TILE_WIDTH - GAP)

    def draw(self):
        if self.num is None:
            return

        pygame.draw.rect(SCREEN, self.colour, self.rect)
        label = FONT_BIG.render(str(self.num), True, self.text_colour)
        label_rect = label.get_rect()
        label_rect.center = self.rect.center
        SCREEN.blit(label, label_rect)

    def update_rect(self):
        self.rect.x = self.x * TILE_WIDTH + GAP / 2
        self.rect.y = (self.y + 1) * TILE_WIDTH + GAP / 2
