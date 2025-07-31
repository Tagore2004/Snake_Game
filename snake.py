import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions and block size
height = 500
width = 700
block_size = 20

# Setup screen
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("🐍 Snake Game")

# Colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

# Clock and font
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)

# Draw snake blocks
def draw_snake(snake_list):
    for block in snake_list:
        pygame.draw.rect(screen, GREEN, (*block, block_size, block_size))

# Draw the food
def draw_food(position):
    pygame.draw.rect(screen, RED, (*position, block_size, block_size))

# Display message
def message(text, color):
    msg = font.render(text, True, color)
    screen.blit(msg, [width // 4, height // 2])

# Main game loop
def game_loop():
    snake = [(100, 100)]
    direction = "RIGHT"
    change = direction
    food = [random.randrange(0, width, block_size), random.randrange(0, height, block_size)]
    score = 0

    while True:
        for event in pygame.event.get():  # ✅ Fixed this
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != "DOWN":
                    change = "UP"
                elif event.key == pygame.K_DOWN and direction != "UP":
                    change = "DOWN"
                elif event.key == pygame.K_LEFT and direction != "RIGHT":
                    change = "LEFT"
                elif event.key == pygame.K_RIGHT and direction != "LEFT":
                    change = "RIGHT"

        direction = change
        x, y = snake[0]

        if direction == "UP":
            y -= block_size
        elif direction == "DOWN":
            y += block_size
        elif direction == "LEFT":
            x -= block_size
        elif direction == "RIGHT":
            x += block_size

        head = (x, y)  # ✅ Fixed this

        # Check collision
        if x < 0 or x >= width or y < 0 or y >= height or head in snake:
            screen.fill(BLACK)
            message("GAME OVER! SCORE: " + str(score), RED)  # ✅ Typo fixed
            pygame.display.update()
            pygame.time.wait(2000)
            return

        snake.insert(0, head)

        if head == tuple(food):
            score += 1
            food = [random.randrange(0, width, block_size), random.randrange(0, height, block_size)]
        else:
            snake.pop()

        screen.fill(BLACK)
        draw_snake(snake)
        draw_food(food)
        score_text = font.render("Score: " + str(score), True, WHITE)
        screen.blit(score_text, [10, 10])  # ✅ Fixed scree → screen

        pygame.display.update()  # ✅ Fixed displa → display.update
        clock.tick(10)

# Run the game
game_loop()
