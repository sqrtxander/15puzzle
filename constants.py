import pygame
pygame.init()
ROWS, COLS = 4, 4
TILE_WIDTH = 128
GAP = TILE_WIDTH / 20
WIDTH, HEIGHT = TILE_WIDTH * COLS, TILE_WIDTH * (ROWS + 1)
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
FONT = pygame.font.Font("assets/ka1.ttf", 36)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
ORANGE = (255, 140, 0)
YELLOW = (246, 190, 0)
GREEN = (0, 100, 0)
BLUE = (0, 0, 255)
PURPLE = (128, 0, 128)