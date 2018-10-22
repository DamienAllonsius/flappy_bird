"""This class represents the object 'Bird' that has to go through
the holes represented by the space between to vertical plots
(see the Plot class)."""
import random
class Bird(object):
    """The bird class which is now represented as a green ball.
    The Bird is drawn by the class UI."""
    def __init__(self):
        self.position = [150, 300]
        self.color_ball = (random.randrange(256), 120, random.randrange(256))
        self.radius = random.randrange(10,25)
        self.weight = 0.001 * self.radius/20
        self.points = 0
        self.move = 5
        self.alive = 1

    def take_action(self, pole_y_min, pole_y_max):
        """The bird takes the appropriate action according to its y position
        and the position of the holes of the nearest poles. If the bird is
        too high then it goes down, and conversely."""
        if self.position[1] > pole_y_max-50:
            self.position[1] -= self.move
        elif self.position[1] < pole_y_min+50:
            self.position[1] += self.move

    def gain_weight(self):
        """The bird will be able to gain weight at some point.
        (when hitting a special Bonus that will appear soon in the code)."""
        self.weight += 1

    def go_up(self, gain_y):
        """The bird y position will be increased a factor depending on
        gain_y and weight"""
        self.position[1] -= gain_y * self.weight


    def go_down(self, lose_y):
        """The bird y position will be decreased a factor depending on
        lose_y and weight"""
        self.position[1] += lose_y * self.weight

    def is_alive(self, height, pole):
        """This method tells if the bird has hit a pole or the boundary"""
        self.alive = not(self.position[1] < 0 or self.position[1] > height or \
            ((self.position[0] > pole.position[0]) and (self.position[0] < pole.position[1]) \
             and ((self.position[1] < pole.position[2]) or (self.position[1] > pole.position[3]))))
