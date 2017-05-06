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

my_colors = [red,orange,yellow,green,blue,purple,lightpink]

# Setting to slowly move microbit through color range
def color_loop():


# Setting to shift between specific colors
def change_color():


# Setting to flash, slow to so fast its constant
def strobe_loop():
  x = 1
  sleepstep = 0.9
  
  while x < 30:
    
    crntsleep = (sleepstep**x) * 1000   # 1000 is 1 second
    sleep(crntsleep)
    x = x + 1
    



while True:
  rcvd = radio.receive()
  if rcvd:
    if rcvd == "flash":
      strobe_loop()
    elif rcvd == "soft":
      color_loop()
    elif rcvd == "hard":
      
    

