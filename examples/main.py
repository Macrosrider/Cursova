from weather import *

print('WELCOME AT OUR FORECAST PROGRAMM\n')
forecast = Weather()
print('DO YOU WANT TO GET FORECAST FOR TODAY, OR FOR 5 DAYS?(Y/N)\n')
decision = input()
if decision == 'Y':
    weather = forecast.get_daily_weather_in_location()
    forecast.daily_forecast(weather)
else:
    weather = forecast.get_weekly_weather_in_location()
    forecast.weekly_forecast(weather)
