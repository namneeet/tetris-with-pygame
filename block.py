from colors import Colors
import pygame
from position import Position

class Block:
    def __init__(self,type):
        self.type = type
        self.cells = {} 
        self.size = 30
        self.row_offset = 0
        self.col_offset = 0
        self.state = 0
        self.colors = Colors.getcolors()

    def move(self,row,col):
        self.row_offset += row
        self.col_offset += col

    def rotate(self):
        self.state += 1
        if self.state == len(self.cells):
            self.state = 0

    def undoRotate(self):
        self.state-=1
        if self.state==-1:
            self.state = len(self.cells)-1
    def getCellPos(self):
        tiles = self.cells[self.state]
        movedTiles = []
        for pos in tiles:
            pos = Position(pos.row + self.row_offset,pos.col + self.col_offset)
            movedTiles.append(pos)
        return movedTiles
  
    def draw(self,screen,offset):
        tiles = self.getCellPos()
        for i in tiles:
            tile = pygame.Rect(i.col*self.size + 1 + offset, i.row*self.size + 91, self.size-1,self.size-1)
            pygame.draw.rect(screen,self.colors[self.type],tile)
            