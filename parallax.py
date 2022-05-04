import turtle as t
from random import uniform
from random import randint

t.speed(0)
t.screensize(canvwidth = 1800, canvheight = 1600, bg = "black")
star_x = []
star_y = []
star_sizes = []

canvas = t.getcanvas()
x, y = canvas.winfo_pointerx(), canvas.winfo_pointery()

def make_star():
  t.penup()
  star_x_pos = uniform(-900, 900,)
  star_y_pos = uniform(-800, 800)
  t.goto(star_x_pos, star_y_pos)
  t.color("yellow")
  current_star_size = uniform(1, 10)
  t.begin_fill()
  t.circle(current_star_size)
  t.end_fill()
  star_x.append(star_x_pos)
  star_y.append(star_y_pos)
  star_sizes.append(current_star_size)

t.tracer(0, 0)
for i in range(40):
  make_star()
  print(str(i) + ": " + str(t.pos()))
t.update()

while True:
  t.tracer(0, 0)
  t.clear()
  for i in range(len(star_x)):
    star_x[i] += (x-900)/50 * (star_sizes[i]/5)
    if star_x[i] > 900:
      star_x[i] = star_x[i] * -1
    elif star_x[i] < -900:
      star_x[i] = star_x[i] * -1
    t.goto(star_x[i], star_y[i])
    t.begin_fill()
    t.circle(star_sizes[i])
    t.end_fill()
  t.update()
  print(x, y)
  x, y = canvas.winfo_pointerx(), canvas.winfo_pointery()