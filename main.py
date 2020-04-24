from sense_hat import SenseHat
from time import sleep

# Represents a sub-key of what data would look like if we used OpenWeather API
data = [
  {
    "weather":{
        "main": "Clear",
        "description": "clear sky",
        "temp": 78
      }
  },
  {
    "weather": {
        "main": "Drizzle",
        "description": "light drizzle",
        "temp": 65
      }
  },
  {
    "weather":{
        "main": "Blizzard",
        "description": "heavy snow",
        "temp": -24
      }
  }
]


def weather_image(x, y, z):
  '''
  When this function is called, an animation will be chosen from x. Additional
  information will also be shown.
  
  @params x is main weather. y is general decription. z is temperature.
  '''
  
  # Append Farenheit(F) to temp
  z = "{}F".format(z) 
  
  # Each animation will run twice before starting statements at line 67
  if x == "Clear":
    for x in range(0,2):
      sense.set_pixels(clear_skies)
      sleep(0.5)
      sense.set_pixels(clear_skies2)
      sleep(0.5)
      sense.set_pixels(clear_skies3)
      sleep(0.5)
      sense.set_pixels(clear_skies4)
      sleep(0.5)
  elif x == "Drizzle":
    for x in range(0,2):
      sense.set_pixels(drizzle)
      sleep(0.5)
      sense.set_pixels(drizzle2)
      sleep(0.5)
  elif x == "Blizzard":
    for x in range(0,2):
      sense.set_pixels(blizzard)
      sleep(0.5)
      sense.set_pixels(blizzard2)
      sleep(0.5)
      sense.set_pixels(blizzard3)
      sleep(0.5)
  sense.show_message(y)
  sense.show_message(z)

# These are commonly used tuple values for RBG colors
b = (0,0,255)
w = (255,255, 255)
y = (255, 255, 0)
g = (0, 255, 0)
lb = (173, 216, 230)
bk = (0, 0, 0)
gr = (134, 136, 138)

# Lines 78-198 are RGB values for LED Matrix
drizzle = [
  bk, bk, bk, bk, bk, y, y, y,
  bk, bk, w, w, w, w, y, y,
  bk, w, w, w, w, w, w, y,
  w, w, w, w, w, w, w, w,
  lb, bk, lb, bk, lb, bk, lb, bk,
  bk, lb, bk, lb, bk, lb, bk, lb,
  lb, bk, lb, bk, lb, bk, lb, bk,
  g, g, g, g, g, g, g, g,
]

drizzle2 = [
  bk, bk, bk, bk, bk, y, y, y,
  bk, bk, w, w, w, w, y, y,
  bk, w, w, w, w, w, w, y,
  w, w, w, w, w, w, w, w,
  bk, lb, bk, lb, bk, lb, bk, lb,
  lb, bk, lb, bk, lb, bk, lb, bk,
  bk, lb, bk, lb, bk, lb, bk, lb,
  g, g, g, g, g, g, g, g,
]

clear_skies = [
  b, b, b, b, b, y, y, y,
  b, b, b, b, b, y, y, y,
  b, b, b, b, b, y, y, y,
  b, b, b, b, b, b, b, b,
  b, b, b, b, b, b, b, b,
  b, b, b, b, b, b, b, b,
  b, b, b, b, b, b, b, b,
  g, g, g, g, g, g, g, g
]

clear_skies2 = [
  b, b, b, b, b, y, y, y,
  w, w, b, b, b, y, y, y,
  w, w, b, b, b, y, y, y,
  b, b, b, b, b, b, b, b,
  b, b, b, b, b, b, b, b,
  b, b, b, b, b, b, b, b,
  b, b, b, b, b, b, b, b,
  g, g, g, g, g, g, g, g
]

clear_skies3 = [
  b, b, b, b, b, y, y, y,
  b, b, w, w, b, y, y, y,
  b, b, w, w, b, y, y, y,
  b, b, b, b, b, b, b, b,
  b, b, b, b, b, b, b, b,
  b, b, b, b, b, b, b, b,
  b, b, b, b, b, b, b, b,
  g, g, g, g, g, g, g, g
]

clear_skies4 = [
  b, b, b, b, b, y, y, y,
  b, b, b, b, w, w, y, y,
  b, b, b, b, w, w, y, y,
  b, b, b, b, b, b, b, b,
  b, b, b, b, b, b, b, b,
  b, b, b, b, b, b, b, b,
  b, b, b, b, b, b, b, b,
  g, g, g, g, g, g, g, g
]

blizzard = [
  gr, gr, gr, gr, gr, gr, gr, gr,
  w, b, w, b, w, b, w, b,
  b, b, b, b, b, b, b, b,
  b, b, b, b, b, b, b, b,
  b, b, b, b, b, b, b, b,
  b, b, b, b, b, b, b, b,
  b, b, b, b, b, b, b, b,
  g, g, g, g, g, g, g, g
]

blizzard2 = [
  gr, gr, gr, gr, gr, gr, gr, gr,
  b, w, b, w, b, w, b, w,
  w, b, w, b, w, b, w, b,
  b, w, b, w, b, w, b, w,
  w, b, w, b, w, b, w, b,
  b, w, b, w, b, w, b, w,
  b, b, b, b, b, b, b, b,
  w, g, g, w, g, g, w, w
]

blizzard3 =[
  gr, gr, gr, gr, gr, gr, gr, gr,
  w, b, w, b, w, b, w, b,
  b, w, b, w, b, w, b, w,
  w, b, w, b, w, b, w, b,
  b, w, b, w, b, w, b, w,
  w, b, w, b, w, b, w, b,
  w, w, w, w, w, w, w, w,
  w, w, w, w, w, w, w, w
]

face = [
  b, b, b, b, b, b, b, b,
  b, w, w, b, b, w, w, b,
  b, w, w, b, b, w, w, b,
  b, b, b, b, b, b, b, b,
  w, w, b, b, b, b, w, w,
  w, w, b, b, b, b, w, w,
  b, b, w, w, w, w, b, b,
  b, b, w, w, w, w, b, b
]

face2 = [
  b, b, b, b, b, b, b, b,
  b, w, w, b, b, w, w, b,
  b, w, w, b, b, w, w, b,
  b, b, b, b, b, b, b, b,
  w, w, w, w, w, w, w, w,
  w, w, w, w, w, w, w, w,
  b, w, w, w, w, w, w, b,
  b, b, w, w, w, w, b, b
]

sense = SenseHat()
sense.set_rotation(270)

name = input('Enter your Name: ')
sense.show_message("Hi {}!".format(name))

sense.set_pixels(face)
sleep(0.5)
sense.set_pixels(face2)
sleep(0.5)
sense.clear()

sense.show_message("Use the joystick")
sense.show_message("L - Room Temp")
sense.show_message("R - City Weather")
sense.show_message("D - Off")


while True:
  '''
  Based on the joystick direction, it will either display the room's
  temperature, display cities current temp, or end the program.
  '''
  for event in sense.stick.get_events():
    if event.action == 'pressed':
      if event.direction == 'left':
        temp = int((sense.get_temperature() * 9/5) + 32)
        msg = "{}F".format(temp)
        sense.show_message(msg)
        
      if event.direction == 'right':
        x = 1
        main = data[x]["weather"]["main"]
        desc = data[x]["weather"]["description"]
        temp = data[x]["weather"]["temp"]
        weather_image(main, desc, temp)
        
      if event.direction == "down":
        sense.show_message("Bye!")
        sleep(0.5)
        sense.clear()
        exit()
    
    sleep(0.5)
    sense.clear()
