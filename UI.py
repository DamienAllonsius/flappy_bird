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
        self.birdImage=pygame.image.load(self.bird.getPathBirdImage()).convert_alpha()
        self.width = pygame.display.Info().current_w
        self.height = pygame.display.Info().current_h
        self.environment=Environment()
        self.label = None
        
    def drawPlots(self):
        for plot in self.environment.plots:
            pygame.draw.rect(self.window,(255,255,255),(plot.xMin,0,plot.xMax-plot.xMin,plot.yMin))
            pygame.draw.rect(self.window,(255,255,255),(plot.xMin,plot.yMax,plot.xMax-plot.xMin,self.height))

    def drawAll(self):
        self.window.fill((0,0,0))
        self.window.blit(self.label, (self.width-700,self.height-fontsize))
        self.window.blit(self.birdImage,[self.bird.getPositionX(),self.bird.getPositionY()])
        self.drawPlots()
        pygame.display.flip()
                 
    def main(self):
        k=0
        pygame.key.set_repeat(1,1)
        
        while(self.environment.cont):
            
            k+=self.bird.weight
            self.environment.points+=1
            self.label =  myfont.render("Points = " + str(int(self.environment.points/self.environment.discountFactorPoints)) + "(Press [ESC] to quit, [UP] or [DOWN] to fly)",3 , (124,255,0))

            # the plots
            if np.mod(self.environment.points,self.environment.speedPlotsAppearing) ==0:
                self.environment.makePlotRandom(self.width,self.height)
            self.environment.movePlots()

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

            self.environment.computeCont(self.bird.getPositionX(),self.bird.getPositionY(),self.height)
            
        

        
        
