# Import the Turtle Graphics and random module
import turtle
import random

# Define program constants
WIDTH = 800
HEIGHT = 600
MAX_DELAY = 50
FOOD_SIZE = 20

# Dictionary containing offsets which determine how much the snake moves in each direction.
offsets = {
    "up": (0, 20),
    "down": (0, -20),
    "left": (-20, 0),
    "right": (20, 0)
}

def bind_direction_keys():
    screen.onkey(lambda: set_snake_direction("up"), "Up")
    screen.onkey(lambda: set_snake_direction("down"), "Down")
    screen.onkey(lambda: set_snake_direction("left"), "Left")
    screen.onkey(lambda: set_snake_direction("right"), "Right")

def set_snake_direction(direction):
    global snake_direction

    if direction == "up":
        if snake_direction != "down": # No self-collision simply by pressing wrong key/
            snake_direction = "up"

    elif direction == "down":
        if snake_direction != "up": # No self-collision simply by pressing wrong key/
            snake_direction = "down"

    elif direction == "left":
        if snake_direction != "right": # No self-collision simply by pressing wrong key/
            snake_direction = "left"

    elif direction == "right":
        if snake_direction != "left": # No self-collision simply by pressing wrong key/
            snake_direction = "right"


def game_loop():
    stamper.clearstamps() # Remove existing stamps made by stamper.

    new_head = snake[-1].copy()
    new_head[0] += offsets[snake_direction][0]
    new_head[1] += offsets[snake_direction][1]

    # Check collisions
    # new_head in snake = self collisions
    # new_head[0] < - WIDTH / 2 = X of new head is less than left-hand wall
    # new_head[1] < - HEIGHT / 2 = Y of new head is less than bottom wall
    # We are basically checking the boundaries of the screen
    if new_head in snake or new_head[0] < - WIDTH / 2 or new_head[0] > WIDTH / 2 \
    or new_head[1] < - HEIGHT / 2 or new_head[1] > HEIGHT / 2:
        game_init() # Restart game
    else:
        # Add new head to snake body
        snake.append(new_head)

        # Check food collision
        # Keep the snake the same length unless fed
        if not food_collision():
            # Remove last segment of snake.
            snake.pop(0)

        # Draw snake for the first time.
        for segment in snake:
            # X = segement[0], Y = segment[1]
            stamper.goto(segment[0], segment[1])
            stamper.stamp()
        
        # Refresh screen
        screen.title(f"Snake Game. Score: {score}")
        screen.update()

        # Rinse and repeat
        turtle.ontimer(game_loop, delay)

def food_collision():
    global food_pos, score
    # If the food and the snake's are within 20 pixels of each other
    if get_distance(snake[-1], food_pos) < 20:
        score += 1
        increment_speed()
        food_pos = get_random_food_pos()
        food.goto(food_pos)
        return True
    
    return False

def get_random_food_pos():
    x = random.randint(-WIDTH / 2 + FOOD_SIZE, WIDTH / 2 - FOOD_SIZE)
    y = random.randint(-HEIGHT / 2 + FOOD_SIZE, HEIGHT / 2 - FOOD_SIZE)
    return (x, y) # return x and y as a tuple

# Get distance between two points
def get_distance(pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2
    # Pythagoras' Theorem
    distance = ((y2 - y1) ** 2 + (x2 - x1) ** 2) ** 0.5 # ** 0.5 is the same as taking the square root
    return distance

def increment_speed():
    global delay
    if delay > MAX_DELAY:
        delay -= 10
    
    #print(delay)

def game_init():
    global score, snake, snake_direction, delay, food_pos

    score = 0
    delay = 200
    # Create snake as a list of coordinate pairs
    snake = [[0, 0], [20, 0], [40, 0], [60, 0]]
    snake_direction = "up"

    food_pos = get_random_food_pos()
    food.goto(food_pos)

    game_loop()

# Create window where we will do our drawing
screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT) # Set the dimension of the Turtle Graphics window.
screen.title("Snake")
screen.bgcolor("pink")
screen.tracer(0) # Disable automatic animation

# Event handlers
screen.listen()
# Callback for key press events
bind_direction_keys()

# Snake
stamper = turtle.Turtle()
stamper.shape("circle")
stamper.color("green")
stamper.penup()

# Food
food = turtle.Turtle()
food.shape("circle")
food.color("red")
food.shapesize(FOOD_SIZE / 20)
food.penup()

# Set animation in motion
game_init()

# This statement (or an equivalent) is needed at the end of all your turtle programs.
turtle.done()