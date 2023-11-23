from colors import Colors

class Block:
    def __innit__(self,type):
        self.type = type
        self.cells = {} 
        self.size = 30
        self.state = 0
        self.colors = Colors.getcolors()

    def draw(self,screen):
