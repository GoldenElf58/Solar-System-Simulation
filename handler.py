import math
import time

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
                 num_celestial_bodies: int = 2, time_scale: float = 1, scale: float = 1, star=False, update=True) -> None:
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
        num_celestial_bodies : int, optional
            number of CelestialBody objects to create in the solar system
            (default is 2)
        time_scale : float, optional
            the time scale of the game loop
            (default is 1)
        scale : float, optional
            meters per pixel
            (default is 1)

        Returns
        -------
        Handler
        """
        if screen is None:
            self.screen: pygame.Surface = pygame.display.set_mode((1920, 1080))
            pygame.display.set_caption("Solar System")
        else:
            self.screen: pygame.Surface = screen
        
        if solar_system is None:
            self.solar_system: SolarSystem = SolarSystem(self.screen, scale=scale)
            self.solar_system.create_celestial_bodies_circular(num_celestial_bodies, star=star)
        else:
            self.solar_system: SolarSystem = solar_system
        
        self.update: bool = update
        self.clock: pygame.time.Clock = pygame.time.Clock()
        self.running: bool = True
        self.time_scale: float = time_scale
        self.scale: float = scale
        self.t_last: float = time.perf_counter()
        self.t_now: float = self.t_last
        self.cps: float = 0
        self.fps: float = 0
        self.font = pygame.font.SysFont("Arial", 24)

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
        t_now = time.perf_counter()
        dt = t_now - self.t_last
        self.cps = 1 / dt
        dt *= self.time_scale
        self.t_last = t_now

        self.event_handling()
        if self.update:
            self.solar_system.update(dt)

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
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False

    def draw(self, cps: bool = False, fps: bool = False) -> None:
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
        # self.screen.fill(pygame.Color('#000000'))
        shape_surf = pygame.Surface(self.screen.get_rect().size, pygame.SRCALPHA)
        pygame.draw.rect(shape_surf, (0, 0, 0, 5), shape_surf.get_rect())
        self.screen.blit(shape_surf, self.screen.get_rect())
        self.solar_system.draw(scale=self.scale)
        
        if cps:
            text = self.font.render(f"CPS: {self.cps:.0f}", True, (255, 255, 255))
            self.screen.blit(text, (10, 10))
        
        if fps and cps:
            text = self.font.render(f"FPS: {self.fps:.0f}", True, (255, 255, 255))
            self.screen.blit(text, (10, 30))
        elif fps:
            text = self.font.render(f"FPS: {self.fps:.0f}", True, (255, 255, 255))
            self.screen.blit(text, (10, 10))
        
        pygame.display.flip()

    def draw_repeatedly(self, fps: bool = False, cps: bool = False) -> None:
        while self.running:
            dt = self.clock.tick(60) / 1000
            self.fps = 1 / dt if dt > 0 else math.inf
            self.event_handling()
            
            self.draw(cps=cps, fps=fps)
