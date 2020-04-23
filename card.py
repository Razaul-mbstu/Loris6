import pygame

class Card:
    def __init__(self,id,x,y,width,height):
        self.id = id
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.show = True

    def setImage(self,image):
        self.image = pygame.transform.scale(image,(self.width,self.height))

    def draw(self,win):
        win.blit(self.image,(self.x,self.y))

    def click(self,pos):
        x1 = pos[0]
        y1 = pos[1]

        if self.x <= x1 <= self.x + self.width and self.y <= y1 <= self.y + self.height and self.show:
            return True
        else:
            return False
