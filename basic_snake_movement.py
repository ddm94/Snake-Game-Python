# Import the Turtle Graphics module
import turtle

# Define program constants
WIDTH = 500
HEIGHT = 500
DELAY = 100 # Milliseconds between frame updates

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


def move_snake():
    stamper.clearstamps() # Remove existing stamps made by stamper.

    new_head = snake[-1].copy()
    new_head[0] += offsets[snake_direction][0]
    new_head[1] += offsets[snake_direction][1]

    # Add new head to snake body
    snake.append(new_head)

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
    turtle.ontimer(move_snake, DELAY)

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

# Set animation in motion
move_snake()

# This statement (or an equivalent) is needed at the end of all your turtle programs.
turtle.done()