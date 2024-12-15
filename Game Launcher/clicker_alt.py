import pygame
import sys

# Initialize Pygame
pygame.init()

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Screen dimensions
WIDTH, HEIGHT = 400, 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Clicker Game")

# Font
font = pygame.font.Font(None, 36)

# Button
button = pygame.Rect(150, 120, 100, 50)

# Score
score = 0

# Game state
game_active = False

def display_start_screen():
    screen.fill(WHITE)
    start_text = font.render("Press ENTER to Start", True, BLUE)
    screen.blit(start_text, (70, 100))
    pygame.display.flip()

def run_game():
    global score
    running = True
    while running:
        screen.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if game_active:
                # Check for mouse click on the button
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if button.collidepoint(event.pos):
                        score += 1  # Increase score when button is clicked

        if game_active:
            # Draw the button
            pygame.draw.rect(screen, RED, button)
            
            # Render the score
            score_text = font.render(f"Score: {score}", True, BLACK)
            screen.blit(score_text, (150, 50))
            
            # Render the button label
            button_text = font.render("Click me!", True, WHITE)
            screen.blit(button_text, (button.x + 10, button.y + 10))
        
        pygame.display.flip()

# Main game loop
start_screen = True
while True:
    if start_screen:
        display_start_screen()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                start_screen = False
                game_active = True
    else:
        run_game()
