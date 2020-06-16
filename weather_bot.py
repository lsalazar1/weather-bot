from sense_hat import SenseHat
from time import sleep
from images import *
import requests

class WeatherBot:
    def __init__(self):
        '''
        Initialize SenseHat object and prompt user welcome message

        @params NONE
        @return NONE
        '''
        self.sense = SenseHat()
        self.name = input('Enter your name: ')

        self.sense.show_message(f'Hello, {self.name}! :)')
        self.sense.set_pixels(face)
        sleep(0.5)
        self.sense.set_pixels(face2)
        sleep(0.5)
        self.sense.clear()

        self.sense.show_message('Use the joystick ')
        sleep(1)
        self.sense.show_message('L - Show room temperature')
        sleep(1)
        self.sense.show_message('R - Show city weather')
        sleep(1)
        self.sense.show_message('D - Exit Program')
        


        