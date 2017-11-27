import sys, pygame, math
from pygame.locals import *
from src.config import game as config
from src.entity import Entity
from src.food import Food
from src.generation import Generation

class Field:

    def __init__(self):

        self.screen_size = config['screen_size']
        self.frames_sec = config['frames']
        self.time_multiplier = config['time_multiplier']
        self.total_time = config['time']
        self.background_color = config['background_color']
        self.text_color = config['text_color']
        self.display = config['display']
        self.min_distance_to_score = config['min_distance_to_score']

        self.generation = Generation()

        if self.display:

            pygame.init()

            self.screen = pygame.display.set_mode(self.screen_size)
            self.screen.fill(self.background_color)

            self.font = pygame.font.SysFont("Arial", 20)

            self.clock = pygame.time.Clock()


    def start(self):

        while True:

            print("Generation: %s | Population: %s" % (self.generation.index, self.generation.population_size))

            for entity in self.generation.population:

                self.food = Food()
                self.time = self.frames_sec * self.total_time

                while self.time > 0 and entity.alive:

                    if self.display:
                        self.display_screen_info(entity, pygame.event.get())

                    entity.update_direction()
                    entity.update_coord()
                    self.check_bounds_collision(entity, self.screen_size)
                    self.check_food_collision(entity, self.food)

                    distance_to_food = ((self.food.coord[0] - entity.coord[0])**2) + ((self.food.coord[1] - entity.coord[1])**2)
                    distance_to_food = math.sqrt(distance_to_food)/self.screen_size[0]
                    if distance_to_food < self.min_distance_to_score and entity.chromosome_score < 1 and entity.alive:
                        entity.chromosome_score = 1-distance_to_food

                    self.time -= self.frames_sec

                print("Subject: %s | Score: %.2f" % (entity.name,
                                                     round(entity.chromosome_score, 2)))

            print("Generation: %s | Killed: %s | Best: %s" % self.generation.advance_generation())


    def stop(self):

        sys.exit(0)


    def check_bounds_collision(self, entity, screen_size):

        x, y = entity.coord
        x_size, y_size = entity.size
        screen_w, screen_h = screen_size

        if x < 0 or y < 0 or x + x_size > screen_w or y + y_size > screen_h:
            entity.kill()


    def check_food_collision(self, entity, food):

        entity_coord_matrix = []
        for y in range(entity.coord[1], entity.coord[1]+entity.size[1]):
            for x in range(entity.coord[0], entity.coord[0]+entity.size[0]):
                entity_coord_matrix.append([x, y])

        food_coord_matrix = []
        for y in range(food.coord[1], food.coord[1]+food.size[1]):
            for x in range(food.coord[0], food.coord[0]+food.size[0]):
                food_coord_matrix.append([x, y])

        intercede = False
        for entity_coord in entity_coord_matrix:
            for food_coord in food_coord_matrix:
                if entity_coord == food_coord:
                    intercede = True

        if intercede:

            if entity.chromosome_score < 1:
                entity.chromosome_score = self.food.value
            else:
                entity.chromosome_score += self.food.value

            self.food = Food()


    def display_screen_info(self, entity, events):

        for event in events:

            if event.type == pygame.QUIT:
                self.stop()
            # elif event.type == pygame.KEYDOWN:
            #     entity.update_direction(event.key)

        self.screen.fill(self.background_color)

        pygame.draw.rect(self.screen, entity.color,
                         pygame.Rect(entity.coord[0], entity.coord[1],
                                     entity.size[0], entity.size[1]))

        pygame.draw.rect(self.screen, self.food.color,
                         pygame.Rect(self.food.coord[0], self.food.coord[1],
                                     self.food.size[0], self.food.size[1]))

        self.screen.blit(self.font.render(
            "Subject: %s" % entity.name, 1, self.text_color), (20, 20))

        self.screen.blit(self.font.render(
            "Score: %.2f" % round(entity.chromosome_score, 2), 1, self.text_color), (20, 50))

        self.screen.blit(self.font.render(
            "Time: %ss" % round(self.time/self.frames_sec), 1, self.text_color), (20, 80))

        pygame.display.flip()
        self.clock.tick(self.frames_sec * self.time_multiplier)
