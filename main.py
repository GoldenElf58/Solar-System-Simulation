import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the window dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moving Circle")

# Define circle properties
circle_radius = 30
circle_x = WIDTH // 2
circle_y = HEIGHT // 2
circle_color = (255, 0, 0)  # Red color

# Movement speed
circle_speed_x = 5  # pixels per frame

# Set up the clock for controlling the frame rate
clock = pygame.time.Clock()

def loop():
    # Cap the frame rate at 60 frames per second
    clock.tick(60)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update circle position
    circle_x += circle_speed_x

    # Reverse direction upon reaching screen edges
    if circle_x - circle_radius <= 0 or circle_x + circle_radius >= WIDTH:
        circle_speed_x *= -1

    # Clear the screen with a white background
    screen.fill((255, 255, 255))

    # Draw the circle
    pygame.draw.circle(screen, circle_color, (circle_x, circle_y), circle_radius)

    # Update the display
    pygame.display.flip()

def main():
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
