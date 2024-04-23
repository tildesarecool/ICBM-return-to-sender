import pygame
import sys
import math

clock = pygame.time.Clock()

class RightTriangleLines:
    def __init__(self):
        self.start_point = None
        self.end_point = None
        self.drawn_length = 0  # Variable to track the length of the drawn line

    def vertices_from_hypotenuse(self, start_x, start_y, end_x, end_y):
        self.start_point = (start_x, start_y)
        self.end_point = (end_x, end_y)

    def draw(self, screen, color, thickness, iterator):
        if self.start_point is None or self.end_point is None:
            raise ValueError("Start and end points not specified")

        # Calculate the length of the hypotenuse using math.hypot()
        hypotenuse_length = math.hypot(self.end_point[0] - self.start_point[0], self.end_point[1] - self.start_point[1])

        # Increase the drawn_length by iterator in each iteration
        self.drawn_length += iterator

        # Calculate the end point of the drawn line based on the drawn_length
        drawn_end_x = self.start_point[0] + (self.end_point[0] - self.start_point[0]) * (self.drawn_length / hypotenuse_length)
        drawn_end_y = self.start_point[1] + (self.end_point[1] - self.start_point[1]) * (self.drawn_length / hypotenuse_length)
        drawn_end_point = (int(drawn_end_x), int(drawn_end_y))

        # Draw the line segment
        pygame.draw.line(screen, color, self.start_point, drawn_end_point, thickness)

        # If the drawn length exceeds the length of the hypotenuse, stop the animation
        if self.drawn_length >= hypotenuse_length:
            self.drawn_length = hypotenuse_length


# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Right Triangle Animation")

# Define colors
WHITE = (255, 255, 255)

# Clear the screen
screen.fill((0, 0, 0))

# Create an instance of RightTriangleLines
MyRightTriangle = RightTriangleLines()

# Set the vertices from the hypotenuse
MyRightTriangle.vertices_from_hypotenuse(100, 500, 600, 100)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw the triangle with animation
    MyRightTriangle.draw(screen, WHITE, 3, 2)  # Change the iterator value to control the speed of animation

    # Update the display
    pygame.display.flip()
    clock.tick(60)

# Quit Pygame
pygame.quit()
sys.exit()


























#import pygame 
#import sys
#
#clock = pygame.time.Clock()
#
## Geeze. Finally.
## 
## 
#
#
#class RightTriangleLines:
#    def __init__(self):
#        self.start_point = None
#        self.end_point = None
#        self.drawn_length = 0  # Variable to track the length of the drawn line
#
#    def vertices_from_hypotenuse(self, start_x, start_y, end_x, end_y):
#        self.start_point = (start_x, start_y)
#        self.end_point = (end_x, end_y)
#
#    def draw(self, screen, color, thickness, iterator):
#        if self.start_point is None or self.end_point is None:
#            raise ValueError("Start and end points not specified")
#
#        # Calculate the length of the hypotenuse
#        hypotenuse_length = ((self.end_point[0] - self.start_point[0]) ** 2 +
#                             (self.end_point[1] - self.start_point[1]) ** 2) ** 0.5
#
#        # Increase the drawn_length by iterator in each iteration
#        self.drawn_length += iterator
#
#        # Calculate the end point of the drawn line based on the drawn_length
#        drawn_end_x = self.start_point[0] + (self.end_point[0] - self.start_point[0]) * (self.drawn_length / hypotenuse_length)
#        drawn_end_y = self.start_point[1] + (self.end_point[1] - self.start_point[1]) * (self.drawn_length / hypotenuse_length)
#        drawn_end_point = (int(drawn_end_x), int(drawn_end_y))
#
#        # Draw the line segment
#        pygame.draw.line(screen, color, self.start_point, drawn_end_point, thickness)
#
#        # If the drawn length exceeds the length of the hypotenuse, stop the animation
#        if self.drawn_length >= hypotenuse_length:
#            self.drawn_length = hypotenuse_length
#
#
## Initialize Pygame
#pygame.init()
#
## Set up the display
#WIDTH, HEIGHT = 800, 600
#screen = pygame.display.set_mode((WIDTH, HEIGHT))
#pygame.display.set_caption("Right Triangle Animation")
#
## Define colors
#WHITE = (255, 255, 255)
#
## Clear the screen
#screen.fill((0, 0, 0))
#
## Create an instance of RightTriangleLines
#MyRightTriangle = RightTriangleLines()
#
## Set the vertices from the hypotenuse
#MyRightTriangle.vertices_from_hypotenuse(100, 500, 650, 400)
#
## Main loop
#running = True
#while running:
#    for event in pygame.event.get():
#        if event.type == pygame.QUIT:
#            running = False
#
#    # Clear the screen
#    screen.fill((0, 0, 0))
#
#    # Draw the triangle with animation
#    MyRightTriangle.draw(screen, WHITE, 3, 1)  # Change the iterator value to control the speed of animation
#
#    # Update the display
#    pygame.display.flip()
#    clock.tick(60)
#
## Quit Pygame
#pygame.quit()
#sys.exit()
#