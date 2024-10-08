import sys
from random import randrange

import pygame

from planet import Planet

# Initialize Pygame
pygame.init()

# Set up the window dimensions
screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Moving Planet")

# Set up the clock for controlling the frame rate
clock = pygame.time.Clock()

running = False

num_planets = 2
planets = [
    Planet(randrange(0, screen.get_width()), randrange(0, screen.get_height()), 10, screen, x_speed=randrange(-50, 50),
           x_vel=randrange(-50, 50)) for i in range(2)]


def draw() -> None:
    """
    Draw the planet onto the screen.

    Clears the screen with a white background, draws the planet
    at its current position, and updates the display.

    Parameters
    ----------

    Returns
    -------
    None
    """
    global planets
    # Clear the screen with a white background
    screen.fill((255, 255, 255))

    for planet in planets:
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

    Returns
    -------
    None
    """
    global clock, planets
    # Cap the frame rate at 60 frames per second
    dt = clock.tick(60) / 1000  # ms to s
    event_handling()

    for planet in planets:
        planet.update(dt)
    draw()
    # clear()
    # print(planet.x, planet.y)


def main():
    """
    Main function.

    Initializes the game loop and calls the loop() function
    until the user closes the window.

    Parameters
    ----------

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
