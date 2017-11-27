from src.config import chromossome as config 
import random

class Chromosome:

    def __init__(self):

        self.max_size = config['max_size']
        self.min_size = config['min_size']
        self.mutation_chance = config['mutation_chance']
        self.chromosome = self.generate_random_chromosome(self.min_size, self.max_size)
        self.chromosome_index = 0
        self.chromosome_score = 0

        random.seed(None)


    def generate_random_chromosome(self, min_size, max_size):

        random_chromosome = []

        for x in range(random.randint(min_size, max_size)):
            random_chromosome.append(random.randint(0, 4))

        return random_chromosome


    def mutate_chromosome(self):

        if random.random() < self.mutation_chance:
            start_pos = random.randint(0, len(self.chromosome)-1)
            end_pos = start_pos + random.randint(0, 5)

            for index in range(start_pos, end_pos):
                if index < len(self.chromosome):
                    self.chromosome[index] = random.randint(0, 4)
