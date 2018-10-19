"""The bird has to get through the poles !"""
import random

class Pole(object):
    """A pole is constituted of two vertical
    (and aligned) obstacles for the bird.
    The bird must go through a hole between
    the two obstacles"""

    def __init__(self, width, height):
        self.pole_width_max = 1/10
        self.pole_height_max = 0.75
        # the hole between the two obstacles.
        self.pole_hole = 0.3
        plot_height = random.randrange(int(height * self.pole_height_max))
        self.position = [width - random.randrange(1, int(width * self.pole_width_max)),
                         width,
                         plot_height,
                         plot_height + height * self.pole_hole]

    def move_pole(self, speed_pole_moving):
        """This makes the pole move toward the bird"""
        self.position[0] -= speed_pole_moving
        self.position[1] -= speed_pole_moving
