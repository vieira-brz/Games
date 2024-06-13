# Imports necessary libraries for the game
import pygame  # Library for creating games in Python
import random  # Library for generating random numbers

# Initializes Pygame for usage
pygame.init()

# Defines the screen dimensions for the game
s_width = 800           # Width of the main game screen
s_height = 700          # Height of the main game screen

# Defines the dimensions of the play area within the main screen
play_width = 300        # Width of the play area (300 pixels)
play_height = 600       # Height of the play area (600 pixels)

# Defines the size of each block that makes up the game
block_size = 30  # Size of each game block in pixels

# Calculates the initial position of the top-left corner of the play area
top_left_x = (s_width - play_width) // 2    # X position of the top-left corner of the play area
top_left_y = s_height - play_height         # Y position of the top-left corner of the play area

# Shape formats
S = [['.....',
      '.....',
      '..00.',
      '.00..',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '...0.',
      '.....']]

Z = [['.....',
      '.....',
      '.00..',
      '..00.',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '.0...',
      '.....']]

I = [['.....',
      '..0..',
      '..0..',
      '..0..',
      '..0..'],
     ['.....',
      '0000.',
      '.....',
      '.....',
      '.....']]

O = [['.....',
      '.....',
      '.00..',
      '.00..',
      '.....']]

J = [['.....',
      '.0...',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..00.',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '...0.',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '.00..',
      '.....']]

L = [['.....',
      '...0.',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '..00.',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '.0...',
      '.....'],
     ['.....',
      '.00..',
      '..0..',
      '..0..',
      '.....']]

T = [['.....',
      '..0..',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '..0..',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '..0..',
      '.....']]

shapes = [S, Z, I, O, J, L, T]  # List of shapes for the pieces
shape_colors = [(0, 255, 0), (255, 0, 0), (0, 255, 255), (255, 255, 0), (255, 165, 0), (0, 0, 255), (128, 0, 128)]  # Corresponding colors for each shape


class Piece(object):
    rows = 20       # Number of rows in the game grid (y-axis)
    columns = 10    # Number of columns in the game grid (x-axis)

    def __init__(self, column, row, shape):
        self.x = column                                     # X position of the piece
        self.y = row                                        # Y position of the piece
        self.shape = shape                                  # Shape of the piece (e.g., S, Z, I, O, J, L, T)
        self.color = shape_colors[shapes.index(shape)]      # Color of the piece based on its shape
        self.rotation = 0                                   # Initial rotation state of the piece



def create_grid(locked_positions={}):
    # Creates a grid filled with black color (0,0,0)
    grid = [[(0, 0, 0) for _ in range(10)] for _ in range(20)]

    # Updates the grid with locked positions
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (j, i) in locked_positions:      # Check if the current position is locked
                c = locked_positions[(j, i)]    # Get the color of the locked position
                grid[i][j] = c                  # Update the grid position with the locked color
    return grid


def convert_shape_format(shape):
    positions = []
    format = shape.shape[shape.rotation % len(shape.shape)]  # Get the current rotation of the shape

    # Convert the shape format to positions
    for i, line in enumerate(format):
        row = list(line)
        for j, column in enumerate(row):
            if column == '0':
                positions.append((shape.x + j, shape.y + i))  # Calculate the position of the shape block

    # Adjust positions based on the shape's offset
    for i, pos in enumerate(positions):
        positions[i] = (pos[0] - 2, pos[1] - 4)  # Offset adjustment for the shape's position

    # Return the list of positions representing the current shape
    return positions  



def valid_space(shape, grid):
    # Generates a list of all positions that are currently accepted (black squares) in the grid
    accepted_positions = [[(j, i) for j in range(10) if grid[i][j] == (0, 0, 0)] for i in range(20)]
    accepted_positions = [j for sub in accepted_positions for j in sub]  # Flattens the list

    formatted = convert_shape_format(shape)  # Converts the shape format to positions

    # Checks if each position of the current shape is valid (falls within accepted positions)
    for pos in formatted:
        if pos not in accepted_positions:   # If the position is not in accepted positions
            if pos[1] > -1:                 # Checks if the position is above the top boundary of the grid
                return False                # Returns False indicating invalid space
    return True                             # Returns True indicating valid space


def check_lost(positions):
    # Checks if any of the given positions indicate that the game is lost (piece above the top boundary)
    for pos in positions:
        x, y = pos
        if y < 1:           # If the y-coordinate of the position is less than 1 (above the top boundary)
            return True     # Returns True indicating the game is lost
    return False            # Returns False indicating the game is not lost



def get_shape():
    # Returns a new Piece object with a random shape at the top center of the grid
    return Piece(5, 0, random.choice(shapes))


def draw_text_middle(text, size, color, surface):
    # Draws text in the middle of a given surface
    font = pygame.font.Font(pygame.font.get_default_font(), size)
    label = font.render(text, 1, color)

    # Calculates the center position for the text
    surface.blit(label, (top_left_x + play_width / 2 - (label.get_width() / 2),
                         top_left_y + play_height / 2 - (label.get_height() / 2)))


def draw_grid(surface, grid):
    # Draws the grid lines on the given surface
    sx = top_left_x
    sy = top_left_y

    # Draws horizontal lines
    for i in range(len(grid)):
        pygame.draw.line(surface, (128, 128, 128), (sx, sy + i * block_size), (sx + play_width, sy + i * block_size))
        
        # Draws vertical lines
        for j in range(len(grid[i])):
            pygame.draw.line(surface, (128, 128, 128), (sx + j * block_size, sy), (sx + j * block_size, sy + play_height))


def clear_rows(grid, locked):
    # Variable to count the number of rows cleared
    increment = 0
    
    # Iterate through the grid from bottom to top
    for i in range(len(grid) - 1, -1, -1):
        row = grid[i]
        # Check if there are no empty spaces (black squares) in the row
        if (0, 0, 0) not in row:
            increment += 1  # Increment the row clear count
            ind = i  # Store the index of the cleared row
            # Remove the locked positions from the dictionary
            for j in range(len(row)):
                try:
                    del locked[(j, i)]
                except:
                    continue

    # If rows were cleared, update the positions in the locked dictionary
    if increment > 0:
        for key in sorted(list(locked), key=lambda x: x[1])[::-1]:
            x, y = key
            if y < ind:
                newKey = (x, y + increment)
                locked[newKey] = locked.pop(key)

    return increment  # Return the number of rows cleared


def draw_next_shape(shape, surface):
    # Font and label for the "Next Shape" text
    font = pygame.font.Font(pygame.font.get_default_font(), 30)
    label = font.render('Next Shape', 1, (255, 255, 255))

    # Coordinates for drawing the next shape preview
    sx = top_left_x + play_width + 50
    sy = top_left_y + (play_height / 2 - 100)

    # Get the current rotation format of the shape
    format = shape.shape[shape.rotation % len(shape.shape)]

    # Draw the next shape preview on the surface
    for i, line in enumerate(format):
        row = list(line)
        for j, column in enumerate(row):
            if column == '0':
                pygame.draw.rect(surface, shape.color,
                                 (sx + j * block_size, sy + i * block_size, block_size, block_size), 0)

    # Draw the "Next Shape" label on the surface
    surface.blit(label, (sx + 10, sy - 30))


def draw_window(surface, grid, score=0, level=0):
    # Fill the surface with black
    surface.fill((0, 0, 0))

    # Initialize and render the "Tetris" title
    pygame.font.init()
    font = pygame.font.Font(pygame.font.get_default_font(), 60)
    label = font.render('Tetris', 1, (255, 255, 255))

    # Draw the "Tetris" title in the middle of the play area
    surface.blit(label, (top_left_x + play_width / 2 - (label.get_width() / 2), 30))

    # Render and draw the score and level information
    font = pygame.font.Font(pygame.font.get_default_font(), 30)
    label = font.render('Score: ' + str(score), 1, (255, 255, 255))
    sx = top_left_x + play_width + 50
    sy = top_left_y + (play_height / 2 - 100)
    surface.blit(label, (sx + 20, sy + 160))

    label = font.render('Level: ' + str(level), 1, (255, 255, 255))
    surface.blit(label, (sx + 20, sy + 200))

    # Draw the game grid on the surface
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            pygame.draw.rect(surface, grid[i][j],
                             (top_left_x + j * block_size, top_left_y + i * block_size, block_size, block_size), 0)

    # Draw the grid lines
    draw_grid(surface, grid)

    # Draw the boundary around the play area
    pygame.draw.rect(surface, (255, 0, 0), (top_left_x, top_left_y, play_width, play_height), 5)


def main():
    # Initialize variables for the game
    locked_positions = {}
    grid = create_grid(locked_positions)
    change_piece = False
    run = True
    current_piece = get_shape()
    next_piece = get_shape()
    clock = pygame.time.Clock()
    fall_time = 0
    level_time = 0
    score = 0
    level = 0
    fall_speed = 0.27

    while run:
        # Refresh the game grid and update time variables
        grid = create_grid(locked_positions)
        fall_time += clock.get_rawtime()
        level_time += clock.get_rawtime()
        clock.tick()

        # Increase difficulty level over time
        if level_time / 1000 > 5:
            level_time = 0
            if fall_speed > 0.12:
                fall_speed -= 0.005
                level += 1

        # Move the current piece down automatically based on fall speed
        if fall_time / 1000 >= fall_speed:
            fall_time = 0
            current_piece.y += 1
            # If the piece cannot move down further, lock it in place
            if not (valid_space(current_piece, grid)) and current_piece.y > 0:
                current_piece.y -= 1
                change_piece = True

        # Handle user input events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.display.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                # Move the current piece left, right, down, or rotate based on key press
                if event.key == pygame.K_LEFT:
                    current_piece.x -= 1
                    if not valid_space(current_piece, grid):
                        current_piece.x += 1
                if event.key == pygame.K_RIGHT:
                    current_piece.x += 1
                    if not valid_space(current_piece, grid):
                        current_piece.x -= 1
                if event.key == pygame.K_DOWN:
                    current_piece.y += 1
                    if not valid_space(current_piece, grid):
                        current_piece.y -= 1
                if event.key == pygame.K_UP:
                    current_piece.rotation = current_piece.rotation + 1 % len(current_piece.shape)
                    if not valid_space(current_piece, grid):
                        current_piece.rotation = current_piece.rotation - 1 % len(current_piece.shape)

        # Convert the current piece shape to grid positions and update the grid
        shape_pos = convert_shape_format(current_piece)
        for i in range(len(shape_pos)):
            x, y = shape_pos[i]
            if y > -1:
                grid[y][x] = current_piece.color

        # Check if the piece has landed and lock it in place
        if change_piece:
            for pos in shape_pos:
                p = (pos[0], pos[1])
                locked_positions[p] = current_piece.color
            current_piece = next_piece
            next_piece = get_shape()
            change_piece = False
            score += clear_rows(grid, locked_positions) * 10  # Increase score based on cleared rows

        # Draw the game window with updated grid, score, and level
        draw_window(win, grid, score, level)
        draw_next_shape(next_piece, win)
        pygame.display.update()

        # Check if the game is lost and display "YOU LOST" message
        if check_lost(locked_positions):
            run = False
            draw_text_middle("YOU LOST", 80, (255, 255, 255), win)
            pygame.display.update()
            pygame.time.delay(1500)
            pygame.quit()


def main_menu():
    run = True
    while run:
        win.fill((0, 0, 0))
        draw_text_middle('Press Any Key To Play', 60, (255, 255, 255), win)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                main()
    pygame.quit()


# Initialize the Pygame window and start the main menu loop
win = pygame.display.set_mode((s_width, s_height))
pygame.display.set_caption('Tetris')
main_menu()
