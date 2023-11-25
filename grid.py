import pygame
from colors import Colors
class Grid:
    def __init__(self):
        self.rows = 20
        self.cols = 10
        self.size = 30
        self.grid = [[0 for j in range(self.cols)] for i in range(self.rows)]
        #gray,green,red,yellow,purple,cyan,blue
        self.colors = Colors.getcolors()

    def print_grid(self):
        for row in range(self.rows):
            for col in range(self.cols):
                print(self.grid[row][col], end = " ")
            print()

    def inside(self,row,col):
        if row>=0 and row<self.rows and col<self.cols and col>=0:
            return True
        return False

    def empty(self,row,col):
        if self.grid[row][col] == 0:
            return True
        return False
    
    def rowFull(self,row):
        for i in range(self.cols):
            if self.grid[row][i] == 0:
                return False
        return True

    def clear(self,row):
        for i in range(self.cols):
            self.grid[row][i] = 0

    def moveRow(self,row,numRows):
        for i in range(self.cols):
            self.grid[row+numRows][i] = self.grid[row][i]
            self.grid[row][i] = 0

    def clearRow(self):
        completed = 0
        for i in range(self.rows-1,0,-1):
            if self.rowFull(i):
                self.clear(i)
                completed += 1
            elif completed > 0:
                self.moveRow(i,completed)
        return completed

    def reset(self):
        for i in range(self.rows):
            for j in range(self.cols):
                self.grid[i][j] = 0

    def draw(self,screen,offset):
        for row in range(self.rows):
            for col in range(self.cols):
                val = self.grid[row][col]
                rect = pygame.Rect(col*self.size+1+offset,row*self.size+91,self.size-1,self.size-1)
                pygame.draw.rect(screen, self.colors[val],rect)