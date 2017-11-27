import random
from src.config import generation as config
from src.entity import Entity

class Generation:

    def __init__(self):

        self.population_size = config['population_size']
        self.die_chance = config['die_chance']

        self.index = 1
        self.population = self.generate_initial_population()

        random.seed(None)
        

    def generate_initial_population(self):

        return [Entity("%s_%s" % (self.index, ent)) for ent in range(self.population_size)]


    def order_population(self):

        self.population.sort(key=lambda entity: entity.chromosome_score, reverse=True)

    
    def kill_weak(self):

        body_count = 0
        for index in range(self.population_size):

            if random.random()*index > self.die_chance:
                self.population[index] = Entity("%s_%s" % (self.index+1, index))
                body_count += 1
            else:
                self.population[index].mutate_chromosome()
                self.population[index].chromosome_score = 0

        return body_count


    def advance_generation(self):

        self.order_population()
        best_entity = self.population[0].name
        body_count = self.kill_weak()
        generation_index = self.index
        self.index += 1

        return generation_index, body_count, best_entity
                
