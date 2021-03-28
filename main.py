# Import and initialize the pygame library
import pygame
from pygame import display, draw, time

from app.classes.entities import NPC, Food, foods, npcs
from app.config import colour, config

# Basic Pygame Setup
pygame.init()


screen = display.set_mode([config.SCREEN_W, config.SCREEN_H])

# Create Entities for first run

for _ in range(config.START_NPC):
    new_npc = NPC()
    npcs.add(new_npc)

for _ in range(config.START_FOOD):
    new_food = Food()
    foods.add(new_food)

# Set Game variables
clock = time.Clock()
screen = display.set_mode([config.SCREEN_W, config.SCREEN_H])
food_time = 0

# Main Loop
running = True
while running:

    # Close Button
    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False

    # Setup the game board

    # Set background
    screen.fill((200, 200, 200))

    # Create the grass
    draw.rect(
        screen,
        (colour.GREEN),
        (
            config.SCREEN_W * config.SPAWN_AREA,
            config.SCREEN_H * config.SPAWN_AREA,
            config.SCREEN_W * (1 - (config.SPAWN_AREA * 2)),
            config.SCREEN_H * (1 - (config.SPAWN_AREA * 2)),
        ),
    )

    # Game Logic

    # Update Food

    foods.draw(screen)

    # Add more food
    food_time = Food.grow(food_time)

    # Update NPCs

    npcs.update(foods)
    npcs.draw(screen)

    # Draw and tick clock
    # Flip the display
    display.flip()
    clock.tick(144)


# End Program
pygame.quit()
