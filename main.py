import pygame
import sys
from game import Game

pygame.init()

disp = pygame.display.set_mode((300,600))
pygame.display.set_caption("Tetris")

clk = pygame.time.Clock()

game = Game()

game_update = pygame.USEREVENT
pygame.time.set_timer(game_update, 150)

while True:

    #checks if "quit" is in the list of events and exits if true

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if game.gameOver == True:
                game.gameOver = False
                game.reset()
            if event.key == pygame.K_LEFT and game.gameOver == False:
                game.moveLeft()
            if event.key == pygame.K_RIGHT and game.gameOver == False:
                game.moveRight()
            if event.key == pygame.K_DOWN and game.gameOver == False:
                game.moveDown()
            if event.key == pygame.K_UP and game.gameOver == False:
                game.rotate()
        if event.type == game_update and game.gameOver == False:
            game.moveDown()
        
    disp.fill((87,60,125))
    game.draw(disp)
    #updates and sets tick speed to 60 

    pygame.display.update()
    clk.tick(60)