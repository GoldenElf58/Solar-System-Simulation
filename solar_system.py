from random import randrange
from typing import List

import pygame

from planet import Planet


class SolarSystem:
    def __init__(self, screen: pygame.Surface, planets: List[Planet] | None = None) -> None:
        """
        Initialize a SolarSystem object

        Parameters
        ----------
        screen : pygame.Surface
            the screen onto which the solar system will be drawn
        planets : List[Planet] | None, optional
            list of Planet objects to include in the solar system
            (default is an empty list)
        """
        if planets is None:
            planets = []
        self.screen = screen
        self.planets = planets

    def create_planets(self, num_planets: int) -> None:
        """
        Create and add a specified number of new Planet objects to the solar system.

        The new Planet objects will have random x and y positions within the screen,
        a radius of 10, and the screen onto which the solar system will be drawn.

        Parameters
        ----------
        num_planets : int
            the number of new Planet objects to create and add to the solar system
        """
        for _ in range(num_planets):
            self.planets.append(
                Planet(randrange(0, self.screen.get_width()), randrange(0, self.screen.get_height()), self.screen,
                       mass=randrange(10, 20)))

    def add_planets(self, planets: List[Planet]) -> None:
        """
        Add multiple planets to the solar system.

        Parameters
        ----------
        planets : List[Planet]
            the planets to add to the solar system
        """
        self.planets.extend(planets)

    def remove_planets(self, planets: List[Planet]) -> None:
        """
        Remove multiple planets from the solar system.

        Parameters
        ----------
        planets : List[Planet]
            the planets to remove from the solar system
        """
        self.planets = [planet for planet in self.planets if planet not in planets]

    def add_planet(self, planet: Planet) -> None:
        """
        Add a planet to the solar system.

        Parameters
        ----------
        planet : Planet
            the planet to add to the solar system
        """
        self.planets.append(planet)

    def remove_planet(self, planet: Planet) -> None:
        """
        Remove a planet from the solar system.

        Parameters
        ----------
        planet : Planet
            the planet to remove from the solar system
        """
        self.planets.remove(planet)

    def update(self, dt: float) -> None:
        """
        Update all the planets in the solar system.

        Parameters
        ----------
        dt : float
            time elapsed since the last frame
        """
        self.apply_gravity()
        for planet in self.planets:
            planet.update(dt)

    def apply_gravity(self) -> None:
        """
        Apply gravity between all the planets in the solar system.

        Parameters
        ----------

        Returns
        -------
        None
        """
        for planet in self.planets:
            planet.reset_accelerations()

        for i, planet in enumerate(self.planets):
            for other_planet in self.planets[i + 1:]:
                planet.apply_gravity(other_planet)

    def draw(self) -> None:
        """
        Draw all the planets in the solar system onto the screen.

        This function will go through each of the planets in the solar system
        and call the draw() method on each of them.

        Parameters
        ----------

        Returns
        -------
        None

        """
        for planet in self.planets:
            planet.draw()
