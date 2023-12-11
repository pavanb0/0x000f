import pygame
import sys
import random

pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
TARGET_SIZE = 50
TARGET_SPEED = 5
BULLET_SPEED = 10
FPS = 30

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Initialize game
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Target Shooting Game")
clock = pygame.time.Clock()

targets = []

# Target class
class Target:
    def __init__(self):
        self.x = random.randint(0, WIDTH - TARGET_SIZE)
        self.y = random.randint(0, HEIGHT - TARGET_SIZE)
        self.speed = TARGET_SPEED

    def move(self):
        self.y += self.speed
        if self.y > HEIGHT:
            self.y = 0
            self.x = random.randint(0, WIDTH - TARGET_SIZE)

    def draw(self):
        pygame.draw.rect(screen, RED, (self.x, self.y, TARGET_SIZE, TARGET_SIZE))

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        bullet_y = HEIGHT - TARGET_SIZE
        for target in targets:
            if target.x <= pygame.mouse.get_pos()[0] <= target.x + TARGET_SIZE and target.y <= bullet_y <= target.y + TARGET_SIZE:
                targets.remove(target)

    # Update targets
    for target in targets:
        target.move()

    # Create new target
    if random.randint(0, 100) < 5:  # Adjust the probability as needed
        targets.append(Target())

    # Draw everything
    screen.fill(WHITE)
    for target in targets:
        target.draw()

    pygame.display.flip()
    clock.tick(FPS)
