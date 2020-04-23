import pygame
pygame.font.init()

'''
Drawing The middle of the Game and The Players... 
'''
class Table:
    def __init__(self,win,width,height):
        self.cords = [(int(width*47.3/100),int(height*42.9/100)),(int(width*53.8/100),int(height*40.9/100)),(int(width*53.8/100),int(height*29.9/100)),(int(width*47.3/100),int(height*19.5/100)),(int(width*36.9/100),int(height*29.9/100)),(int(width*36.9/100),int(height*40.9/100))]
        self.plCords = [(int(width*44.6/100),int(height*85/100)),(int(width*66.2/100),int(height*40.9/100)),(int(width*66.2/100),int(height*29.9/100)),(int(width*43.1/100),int(height*7.8/100)),(int(width*21.5/100),int(height*29.9/100)),(int(width*21.5/100),int(height*40.9/100))]
        self.plW = int(width*11.5/100)
        self.plH = int(height*6.5/100)
        self.width = width
        self.height = height
        pygame.draw.rect(win,(100,100,0),(int(width*37.3/100),int(height*19.5/100),int(width*25.8/100),int(height*39/100)))

    def draw(self,win,im,p):
        if p == 1 or p == 2:
            im = pygame.transform.rotate(im,-90)
        if p == 4 or p == 5:
            im = pygame.transform.rotate(im,90)
        win.blit(im,self.cords[p])

    def draw_player(self,win,p,text):
        color = (51,102,255)
        if p == 0 or p == 2 or p == 4:
            color = (255,153,0)
        pygame.draw.rect(win,color,(self.plCords[p][0],self.plCords[p][1],self.plW,self.plH))
        font = pygame.font.SysFont('comicsans',int(self.width*3.1/100))
        text = font.render(text,1,(0,0,0))
        win.blit(text,(self.plCords[p][0]+int(self.width*0.77/100),self.plCords[p][1]+int(self.height*2/100)))

