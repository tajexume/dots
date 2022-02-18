import colorgram as col
import turtle as t
t.colormode(255)
pic = col.extract('dot.jpg', 20)
tim = t.Turtle()
tim.home()
tim.up()
for dots in range(len(pic)):
  tim.dot(40,pic[dots].rgb)
  tim.forward(40)
  if dots == 4:
    tim.home()
    tim.right(90)
    tim.forward(60)
    tim.left(90)
  elif dots == 9:
    tim.home()
    tim.right(90)
    tim.forward(120)
    tim.left(90)
  elif dots == 14:
    tim.home()
    tim.right(90)
    tim.forward(180)
    tim.left(90) 