from src.config import game, snake as config
from src.chromosome import Chromosome
from random import randint

class Entity(Chromosome):

    def __init__(self, last_name):

        self.size = config['size']
        self.color = config['color']
        self.speed = config['speed']
        self.first_name = config['first_name']
        self.name = "%s_%s" % (self.first_name, last_name)
        self.alive = True

        screen_size = game['screen_size']

        Chromosome.__init__(self)
        self.coord = self.generate_random_position(screen_size)
        self.direction = 0
        self.prev_direction = 4


    def update_coord(self):

        # 0 -> Empty
        # 1 -> Right
        # 2 -> Down
        # 3 -> Left
        # 4 -> Up

        if self.direction == 0:
            self.direction = self.prev_direction

        if self.direction == 1:
            self.coord[0] -= self.speed
        elif self.direction == 2:
            self.coord[1] -= self.speed
        elif self.direction == 3:
            self.coord[0] += self.speed
        elif self.direction == 4:
            self.coord[1] += self.speed


    def update_direction(self, key=None):

        if key != None:
            self.direction = {276: 1, 275: 3, 274: 4, 273: 2}.get(key, self.direction)
        else:
            if self.chromosome_index < len(self.chromosome) - 1:
                self.chromosome_index += 1
                self.direction = self.chromosome[self.chromosome_index]


    def generate_random_position(self, screen_size):

        x = randint(0, screen_size[0] - self.size[0])
        y = randint(0, screen_size[1] - self.size[1])
        # return [x, y]
        return [200, 200]


    def kill(self):

        self.chromosom_score = 0
        self.speed = 0
        self.alive = False
