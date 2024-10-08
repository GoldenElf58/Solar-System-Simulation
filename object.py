import pygame

class Object():
    def __init__(self, x, y, x_acc, y_acc, screen):
        self.x = x
        self.y = y
        self.x_acc = x_acc
        self.y_acc = y_acc
        self.x_vel = 0
        self.y_vel = 0
    
    def update(self):
        self.x_vel += self.x_acc
        self.y_vel += self.y_acc
        self.x += self.x_vel
        self.y += self.y_vel
    
    def draw(self):
        self.pygame.draw.rectangle(screen, (255,0,0), self.x, self.y, self.x + 10, self.y + 10)
