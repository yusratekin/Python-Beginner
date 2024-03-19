import turtle

drawing_board = turtle.Screen()
drawing_board.bgcolor("light blue")
drawing_board.title("Turtle Drawing")

turtle_instance = turtle.Turtle()

def turtle_forward():
    turtle_instance.forward(10)

def rotate_angle_right():
    turtle_instance.right(10)

def rotate_angel_left():
    turtle_instance.left(10)

def clear_screen():
    turtle_instance.clear()

def turtle_return_home():
    turtle_instance.home()

def turtle_pen_up():
    turtle_instance.penup()

def turtle_pen_down():
    turtle_instance.pendown()


drawing_board.listen()
drawing_board.onkey(fun=turtle_forward,key="space")
drawing_board.onkey(fun=rotate_angle_right, key="Down")
drawing_board.onkey(fun=rotate_angel_left, key="Up")
drawing_board.onkey(fun=clear_screen, key="s")
drawing_board.onkey(fun=turtle_return_home, key="h")
drawing_board.onkey(fun=turtle_pen_up, key="b")
drawing_board.onkey(fun=turtle_pen_down, key="a")


turtle.mainloop()