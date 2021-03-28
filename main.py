# Simple pygame program


# Import and initialize the pygame library
import pygame
from pygame import display, draw, time

from app.classes.entities import NPC, Food
from app.config import colour, config

pygame.init()
# Setup the clock for a decent framerate

clock = time.Clock()


# Set up the drawing window

screen = display.set_mode([800, 800])

# Create npcs
npcs = [NPC() for _ in range(config.START_NPC)]
foods = [Food() for _ in range(config.START_FOOD)]


# Run until the user asks to quit

running = True

while running:

    # Did the user click the window close button?

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False

    # Setup the game board

    # Set background
    screen.fill((200, 200, 200))

    # Create the grass
    draw.rect(screen, (colour.GREEN), (50, 50, 700, 700))

    # Update Food
    for food in foods:
        draw.circle(screen, (colour.BLUE), (food.draw), food.r)

    if len(foods) < config.START_FOOD - 20:
        for _ in range(20):
            foods.append(Food())

    # Update NPCs
    for npc in npcs:
        npc.find_target(foods)
        npc.move()
        draw.rect(screen, npc.colour, (npc.draw))
        foods = npc.eat(foods)

        if npc.food >= 2:
            npc.food -= 1
            npcs.append(NPC(npc.colour, npc.x + 5, npc.y + 5, npc.w, npc.h, npc.speed))

    npcs = [npc for npc in npcs if npc.food >= 0]

    # Flip the display

    display.flip()

    # Ensure program maintains a rate of 30 frames per second

    clock.tick(144)


# Done! Time to quit.

pygame.quit()
