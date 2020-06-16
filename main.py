from weather_bot import WeatherBot

if __name__ == '__main__':
  bot = WeatherBot()

  try:
    while True:
      for event in bot.sense.get_events():
        if event.action == 'pressed':
          if event.direction == 'left':
            bot.show_currentWeather()
  except KeyboardInterrupt:
    bot.end_program()
  