import turtle


def koch_segment(t: turtle.Turtle, length: float, level: int):
    if level == 0:
        t.forward(length)
        return

    length /= 3
    koch_segment(t, length, level - 1)
    t.left(60)
    koch_segment(t, length, level - 1)
    t.right(120)
    koch_segment(t, length, level - 1)
    t.left(60)
    koch_segment(t, length, level - 1)


def draw_koch_snowflake(level: int):
    screen = turtle.Screen()
    screen.setup(width=800, height=800)
    screen.title(f"Сніжинка Коха, рівень {level}")

    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(-250, 150)
    t.pendown()

    length = 500
    for _ in range(3):
        koch_segment(t, length, level)
        t.right(120)

    t.hideturtle()
    screen.mainloop()


def main():
    level_str = input("Введи рівень рекурсії (0–6): ")
    try:
        level = int(level_str)
    except ValueError:
        print("Потрібно ввести ціле число.")
        return

    if level < 0:
        print("Рівень рекурсії має бути невід'ємним.")
        return

    draw_koch_snowflake(level)


if __name__ == "__main__":
    main()