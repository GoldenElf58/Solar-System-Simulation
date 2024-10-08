import pygame

class Object():
    def __init__(self, x, y, x_acc, y_acc, screen, x_vel=0, y_vel=0):
        self.x = x
        self.y = y
        self.x_acc = x_acc
        self.y_acc = y_acc
        self.x_vel = x_vel
        self.y_vel = y_vel
        self.screen = screen
    
    def update(self, dt):
        self.x_vel += self.x_acc
        self.y_vel += self.y_acc
        self.x += self.x_vel * dt
        self.y += self.y_vel * dt
    
    def draw(self):
        self.pygame.draw.rectangle(self.screen, (255,0,0), self.x, self.y, self.x + 10, self.y + 10)
