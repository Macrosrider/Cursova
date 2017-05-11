import location
from weather import Weather

address = input('Enter the location you want to know weather:\n')
weather_n = Weather(address)
print('Enter the numbers of information you want to know:\n')
print('temperature - 1, wind speed - 2, wind direction - 3, humidity - 4, pressure - 5, status - 6, rain - 7, snow - 8')
information = input()
information = information.split(' ')
forecast = weather_n.get_weather_in_location()
if str(1) in information:
    print('Temperature: {}\n'.format(weather_n.temperature(forecast)))
if str(2) in information:
    print('Wind speed: {} m/s\n'.format(weather_n.wind_speed(forecast)))
if str(3) in information:
    print('Wind direction: {}\n'.format(weather_n.wind_vector(forecast)))
if str(4) in information:
    print('Humidity = {}\n'.format(weather_n.humidity(forecast)))
if str(5) in information:
    print('Pressure: {}\n'.format(weather_n.pressure(forecast)))
if str(6) in information:
    print('Status: {}\n'.format(weather_n.status(forecast)))
if str(7) in information:
    print('Rain: {}\n'.format(weather_n.rain(forecast)))
if str(8) in information:
    print('Snow: {}'.format(weather_n.snow(forecast)))
