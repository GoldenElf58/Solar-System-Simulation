import pygame
import sys

from circle import Circle
from utils import clear

# Initialize Pygame
pygame.init()

# Set up the window dimensions
screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Moving Circle")

# Set up the clock for controlling the frame rate
clock = pygame.time.Clock()

running = False

circle = Circle(300, 300, 10, screen, x_speed=50, x_vel=50)

def draw():
    global circle
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
    global clock, circle, deltaTime
    # Cap the frame rate at 60 frames per second
    dt = clock.tick(60) / 1000 # ms to s
    event_handling()

    circle.update(dt)
    draw()
    # clear()
    # print(circle.x, circle.y)


def main():
    global running
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
