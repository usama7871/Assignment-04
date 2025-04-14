"""
Interactive Canvas Eraser (No External Libraries)
-----------------------------------------------
This program creates a grid of blue cells on a canvas and implements
a pink eraser that turns cells white when dragged over them, using only
Python's built-in turtle module.

Key Features:
- Uses only standard library (turtle)
- Grid creation using nested loops
- Mouse interaction tracking
- Object collision detection
- Real-time canvas updating
"""

import turtle

# Constants for canvas and cell sizes
CANVAS_WIDTH = 400      # Width of the drawing canvas
CANVAS_HEIGHT = 400     # Height of the drawing canvas
CELL_SIZE = 40          # Size of each grid cell
ERASER_SIZE = 20        # Size of the eraser square

class Cell:
    """Represents a single cell in the grid"""
    def __init__(self, x, y, size, color):
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.drawn = False
        self.turtle = None

    def draw(self):
        """Draw the cell on screen"""
        if not self.drawn:
            t = turtle.Turtle()
            t.speed(0)
            t.hideturtle()
            t.penup()
            t.goto(self.x, self.y)
            t.pendown()
            t.fillcolor(self.color)
            t.begin_fill()
            for _ in range(4):
                t.forward(self.size)
                t.right(90)
            t.end_fill()
            self.turtle = t
            self.drawn = True
        else:
            self.turtle.clear()
            self.turtle.fillcolor(self.color)
            self.turtle.begin_fill()
            for _ in range(4):
                self.turtle.forward(self.size)
                self.turtle.right(90)
            self.turtle.end_fill()

def setup_canvas():
    """Set up the turtle canvas"""
    screen = turtle.Screen()
    screen.setup(CANVAS_WIDTH, CANVAS_HEIGHT)
    screen.title("Canvas Eraser")
    screen.tracer(0)  # Turn off animation for instant drawing
    return screen

def create_grid(screen):
    """Create the grid of blue cells"""
    cells = []
    num_rows = CANVAS_HEIGHT // CELL_SIZE
    num_cols = CANVAS_WIDTH // CELL_SIZE
    
    for row in range(num_rows):
        for col in range(num_cols):
            x = col * CELL_SIZE - CANVAS_WIDTH//2 + CELL_SIZE//2
            y = CANVAS_HEIGHT//2 - CELL_SIZE//2 - row * CELL_SIZE
            cell = Cell(x, y, CELL_SIZE, 'blue')
            cell.draw()
            cells.append(cell)
    
    screen.update()
    return cells

def create_eraser():
    """Create the eraser turtle"""
    eraser = turtle.Turtle()
    eraser.shape('square')
    eraser.shapesize(ERASER_SIZE/20, ERASER_SIZE/20)  # turtle size is in units of 20px
    eraser.color('pink')
    eraser.penup()
    return eraser

def check_collision(eraser, cell):
    """Check if eraser overlaps with a cell"""
    eraser_x, eraser_y = eraser.pos()
    return (abs(eraser_x - cell.x) < (ERASER_SIZE + CELL_SIZE)/2 and
            abs(eraser_y - cell.y) < (ERASER_SIZE + CELL_SIZE)/2)

def main():
    """Main function that sets up and runs the eraser simulation"""
    screen = setup_canvas()
    cells = create_grid(screen)
    eraser = create_eraser()
    
    def move_eraser(x, y):
        """Move eraser to mouse position and handle collisions"""
        eraser.goto(x, y)
        for cell in cells:
            if check_collision(eraser, cell) and cell.color != 'white':
                cell.color = 'white'
                cell.draw()
        screen.update()
    
    screen.onclick(lambda x, y: None)  # Dummy click handler
    screen.onscreenclick(move_eraser, btn=1, add=True)  # Left mouse button
    screen.listen()
    
    print("Click and drag the mouse to erase cells")
    turtle.done()

if __name__ == '__main__':
    main()