import pygame

from object import Object

class Circle(Object):
    def __init__(self, x, y, radius, screen, color=(255,0,0), x_acc=0, y_acc=0, x_speed=5, y_speed=5):
        super().__init__(x, y, x_acc, y_acc, screen)
        self.radius = radius
        self.color = color
        self.x_speed = x_speed
        self.y_speed = y_speed
    
    def update(self, dt):
        global WIDTH
        # Reverse direction upon reaching screen edges
        if self.x - self.radius <= 0:
            self.x_acc = self.x_speed
        elif self.x + self.radius >= self.screen.get_width():
            self.x_acc = -self.x_speed
        super().update(dt)

    def draw(self):
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.radius)
