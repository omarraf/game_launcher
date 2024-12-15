import pygame
import random
import time

# Initialize Pygame
pygame.init()

# Screen settings
screen_width, screen_height = 600, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Tile Slider Puzzle")

# Colors and Fonts
black = (0, 0, 0)
white = (255, 255, 255)
gray = (211, 211, 211)
blue = (70, 130, 180)
green = (50, 205, 50)
red = (255, 99, 71)
yellow = (255, 255, 0)
font_large = pygame.font.Font(None, 72)
font_small = pygame.font.Font(None, 36)

# Sound Effects
move_sound = pygame.mixer.Sound("move_sound.mp3")
victory_sound = pygame.mixer.Sound("victory_sound.wav")

# Tile Puzzle Variables
grid_size = 4  # 4x4 grid
tile_size = screen_width // grid_size
tiles = []
empty_tile = (grid_size - 1, grid_size - 1)
moves = 0
start_time = time.time()

# Generate tiles with numbers
def create_tiles():
    global tiles
    tiles = [[grid_size * y + x + 1 for x in range(grid_size)] for y in range(grid_size)]
    tiles[-1][-1] = 0  # Empty tile

def draw_grid():
    for y in range(grid_size):
        for x in range(grid_size):
            if tiles[y][x] != 0:
                pygame.draw.rect(screen, blue, (x * tile_size, y * tile_size, tile_size, tile_size), border_radius=10)
                draw_text_centered(str(tiles[y][x]), font_large, white, x * tile_size + tile_size // 2, y * tile_size + tile_size // 2)
            else:
                pygame.draw.rect(screen, black, (x * tile_size, y * tile_size, tile_size, tile_size))

# Function to shuffle the puzzle
def shuffle_tiles():
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for _ in range(1000):
        move = random.choice(directions)
        move_tile(empty_tile[0] + move[0], empty_tile[1] + move[1])

# Move the tile
def move_tile(x, y):
    global empty_tile, moves
    if 0 <= x < grid_size and 0 <= y < grid_size:
        tiles[empty_tile[1]][empty_tile[0]] = tiles[y][x]
        tiles[y][x] = 0
        empty_tile = (x, y)
        moves += 1
        move_sound.play()

# Draw centered text
def draw_text_centered(text, font, color, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x, y))
    screen.blit(text_surface, text_rect)

# Check if the puzzle is solved
def is_solved():
    for y in range(grid_size):
        for x in range(grid_size):
            if tiles[y][x] != grid_size * y + x + 1 and not (y == grid_size - 1 and x == grid_size - 1):
                return False
    return True

# Victory animation
def victory_animation():
    victory_sound.play()
    for i in range(100):
        pygame.draw.circle(screen, yellow, (random.randint(0, screen_width), random.randint(0, screen_height)), random.randint(5, 15))
        pygame.display.flip()
        pygame.time.wait(20)

# Reset the puzzle
def reset_puzzle():
    create_tiles()
    shuffle_tiles()
    global start_time, moves
    start_time = time.time()
    moves = 0

# Main Game Loop
create_tiles()
shuffle_tiles()
running = True
clock = pygame.time.Clock()

while running:
    screen.fill(gray)

    # Draw the grid of tiles
    draw_grid()

    # Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                move_tile(empty_tile[0] + 1, empty_tile[1])
            elif event.key == pygame.K_RIGHT:
                move_tile(empty_tile[0] - 1, empty_tile[1])
            elif event.key == pygame.K_UP:
                move_tile(empty_tile[0], empty_tile[1] + 1)
            elif event.key == pygame.K_DOWN:
                move_tile(empty_tile[0], empty_tile[1] - 1)

    # Check if solved
    if is_solved():
        draw_text_centered("You Win!", font_large, green, screen_width // 2, screen_height // 2)
        pygame.display.flip()
        pygame.time.wait(1000)
        victory_animation()
        reset_puzzle()

    # Draw the timer and move counter
    elapsed_time = time.time() - start_time
    draw_text_centered(f"Time: {int(elapsed_time)}s", font_small, black, screen_width // 2, screen_height - 50)
    draw_text_centered(f"Moves: {moves}", font_small, black, screen_width // 2, screen_height - 100)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
