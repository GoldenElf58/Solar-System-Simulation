import pygame
import sys
from random import random

from planet import Planet
from utils import clear

# Initialize Pygame
pygame.init()

# Set up the window dimensions
screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Moving Circle")

# Set up the clock for controlling the frame rate
clock = pygame.time.Clock()

running = False

num_planets = 2
planets = [Planet(random(0, screen.get_width()), random(0, screen.get_height()), 10, screen, x_speed=50, x_vel=50) for i in range(2)]

def draw():
    """
    Draw the circle onto the screen.

    Clears the screen with a white background, draws the circle
    at its current position, and updates the display.

    Parameters
    ----------
    None

    Returns
    -------
    None
    """
    global planet
    # Clear the screen with a white background
    screen.fill((255, 255, 255))

    # Draw the circle
    planet.draw()

    # Update the display
    pygame.display.flip()

def event_handling():
    """
    Handle any events that have occurred.

    Currently, the only event that is handled is the pygame.QUIT event,
    which is triggered when the user closes the window.

    Parameters
    ----------
    None

    Returns
    -------
    None
    """
    global running
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


def loop():
    """
    Main game loop.

    This function contains the main game loop. It will continually
    call itself until the user closes the window.

    Parameters
    ----------
    None

    Returns
    -------
    None
    """
    global clock, planet, deltaTime
    # Cap the frame rate at 60 frames per second
    dt = clock.tick(60) / 1000 # ms to s
    event_handling()

    planet.update(dt)
    draw()
    # clear()
    # print(circle.x, circle.y)


def main():
    """
    Main function.

    Initializes the game loop and calls the loop() function
    until the user closes the window.

    Parameters
    ----------
    None

    Returns
    -------
    None
    """
    global running
    # Main loop
    running = True
    while running:
        loop()

    # Clean up and exit
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    print("Program Started")
    main()
