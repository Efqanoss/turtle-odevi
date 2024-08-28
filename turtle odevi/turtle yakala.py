from PIL import Image
import turtle
from random import randint
import time
import os

# Görüntüyü yükle ve yeniden boyutlandır
directory=os.path.dirname(os.path.abspath(__file__))
image_path=os.path.join(directory,"images (turtle)","output-onlinegiftools.gif")
image = Image.open(image_path)
resized_image = image.resize((80, 80))  # Boyutları değiştir, örneğin 80x80 piksel

resized_image_path=os.path.join(directory,"images (turtle)","resized_output.gif")
resized_image.save(resized_image_path)

# Turtle'da yeniden boyutlandırılmış görüntüyü kullan
turtle.register_shape(resized_image_path)

# Global skor değişkeni
score_value = 0

def update_score():
    """Skoru güncelle ve ekranda göster."""
    global score_value
    score_value += 1
    score.clear()
    score.write(f"SOCCER: {score_value}", align="center", font=("Arial", 24))

def window():
    win = turtle.Screen()
    win.screensize(200, 200)
    win.bgcolor("blue")
    win.title("oyun")

def plyr():
    player = turtle.Turtle()
    player.shape(resized_image_path)
    player.pensize(9)
    player.penup()

    def on_click(x, y):
        update_score()

    player.onclick(on_click)

    # random yere goturme
    for i in range(10):
        player.goto(randint(-300, 300), randint(-300, 300))
        time.sleep(1)

def score_board():
    global score
    score = turtle.Turtle()
    score.hideturtle()
    score.penup()
    score.goto(0, 290)
    score.pendown()
    score.write("SOCCER: 0", align="center", font=("Arial", 24))

window()
score_board()
plyr()
turtle.mainloop()
