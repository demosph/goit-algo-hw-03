import turtle

def koch_curve(turtle, order, size):
    if order == 0:
        turtle.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve(turtle, order-1, size/3)
            turtle.left(angle)

def koch_snowflake(turtle, order, size):
    for _ in range(3):
        koch_curve(turtle, order, size)
        turtle.right(120)

def main():
    # Введення рівня рекурсії від користувача
    recursion_level = int(input("Enter the recursion level for the Koch snowflake: "))

    # Налаштування вікна для малювання
    turtle.speed(0)
    turtle.hideturtle()
    turtle.bgcolor("white")

    # Початкові параметри для сніжинки Коха
    size = 500
    turtle.penup()
    turtle.goto(-size/2, 150)
    turtle.pendown()

    # Малювання сніжинки Коха
    koch_snowflake(turtle, recursion_level, size)

    # Закриття вікна при кліку
    turtle.exitonclick()

if __name__ == "__main__":
    main()