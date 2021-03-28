# Import and initialize the pygame library
import pygame
from pygame import display, draw, time

from app.classes.entities import NPC, Food
from app.config import colour, config


# Basic Pygame Setup
pygame.init()


screen = display.set_mode([config.SCREEN_W, config.SCREEN_H])

# Create Entities for first run
npcs = [NPC() for _ in range(config.START_NPC)]
foods = [Food() for _ in range(config.START_FOOD)]

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
    # Add more food
    foods, food_time = Food.add(foods, food_time)

    for food in foods:
        draw.circle(screen, (colour.BLUE), (food.draw), food.r)

    # Update NPCs

    #
    for npc in npcs:
        npc.find_target(foods)
        npc.move()
        foods = npc.eat(foods)
        npc.check_pregnant()
        npc.breed(npcs)

        draw.rect(screen, npc.colour, (npc.draw))

    # Kill any NPCs that have no food left.
    npcs = [npc for npc in npcs if npc.energy >= 0]

    # Draw and tick clock
    # Flip the display
    display.flip()
    clock.tick(144)


# End Program
pygame.quit()
