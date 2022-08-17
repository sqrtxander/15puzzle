import pygame
import sys
from fifteenpuzzle import FifteenPuzzle
from constants import *

pygame.init()

def menu():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    game()
                

        SCREEN.fill(WHITE)

        title = FONT.render("15 Puzzle", True, (0, 0, 0))
        title_rect = title.get_rect()
        title_rect.center = WIDTH / 2, HEIGHT / 2 - title_rect.height / 2
        SCREEN.blit(title, title_rect)

        instructions = FONT.render("Press SPACE to start", True, (0, 0, 0))
        instructions_rect = instructions.get_rect()
        instructions_rect.center = WIDTH / 2, HEIGHT / 2 + instructions_rect.height / 2
        SCREEN.blit(instructions, instructions_rect)


        pygame.display.flip()

def game():
    puzzle = FifteenPuzzle()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    puzzle.move_tile((0, -1))
                elif event.key == pygame.K_DOWN:
                    puzzle.move_tile((0, 1))
                elif event.key == pygame.K_LEFT:
                    puzzle.move_tile((-1, 0))
                elif event.key == pygame.K_RIGHT:
                    puzzle.move_tile((1, 0))
                elif event.key == pygame.K_SPACE:
                    puzzle.scramble()
                elif event.key == pygame.K_ESCAPE:
                    menu()
        
        SCREEN.fill(WHITE)
        
        puzzle.draw()

        pygame.display.flip()

def main():
    pygame.display.set_caption("15 Puzzle")
    menu()
    

if __name__ == "__main__":
    main()