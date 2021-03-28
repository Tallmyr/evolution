import random
from app.config import config


def horizontal_spawn():
    roll = random.randint(0, 1)
    if roll == 1:
        return random.randint(0, config.SCREEN_W * config.SPAWN_AREA)
    return random.randint(
        config.SCREEN_W * (1 - (config.SPAWN_AREA * 2)), config.SCREEN_H
    )


def vertical_spawn():
    roll = random.randint(0, 1)
    if roll == 1:
        return random.randint(0, config.SCREEN_H * config.SPAWN_AREA)
    return random.randint(
        config.SCREEN_H * (1 - (config.SPAWN_AREA * 2)), config.SCREEN_W
    )
