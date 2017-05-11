import pyowm
import json
api_key= pyowm.OWM(API_key ='f2355410d95beeedbbd84dc9cc762fdc', language='ru')


class Weather():
    def __init__(self, location):
        self.location = location

    def get_weather_in_location(self):
        return api_key.weather_at_place(self.location).get_weather()

    def temperature(self, data):
        temp = data.get_temperature('celsius')
        return temp['temp']

    def wind_speed(self, data):
        temp = data.get_wind()
        return temp['speed']

    def humidity(self, data):
        temp = data.get_humidity()
        return temp

    def pressure(self, data):
        temp = data.get_pressure()
        return temp['press']

    def status(self, data):
        temp = data.get_status()
        return temp

    def rain(self, data):
        temp = data.get_rain()
        if len(temp) == 0:
            return 'Without rain'
        else:
            return temp

    def snow(self, data):
        temp = data.get_snow()
        if len(temp) == 0:
            return 'Without snow'
        else:
            return temp

    def wind_vector(self, data):
        temp = data.get_wind()
        if temp['deg'] > 45 and temp['deg'] < 135:
            return 'North'
        elif temp['deg'] > 135 and temp['deg'] < 225:
            return 'West'
        elif temp['deg'] > 225 and temp['deg'] < 315:
            return 'South'
        elif temp['deg'] > 315 or temp['deg'] < 45:
            return 'East'
