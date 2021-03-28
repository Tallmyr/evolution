import math
import random

from app.config import config
from pygame import Surface, sprite

# Use a specific seed
if config.RANDOM_SEED:
    random.seed(config.RANDOM_SEED)

npcs = sprite.Group()
foods = sprite.Group()


def npc_collide(sprite1, sprite2):
    if sprite1 is not sprite2:
        return sprite1.rect.colliderect(sprite2.rect)
    else:
        return False


class NPC(sprite.Sprite):
    def __init__(self, x=None, y=None, w=None, h=None, energy_use=None, colour=None):
        sprite.Sprite.__init__(self, npcs)

        self.x = x or random.randint(0, config.SCREEN_W)
        self.y = y or random.randint(0, config.SCREEN_H)
        self.w = w or random.randint(5, 15)
        self.h = h or random.randint(5, 15)
        self.colour = colour or (
            random.randint(25, 230),
            random.randint(25, 230),
            random.randint(25, 230),
        )

        self.image = Surface([self.w, self.h])
        self.image.fill(self.colour)

        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

        self.pregnant = None
        self.energy = config.FOOD_VALUE
        self.energy_use = energy_use or random.random()
        self.speed = self.energy_use / 2

    def update(self, foods):
        self.find_target(foods)
        self.move()

        if sprite.spritecollide(self, foods, True):
            self.eat()

        self.check_pregnant()
        self.breed()

        if self.energy <= 0:
            self.kill()

        if self.energy > config.FOOD_VALUE * 3:
            self.breed

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
            block = sprite.spritecollide(self, npcs, False, npc_collide)
            if block:
                self.move_away(block)
            else:
                self.move_to()

        self.energy = self.energy - 1 * config.BASE_ENERGY_USE

        self.update_center()

    def move_to(self):
        if self.x < self.target_x:
            self.x += self.speed
        elif self.x > self.target_x:
            self.x -= self.speed
        if self.y < self.target_y:
            self.y += self.speed
        elif self.y > self.target_y:
            self.y -= self.speed

    def move_away(self, block):
        if self.x < block[0].x:
            self.x -= self.speed
        elif self.x > block[0].x:
            self.x += self.speed
        if self.y < block[0].y:
            self.y += self.speed
        elif self.y > block[0].y:
            self.y -= self.speed

    def update_center(self):
        self.rect.center = (self.x, self.y)

    def eat(self):
        self.energy += config.FOOD_VALUE

    def breed(self):
        if self.pregnant == 0:
            self.pregnant = None
            self.energy -= config.FOOD_VALUE
            NPC(self.x + 10, self.y + 10, self.w, self.h, self.energy_use, self.colour)

    def check_pregnant(self):
        if self.energy > config.FOOD_VALUE * 3 and self.pregnant is None:
            self.pregnant = 200


class Food(sprite.Sprite):
    def __init__(self):
        sprite.Sprite.__init__(self, foods)

        self.image = Surface([5, 5])
        self.image.fill((0, 0, 255))

        self.x = random.randint(50, 750)
        self.y = random.randint(50, 750)

        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

    def grow(food_time):
        if food_time >= config.FOOD_TIMER:
            for _ in range(2):
                Food()
            food_time = 0
        food_time += 1
        return food_time
