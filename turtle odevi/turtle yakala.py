from PIL import Image
import turtle
from random import randint

# Görüntüyü yükle ve yeniden boyutlandır
image_path = r"C:\Users\firdo\Desktop\phyton projects\images - Copy\output-onlinegiftools.gif"
image = Image.open(image_path)
resized_image = image.resize((80, 80))  # Boyutları değiştir, örneğin 100x100 piksel
resized_image_path = r"C:\Users\firdo\Desktop\phyton projects\images - Copy\resized_output.gif"
resized_image.save(resized_image_path)

# Turtle'da yeniden boyutlandırılmış görüntüyü kullan
turtle.register_shape(resized_image_path)
def window():
    win = turtle.Screen()
    win.bgcolor("blue")
    win.title("oyun")
def plyr():
    player = turtle.Turtle()
    player.shape(resized_image_path)
    player.pensize(9)
    player.penup()
    #random yere goturme
    player.goto(randint(-100,0),randint(0,100))

window()
plyr()
turtle.mainloop()
