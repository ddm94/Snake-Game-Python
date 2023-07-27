# Import the Turtle Graphics module
import turtle

# Define program constants
WIDTH = 500
HEIGHT = 500
DELAY = 400 # Milliseconds between frame updates

def move_snake():
    stamper.clearstamps() # Remove existing stamps made by stamper.

    new_head = snake[-1].copy()
    new_head[0] += 20

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

stamper = turtle.Turtle()
stamper.shape("square")
stamper.penup()

# Create snake as a list of coordinate pairs
snake = [[0, 0], [20, 0], [40, 0], [60, 0]]

# Set animation in motion
move_snake()

# This statement (or an equivalent) is needed at the end of all your turtle programs.
turtle.done()