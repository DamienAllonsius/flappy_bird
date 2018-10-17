import numpy as np
import pygame.mixer
from pygame.locals import *
from bird import *
from environment import *
pygame.init()
fontsize=20
myfont = pygame.font.SysFont("monospace", fontsize)


class UI:
    def __init__(self,bird):

        self.window=pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        self.bird=bird
        self.width = pygame.display.Info().current_w
        self.height = pygame.display.Info().current_h
        self.environment=Environment()
        self.label = None
        self.labelPointBird = None
        
    def drawPoles(self):
        for pole in self.environment.poles:
            pygame.draw.rect(self.window,(255,255,255),(pole.xMin,0,pole.xMax-pole.xMin,pole.yMin))
            pygame.draw.rect(self.window,(255,255,255),(pole.xMin,pole.yMax,pole.xMax-pole.xMin,self.height))


    def drawAll(self):
        # set the black background color and the labels
        self.window.fill((0,0,0))
        self.window.blit(self.label, (self.width-550,self.height-fontsize))
        self.window.blit(self.labelPointBird, (0,self.height-fontsize))
        # draw the birds
        pygame.draw.circle(self.window,self.bird.colorBall,[int(self.bird.x),int(self.bird.y)],self.bird.radius)

        # draw the poles
        self.drawPoles()
        pygame.display.flip()
                 
    def main(self):
        k=0
        pygame.key.set_repeat(1,1)
        
        while(self.environment.cont):
              # Number of points
            self.label =  myfont.render("(Press [ESC] to quit, [UP] or [DOWN] to fly)",3 , (255,255,255))
            self.labelPointBird =  myfont.render("Points = " + str(int(self.bird.points/self.environment.discountFactorPoints)),3 ,self.bird.colorBall)

            # gravity
            
            k+=self.bird.weight
            self.bird.y=self.bird.y + self.environment.gravity*k

            # the poles
            if np.mod(self.environment.cont,self.environment.speedPolesAppearing) ==0:
                self.environment.makePoleRandom(self.width,self.height)
            self.environment.movePoles()

            # draw this state
            self.drawAll()
            
            self.bird.y=self.bird.y + self.environment.gravity*k
            for event in pygame.event.get():
                if (event.type == pygame.KEYDOWN):
                    if (event.key == K_UP):
                        self.bird.y=self.bird.y - self.environment.moveup
                        k=0
                    if (event.key == K_DOWN):
                        self.bird.y=self.bird.y + self.environment.moveup
                        k=0
                    if (event.key == pygame.K_ESCAPE):
                        cont=0

            # are you still alive bird ?
            self.environment.computeCont(self.bird.x,self.bird.y,self.height)
            # then you get points !
            if (self.environment.cont):
                self.bird.points+=1
