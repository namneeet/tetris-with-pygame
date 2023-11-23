from colors import Colors
import pygame

class Block:
    def __init__(self,type):
        self.type = type
        self.cells = {} 
        self.size = 30
        self.state = 0
        self.colors = Colors.getcolors()

    def draw(self,screen):
        tiles = self.cells[self.state]
        for i in tiles:
            tile = pygame.Rect(i.col*self.size + 1, i.row*self.size + 1, self.size-1,self.size-1)
            pygame.draw.rect(screen,self.colors[self.type],tile)
            