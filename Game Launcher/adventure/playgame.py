import os
import pygame
import sys
import random

# Set the working directory to the script's location
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Initialize pygame
pygame.init()

# Screen dimensions
screen_width = 800
screen_height = 600

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# Create the screen object
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Mystical Forest Adventure')

# Load assets
background_image = pygame.image.load('background.jpg')
player_image = pygame.image.load('player.png')
enemy_image = pygame.image.load('enemy.png')
gem_image = pygame.image.load('gem.png')
powerup_image = pygame.image.load('powerup.png')
pygame.mixer.music.load('background_music.mp3')

# Scale images
background_image = pygame.transform.scale(background_image, (screen_width, screen_height))
# Load assets
background_image = pygame.image.load('background.jpg')
player_image = pygame.image.load('player.png')
enemy_image = pygame.image.load('enemy.png')
gem_image = pygame.image.load('gem.png')
powerup_image = pygame.image.load('powerup.png')  # Ensure you have 'powerup.png' in your assets
pygame.mixer.music.load('background_music.mp3')

# Scale images
background_image = pygame.transform.scale(background_image, (screen_width, screen_height))
player_image = pygame.transform.scale(player_image, (int(player_image.get_width() * 0.07), int(player_image.get_height() * 0.07)))
enemy_image = pygame.transform.scale(enemy_image, (int(enemy_image.get_width() * 0.05), int(enemy_image.get_height() * 0.05)))
powerup_image = pygame.transform.scale(powerup_image, (int(powerup_image.get_width() * 0.6), int(powerup_image.get_height() * 0.6)))
gem_image = pygame.transform.scale(gem_image, (int(gem_image.get_width() * 0.6), int(gem_image.get_height() * 0.6)))

# Clock for controlling the frame rate
clock = pygame.time.Clock()

# Game variables
score = 0
level = 1
gems_collected = 0
gems_required = 5
player_speed = 25
enemy_speed = 3
player_health = 3

# Initialize positions
player_pos = [screen_width // 2, screen_height // 2]
enemy_pos = [random.randint(0, screen_width - enemy_image.get_width()), 
             random.randint(0, screen_height - enemy_image.get_height())]
gem_pos = [random.randint(0, screen_width - gem_image.get_width()), 
           random.randint(0, screen_height - gem_image.get_height())]
powerup_pos = [random.randint(0, screen_width - powerup_image.get_width()), 
               random.randint(0, screen_height - powerup_image.get_height())]

# Define game states
GAME_RUNNING = 0
GAME_OVER = 1
GAME_PAUSED = 2
game_state = GAME_RUNNING

# Enemy class
class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = enemy_image
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = 2  # Adjust speed as needed

    def update(self):
        if self.rect.x < player_pos[0]:
            self.rect.x += self.speed
        elif self.rect.x > player_pos[0]:
            self.rect.x -= self.speed
        if self.rect.y < player_pos[1]:
            self.rect.y += self.speed
        elif self.rect.y > player_pos[1]:
            self.rect.y -= self.speed

# Initialize enemy variables
enemy_list = pygame.sprite.Group()

# Spawn initial enemies
def spawn_initial_enemies():
    for _ in range(level * 3):
        x = random.randrange(screen_width)
        y = random.randrange(screen_height)
        enemy = Enemy(x, y)
        enemy_list.add(enemy)

spawn_initial_enemies()

# Helper functions
def handle_collisions():
    global score, gems_collected, gems_required, level, player_speed, player_health, game_state

    if pygame.Rect(player_pos, player_image.get_size()).colliderect(pygame.Rect(gem_pos, gem_image.get_size())):
        gems_collected += 1
        score += 10
        if gems_collected >= gems_required:
            increase_level()
        reset_positions('gem')

    if pygame.Rect(player_pos, player_image.get_size()).colliderect(pygame.Rect(powerup_pos, powerup_image.get_size())):
        player_speed += 2
        pygame.time.set_timer(pygame.USEREVENT, 5000)
        reset_positions('powerup')

    for enemy in enemy_list:
        if pygame.Rect(player_pos, player_image.get_size()).colliderect(enemy.rect):
            player_health -= 1
            if player_health <= 0:
                handle_game_over()

def increase_level():
    global level, player_speed
    level += 1
    player_speed += 1
    spawn_enemies(level * 3)
    reset_positions()

def spawn_enemies(num):
    for _ in range(num):
        x = random.randrange(screen_width)
        y = random.randrange(screen_height)
        enemy = Enemy(x, y)
        enemy_list.add(enemy)

def reset_positions(obj_type=None):
    global enemy_pos, gem_pos, powerup_pos
    if obj_type in ('enemy', None):
        enemy_pos = [random.randint(0, screen_width - enemy_image.get_width()), 
                     random.randint(0, screen_height - enemy_image.get_height())]
    if obj_type in ('gem', None):
        gem_pos = [random.randint(0, screen_width - gem_image.get_width()), 
                   random.randint(0, screen_height - gem_image.get_height())]
    if obj_type in ('powerup', None):
        powerup_pos = [random.randint(0, screen_width - powerup_image.get_width()), 
                       random.randint(0, screen_height - powerup_image.get_height())]

def draw_gems():
    screen.blit(gem_image, gem_pos)

def draw_powerup():
    screen.blit(powerup_image, powerup_pos)

def draw_hud():
    draw_text(f'Score: {score}', white, 10, 10)
    draw_text(f'Level: {level}', white, 10, 40)
    draw_text(f'Gems Collected: {gems_collected}/{gems_required}', white, 10, 70)
    draw_text(f'Health: {player_health}', white, 10, 100)

def draw_text(text, color, x, y):
    font = pygame.font.Font(None, 36)
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

def handle_game_over():
    global game_state
    draw_text('Game Over', red, screen_width // 2 - 80, screen_height // 2)
    pygame.display.flip()
    pygame.time.wait(2000)
    game_state = GAME_RUNNING
    reset_game()

def reset_game():
    global score, level, gems_collected, gems_required, player_speed, player_health, enemy_list
    score = 0
    level = 1
    gems_collected = 0
    gems_required = 5
    player_speed = 5
    player_health = 3
    reset_positions()
    enemy_list.empty()
    spawn_initial_enemies()
    pygame.mixer.music.play(-1)

def display_controls():
    controls = [
        "Arrow keys to move the player.",
        "Collect gems to increase score.",
        "Avoid enemies to stay alive.",
        "Level up by collecting required gems.",
        "Enemies increase with each level.",
        "Game over if enemy catches you.",
        "Restart the game after game over.",
        "Music plays throughout the game.",
        "Use strategies to avoid enemies.",
        "Enjoy the mystical forest adventure!"
    ]
    y = 100
    for control in controls:
        draw_text(control, white, 20, y)
        y += 40

def draw_background():
    screen.blit(background_image, (0, 0))

def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                intro = False
        screen.fill(black)
        draw_text("Welcome to Mystical Forest Adventure", white, 100, screen_height // 2 - 50)
        draw_text("Press any key to start", white, 100, screen_height // 2 + 10)
        pygame.display.flip()
        clock.tick(15)

def pause_menu():
    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    paused = False
        screen.fill(black)
        draw_text("Paused", white, screen_width // 2 - 50, screen_height // 2 - 30)
        draw_text("Press 'P' to resume", white, screen_width // 2 - 100, screen_height // 2 + 10)
        pygame.display.flip()
        clock.tick(15)

def settings_menu():
    settings = True
    while settings:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    settings = False
        screen.fill(black)
        draw_text("Settings", white, screen_width // 2 - 50, screen_height // 2 - 100)
        draw_text("Press 'S' to return", white, screen_width // 2 - 100, screen_height // 2)
        pygame.display.flip()
        clock.tick(15)

# Main game loop
pygame.mixer.music.play(-1)
game_intro()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                game_state = GAME_PAUSED
            if event.key == pygame.K_s:
                settings_menu()

        if event.type == pygame.USEREVENT:
            player_speed = 5

    if game_state == GAME_RUNNING:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player_pos[0] -= player_speed
        if keys[pygame.K_RIGHT]:
            player_pos[0] += player_speed
        if keys[pygame.K_UP]:
            player_pos[1] -= player_speed
        if keys[pygame.K_DOWN]:
            player_pos[1] += player_speed

        # Ensure player stays within screen bounds
        player_pos[0] = max(0, min(player_pos[0], screen_width - player_image.get_width()))
        player_pos[1] = max(0, min(player_pos[1], screen_height - player_image.get_height()))

        # Update game objects, collisions, etc.
        handle_collisions()

        # Draw everything
        screen.fill(black)  # Clear screen with black color
        draw_background()  # Draw background

        # Draw player
        screen.blit(player_image, player_pos)

        # Draw enemies
        enemy_list.update()
        enemy_list.draw(screen)

        # Draw gems, powerups, HUD, etc.
        draw_gems()
        draw_powerup()
        draw_hud()

        # Update display
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(30)  # Adjust FPS as needed

    elif game_state == GAME_PAUSED:
        pause_menu()

    elif game_state == GAME_OVER:
        handle_game_over()
