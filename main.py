import pygame
import sys
import os
import time

from circle import Circle

# Initialize Pygame
pygame.init()

# Set up the window dimensions
WIDTH, HEIGHT = 400, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moving Circle")

# Set up the clock for controlling the frame rate
clock = pygame.time.Clock()

running = False
deltaTime = 0

circle = Circle(300, 300, 10, screen, x_speed=1, x_acc=1)

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
    dt = clock.tick(60) / 1000
    event_handling()

    circle.update(dt)
    draw()


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