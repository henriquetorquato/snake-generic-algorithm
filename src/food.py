from src.config import game, apple as config
from random import randint

class Food:

    def __init__(self):

        self.color = config['color']
        self.value = config['value']
        self.size = config['size']

        screen_size = game['screen_size']

        self.coord = self.generate_random_position(screen_size)


    def generate_random_position(self, screen_size):

        x = randint(0, screen_size[0] - self.size[0])
        y = randint(0, screen_size[1] - self.size[1])
        # return [x, y]
        return [200, 50]
