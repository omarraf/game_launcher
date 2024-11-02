import pygame
import random

# Initialize Pygame
pygame.init()

# Screen settings
screen_width, screen_height = 600, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Drag-and-Drop Puzzle")

# Colors and Fonts
white = (255, 255, 255)
blue = (100, 149, 237)
green = (50, 205, 50)
red = (255, 69, 0)
font = pygame.font.Font(None, 40)

# Grid and Tile Settings
grid_size = 3  # 3x3 puzzle grid
tile_size = screen_width // grid_size
tiles = []
original_tiles = []
empty_tile_pos = (grid_size - 1, grid_size - 1)
tile_moving = None

# Load Images for Puzzle Tiles (Replace with your own image paths)
image = pygame.image.load('puzzle_image.png')
image = pygame.transform.scale(image, (screen_width, screen_height))

# Function to Create Puzzle Tiles
def create_tiles():
    global tiles, original_tiles
    tiles = []
    original_tiles = []
    for y in range(grid_size):
        for x in range(grid_size):
            if (y, x) != empty_tile_pos:
                rect = pygame.Rect(x * tile_size, y * tile_size, tile_size, tile_size)
                tile_image = image.subsurface(rect)
                tiles.append({'rect': rect, 'image': tile_image, 'correct_pos': (x, y), 'current_pos': (x, y)})
                original_tiles.append({'rect': rect, 'image': tile_image, 'correct_pos': (x, y), 'current_pos': (x, y)})

def draw_tiles():
    for tile in tiles:
        screen.blit(tile['image'], (tile['current_pos'][0] * tile_size, tile['current_pos'][1] * tile_size))

def check_win():
    for tile in tiles:
        if tile['current_pos'] != tile['correct_pos']:
            return False
    return True

def shuffle_tiles():
    for _ in range(100):
        random.shuffle(tiles)
        for i, tile in enumerate(tiles):
            tile['current_pos'] = (i % grid_size, i // grid_size)

def draw_text(text, color, x, y):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

def display_hint():
    screen.blit(image, (0, 0))
    pygame.display.flip()
    pygame.time.wait(2000)  # Display the correct image for 2 seconds

# Main Game Loop
create_tiles()
shuffle_tiles()
running = True
dragging = False
clock = pygame.time.Clock()

while running:
    screen.fill(white)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN and not dragging:
            pos = pygame.mouse.get_pos()
            for tile in tiles:
                if tile['rect'].collidepoint(pos):
                    dragging = True
                    tile_moving = tile
                    break

        if event.type == pygame.MOUSEBUTTONUP and dragging:
            dragging = False
            tile_moving = None

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_h:  # Press 'H' to show hint
                display_hint()

    if dragging and tile_moving:
        tile_moving['current_pos'] = (pygame.mouse.get_pos()[0] // tile_size, pygame.mouse.get_pos()[1] // tile_size)

    draw_tiles()

    if check_win():
        draw_text("You Win!", green, screen_width // 2 - 80, screen_height // 2)
        pygame.display.flip()
        pygame.time.wait(2000)
        running = False

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
