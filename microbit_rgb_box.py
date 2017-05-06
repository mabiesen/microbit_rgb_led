from microbit import *
import radio


# connect microbit 0,1,2 to r,g,b inputs
# connect ground to ground, volts in to volts in

radio.on()

# here we are going to set the rgb values that produce each color
red = []
lightpink = []
yellow = []
green = []
blue = []
purple = []
orange = []
white = []

my_colors = [red,orange,yellow,green,blue,purple,pink,white]

# current color here is "red" to start.  0 refers to index of above array
# Note: if you are new to programming you should know, lists start at 0 in python ( not 1)
current_color_index = 0

# Setting to slowly move microbit through color range
def color_loop():
  least = 1023
  most = 0
  


# Setting to shift between specific colors
def change_color():
  global current_color_index
  if current_color_index == (len(my_colors)-1):
    current_color_index = 1
  else:
    current_color_index += 1
  turn_on_led(my_colors[current_color_index][0],my_colors[current_color_index][1],my_colors[current_color_index][2])
  

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
  on = 1
  while x < 30:
    turn_on_led(on,on,on)
    crntsleep = (sleepstep**x) * 1000   # 1000 is 1 second
    sleep(crntsleep)
    turn_off_led()
    x = x + 1

def eval_radio(received):
  if rcvd == "flash":
    strobe_loop()
  elif rcvd == "soft":
    color_loop()
  elif rcvd == "change":
    change_color()

while True:
  rcvd = radio.receive()
  if rcvd:
    eval_radio(rcvd)
      
    

