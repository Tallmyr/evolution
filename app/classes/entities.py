import math
import random

from app.config import config
from app.functions import common

from pygame import sprite, Surface

# Use a specific seed
if config.RANDOM_SEED:
    random.seed(config.RANDOM_SEED)


class NPC(sprite.Sprite):
    def __init__(self):
        sprite.Sprite.__init__(self)

        self.x = random.randint(0, 50)
        self.y = random.randint(0, 50)

        self.image = Surface([5, 5])
        self.image.fill((255, 0, 0))

        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

        self.pregnant = None
        self.speed = 1

    def update(self, foods):
        self.find_target(foods)
        self.move()

    def find_target(self, foods):
        self.distance = 5000
        for food in foods:
            distance = math.dist(self.rect.center, food.rect.center)
            if distance < self.distance:
                self.target = food
                self.target_x = food.x
                self.target_y = food.y
                self.distance = distance

    def move(self):
        if self.pregnant:
            self.pregnant -= 1
        else:
            if self.x < self.target_x:
                self.x += self.speed
            elif self.x > self.target_x:
                self.x -= self.speed

            if self.y < self.target_y:
                self.y += self.speed
            elif self.y > self.target_y:
                self.y -= self.speed

        # self.energy = self.energy - self.energy_usage * config.BASE_ENERGY_USE

        self.update_center()
        # self.update_draw()

    def update_center(self):
        self.rect.center = (self.x, self.y)

    # def update_draw(self):
    #     self.draw = (self.x, self.y, self.w, self.h)

    # def eat(self, foods):
    #     food_list = []
    #     for food in foods:
    #         if math.isclose(food.x, self.x, abs_tol=1) and math.isclose(
    #             food.y, self.y, abs_tol=1
    #         ):
    #             self.energy += config.FOOD_VALUE
    #         else:
    #             food_list.append(food)
    #     return food_list

    # def breed(self, npcs):
    #     if self.pregnant == 0:
    #         self.pregnant = None
    #         self.energy -= config.FOOD_VALUE
    #         npcs.append(
    #             NPC(
    #                 self.colour,
    #                 self.x + 10,
    #                 self.y + 10,
    #                 self.w,
    #                 self.h,
    #                 self.energy_usage,
    #             )
    #         )

    # def check_pregnant(self):
    #     if self.energy > config.FOOD_VALUE * 3 and self.pregnant is None:
    #         self.pregnant = 20


class Food(sprite.Sprite):
    def __init__(self):
        sprite.Sprite.__init__(self)

        self.image = Surface([5, 5])
        self.image.fill((0, 0, 255))

        self.x = random.randint(50, 750)
        self.y = random.randint(50, 750)

        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

    def add(foods, food_time):
        if food_time >= config.FOOD_TIMER:
            for _ in range(2):
                foods.append(Food())
            food_time = 0
        food_time += 1
        return foods, food_time
