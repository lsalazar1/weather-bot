from sense_hat import SenseHat
from time import sleep
from keys import apiKey
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
        self.city = input('Enter city (i.e Houston, Kansas City): ')
        self.state = input('Enter State Code (i.e TX): ')
        self.country = input('Enter Country Code (i.e US, UK): ')

        self.sense.show_message(f'Hello, {self.name}!')
        self.sense.set_pixels(face)
        sleep(0.5)
        self.sense.set_pixels(face2)
        sleep(0.5)
        self.sense.clear()

        self.sense.show_message('Use the joystick ')
        sleep(1)
        self.sense.show_message('L - Show current weather')
        sleep(1)
        self.sense.show_message('D - Exit Program')
    
    def show_currentWeather(self):
        '''
        Shows current weather from user's config variables on
        weather bot.

        @params NONE
        @return NONE
        '''
        response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={self.city},{self.state},{self.country}&appid={apiKey}&units=imperial')
        print(response.json())

    def end_program(self):
        self.sense.show_message('Bye!')
        exit()


        