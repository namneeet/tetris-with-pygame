import pygame
import sys
import pandas as pd
from game import Game
from score import Score

pygame.init()

yes = pygame.font.Font(None, 80)
yes2 = pygame.font.Font(None, 60)

 
disp = pygame.display.set_mode((1030,690))
pygame.display.set_caption("Tetris")
clk = pygame.time.Clock()

game1 = Game(0)
game2 = Game(330)


# ----------------------- SCORES ------------------------

score = Score()
lb = []


# ----------------------- ------ ------------------------


game_update = pygame.USEREVENT
pygame.time.set_timer(game_update, 120)



while True:

    #checks if "quit" is in the list of events and exits if true

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.KEYDOWN:
            if game1.gameOver == True or game2.gameOver == True:
                
                score.addScore("P1",game1.score)
                score.addScore("P2",game2.score)
                lb = score.display().split("\n")
                    
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
            game1.score += 1
            game2.score += 1
        
              


    disp.fill((55,26,70))
    
    game1.draw(disp)
    game2.draw(disp)
    score1 = yes.render(str(game1.score), True, (255,255,255))
    score2 = yes.render(str(game2.score), True, (255,255,255))

    for i in range(len(lb)):
        lbDisp = yes2.render(lb[i], True, (255,255,255))
        disp.blit(lbDisp,(750,25 + 60*i,50,50))

    disp.blit(score1,(130,25,50,50))
    disp.blit(score2,(460,25,50,50))
    if game1.gameOver == True or game2.gameOver == True:
        gameOverDisplay = yes.render("game over :c", True, (255,255,255))
        disp.blit(gameOverDisplay,(140,300,50,50))



    #updates and sets tick speed to 60 

    pygame.display.update()
    clk.tick(60)