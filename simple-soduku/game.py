import pygame
import os
from grid import Grid

os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d"%  (400,100)

board = pygame.display.set_mode((1200,900))
pygame.display.set_caption("Soduku")


pygame.font.init()
game_font = pygame.font.SysFont("Times New Roman", 70)

grid = Grid(game_font)
running = True

while(running):
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            running = False

            

    board.fill((0,0,0))


    grid.draw_all(pygame, board)

    pygame.display.flip()

    











