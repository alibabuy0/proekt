import turtle

def draw_heart():
    turtle.fillcolor("red")
    turtle.begin_fill()
    turtle.left(140)
    turtle.forward(180)
    turtle.circle(-90, 200)
    turtle.left(120)
    turtle.circle(-90, 200)
    turtle.forward(180)
    turtle.end_fill()

def write_text():
    turtle.up()
    turtle.goto(0, 50)  # Коригування позиції тексту
    turtle.color("white")
    turtle.write("Малуля, вітаю тебе з твоїм днем!", align="center", font=("Arial", 14, "bold"))
    turtle.goto(0, 20)
    turtle.write("Щоб у тебе все було добре,", align="center", font=("Arial", 14, "bold"))
    turtle.goto(0, -10)
    turtle.write("щоб плече не боліло.", align="center", font=("Arial", 14, "bold"))
    turtle.goto(0, -40)
    turtle.write("Усміхайся частіше – тобі це йде!", align="center", font=("Arial", 14, "bold"))
    turtle.hideturtle()

def main():
    turtle.bgcolor("white")  # Змінено колір фону на білий
    turtle.speed(3)
    turtle.pensize(3)
    turtle.color("red")
    turtle.up()
    turtle.goto(0, -150)
    turtle.down()
    draw_heart()
    write_text()
    turtle.done()

if __name__ == "__main__":
    main()
