import pygame

from object import Object


class Planet(Object):
    def __init__(self, x: int, y: int, radius: int, screen: pygame.Surface,
                 color: tuple = (255, 0, 0), x_vel: int = 0, y_vel: int = 0,
                 x_acc: int = 0, y_acc: int = 0, x_speed: int = 0,
                 y_speed: int = 0) -> None:
        """
        Initialize a Planet object

        Parameters
        ----------
        x : int
            initial x position
        y : int
            initial y position
        radius : int
            radius of the planet
        screen : pygame.Surface
            the screen onto which the planet will be drawn
        color : tuple of 3 ints, optional
            color of the planet (default is red)
        x_vel : int, optional
            initial x velocity
        y_vel : int, optional
            initial y velocity
        x_acc : int, optional
            x acceleration
        y_acc : int, optional
            y acceleration
        x_speed : int, optional
            x speed at which the planet will move
        y_speed : int, optional
            y speed at which the planet will move
        """
        super().__init__(x, y, x_acc, y_acc, screen, x_vel=x_vel, y_vel=y_vel)
        self.radius: int = radius
        self.color: tuple = color
        self.x_speed: int = x_speed
        self.y_speed: int = y_speed

    def update(self, dt: float) -> None:
        """
        Update the planet's velocity and position

        If the planet hits the edge of the screen, it will
        bounce off and change direction.

        Parameters
        ----------
        dt : float
            time elapsed since the last frame
        """
        if self.x - self.radius <= 0:
            self.x_vel = self.x_speed
        elif self.x + self.radius >= self.screen.get_width():
            self.x_vel = -self.x_speed
        super().update(dt)

    def draw(self) -> None:
        """
        Draw the planet onto its screen

        Draws a circle of radius self.radius at position (self.x, self.y) with
        color self.color onto the screen self.screen
        """
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.radius)