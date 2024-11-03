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
    
    update = True
    star = True
    scale = 1
    time_scale = 1
    n = 10
    
    # Initialize pygame
    pygame.init()
    
    handler: Handler = Handler(num_celestial_bodies=n, time_scale=time_scale, scale=scale, star=star, update=update)
    t1 = threading.Thread(target=handler.draw_repeatedly)
    t1.start()
    
    # handler.draw_repeatedly(fps=True, cps=True)
    
    while handler.running:
        handler.loop()
    
    # Clean up and exit
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    print("Program Started")
    main()
