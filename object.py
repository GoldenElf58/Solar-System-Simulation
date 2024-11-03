import pygame

from vector import Point, Vector


class Object:
    def __init__(self, x: float, y: float, x_acc: float, y_acc: float, screen: pygame.Surface,
                 x_vel: float = 0, y_vel: float = 0) -> None:
        """
        Initialize an Object

        Parameters
        ----------
        x : int
            initial x position
        y : int
            initial y position
        x_acc : int
            initial x acceleration
        y_acc : int
            initial y acceleration
        screen : pygame.Surface
            the screen onto which the object will be drawn
        x_vel : int, optional
            initial x velocity
        y_vel : int, optional
            initial y velocity
        """
        self.pos: Point = Point(x, y)
        self.vel: Vector = Vector(x_vel, y_vel)
        self.acc: Vector = Vector(x_acc, y_acc)
       
        # self.x: float = x
        # self.y: float = y
        # self.x_acc: float = x_acc
        # self.y_acc: float = y_acc
        # self.x_vel: float = x_vel
        # self.y_vel: float = y_vel
        
        self.screen: pygame.Surface = screen

    def update(self, dt: float) -> None:
        """
        Update the object's velocity and position

        Parameters
        ----------
        dt : float
            time elapsed since the last frame
        """
        self.vel.x += self.acc.x
        self.vel.y += self.acc.y
        self.pos.x += self.vel.x * dt
        self.pos.y += self.vel.y * dt
        
        # self.x_vel += self.x_acc
        # self.y_vel += self.y_acc
        # self.x += self.x_vel * dt
        # self.y += self.y_vel * dt

    def show(self) -> None:
        """
        Draw the object onto its screen
        Draws a red rectangle of width and height 10 at position (self.x, self.y) onto the screen self.screen
        """
        pygame.draw.rect(self.screen, (255, 0, 0), pygame.Rect(self.x, self.y, self.x + 10, self.y + 10))
