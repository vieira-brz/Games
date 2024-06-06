import warnings

# Disable all warnings
warnings.filterwarnings("ignore")

import pygame
from pygame.locals import *
import random


# Setting Up Constants
WINDOW_SIZE = (600, 600)
PIXEL_SIZE = 10


# Helper Functions

# Collision detection function
def collision(pos1, pos2):
    """
    Check if two positions are colliding.

    Parameters:
        pos1 (tuple): Position of the first object.
        pos2 (tuple): Position of the second object.

    Returns:
        bool: True if the positions are equal (colliding), False otherwise.
    """
    return pos1 == pos2  # Returns True if the positions are equal, indicating a collision.


# Boundary Check function
def off_limits(pos):
    """
    Check if a position is within the boundaries of the game window.

    Parameters:
        pos (tuple): Position to check.

    Returns:
        bool: True if the position is off the limits, False if within the limits.
    """
    if 0 <= pos[0] < WINDOW_SIZE[0] and 0 <= pos[1] < WINDOW_SIZE[1]:  # Check if the position is within the window bounds.
        return False  # Position is within the limits.
    else:
        return True  # Position is off the limits.



# Generate a random position for the apple function
def random_on_grid():
    """
    Generate a random position within the grid for the apple.

    Returns:
        tuple: Random position within the grid, aligned to the grid cell size.
    """
    x = random.randint(0, WINDOW_SIZE[0] - PIXEL_SIZE)  # Generate a random x-coordinate within the grid.
    y = random.randint(0, WINDOW_SIZE[1] - PIXEL_SIZE)  # Generate a random y-coordinate within the grid.
    return x // PIXEL_SIZE * PIXEL_SIZE, y // PIXEL_SIZE * PIXEL_SIZE  # Align the coordinates to the grid cell size and return as a tuple.



# Step 4
pygame.init()  # Initialize all imported Pygame modules.
screen = pygame.display.set_mode(WINDOW_SIZE)  # Set the display window size.
pygame.display.set_caption('Snake')  # Set the window title to 'Snake'.

# Step 5
snake_pos = [(250, 50), (260, 50), (270, 50)]  # Initial position of the snake as a list of tuples.
snake_surface = pygame.Surface((PIXEL_SIZE, PIXEL_SIZE))  # Create a surface for the snake of size PIXEL_SIZE x PIXEL_SIZE.
snake_surface.fill((0, 255, 0))  # Fill the snake surface with green color.
snake_direction = K_LEFT  # Initial direction of the snake is left.

apple_surface = pygame.Surface((PIXEL_SIZE, PIXEL_SIZE))  # Create a surface for the apple of size PIXEL_SIZE x PIXEL_SIZE.
apple_surface.fill((255, 0, 0))  # Fill the apple surface with red color.
apple_pos = random_on_grid()  # Place the apple at a random position on the grid.

# Step 6
score = 0  # Initialize the score to zero.
font = pygame.font.SysFont(None, 35)  # Set the font for displaying the score.

def display_score(score):
    score_text = font.render('Score: '+ str(score), True, (255, 255, 255))  # Render the score text in white color.
    screen.blit(score_text, [0, 0])  # Draw the score text on the screen at the top left corner.

# Step 7
def restart_game():
    global snake_pos, apple_pos, snake_direction, score
    snake_pos = [(250, 50), (260, 50), (270, 50)]  # Reset snake position.
    snake_direction = K_LEFT  # Reset snake direction to left.
    apple_pos = random_on_grid()  # Place the apple at a random position on the grid.
    score = 0  # Reset score to zero.

# Step 8
while True:
    pygame.time.Clock().tick(15)  # Control the game speed, 15 frames per second.
    screen.fill((0, 0, 0))  # Fill the screen with black color, effectively clearing it.

    for event in pygame.event.get():
        if event.type == QUIT:  # If the quit event is triggered (window closed), exit the game.
            pygame.quit()  # Uninitialize all Pygame modules.
            quit()  # Exit the program.

        elif event.type == KEYDOWN:  # If a key is pressed down.
            if event.key in [K_UP, K_DOWN, K_LEFT, K_RIGHT]:  # If the key is an arrow key.
                # Change direction only if it's not directly opposite to the current direction.
                if (event.key == K_UP and snake_direction != K_DOWN) or \
                    (event.key == K_DOWN and snake_direction != K_UP) or \
                    (event.key == K_LEFT and snake_direction != K_RIGHT) or \
                    (event.key == K_RIGHT and snake_direction != K_LEFT):
                    snake_direction = event.key  # Update snake direction.

    screen.blit(apple_surface, apple_pos)  # Draw the apple on the screen at its current position.

    # Collisions
    if collision(apple_pos, snake_pos[0]):  # Check if the snake's head collides with the apple.
        snake_pos.append((-10, -10))  # Add a new segment to the snake (initially off-screen).
        apple_pos = random_on_grid()  # Place a new apple at a random position on the grid.
        score += 1  # Increment the score.

    for pos in snake_pos:  # For each segment of the snake.
        screen.blit(snake_surface, pos)  # Draw the segment on the screen.

    for i in range(len(snake_pos) - 1, 0, -1):  # Check for self-collision from the tail towards the head.
        if collision(snake_pos[0], snake_pos[i]):  # If the head collides with any segment.
            restart_game()  # Restart the game.
            break
        snake_pos[i] = snake_pos[i-1]  # Move the segment to the position of the previous segment.

    # Screen limits
    if off_limits(snake_pos[0]):  # Check if the snake's head is outside the screen boundaries.
        restart_game()  # Restart the game.

    # Snake direction update
    if snake_direction == K_UP:  # If the direction is up.
        snake_pos[0] = (snake_pos[0][0], snake_pos[0][1] - PIXEL_SIZE)  # Move the head up by PIXEL_SIZE.
    elif snake_direction == K_DOWN:  # If the direction is down.
        snake_pos[0] = (snake_pos[0][0], snake_pos[0][1] + PIXEL_SIZE)  # Move the head down by PIXEL_SIZE.
    elif snake_direction == K_LEFT:  # If the direction is left.
        snake_pos[0] = (snake_pos[0][0] - PIXEL_SIZE, snake_pos[0][1])  # Move the head left by PIXEL_SIZE.
    elif snake_direction == K_RIGHT:  # If the direction is right.
        snake_pos[0] = (snake_pos[0][0] + PIXEL_SIZE, snake_pos[0][1])  # Move the head right by PIXEL_SIZE.

    display_score(score)  # Display the current score on the screen.
    pygame.display.update()  # Update the display with the new changes.
