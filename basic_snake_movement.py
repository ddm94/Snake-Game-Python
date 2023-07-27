# Import the Turtle Graphics and random module
import turtle
import random

# Define program constants
WIDTH = 500
HEIGHT = 500
DELAY = 100 # Milliseconds between frame updates
FOOD_SIZE = 10

# Dictionary containing offsets which determine how much the snake moves in each direction.
offsets = {
    "up": (0, 20),
    "down": (0, -20),
    "left": (-20, 0),
    "right": (20, 0)
}

def go_up():
    global snake_direction

    # Move up only if we are not already moving down
    if snake_direction != "down":
        snake_direction = "up"

def go_right():
    global snake_direction

    if snake_direction != "left":
        snake_direction = "right"

def go_down():
    global snake_direction

    if snake_direction != "up":
        snake_direction = "down"

def go_left():
    global snake_direction

    if snake_direction != "right":
        snake_direction = "left"


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
        turtle.bye() # Close program
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
        screen.update()

        # Rinse and repeat
        turtle.ontimer(game_loop, DELAY)

def food_collision():
    global food_pos
    # If the food and the snake's are within 20 pixels of each other
    if get_distance(snake[-1], food_pos) < 20:
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

# Create window where we will do our drawing
screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT) # Set the dimension of the Turtle Graphics window.
screen.title("Snake")
screen.bgcolor("pink")
screen.tracer(0) # Disable automatic animation

# Event handlers
screen.listen()
# Callbacks for key press events
screen.onkey(go_up, "Up")
screen.onkey(go_right, "Right")
screen.onkey(go_down, "Down")
screen.onkey(go_left, "Left")

stamper = turtle.Turtle()
stamper.shape("square")
stamper.penup()

# Create snake as a list of coordinate pairs
snake = [[0, 0], [20, 0], [40, 0], [60, 0]]
snake_direction = "up"

# Food
food = turtle.Turtle()
food.shape("circle")
food.color("red")
food.shapesize(FOOD_SIZE / 20)
food.penup()
food_pos = get_random_food_pos()
food.goto(food_pos)

# Set animation in motion
game_loop()

# This statement (or an equivalent) is needed at the end of all your turtle programs.
turtle.done()