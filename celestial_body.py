from math import sqrt

import pygame

from object import Object
from utils import gravitational_constant
from vector import Vector


class CelestialBody(Object):
    def __init__(self,
                 x: float,
                 y: float,
                 screen: pygame.Surface,
                 color: tuple = (150, 150, 150, 255),
                 mass: float = 0,
                 x_vel: float = 0,
                 y_vel: float = 0,
                 x_acc: float = 0,
                 y_acc: float = 0,
                 x_speed: float = 0,
                 y_speed: float = 0,
                 fixed: bool = False,
                 bounded: bool = False,
                 scale: float = 1) -> None:
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
        fixed : bool, optional
            whether the planet is fixed
        bounded : bool, optional
            whether the celestial body is bounded
        scale : float, optional
            meters per pixel
        """
        super().__init__(x, y, x_acc, y_acc, screen, x_vel=x_vel, y_vel=y_vel)
        self.radius: float = 4  # max(min(mass / scale, 2), 2)
        self.color: tuple = color
        self.x_speed: float = x_speed
        self.y_speed: float = y_speed
        self.mass: float = mass
        self.fixed: bool = fixed
        self.bounded: bool = bounded
        self.scale: float = scale

    def update(self, dt: float) -> None:
        """
        Update the planet's velocity and position

        Parameters
        ----------
        dt : float
            time elapsed since the last frame
        """
        if self.fixed:
            return

        super().update(dt)

        if not self.bounded:
            return

        if self.pos.x >= self.screen.get_width() or self.pos.x <= 0:
            self.vel.x *= -1
        if self.pos.y >= self.screen.get_height() or self.pos.y <= 0:
            self.vel.y *= -1

    def show(self, scale: float = 1) -> None:
        """
        Draw the planet onto its screen

        Draws a circle of radius self.radius at position (self.pos.x, self.pos.y) with
        color self.color onto the screen self.screen
        """
        target_rect = pygame.Rect((self.pos.x / scale, self.pos.y / scale), (0, 0)).inflate((self.radius * 2, self.radius * 2))
        shape_surf = pygame.Surface(target_rect.size, pygame.SRCALPHA)
        pygame.draw.circle(shape_surf, self.color, (self.radius, self.radius),self. radius)
        self.screen.blit(shape_surf, target_rect)
        # pygame.draw.circle(self.screen, self.color, (self.pos.x / scale, self.pos.y / scale), self.radius)

    def apply_gravity(self, celestial_body: "CelestialBody") -> None:
        """
        Apply gravitational force to the planet and another planet.

        Parameters
        ----------
        celestial_body : CelestialBody
            the celestial body to apply gravity to

        Returns
        -------
        None
        """
        dx: float = celestial_body.pos.x - self.pos.x
        dy: float = celestial_body.pos.y - self.pos.y
        distance: float = sqrt(dx ** 2 + dy ** 2)

        if distance == 0:
            return  # Avoid division by zero

        force_over_distance: float = (gravitational_constant * self.mass * celestial_body.mass) / (distance ** 3)

        # Calculate the acceleration components
        x_acc_delta: float = force_over_distance * dx
        y_acc_delta: float = force_over_distance * dy

        self.acc.x += x_acc_delta / self.mass
        self.acc.y += y_acc_delta / self.mass
        celestial_body.acc.x -= x_acc_delta / celestial_body.mass
        celestial_body.acc.y -= y_acc_delta / celestial_body.mass

    def reset_accelerations(self, info: bool = False) -> None:
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
        self.acc = Vector(0)
        if info:
            print('===== New Celestial Body =====')
            print(f'X Pos: {self.pos.x}')
            print(f'Y Pos: {self.pos.y}')
            print(f'X Vel: {self.vel.x}')
            print(f'Y Vel: {self.vel.y}')
