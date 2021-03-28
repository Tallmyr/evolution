import random
import math


class NPC:
    def __init__(self, colour=None, x=None, y=None, w=None, h=None, speed=None):
        self.colour = colour
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.speed = speed
        if self.colour is None:
            self.colour = (
                random.randint(20, 235),
                random.randint(20, 235),
                random.randint(20, 235),
            )
        if self.x is None:
            self.x = random.randint(0, 50)
        if self.y is None:
            self.y = random.randint(0, 750)
        if self.w is None:
            self.w = random.randint(3, 7)
        if self.h is None:
            self.h = random.randint(3, 7)
        if self.speed is None:
            self.speed = random.random()

        self.loc = [self.x, self.y]
        self.draw = (self.x, self.y, self.w, self.h)
        self.food = 1

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
        self.food = self.food - 0.001

        self.update_loc()
        self.update_draw()

    def update_loc(self):
        self.loc = [round(self.x), round(self.y)]

    def update_draw(self):
        self.draw = (self.x, self.y, self.w, self.h)

    def eat(self, foods):
        food_list = []
        for food in foods:
            if food.loc == self.loc:
                self.food += 1
            else:
                food_list.append(food)
        return food_list


class Food:
    def __init__(self):
        self.x = random.randint(50, 750)
        self.y = random.randint(50, 750)
        self.r = 2.5
        self.loc = [self.x, self.y]
        self.draw = (self.x, self.y)
