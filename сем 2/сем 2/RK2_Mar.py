import math
import pygame

# Set up the screen
pygame.init()
screen_width, screen_height = 600, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Rotating Triangle")

# Set up the colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# Set up the clock
clock = pygame.time.Clock()

# Set up the parameters
radius = 150
angular_velocity = 0.01
edge_length = 100
phi = 35.264 # angle between the z-axis and the xy-plane in an isometric projection
cos_phi = math.cos(math.radians(phi))
sin_phi = math.sin(math.radians(phi))

# Set up the initial position of the triangle vertices
center = (screen_width//2, screen_height//2)
vertex1 = (center[0], center[1] + edge_length/2)
vertex2 = (center[0] - edge_length/2*cos_phi, center[1] - edge_length/2*sin_phi)
vertex3 = (center[0] + edge_length/2*cos_phi, center[1] - edge_length/2*sin_phi)

# Start the main loop
angle = 0
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    
    # Clear the screen
    screen.fill(white)
    
    # Calculate the new center position
    angle += angular_velocity
    
    # Calculate the new vertices positions
    vertex1 = (center[0], center[1] + edge_length/2)
    vertex2 = (center[0] - edge_length/2*cos_phi*math.cos(angle) + edge_length/2*sin_phi*math.sin(angle), center[1] - edge_length/2*sin_phi*cos_phi)
    vertex3 = (center[0] + edge_length/2*cos_phi*math.cos(angle) + edge_length/2*sin_phi*math.sin(angle), center[1] - edge_length/2*sin_phi*cos_phi)
    
    # Draw the triangle
    pygame.draw.polygon(screen, red, [vertex1, vertex2, vertex3])
    
    # Draw the circle
    pygame.draw.arc(screen, black, (center[0]-radius, center[1]-radius, radius*2, radius*2), 0, math.pi*2, 1)
    
    # Update the display
    pygame.display.update()
    
    # Control the framerate
    clock.tick(60)
