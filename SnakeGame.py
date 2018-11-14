from sense_hat import SenseHat
from random import randint
from time import sleep

sense = SenseHat()

white = (255,255,255)
blank = (0, 0, 0)
slug = [ [2,4], [3,4], [4,4] ]
direction = "right"
direction = "left"
direction = "up"
direction = "down"


def drawslug():
  for segment in slug:
    sense.set_pixel(segment[0], segment[1], white)
    
def move():
  last = slug[-1]
  first = slug[0]
  #Create a copy of the last item
  next = list(last)
  if direction == "right":
    if last[0]+1==8:
      next[0]=0
    else:
      next[0]=last[0]+1
      
  elif direction == "left":
    if last[0]-1==-1:
      next[0]=7
    else:
      next[0]=last[0]-1
      
  elif direction == "down":
    if last[1]+1==8:
      next[1]=0
    else:
      next[1]=last[1]+1
      
  elif direction == "up":
    if last[1]-1==-1:
      next[1]=7
    else:
      next[1]=last[1]-1
  slug.append(next)
  
  sense.set_pixel(next[0],next[1],white)
  sense.set_pixel(first[0], first[1], blank)
  slug.remove(first)
  
def joystick_moved(event):
  global direction
  direction = event.direction
  
while True:    
  sense.clear()
  drawslug()
  sense.stick.direction_any = joystick_moved
  move()
  sleep(0.5)
