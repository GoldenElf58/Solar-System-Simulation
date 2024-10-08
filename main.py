import pygame
import sys
import os

from circle import Circle

# Initialize Pygame
pygame.init()

# Set up the window dimensions
WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moving Circle")

print(screen.get_width())

# Set up the clock for controlling the frame rate
clock = pygame.time.Clock()

running = False

circle = Circle(300, 300, 10, screen, x_speed=5, x_acc=5)

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
    global clock, circle
    # Cap the frame rate at 60 frames per second
    clock.tick(60)
    event_handling()

    circle.update()
    draw()
    
    os.system("clear")

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