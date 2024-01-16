import pygame
import sys
import random

class Sound:
    def __init__(self):
        pygame.mixer.init()

    @staticmethod
    def play_sound(filename):
        pygame.mixer.Sound(filename).play()

class Actor(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        super().__init__()
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = 5

    def update(self):
        self.rect.x -= self.speed

class Cube(pygame.sprite.Sprite):
    def __init__(self, floor):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.bottom = floor.rect.top
        self.velocity = 0

    def jump(self):
        self.velocity = -20
        Sound.play_sound("StereoMadness.wav")

    def update(self):
        self.velocity += 1
        self.rect.y += self.velocity
        if self.rect.bottom > floor.rect.top:
            self.rect.bottom = floor.rect.top
            self.velocity = 0

# Constants
WIDTH, HEIGHT = 737, 545
GRAVITY = 1
TIME_TICK = 2
LOGO_SCREEN_DURATION = 5000

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Pygame Initialization
pygame.init()

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
jump_sound = pygame.mixer.Sound("StereoMadness.wav")

# Create sprites
spikes = pygame.sprite.Group()
spikes.add(Actor("images/spike.png", 550, 310))
spikes.add(Actor("images/spike.png", 700, 310))

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
            if event.key == pygame.K_SPACE and not cube.dead:
                cube.jump()
            elif event.key == pygame.K_r:
                cube.reset_game()

    # Update
    current_time = pygame.time.get_ticks()

    if cube.show_logo:
        if current_time > logo_timer:
            cube.show_logo = False
            start_game_timer = current_time + 1000
    elif not cube.dead:
        cube.update()
        spikes.update()

        # Check collision with spikes
        if pygame.sprite.spritecollide(cube, spikes, False):
            cube.dead = True

        # Check if a spike is off-screen and reset its position
        for spike in spikes:
            if spike.rect.right < 0:
                spike.rect.x = WIDTH + random.randint(0, 200)
                spike.image = pygame.transform.scale(spike_image, (50, 50))
                spike.speed *= 1.5

        cube.score += 1

    # Draw
    screen.blit(background, (0, 0))

    if not cube.dead:
        spikes.draw(screen)
        cube_group = pygame.sprite.Group()
        cube_group.add(cube)
        cube_group.draw(screen)

        # Draw score and attempt
        score_text = font.render("Score: " + str(cube.score), True, WHITE)
        attempt_text = font.render("Attempt: " + str(cube.attempt), True, WHITE)
        screen.blit(score_text, (40, 40))
        screen.blit(attempt_text, (600, 40))
    else:
        # Draw game over screen
        game_over_text = font.render("Game Over!", True, WHITE)
        your_score_text = font.render("Your Score: " + str(cube.score), True, WHITE)
        restart_text = font.render("Press 'R' key to play again.", True, WHITE)
        screen.blit(game_over_text, (250, 200))
        screen.blit(your_score_text, (225, 300))
        screen.blit(restart_text, (130, 400))

    if cube.show_logo:
        screen.blit(logo, ((WIDTH - 737) // 2, (HEIGHT - 515) // 2))

    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
