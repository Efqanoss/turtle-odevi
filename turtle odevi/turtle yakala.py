import turtle
image=(r"C:\Users\firdo\Desktop\phyton projects\images - Copy\output-onlinegiftools.gif")
turtle.register_shape(image)


win=turtle.Screen()
win.bgcolor("blue")
win.title("oyun")
player=turtle.Turtle()
player.shape(image)
player.forward(100)


turtle.mainloop()