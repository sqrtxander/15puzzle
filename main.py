import pygame
import sys
from fifteenpuzzle import FifteenPuzzle
from button import Button
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

        title = FONT_BIG.render("15 Puzzle", True, (0, 0, 0))
        title_rect = title.get_rect()
        title_rect.center = WIDTH / 2, HEIGHT / 2 - title_rect.height / 2
        SCREEN.blit(title, title_rect)

        instructions = FONT_BIG.render("Press SPACE to start", True, (0, 0, 0))
        instructions_rect = instructions.get_rect()
        instructions_rect.center = WIDTH / 2, HEIGHT / 2 + instructions_rect.height / 2
        SCREEN.blit(instructions, instructions_rect)

        pygame.display.flip()

def game():
    puzzle = FifteenPuzzle()
    controls_btn = Button(0, 0, "Controls: Arrow keys", FONT_SMALL, BLACK, BLUE)
    controls_btn.rect.topright = WIDTH - GAP, GAP
    controls = False
    clock = pygame.time.Clock()
    moves_lbl = FONT_SMALL.render("Moves: 0", True, BLACK)
    moves_lbl_rect = moves_lbl.get_rect()
    moves_lbl_rect.topright = WIDTH - GAP, GAP + controls_btn.rect.height
    while True:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    puzzle.scramble()
                elif event.key == pygame.K_ESCAPE:
                    menu()
                elif controls:
                    continue
                elif event.key == pygame.K_UP:
                    puzzle.move_tile((0, -1))
                elif event.key == pygame.K_DOWN:
                    puzzle.move_tile((0, 1))
                elif event.key == pygame.K_LEFT:
                    puzzle.move_tile((-1, 0))
                elif event.key == pygame.K_RIGHT:
                    puzzle.move_tile((1, 0))
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    if controls_btn.is_hovering(pygame.mouse.get_pos()):
                        controls = not controls
                        if controls:            
                            controls_btn.text_input = "Controls: Mouse hover"            
                        else:
                            controls_btn.text_input = "Controls: Arrow keys"
                        controls_btn.change_colour(pygame.mouse.get_pos())
                        controls_btn.rect = controls_btn.text.get_rect()
                        controls_btn.rect.topright = WIDTH - GAP, GAP

        SCREEN.fill(WHITE)
        mouse_pos = pygame.mouse.get_pos()

        controls_btn.draw(SCREEN)
        controls_btn.change_colour(mouse_pos)

        puzzle.draw()

        SCREEN.blit(moves_lbl, moves_lbl_rect)



        if controls and not pygame.mouse.get_pressed()[0]:
            puzzle.handle_hover(mouse_pos)

        moves_lbl = FONT_SMALL.render(f"Moves: {puzzle.moves}", True, BLACK)
        moves_lbl_rect = moves_lbl.get_rect()
        moves_lbl_rect.topright = WIDTH - GAP, GAP + controls_btn.rect.height
        SCREEN.blit(moves_lbl, moves_lbl_rect)

        if not puzzle.solved:
            puzzle.solved = puzzle.is_solved()

        pygame.display.flip()

def main():
    pygame.display.set_caption("15 Puzzle")
    menu()
    

if __name__ == "__main__":
    main()