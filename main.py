import pygame
import sys

# Test

# Initialize Pygame
pygame.init()

# Set up the window dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moving Circle")

# Set up the clock for controlling the frame rate
clock = pygame.time.Clock()

running = False


class Object():
    def __init__(self, x, y, x_acc, y_acc):
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
        pygame.draw.rectangle(screen, (255,0,0), self.x, self.y, self.x + 10, self.y + 10)


class Circle(Object):
    def __init__(self, x, y, radius, color=(255,0,0), x_acc=0, y_acc=0, x_speed=5, y_speed=5):
        super().__init__(x, y, x_acc, y_acc)
        self.radius = radius
        self.color = color
        self.x_speed = x_speed
        self.y_speed = y_speed
    
    def update(self):
        global WIDTH
        # Reverse direction upon reaching screen edges
        if self.x - self.radius <= 0 or self.x + self.radius >= WIDTH:
            self.x_acc *= -1
        super().__init__()

    def draw(self):
        global screen
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)


def draw():
    # Clear the screen with a white background
    screen.fill((255, 255, 255))

    # Draw the circle
    circle.draw()

    # Update the display
    pygame.display.flip()

def event_handling():
    global running
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


def loop():
    global clock
    # Cap the frame rate at 60 frames per second
    clock.tick(60)
    event_handling()

    circle.update()
    draw()

def main():
    global running
    circle = Circle(0, 0, 10, x_acc=5)
    # Main loop
    running = True
    while running:
        loop()
    
    # Clean up and exit
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    print("Program Started")
    main()
