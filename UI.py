"""Welcome to the User Interface"""

import numpy as np
import pygame.mixer
from pygame.locals import *
from environment import Environment

pygame.init()
fontsize = 20
myfont = pygame.font.SysFont("monospace", fontsize)


class UI(object):
    """This class display all the elements of the game
    and make the dynamic moves of the bird and the poles.
    The game ends when all the birds are deads.
    Birds die when hitting a pole or the boundary of the environment"""
    def __init__(self):
        #self.window = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        self.window = pygame.display.set_mode((0,0))
        self.width = pygame.display.Info().current_w
        self.height = pygame.display.Info().current_h
        self.environment = Environment(self.width,self.height)
        
    def draw_poles(self):
        """Draw the poles contained in environment, by default in white"""
        for pole in self.environment.poles:
            pygame.draw.rect(self.window, (255, 255, 255),
                             (pole.position[0],
                              0,
                              pole.position[1] - pole.position[0],
                              pole.position[2]))
            pygame.draw.rect(self.window, (255, 255, 255),
                             (pole.position[0],
                              pole.position[3],
                              pole.position[1] - pole.position[0],
                              self.height))

    def draw_birds(self):
        for bird in self.environment.birds:
            pygame.draw.circle(self.window, bird.color_ball,
                               [int(bird.position[0]),
                                int(bird.position[1])],
                               bird.radius)
    def draw_labels(self):
        label = myfont.render(
            "(Press [ESC] to quit, [UP] or [DOWN] to fly)",
            3, (255, 255, 255))                        
        self.window.blit(label,
                         (self.width - 550, self.height - fontsize))
        i = 0
        for bird in self.environment.birds:
            label_points = myfont.render(
                "Points = " +
                str(int(bird.points / self.environment.discount_factor_points)),
                3,
                bird.color_ball)
            self.window.blit(label_points, (i*fontsize, self.height - fontsize))
            i += 1.5
            
    def drawAll(self):
        """Draw all the components of the game
        the black background color and the labels"""
        self.window.fill((0, 0, 0))
        self.draw_birds()
        self.draw_labels()
        self.draw_poles()
        pygame.display.flip()
                 
    def main(self):
        """The main function where the rules and the dynamic of the game is implemented"""
        multiplicator_gravity = 0
        pygame.key.set_repeat(1, 1)        
        while(self.environment.cont):
            for bird in self.environment.birds:
                multiplicator_gravity += bird.weight
                bird.position[1] += self.environment.gravity * multiplicator_gravity
            if np.mod(self.environment.cont,
                      self.environment.speed_poles_appearing) == 0:
                self.environment.poles.append(self.width, self.height)
                self.environment.movePoles()
            self.drawAll()

            
            # are you still alive bird ?
            self.environment.birds_alive(self.height)

            # player moves 
            for event in pygame.event.get():
                if (event.type == pygame.KEYDOWN):
                    if (event.key == K_UP):
                        self.environment.birds[0].position[1] = self.environment.birds[0].position[1] - self.environment.birds[0].move
                        multiplicator_gravity = 0
                    if (event.key == K_DOWN):
                        self.environment.birds[0].position[1] = self.environment.birds[0].position[1] + self.environment.birds[0].move
                        multiplicator_gravity = 0
                    if (event.key == pygame.K_ESCAPE):
                        self.environment.cont=0

            
