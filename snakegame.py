import turtle
import random
import time

# Initial delay (higher value for slower start)
delay = 0.15

# Create screen
wn = turtle.Screen()
wn.bgcolor('lightBlue')
wn.title('Anaconda Game by Gowtham')
wn.setup(width=600, height=600)
wn.tracer(0)

# Score
score = 0
pen = turtle.Turtle()
pen.color('Blue')
pen.speed(0)
pen.penup()
pen.goto(0, 260)
pen.hideturtle()
pen.write(f'SCORE: {score}', align='center', font='Arial')

# Snake head
head = turtle.Turtle()
head.shape('turtle')
head.color('red')
head.speed(0)
head.penup()
head.goto(0, 0)
head.direction = 'stop'

# Snake food
food = turtle.Turtle()
food.shape('circle')
food.color('Green')
food.speed(0)
food.penup()
food.goto(random.randint(-290, 290), random.randint(-290, 290))


def move():
    if head.direction == 'Up':
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == 'Down':
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == 'Right':
        x = head.xcor()
        head.setx(x + 20)

    if head.direction == 'Left':
        x = head.xcor()
        head.setx(x - 20)


def go_up():
    if head.direction != 'Down':
        head.direction = 'Up'


def go_down():
    if head.direction != 'Up':
        head.direction = 'Down'


def go_right():
    if head.direction != 'Left':
        head.direction = 'Right'


def go_left():
    if head.direction != 'Right':
        head.direction = 'Left'


wn.listen()
wn.onkeypress(go_up, 'Up')
wn.onkeypress(go_down, 'Down')
wn.onkeypress(go_right, 'Right')
wn.onkeypress(go_left, 'Left')

body = []

while True:
    wn.update()

    # Check for collision with the wall
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        head.goto(0, 0)
        head.direction = 'stop'
        for segment in body:
            segment.goto(1000, 1000)
        body.clear()
        score = 0
        delay = 0.15  # Reset delay to initial value
        pen.clear()
        pen.write(f'SCORE: {score}', align='center', font='Arial')

    # Check for collision with the food
    if head.distance(food) < 20:
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        # Increase the score
        score += 1
        delay *= 0.95  # Decrease delay by 5% to increase speed
        pen.clear()
        pen.write(f'SCORE: {score}', align='center', font='Arial')

        # Add a new body segment
        new_body = turtle.Turtle()
        new_body.shape('square')
        new_body.color('Black')
        new_body.speed(0)
        new_body.penup()
        body.append(new_body)

    # Move the body segments in reverse order
    for i in range(len(body) - 1, 0, -1):
        x = body[i - 1].xcor()
        y = body[i - 1].ycor()
        body[i].goto(x, y)

    # Move the first segment to the head's position
    if len(body) > 0:
        x = head.xcor()
        y = head.ycor()
        body[0].goto(x, y)

    move()

    # Check for collision with the body
    for segment in body:
        if segment.distance(head) < 20:
            head.goto(0, 0)
            head.direction = 'stop'
            for segment in body:
                segment.goto(1000, 1000)
            body.clear()
            score = 0
            delay = 0.15  # Reset delay to initial value
            pen.clear()
            pen.write(f'SCORE: {score}', align='center', font='Arial')

    time.sleep(delay)

wn.mainloop()
