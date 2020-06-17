from weather_bot import WeatherBot

if __name__ == '__main__':
  bot = WeatherBot()

  try:
    while True:

      # Captures SenseHat's joystick events
      for event in bot.sense.stick.get_events():
        if event.action == 'pressed' and event.direction == 'left':
            bot.show_currentWeather()
        elif event.action == 'pressed' and event.direction == 'down':
            bot.end_program()
        elif event.action == 'pressed' and event.direction == 'up':
          bot.change_settings()
  except KeyboardInterrupt:
    bot.end_program()  