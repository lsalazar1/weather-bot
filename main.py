from sense_hat import SenseHat
from time import sleep
from images import *

# Represents a sub-key of what data would look like if we used OpenWeather API
# data = [
#   {
#     "weather":{
#         "main": "Clear",
#         "description": "clear sky",
#         "temp": 78
#       }
#   },
#   {
#     "weather": {
#         "main": "Drizzle",
#         "description": "light drizzle",
#         "temp": 65
#       }
#   },
#   {
#     "weather":{
#         "main": "Blizzard",
#         "description": "heavy snow",
#         "temp": -24
#       }
#   }
# ]


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

if __name__ == '__main__':
  sense = SenseHat()
  sense.set_rotation(270)

  name = input('Enter your Name: ')
  sense.show_message("Hi, {}!".format(name))

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
          # x = 1
          # main = data[x]["weather"]["main"]
          # desc = data[x]["weather"]["description"]
          # temp = data[x]["weather"]["temp"]
          # weather_image(main, desc, temp)
          pass
          
        if event.direction == "down":
          sense.show_message("Bye!")
          sleep(0.5)
          sense.clear()
          exit()
      
      sleep(0.5)
      sense.clear()
