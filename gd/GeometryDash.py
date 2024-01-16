import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 737, 545
GRAVITY = 1
TIME_TICK = 2
LOGO_SCREEN_DURATION = 5000

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Geometry Dash")

# Load images
background = pygame.image.load("images/background.png")
logo = pygame.image.load("images/geometrydash_logo.png")
logo = pygame.transform.scale(logo, (737, 515))
spike_image = pygame.image.load("images/spike.png")

# Fonts
font = pygame.font.SysFont("Arial", 40)

# Sounds
pygame.mixer.init()
jump_sound = pygame.mixer.Sound("StereoMadness.wav")

# Classes
class Cube(pygame.sprite.Sprite):
    def __init__(self, floor):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.bottom = floor.rect.top
        self.velocity = 0

    def jump(self):
        self.velocity = -20
        jump_sound.play()

    def update(self):
        self.velocity += GRAVITY
        self.rect.y += self.velocity

        # Keep the cube above the floor
        if self.rect.bottom > floor.rect.top:
            self.rect.bottom = floor.rect.top
            self.velocity = 0

# Game initialization
clock = pygame.time.Clock()
attempt = 0
score = 0
dead = False
show_logo = True

# Create sprites
spikes = pygame.sprite.Group()
spikes.add(pygame.sprite.Sprite())
spikes.add(pygame.sprite.Sprite())
spikes.sprites()[0].image = spike_image
spikes.sprites()[1].image = spike_image
spikes.sprites()[0].rect = spike_image.get_rect(topleft=(550, 310))
spikes.sprites()[1].rect = spike_image.get_rect(topleft=(700, 310))

floor = pygame.sprite.Sprite()
floor.image = pygame.Surface((WIDTH, 3))
floor.image.fill(WHITE)
floor.rect = floor.image.get_rect(bottom=HEIGHT)

cube = Cube(floor)

# Timers
logo_timer = pygame.time.get_ticks() + LOGO_SCREEN_DURATION
start_game_timer = 0

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not dead:
                cube.jump()
            elif event.key == pygame.K_r:
                attempt += 1
                dead = False
                score = 0
                for spike in spikes:
                    spike.rect.x = WIDTH + random.randint(0, 200)

    # Update
    current_time = pygame.time.get_ticks()

    if show_logo:
        if current_time > logo_timer:
            show_logo = False
            start_game_timer = current_time + 1000
    elif not dead:
        cube.update()
        spikes.update()

        # Check collision with spikes
        if pygame.sprite.spritecollide(cube, spikes, False):
            dead = True

        # Check if a spike is off-screen and reset its position
        for spike in spikes:
            if spike.rect.right < 0:
                spike.rect.x = WIDTH + random.randint(0, 200)
                spike.image = pygame.transform.scale(spike_image, (50, 50))
                spike.velocity *= 1.5

        score += 1

    # Draw
    screen.blit(background, (0, 0))

    if not dead:
        spikes.draw(screen)
        cube_group = pygame.sprite.Group()
        cube_group.add(cube)
        cube_group.draw(screen)

        # Draw score and attempt
        score_text = font.render("Score: " + str(score), True, WHITE)
        attempt_text = font.render("Attempt: " + str(attempt), True, WHITE)
        screen.blit(score_text, (40, 40))
        screen.blit(attempt_text, (600, 40))
    else:
        # Draw game over screen
        game_over_text = font.render("Game Over!", True, WHITE)
        your_score_text = font.render("Your Score: " + str(score), True, WHITE)
        restart_text = font.render("Press 'R' key to play again.", True, WHITE)
        screen.blit(game_over_text, (250, 200))
        screen.blit(your_score_text, (225, 300))
        screen.blit(restart_text, (130, 400))

    if show_logo:
        screen.blit(logo, ((WIDTH - 737) // 2, (HEIGHT - 515) // 2))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
