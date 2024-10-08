import pygame

from object import Object

class Planet(Object):
    def __init__(self, x, y, radius, screen, color=(255,0,0), x_vel=0, y_vel=0, x_acc=0, y_acc=0, x_speed=0, y_speed=0):
        """
        Initialize a Circle object

        Parameters
        ----------
        x : int
            initial x position
        y : int
            initial y position
        radius : int
            radius of the circle
        screen : pygame.Surface
            the screen onto which the circle will be drawn
        color : tuple of 3 ints, optional
            color of the circle (default is red)
        x_vel : int, optional
            initial x velocity
        y_vel : int, optional
            initial y velocity
        x_acc : int, optional
            x acceleration
        y_acc : int, optional
            y acceleration
        x_speed : int, optional
            x speed at which the circle will move
        y_speed : int, optional
            y speed at which the circle will move
        """
        super().__init__(x, y, x_acc, y_acc, screen, x_vel=x_vel, y_vel=y_vel)
        self.radius = radius
        self.color = color
        self.x_speed = x_speed
        self.y_speed = y_speed
    
    def update(self, dt):
        """
        Update the circle's velocity and position

        If the circle hits the edge of the screen, it will
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

    def draw(self):
        """
        Draw the circle onto its screen

        Draws a circle of radius self.radius at position (self.x, self.y) with
        color self.color onto the screen self.screen
        """
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.radius)
