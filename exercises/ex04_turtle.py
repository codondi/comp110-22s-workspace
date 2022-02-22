"""Night sky using Turtle Graphics."""

__author__ = "730449161"

from turtle import Turtle, colormode, done

colormode(255)


def draw_night_sky(x: float, y: float) -> None:
    """Draws a dark blue night sky."""
    leo: Turtle = Turtle()
    leo.penup()
    leo.goto(x, y)
    leo.pendown()
    leo.fillcolor(17, 3, 62)
    leo.begin_fill()
    i: int = 0
    while i < 4:
        leo.forward(800)
        leo.left(90)
        i += 1
    leo.end_fill()


def draw_one_star(x: float, y: float) -> None:
    """Draws one filled in star."""
    star: Turtle = Turtle()
    star.fillcolor(237, 241, 96)
    star.penup()
    star.goto(x, y)
    star.pendown()
    i: int = 0
    star.begin_fill()
    while i < 5:
        star.forward(50)
        star.left(324)
        star.forward(50)
        star.left(108)
        i += 1
    star.end_fill()


def draw_stars(x: float, y: float) -> None:
    """Draws three filled in stars."""
    j: int = 0
    z: float = x
    while j < 3:
        draw_one_star(z, y)
        z = z + 150
        j += 1


def draw_pavement(x: float, y: float) -> None:
    """Draws pavement."""
    pave: Turtle = Turtle()
    pave.fillcolor(181, 183, 190)
    pave.penup()
    pave.goto(x, y)
    pave.pendown()
    k: int = 0
    pave.begin_fill()
    while k < 2:
        pave.forward(800)
        pave.left(90)
        pave.forward(100)
        pave.left(90)
        k += 1
    pave.end_fill()


def draw_firefly(fly: Turtle, x: float, y: float) -> None:
    """Draws, a firefly on coordinate (x, y)."""
    j: int = 0
    i: int = 0
    fly.fillcolor(243, 101, 37)
    fly.penup()
    fly.goto(x, y)
    fly.pendown()
    fly.begin_fill()
    while j < 4:
        fly.forward(30)
        fly.left(90)
        j += 1
        y += 5
    fly.end_fill()
    fly.penup()
    fly.goto(x, y)
    fly.pendown()
    fly.fillcolor(77, 44, 34)
    fly.begin_fill()
    while i < 2:
        fly.forward(30)
        fly.left(90)
        fly.forward(50)
        fly.left(90)
        i += 1
    fly.end_fill()


def main() -> None:
    """Compiles the mini-functions to create an image of a night sky."""
    draw_night_sky(-400, -400)
    draw_pavement(-400, -400)
    draw_stars(-200, 200)
    draw_firefly(Turtle(), 60, 0)
    done()


if __name__ == "__main__":
    main()