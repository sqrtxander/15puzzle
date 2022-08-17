import pygame
from constants import *

class Button:
    def __init__(self, x, y, text_input, base_colour, hovering_colour):
        self.x = x
        self.y = y
        self.text_input = text_input
        self.base_colour = base_colour
        self.hovering_colour = hovering_colour
        
        self.text = FONT.render(self.text_input, True, self.base_colour)

        self.rect = self.text.get_rect()
        self.rect.center = (self.x, self.y)

    def draw(self, screen):
        screen.blit(self.text, self.rect)

    def is_hovering(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            return True
        return False

    def change_colour(self, mouse_pos):
        if self.is_hovering(mouse_pos):
            self.text = FONT.render(self.text_input, True, self.hovering_colour)
        else:
            self.text = FONT.render(self.text_input, True, self.base_colour)