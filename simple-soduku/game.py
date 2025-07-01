import pygame
import os
from grid import Grid

os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d"%  (400,100)

board = pygame.display.set_mode((1200,900))
pygame.display.set_caption("Soduku")


pygame.font.init()
game_font = pygame.font.SysFont("Times New Roman", 70)
game_font2 = pygame.font.SysFont("Comic Sans MS", 25)

grid = Grid(pygame, game_font)
running = True

while(running):
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            running = False
        if(event.type == pygame.MOUSEBUTTONDOWN and not grid.win):
            if(pygame.mouse.get_pressed()[0]):
                pos = pygame.mouse.get_pos()
                grid.get_mouse_click(pos[0], pos[1])

            

    board.fill((0,0,0))


    grid.draw_all(pygame, board)

    if(grid.win == True):
        won_surface = game_font.render("You Won!", False, (0,255,0))
        board.blit(won_surface, (910,650))
        press_space_surface = game_font2.render("Press Space to restart", False, (0,255,200))
        board.blit(press_space_surface, (915,750))

    pygame.display.flip()

    











