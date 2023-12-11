"""
import pygame
from pygame.locals import *

# Initialize Pygame
pygame.init()

# Define the screen dimensions
screen = pygame.display.set_mode((800, 600))

# Create a square surface
square_size = 25
square_surf = pygame.Surface((square_size, square_size))
square_surf.fill((0, 200, 255))
square_rect = square_surf.get_rect()

# Variable to keep the game loop running
running = True

# Main game loop
while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_BACKSPACE:
                running = False
        elif event.type == QUIT:
            running = False

    # Blit the square onto the screen
    screen.blit(square_surf, (400 - square_size // 2, 300 - square_size // 2))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()


import pygame

# Initializing Pygame
pygame.init()

# Creating a window with dimensions 400x500
window = pygame.display.set_mode((400, 500))

# Variable to control the game loop
running = True

# Variable to store the background color
color = (255, 0, 0)  # Initial color: Red

# Game Loop
while running:
    # Check for events
    for event in pygame.event.get():
        # If the user clicks the close button, exit the loop
        if event.type == pygame.QUIT:
            running = False

    # Set the background color of the window
    window.fill(color)

    # Update the window
    pygame.display.flip()

    # Change the background color in each iteration
    if color == (255, 0, 0):
        color = (0, 255, 0)  # Change to Green
    else:
        color = (255, 0, 0)  # Change to Red

# Quit Pygame
pygame.quit()

"""