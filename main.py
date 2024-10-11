import sys
import threading

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

    handler: Handler = Handler(num_celestial_bodies=200, time_scale=60*60*24*365*1_000, scale=500_000_000, star=False)
    t1 = threading.Thread(target=handler.draw_repeatedly)
    t1.start()
    while handler.running:
        handler.loop()

    # Clean up and exit
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    print("Program Started")
    main()
