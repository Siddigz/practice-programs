import pygame
import os

os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d"%  (400,100)

board = pygame.display.set_mode((1200,900))
pygame.display.set_caption("Soduku")

running = True

while(running):
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            running = False

    board.fill((0,0,0))

    pygame.display.flip()

    











