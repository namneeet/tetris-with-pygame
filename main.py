import pygame
import sys
from grid import Grid
from blocks import *

pygame.init()

disp = pygame.display.set_mode((300,600))
pygame.display.set_caption("Tetris")

gridPlane = Grid()
gridPlane.print_grid()

clk = pygame.time.Clock()

block = TBlock()


while True:

    #checks if "quit" is in the list of events and exits if true

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    disp.fill((87,60,125))
    gridPlane.draw(disp)
    block.draw(disp)

    #updates and sets tick speed to 60 

    pygame.display.update()
    clk.tick(60)