import pygame
import sys
from game import Game

pygame.init()

yes = pygame.font.Font(None, 80)
gameover = yes.render("game over :c", True, (255,255,255))

disp = pygame.display.set_mode((600,600))
player1_rect = pygame.Rect(0,0,300,600)
player2_rect = pygame.Rect(300,0,300,600)

pygame.display.set_caption("Tetris")
clk = pygame.time.Clock()

game1 = Game(0)
game2 = Game(300)


game_update = pygame.USEREVENT
pygame.time.set_timer(game_update, 150)

while True:

    #checks if "quit" is in the list of events and exits if true

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.KEYDOWN:
            if game1.gameOver == True or game2.gameOver == True:
                game1.gameOver = False
                game2.gameOver = False
                game1.reset()
                game2.reset()
            if event.key == pygame.K_LEFT and game2.gameOver == False:
                game2.moveLeft()
            if event.key == pygame.K_RIGHT and game2.gameOver == False:
                game2.moveRight()
            if event.key == pygame.K_DOWN and game2.gameOver == False:
                game2.moveDown()
            if event.key == pygame.K_UP and game2.gameOver == False:
                game2.rotate()
            if event.key == pygame.K_r and game2.gameOver == False:
                game1.reset()
                game2.reset()
            if event.key == pygame.K_a and game1.gameOver == False:
                game1.moveLeft()
            if event.key == pygame.K_d and game1.gameOver == False:
                game1.moveRight()
            if event.key == pygame.K_s and game1.gameOver == False:
                game1.moveDown()
            if event.key == pygame.K_w and game1.gameOver == False:
                game1.rotate()
        if event.type == game_update and game1.gameOver == False and game2.gameOver == False:
            game1.moveDown()
            game2.moveDown()

                

    disp.fill('#000000',player1_rect)
    disp.fill('#FFFFFF',player2_rect)

    game1.draw(disp)
    game2.draw(disp)
    if game1.gameOver == True or game2.gameOver == True:
        disp.blit(gameover,(110,260,50,50))
    #updates and sets tick speed to 60 

    pygame.display.update()
    clk.tick(60)