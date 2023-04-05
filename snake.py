import turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for pos in STARTING_POSITIONS:
            snake = turtle.Turtle()
            snake.shape("square")
            snake.color("white")
            snake.pu()
            snake.goto(pos)
            self.segments.append(snake)

    def move(self):
        for seg_num in range((len(self.segments) - 1), 0, -1):
            x_cor = self.segments[seg_num - 1].xcor()
            y_cor = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(x_cor, y_cor)
        self.segments[0].forward(20)

    def add_segment(self):
        new_seg = turtle.Turtle()
        new_seg.shape("square")
        new_seg.color("white")
        new_seg.pu()
        self.segments.append(new_seg)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
