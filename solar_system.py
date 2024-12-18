import math
from random import uniform
from typing import List

import pygame

from celestial_body import CelestialBody
from utils import clear, gravitational_constant
from vector import PolarVector, Point, Vector


class SolarSystem:
    def __init__(self, screen: pygame.Surface, celestial_bodies: List[CelestialBody] | None = None,
                 scale: float = 1) -> None:
        """
        Initialize a SolarSystem object

        Parameters
        ----------
        screen : pygame.Surface
            the screen onto which the solar system will be drawn
        celestial_bodies : List[CelestialBody] | None, optional
            list of CelestialBody objects to include in the solar system
            (default is an empty list)
        """
        if celestial_bodies is None:
            celestial_bodies = []
        self.screen = screen
        self.celestial_bodies = celestial_bodies
        self.scale = scale
    
    def create_celestial_bodies(self, num_celestial_bodies: int, star=True) -> None:
        """
        Create and add a specified number of new CelestialBody objects to the solar system.

        The new CelestialBody objects will have random x and y positions within the screen,
        a radius of 10, and the screen onto which the solar system will be drawn.

        Parameters
        ----------
        star : bool
            whether to create and add a star to the solar system
        num_celestial_bodies : int
            the number of new CelestialBody objects to create and add to the solar system
        """
        for _ in range(num_celestial_bodies):
            self.celestial_bodies.append(
                CelestialBody(uniform(0, self.screen.get_width() * self.scale),
                              uniform(0, self.screen.get_height() * self.scale), screen=self.screen, mass=1,
                              x_vel=uniform(-5 * gravitational_constant * self.scale,
                                            5 * gravitational_constant * self.scale),
                              y_vel=uniform(-5 * gravitational_constant * self.scale,
                                            5 * gravitational_constant * self.scale), scale=self.scale))
        
        if star:
            self.celestial_bodies.append(
                CelestialBody(self.screen.get_width() * self.scale / 2, self.screen.get_height() * self.scale / 2,
                              screen=self.screen, color=(235, 210, 30), mass=10, fixed=True, scale=self.scale))
    
    def create_celestial_bodies_circular(self, num_celestial_bodies: int, star=False) -> None:
        s = 100
        # pos = PolarVector(math.pi, 75 * self.scale).to_point()
        # vel = pos.to_polar().rotate(math.pi / 2)
        # vel.magnitude = s * self.scale
        # vel = vel.to_cartesian()
        # pos += Point(self.screen.get_width() / 2, self.screen.get_height() / 2) * self.scale
        # self.celestial_bodies.append(CelestialBody(pos.x, pos.y, screen=self.screen, mass=1, x_vel=vel.x, y_vel=vel.y,
        #                                            scale=self.scale))
        # pos = PolarVector(0, 75 * self.scale).to_point()
        # vel = pos.to_polar().rotate(math.pi / 2)
        # vel.magnitude = s * self.scale
        # vel = vel.to_cartesian()
        # pos += Point(self.screen.get_width() / 2, self.screen.get_height() / 2) * self.scale
        # self.celestial_bodies.append(CelestialBody(pos.x, pos.y, screen=self.screen, mass=1, x_vel=vel.x, y_vel=vel.y,
        #                                            scale=self.scale))
        # pos = Point(0,0)
        # vel = Vector(0,0)
        # pos += Point(self.screen.get_width() / 2, self.screen.get_height() / 2) * self.scale
        # self.celestial_bodies.append(CelestialBody(pos.x, pos.y, screen=self.screen, mass=1, x_vel=vel.x, y_vel=vel.y,
        #                                            scale=self.scale))
        for _ in range(num_celestial_bodies):
            pos = PolarVector(uniform(0, math.tau), uniform(50, 100) * self.scale).to_point()
            vel = pos.to_polar().rotate(math.pi / 2)
            vel.magnitude = s * self.scale
            vel = vel.to_cartesian()
            pos += Point(self.screen.get_width() / 2, self.screen.get_height() / 2) * self.scale
            self.celestial_bodies.append(
                CelestialBody(pos.x, pos.y, screen=self.screen, mass=1, x_vel=vel.x, y_vel=vel.y,
                              scale=self.scale))
        
        if star:
            self.celestial_bodies.append(
                CelestialBody(self.screen.get_width() * self.scale / 2, self.screen.get_height() * self.scale / 2,
                              screen=self.screen, color=(235, 210, 30), mass=10, fixed=True, scale=self.scale))
    
    def add_celestial_bodies(self, celestial_bodies: List[CelestialBody]) -> None:
        """
        Add multiple celestial_bodies to the solar system.

        Parameters
        ----------
        celestial_bodies : List[CelestialBody]
            the celestial_bodies to add to the solar system
        """
        self.celestial_bodies.extend(celestial_bodies)
    
    def remove_celestial_bodies(self, celestial_bodies: List[CelestialBody]) -> None:
        """
        Remove multiple celestial_bodies from the solar system.

        Parameters
        ----------
        celestial_bodies : List[CelestialBody]
            the celestial_bodies to remove from the solar system
        """
        self.celestial_bodies = [celestial_body for celestial_body in self.celestial_bodies if
                                 celestial_body not in celestial_bodies]
    
    def add_celestial_body(self, celestial_body: CelestialBody) -> None:
        """
        Add a celestial_body to the solar system.

        Parameters
        ----------
        celestial_body : CelestialBody
            the celestial_body to add to the solar system
        """
        self.celestial_bodies.append(celestial_body)
    
    def remove_celestial_body(self, celestial_body: CelestialBody) -> None:
        """
        Remove a celestial_body from the solar system.

        Parameters
        ----------
        celestial_body : CelestialBody
            the celestial_body to remove from the solar system
        """
        self.celestial_bodies.remove(celestial_body)
    
    def update(self, dt: float) -> None:
        """
        Update all the celestial_bodies in the solar system.

        Parameters
        ----------
        dt : float
            time elapsed since the last frame
        """
        self.apply_gravity()
        for celestial_body in self.celestial_bodies:
            celestial_body.update(dt)
    
    def apply_gravity(self, info: bool = False) -> None:
        """
        Apply gravity between all the celestial_bodies in the solar system.

        Parameters
        ----------

        Returns
        -------
        None
        """
        if info:
            clear()
        for celestial_body in self.celestial_bodies:
            celestial_body.reset_accelerations(info=info)
        for i, celestial_body in enumerate(self.celestial_bodies):
            for other_celestial_body in self.celestial_bodies[i + 1:]:
                if celestial_body != other_celestial_body:
                    celestial_body.apply_gravity(other_celestial_body)
    
    def draw(self, scale: float = None) -> None:
        """
        Draw all the celestial_bodies in the solar system onto the screen.

        This function will go through each of the celestial_bodies in the solar system
        and call the draw() method on each of them.

        Parameters
        ----------

        Returns
        -------
        None

        """
        if scale is None:
            scale = self.scale
        else:
            self.scale = scale
        for celestial_body in self.celestial_bodies:
            celestial_body.show(scale=scale)
