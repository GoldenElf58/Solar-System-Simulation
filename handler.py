import pygame

from solar_system import SolarSystem


class Handler:
    """
    Handler class

    This class is used to manage the game loop and handle events.

    Attributes
    ----------
    screen : pygame.Surface
        the screen onto which the solar system will be drawn
    solar_system : SolarSystem
        a SolarSystem object to use for the handler
    clock : pygame.time.Clock
        the clock used to control the game loop
    running : bool
        whether the game loop is running or not
    """
    def __init__(self, screen: pygame.Surface | None = None, solar_system: SolarSystem | None = None,
                 num_planets: int = 2, time_scale: float = 1) -> None:
        """
        Initialize a Handler object

        Parameters
        ----------
        screen : pygame.Surface, optional
            the screen onto which the solar system will be drawn
            (default is a new 1000x1000 window)
        solar_system : SolarSystem, optional
            a SolarSystem object to use for the handler
            (default is a new SolarSystem object with the given screen)
        num_planets : int, optional
            number of planets to create in the solar system
            (default is 2)
        time_scale : float, optional
            the time scale of the game loop
            (default is 1)
        """
        if screen is None:
            self.screen: pygame.Surface = pygame.display.set_mode((1000, 1000))
            pygame.display.set_caption("Solar System")
        else:
            self.screen: pygame.Surface = screen
        if solar_system is None:
            self.solar_system: SolarSystem = SolarSystem(self.screen)
            self.solar_system.create_planets(num_planets)
        else:
            self.solar_system: SolarSystem = solar_system
        self.clock: pygame.time.Clock = pygame.time.Clock()
        self.running: bool = True
        self.time_scale = time_scale

    def loop(self) -> None:
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
        # Cap the frame rate at 60 frames per second
        dt = self.clock.tick(60) / 1000 * self.time_scale
        self.event_handling()

        self.solar_system.update(dt)
        self.draw()

    def event_handling(self) -> None:
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
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def draw(self) -> None:
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
        self.screen.fill((0, 0, 0))
        self.solar_system.draw()
        pygame.display.flip()
