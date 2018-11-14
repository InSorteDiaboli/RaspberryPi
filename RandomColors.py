from sense_hat import SenseHat
from random import randint
from time import sleep

sense = SenseHat()


while True:
  red = randint(0,255)
  blue = randint(0,255)
  green = randint(0,255)
  rn = randint(0,7)
  rn2 = randint(0,7)
  sense.set_pixel(rn,rn2,red,blue,green)
  sleep(0.09)
  sense.clear()
  
