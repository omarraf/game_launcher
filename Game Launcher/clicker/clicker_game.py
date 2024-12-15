import pygame
import random
import time

# Initialize Pygame
pygame.init()

# Screen settings
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Super Clicker Game")

# Colors and Fonts
white = (255, 255, 255)
black = (0, 0, 0)
blue = (70, 130, 180)
red = (255, 99, 71)
green = (50, 205, 50)
yellow = (255, 255, 0)
font_large = pygame.font.Font(None, 72)
font_small = pygame.font.Font(None, 36)

# Game Variables
clicks = 0
combo = 0
combo_start_time = 0
combo_duration = 3  # Combo resets if inactive for 3 seconds
points_per_click = 1
power_up_active = False
power_up_duration = 5
power_up_time = 0

# Particle effect for click feedback
particles = []

# Load Sound Effects
click_sound = pygame.mixer.Sound("click_sound.wav")
power_up_sound = pygame.mixer.Sound("power_up_sound.wav")
combo_sound = pygame.mixer.Sound("combo_sound.wav")

# Particle Creation Function
def create_particle(x, y):
    for _ in range(5):
        particles.append([[x, y], [random.uniform(-1, 1), random.uniform(-1, 1)], random.randint(5, 10)])

# Function to draw particles
def draw_particles():
    for particle in particles:
        particle[0][0] += particle[1][0]
        particle[0][1] += particle[1][1]
        particle[2] -= 0.1  # Shrink over time
        pygame.draw.circle(screen, white, (int(particle[0][0]), int(particle[0][1])), int(particle[2]))
        if particle[2] <= 0:
            particles.remove(particle)

# Function to draw centered text
def draw_text_centered(text, font, color, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x, y))
    screen.blit(text_surface, text_rect)

# Function to draw the button
def draw_button(text, x, y, w, h, color, hover_color):
    mouse = pygame.mouse.get_pos()
    clicked = False

    # Hover effect
    if x < mouse[0] < x + w and y < mouse[1] < y + h:
        pygame.draw.rect(screen, hover_color, (x, y, w, h))
        if pygame.mouse.get_pressed()[0]:
            clicked = True
    else:
        pygame.draw.rect(screen, color, (x, y, w, h))

    # Button text
    draw_text_centered(text, font_small, white, x + w // 2, y + h // 2)
    return clicked

# Main Game Loop
running = True
clock = pygame.time.Clock()

while running:
    screen.fill(black)
    
    # Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Check for button click
    if draw_button("CLICK ME!", screen_width // 2 - 100, screen_height // 2 - 50, 200, 100, blue, red):
        clicks += points_per_click
        click_sound.play()
        create_particle(screen_width // 2, screen_height // 2)
        combo += 1
        combo_start_time = time.time()
        if combo % 5 == 0:  # Combo reward
            combo_sound.play()
            points_per_click += 1

    # Handle combo duration
    if combo > 0 and time.time() - combo_start_time > combo_duration:
        combo = 0
        points_per_click = 1

    # Display Click Count
    draw_text_centered(f"Clicks: {clicks}", font_large, green, screen_width // 2, 100)
    
    # Display Combo if active
    if combo > 0:
        draw_text_centered(f"Combo: {combo}x", font_small, yellow, screen_width // 2, 200)

    # Power-Up Activation
    if draw_button("Power-Up", 50, screen_height - 100, 200, 50, green, yellow) and not power_up_active:
        power_up_active = True
        power_up_time = time.time()
        points_per_click *= 2
        power_up_sound.play()

    # Handle Power-Up Expiry
    if power_up_active and time.time() - power_up_time > power_up_duration:
        power_up_active = False
        points_per_click = 1

    # Draw Particles
    draw_particles()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
