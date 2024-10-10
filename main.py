import sys

import pygame

from handler import Handler


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

    # Initialize pygame
    pygame.init()

    handler = Handler(num_celestial_bodies=1, time_scale=60*60*24*30, scale=1_500_000_000)
    while handler.running:
        handler.loop()

    # Clean up and exit
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    print("Program Started")
    main()
