import random
import math


class NPC:
    def __init__(self):
        self.colour = (
            random.randint(20, 235),
            random.randint(20, 235),
            random.randint(20, 235),
        )
        self.x = random.randint(0, 50)
        self.y = random.randint(0, 750)
        self.w = 5
        self.h = 5
        self.speed = 1
        self.loc = [self.x, self.y]
        self.draw = (self.x, self.y, self.w, self.h)

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
        if self.x < self.target_x:
            self.x += self.speed
        elif self.x > self.target_x:
            self.x -= self.speed

        if self.y < self.target_y:
            self.y += self.speed
        elif self.y > self.target_y:
            self.y -= self.speed

        self.update_loc()
        self.update_draw()

    def update_loc(self):
        self.loc = [self.x, self.y]

    def update_draw(self):
        self.draw = (self.x, self.y, self.w, self.h)

    def eat(self, foods):
        return [food for food in foods if food.loc != self.loc]


class Food:
    def __init__(self):
        self.x = random.randint(50, 750)
        self.y = random.randint(50, 750)
        self.r = 2.5
        self.loc = [self.x, self.y]
        self.draw = (self.x, self.y)
