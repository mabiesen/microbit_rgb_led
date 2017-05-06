from microbit import *
import radio

radio.on()


red = 0
blue = 0
green = 0


red = []
lightpink = []
yellow = []
green = []
blue = []
purple = []
orange = []
white = []

my_colors = [red,orange,yellow,green,blue,purple,lightpink,white]
current_color = white

# Setting to slowly move microbit through color range
def color_loop():


# Setting to shift between specific colors
def change_color():

# turn it off
def turn_off_led():
  off = 1023
  pin0.write_analog(off)
  pin1.write_analog(off)
  pin2.write_analog(off)
  
# turn it on, providing
def turn_on_led(r,g,b):
  pin0.write_analog(r)
  pin1.write_analog(g)
  pin2.write_analog(b)
  


# Setting to flash, slow to so fast its constant
def strobe_loop():
  x = 1
  sleepstep = 0.9
  while x < 30:
    on = 1
    turn_on_led(on,on,on)
    crntsleep = (sleepstep**x) * 1000   # 1000 is 1 second
    sleep(crntsleep)
    turn_off_led()
    x = x + 1
    



while True:
  rcvd = radio.receive()
  if rcvd:
    if rcvd == "flash":
      strobe_loop()
    elif rcvd == "soft":
      color_loop()
    elif rcvd == "hard":
      
    

