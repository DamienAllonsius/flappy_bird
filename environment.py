"""This class will deal with all the variables
of the game environment:
the bird, the poles, the points, the speed, gravity..."""
from pole import Pole
from bird import Bird

class Environment(object):
    """This class make the poles appear and move.
    It contains the variable cont
    which is 0 if the player lost"""
    def __init__(self, width, height):
        self.gravity = 10
        self.speed_pole_moving = 1
        self.discount_factor_points = 100
        self.speed_poles_appearing = 500
        self.birds = [Bird()]
        self.poles = [Pole(width, height)] 
        self.cont = 1

    def move_poles(self):
        """This method make the poles move and disappear
        when they are behind the bird"""
        for pole in self.poles:
            pole.move_pole()
        x_max_bird = 0
        for bird in self.birds:
            x_max_bird = max(x_max_bird, bird.position[0])
        if self.poles[0].position[1] < x_max_bird:
            self.poles = self.poles[1:]

    def birds_alive(self, height):
        """Refresh the status of birds (points + alive)"""
        all_cont = False
        for bird in self.birds:
            bird.is_alive(height, self.poles[0])
            if bird.alive:
                bird.points += 1
                all_cont = all_cont or bird.alive
        self.cont=all_cont
