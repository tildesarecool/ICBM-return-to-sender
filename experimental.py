import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH  = 1024 #160 * 3    
HEIGHT = 768 #128 * 3
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Missile Command")

# Define colors
WHITE = (255, 255, 255)

# Set starting point and final destination
start_point = (WIDTH // 2, HEIGHT - 50)
end_point = (1000, 250)

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
#    pygame.draw.line(screen, WHITE, start_point, (int(current_point[0]), int(current_point[1])))

    # Update the endpoint
    print(f"int(current_point[0]) {int(current_point[0]) } <= int(end_point[0]) {int(end_point[0])} and int(current_point[1]) {int(current_point[1])}  >= int(end_point[1]) {int(end_point[1])} is  {int(current_point[0]) <= int(end_point[0]) and int(current_point[1]) >= int(end_point[1])}")


if int(current_point[0]) <= int(end_point[0]) and int(current_point[1]) >= int(end_point[1]):
    pygame.draw.line(screen, WHITE, start_point, (int(current_point[0]), int(current_point[1])), 3)
    current_point[0] += int((end_point[0] - start_point[0]) / 100)  # Adjust the division factor to control the speed
    current_point[1] -= int((start_point[1] - end_point[1]) / 100)


# i modified gpt's code to this below and it seems to almost entirely work    
#    if int(current_point[0]) <= int(end_point[0]) and int(current_point[1]) >= int(end_point[1]) :
#        
#        pygame.draw.line(screen, WHITE, start_point, (int(current_point[0]), int(current_point[1])), 3)
#        current_point[0] += int((end_point[0] - start_point[0]) / 100)  # Adjust the division factor to control the speed
#        current_point[1] -= int((start_point[1] - end_point[1]) / 100)
#        print(f"current_point[1] is {current_point[1]} and (start_point[1] - end_point[1]) / 100 is {(start_point[1] - end_point[1]) / 100}")
    
    # Stop drawing if the line reaches or exceeds the final destination
    #if current_point[1] <= end_point[1]:
    #    break

    # Update the display
    pygame.display.flip()

    # Slow down the loop to control the drawing speed
    pygame.time.delay(20)

pygame.quit()
sys.exit()