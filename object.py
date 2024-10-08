import pygame


class Object():
    def __init__(self, x, y, x_acc, y_acc, screen, x_vel=0, y_vel=0):
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
        self.x = x
        self.y = y
        self.x_acc = x_acc
        self.y_acc = y_acc
        self.x_vel = x_vel
        self.y_vel = y_vel
        self.screen = screen
    
    def update(self, dt):
        """
        Update the object's velocity and position

        Parameters
        ----------
        dt : float
            time elapsed since the last frame
        """
        self.x_vel += self.x_acc
        self.y_vel += self.y_acc
        self.x += self.x_vel * dt
        self.y += self.y_vel * dt
    
    def draw(self):
        """
        Draw the object onto its screen

        Draws a red rectangle of width and height 10 at position (self.x, self.y) onto the screen self.screen
        """
        pygame.draw.rect(self.screen, (255,0,0), pygame.Rect(self.x, self.y, self.x + 10, self.y + 10))
