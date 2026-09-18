import turtle
import math

screen = turtle.Screen()
screen.setup(width=850, height=700)
screen.bgcolor("black")

t = turtle.Turtle()
t.speed(1)
t.hideturtle()
t.penup()

# Different shades of pink
pink_colors = [
    "#ffb6c1",
    "#ff91a4",
    "#ff69b4",
    "#ff4f81",
    "#ff1493",
    "#ff007f"
]

for scale in range(15, 26):
    for i in range(120):

        # Change color for each "I love you"
        t.color(pink_colors[i % len(pink_colors)])

        angle = i * (math.pi * 2) / 120

        x = 16 * (math.sin(angle) ** 3) * scale

        y = (13 * math.cos(angle)
             - 5 * math.cos(2 * angle)
             - 2 * math.cos(3 * angle)
             - math.cos(4 * angle)) * scale

        t.goto(x, y)

        t.write(
            "I love you",
            align="center",
            font=("Arial", 12, "bold")
        )

turtle.done()