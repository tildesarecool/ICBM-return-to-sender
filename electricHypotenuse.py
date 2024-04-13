import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 1024, 768
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Missile Command")

# Define colors
WHITE = (255, 255, 255)

# Set starting point and final destination
start_point = (WIDTH // 2, HEIGHT - 50)
end_point = (1000, 250)

# Calculate the length of the hypotenuse (line)
hypotenuse_length = math.hypot(end_point[0] - start_point[0], start_point[1] - end_point[1])

# Determine which side is longer (adjacent or opposite)
if end_point[0] - start_point[0] >= start_point[1] - end_point[1]:
    longer_side = end_point[0] - start_point[0]
else:
    longer_side = start_point[1] - end_point[1]

# Main loop
running = True
current_point = list(start_point)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill((0, 0, 0))

    # Incrementally draw the line
    pygame.draw.line(screen, WHITE, start_point, (int(current_point[0]), int(current_point[1])))

    # Update the endpoint
    current_point[0] += int((end_point[0] - start_point[0]) / (hypotenuse_length / longer_side))
    current_point[1] -= int((start_point[1] - end_point[1]) / (hypotenuse_length / longer_side))

    # Update the display
    pygame.display.flip()

    # Slow down the loop to control the drawing speed
    pygame.time.delay(20)

pygame.quit()
sys.exit()
