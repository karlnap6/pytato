import turtle
import time

t = turtle.Turtle()

def draw_shape(lisColors, angle=1):
    for c in lisColors:
        t.color(c)
        t.forward(120)
        t.left(360/angle)
# draw_shape(['red', 'blue', 'yellow'], 3)
# draw_shape(['red', 'blue', 'yellow', 'green'], 4)
# draw_shape(['red', 'blue', 'yellow', 'green', 'purple'], 5)
# draw_shape(['red', 'blue', 'yellow', 'green', 'purple', 'gold'], 6)
# draw_shape(['red', 'blue', 'yellow', 'green', 'purple', 'black', 'gold', 'orange'], 8)

def test_list(color_list, angle):
    for i in range(angle):
        t.color(color_list[i])
        t.forward(100)
        t.left(360/angle)
    # time.sleep(3)
color_list = ['red', 'blue', 'yellow', 'green', 'purple', 'black', 'gold', 'orange']
# test_list(color_list, 3)
# test_list(color_list, 4)
# test_list(color_list, 5)
# test_list(color_list, 6)
# test_list(color_list, 7)
# test_list(color_list, 8)

def draw_star(speed='normal'):
    t.screen.title("Welcome to the turtle zoo!")
    turtle.textinput('Your name: ', 'here')
    # t.title("Welcome to the turtle zoo!")
    t.screen.bgcolor('black')
    t.color('red', 'yellow')
    t.begin_fill()
    t.speed(speed)
    print(turtle.pos(), turtle.position())
    while True:
        t.forward(200)
        t.left(170)
        if abs(t.pos()) < 1:
            break
    t.end_fill()
    turtle.exitonclick()

draw_star(100)