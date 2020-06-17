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

        self.sense.show_message('Use the joystick')
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

        # HTTP GET to OpenWeather, then convert response to json
        response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={self.city},{self.state},{self.country}&appid={apiKey}&units=imperial').json()
        temp = int(round(response['main']['temp'], 0))
        feelsLike = int(round(response['main']['feels_like'], 0))
        humidity = response['main']['humidity']


        self.get_animation(response['weather'][0]['main'])

        self.sense.show_message(f'Temperature: {temp}F')
        sleep(1)
        self.sense.show_message(f'Feels Like: {feelsLike}F')
        sleep(1)
        self.sense.show_message(f'Humidity: {humidity}%')


        
    def get_animation(self, weather):
        '''
        This method gets the proper animation based on the given weather. The animation repeats 
        four times.

        @params weather:comes from api response
        @return NONE
        '''
        if weather == 'Clear':
            for x in range(0, 4):
                self.sense.set_pixels(clear_skies)
                sleep(0.5)
                self.sense.set_pixels(clear_skies2)
                sleep(0.5)
                self.sense.set_pixels(clear_skies3)
                sleep(0.5)
                self.sense.set_pixels(clear_skies4)
                sleep(0.5)
        elif weather == 'Clouds':
            for x in range(0,4):
                self.sense.set_pixels(cloud)
                sleep(0.5)
                self.sense.set_pixels(cloud2)
                sleep(0.5)
                self.sense.set_pixels(cloud3)
                sleep(0.5)
        
        sleep(1)

    def end_program(self):
        self.sense.show_message('Bye!')
        exit()


        