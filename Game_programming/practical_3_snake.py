import pygame
import sys
import random

pygame.init()

# Constants
WIDTH, HEIGHT = 600, 400
GRID_SIZE = 20
SNAKE_SIZE = 20

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Initialize game
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()

snake = [(100, 100)]
direction = (1, 0)
food = (200, 200)

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    direction = (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT],
                 keys[pygame.K_DOWN] - keys[pygame.K_UP])

    # Update snake position
    x, y = snake[0]
    x += direction[0] * SNAKE_SIZE
    y += direction[1] * SNAKE_SIZE
    snake.insert(0, (x, y))

    # Check for collisions
    if snake[0] == food:
        food = (random.randint(0, WIDTH // GRID_SIZE - 1) * GRID_SIZE,
                random.randint(0, HEIGHT // GRID_SIZE - 1) * GRID_SIZE)
    else:
        snake.pop()

    # Draw everything
    screen.fill(BLACK)
    pygame.draw.rect(screen, RED, (*food, SNAKE_SIZE, SNAKE_SIZE))
    for segment in snake:
        pygame.draw.rect(screen, WHITE, (*segment, SNAKE_SIZE, SNAKE_SIZE))

    pygame.display.flip()
    clock.tick(10)
