import pygame
import random
import time

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Geometry Dash Sound Example")

# Load sounds
jump_sound = pygame.mixer.Sound('jump_sound.wav')
collision_sound = pygame.mixer.Sound('collision_sound.wav')

# Game loop
running = True
clock = pygame.time.Clock()
player_y = height // 2
player_speed = 5

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update game logic
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        # Play jump sound when space bar is pressed
        jump_sound.play()

    player_y += player_speed

    # Check for collision with the ground
    if player_y > height:
        # Play collision sound when player hits the ground
        collision_sound.play()
        player_y = height

    # Draw the player and update display
    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, (0, 0, 255), (width // 4, player_y, 50, 50))
    pygame.display.flip()

    # Control frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
