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

    handler = Handler(num_planets=5)
    while handler.running:
        handler.loop()

    # Clean up and exit
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    print("Program Started")
    main()
