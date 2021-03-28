import math
import random

from app.config import config
from app.functions import common

# Use a specific seed
if config.RANDOM_SEED:
    random.seed(config.RANDOM_SEED)


class NPC:
    def __init__(self, colour=None, x=None, y=None, w=None, h=None, energy_usage=None):
        self.colour = colour
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.energy_usage = energy_usage
        if self.colour is None:
            self.colour = (
                random.randint(20, 235),
                random.randint(20, 235),
                random.randint(20, 235),
            )
        if self.x is None:
            self.x = common.horizontal_spawn()
        if self.y is None:
            self.y = common.vertical_spawn()
        if self.w is None:
            self.w = random.randint(5, 15)
        if self.h is None:
            self.h = random.randint(5, 15)
        if self.energy_usage is None:
            self.energy_usage = random.random()

        self.pregnant = None
        self.speed = 1 * (config.ENERGY_TO_SPEED * self.energy_usage)

        self.loc = [self.x, self.y]
        self.draw = (self.x, self.y, self.w, self.h)
        self.energy = config.FOOD_VALUE

    def find_target(self, foods):
        self.distance = 5000
        for food in foods:
            distance = math.dist(self.loc, food.loc)
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

        self.energy = self.energy - self.energy_usage * config.BASE_ENERGY_USE

        self.update_loc()
        self.update_draw()

    def update_loc(self):
        self.loc = self.x, self.y

    def update_draw(self):
        self.draw = (self.x, self.y, self.w, self.h)

    def eat(self, foods):
        food_list = []
        for food in foods:
            if math.isclose(food.x, self.x, abs_tol=1) and math.isclose(
                food.y, self.y, abs_tol=1
            ):
                self.energy += config.FOOD_VALUE
            else:
                food_list.append(food)
        return food_list

    def breed(self, npcs):
        self.pregnant = None
        self.energy -= config.FOOD_VALUE
        npcs.append(
            NPC(
                self.colour, self.x + 10, self.y + 10, self.w, self.h, self.energy_usage
            )
        )


class Food:
    def __init__(self):
        self.x = random.randint(50, 750)
        self.y = random.randint(50, 750)
        self.r = 2.5
        self.loc = [self.x, self.y]
        self.draw = (self.x, self.y)
