"""Welcome to the User Interface"""

import numpy as np
import pygame.mixer
from pygame.locals import *
from environment import Environment

pygame.init()
fontsize = 20
myfont = pygame.font.SysFont("monospace", fontsize)


class UI:
    """This class display all the elements of the game
    and make the dynamic moves of the bird and the poles.
    The game ends when all the birds are deads.
    Birds die when hitting a pole or the boundary of the environment"""
    def __init__(self, bird):
        self.window = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        self.width = pygame.display.Info().current_w
        self.height = pygame.display.Info().current_h
        self.environment = Environment(width,height)
        self.label = None
        self.labelPointBird = None
        
    def drawPoles(self):
        """Draw the poles contained in environment, by default in white"""
        for pole in self.environment.poles:
            pygame.draw.rect(self.window, (255, 255, 255), (pole.position[0], 0, pole.position[1] - pole.position[0], pole.position[2]))
            pygame.draw.rect(self.window, (255, 255, 255), (pole.position[0], pole.position[3], pole.position[1] - pole.position[0], self.height))

    def drawAll(self):
        """Draw all the components of the game"""
        # set the black background color and the labels
        self.window.fill((0, 0, 0))
        self.window.blit(self.label, (self.width - 550, self.height - fontsize))
        self.window.blit(self.labelPointBird, (0, self.height - fontsize))
        # draw the birds
        pygame.draw.circle(self.window, self.bird.color_ball, [int(self.bird.position[0]), int(self.bird.position[1])], self.bird.radius)
        # draw the poles
        self.drawPoles()
        pygame.display.flip()
                 
    def main(self):
        """The main function where the rules and the dynamic of the game is implemented"""
        k = 0
        pygame.key.set_repeat(1, 1)
        
        while(self.environment.cont):
              # Number of points
            self.label = myfont.render("(Press [ESC] to quit, [UP] or [DOWN] to fly)", 3, (255, 255, 255))
            self.labelPointBird = myfont.render("Points = " + str(int(self.bird.points / self.environment.discountFactorPoints)), 3, self.bird.color_ball)
            # gravity
            k += self.bird.weight
            self.bird.position[1] = self.bird.position[1] + self.environment.gravity * k
            # the poles
            if np.mod(self.environment.cont, self.environment.speedPolesAppearing) == 0:
                self.environment.makePoleRandom(self.width, self.height)
            self.environment.movePoles()
            # draw this state
            self.drawAll()
            self.bird.position[1] = self.bird.position[1] + self.environment.gravity * k
            
            # player moves 
            for event in pygame.event.get():
                if (event.type == pygame.KEYDOWN):
                    if (event.key == K_UP):
                        self.bird.position_y = self.bird.position_y - self.bird.move
                        k = 0
                    if (event.key == K_DOWN):
                        self.bird.position_y = self.bird.position_y + self.bird.move
                        k = 0
                    if (event.key == pygame.K_ESCAPE):
                        cont = 0


            self.bird.take_action(pole_y_min, pole_y_max)
            
            # are you still alive bird ?
            self.environment.computeCont(self.bird.position[0], self.bird.position[1], self.height)
            # then you get points !
            if (self.environment.cont):
                self.bird.points += 1
