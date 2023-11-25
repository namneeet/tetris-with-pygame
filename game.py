from grid import Grid
from blocks import *
import random

class Game:
    def __init__(self,offset):
        self.score = 0
        self.offset = offset
        self.grid = Grid()
        self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
        self.cur = self.getRandomBlock()
        self.next = self.getRandomBlock()
        self.gameOver = False

    def getRandomBlock(self):
        if len(self.blocks) == 0:
            self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
        block = random.choice(self.blocks)
        self.blocks.remove(block)
        return block

    def moveLeft(self): 
        self.cur.move(0,-1)
        if self.blockInside() == False or self.blockFits() == False:
            self.cur.move(0,1)
    def moveRight(self):
        self.cur.move(0,1)
        if self.blockInside() == False or self.blockFits() == False:
            self.cur.move(0,-1)
    def moveDown(self):
        self.cur.move(1,0)
        if self.blockInside() == False or self.blockFits() == False: 
            self.cur.move(-1,0)
            self.lockBlock()
    def lockBlock(self):
        tiles = self.cur.getCellPos()
        for i in tiles:
            self.grid.grid[i.row][i.col] = self.cur.type
        self.cur = self.next
        self.next = self.getRandomBlock()
        self.score += 100*self.grid.clearRow()
        if self.blockFits() == False:
            self.gameOver=True

    def reset(self):
        self.grid.reset()
        self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
        self.cur = self.getRandomBlock()
        self.next = self.getRandomBlock()
        self.score = 0
    
    def blockFits(self):
        tiles = self.cur.getCellPos()
        for i in tiles:
            if self.grid.empty(i.row,i.col) == False:
                return False
        return True
    def rotate(self):   
        self.cur.rotate()
        if self.blockInside() == False or self.blockFits() == False:
            self.cur.undoRotate()
    def blockInside(self):
        tiles = self.cur.getCellPos()
        for i in tiles:
            if self.grid.inside(i.row,i.col) == False:
                return False
        return True
    def draw(self,screen):
        self.grid.draw(screen,self.offset)
        self.cur.draw(screen,self.offset)