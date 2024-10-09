import math

import pygame

from object import Object


class Planet(Object):
    def __init__(self, x: float, y: float, screen: pygame.Surface, color: tuple = (155, 50, 50), mass: float = 0,
                 x_vel: float = 0, y_vel: float = 0, x_acc: float = 0, y_acc: float = 0, x_speed: float = 0,
                 y_speed: float = 0) -> None:
        """
        Initialize a Planet object

        Parameters
        ----------
        x : float
            initial x position
        y : float
            initial y position
        screen : pygame.Surface
            the screen onto which the planet will be drawn
        color : tuple of 3 ints, optional
            color of the planet (default is red)
        mass : float, optional
            mass of the planet
        x_vel : float, optional
            initial x velocity
        y_vel : float, optional
            initial y velocity
        x_acc : float, optional
            x acceleration
        y_acc : float, optional
            y acceleration
        x_speed : float, optional
            x speed at which the planet will move
        y_speed : float, optional
            y speed at which the planet will move
        """
        super().__init__(x, y, x_acc, y_acc, screen, x_vel=x_vel, y_vel=y_vel)
        self.radius: float = max(min(mass, 20), 2)
        self.color: tuple = color
        self.x_speed: float = x_speed
        self.y_speed: float = y_speed
        self.mass: float = mass

    def update(self, dt: float) -> None:
        """
        Update the planet's velocity and position

        Parameters
        ----------
        dt : float
            time elapsed since the last frame
        """
        if self.x >= self.screen.get_width() or self.x <= 0:
            self.x_vel *= -1
        if self.y >= self.screen.get_height() or self.y <= 0:
            self.y_vel *= -1
        super().update(dt)

    def draw(self) -> None:
        """
        Draw the planet onto its screen

        Draws a circle of radius self.radius at position (self.x, self.y) with
        color self.color onto the screen self.screen
        """
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.radius)

    def apply_gravity(self, planet: "Planet") -> None:
        """
        Apply gravitational force to the planet and another planet.

        Parameters
        ----------
        planet : Planet
            the planet to apply gravity to
        """
        gravitational_constant: float = 6.67430e-11  # Gravitational constant
        dx = planet.x - self.x
        dy = planet.y - self.y
        distance = math.sqrt(dx ** 2 + dy ** 2)

        if distance == 0:
            return  # Avoid division by zero

        force_over_distance = (gravitational_constant * self.mass * planet.mass) / (distance ** 3)

        # Calculate the acceleration components
        x_acc_delta = force_over_distance * dx
        y_acc_delta = force_over_distance * dy

        self.x_acc += x_acc_delta / self.mass
        self.y_acc += y_acc_delta / self.mass
        planet.x_acc -= x_acc_delta / planet.mass
        planet.y_acc -= y_acc_delta / planet.mass

    def reset_accelerations(self) -> None:
        """
        Reset the planet's accelerations to zero.

        This method is used to stop the planet from moving when it is not
        being interacted with.

        Parameters
        ----------

        Returns
        -------
        None
        """
        self.x_acc = 0
        self.y_acc = 0
