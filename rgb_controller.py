# Since the rgb microbit is in the box, lets control it with another microbit
from microbit import *
import radio

radio.on()

options = ["flash","change"]
crnt_option = 0

def change_crnt_option():
  global crnt_option
  if crnt_option = (len(options)-1):
    crnt_option = 0
  elif:
    crnt_option += 1

while True:
  display.scroll(options[crnt_option])
  if button_a.was_pressed():
    change_crnt_option()
  if button_b.was_pressed():
    radio.send(options[crnt_option])
  
