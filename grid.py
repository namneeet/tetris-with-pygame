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

    def draw(self, screen):
        for row in range(self.rows):
            for col in range(self.cols):
                val = self.grid[row][col]
                rect = pygame.Rect(col*self.size+1,row*self.size+1,self.size-1,self.size-1)
                pygame.draw.rect(screen, self.colors[val],rect)