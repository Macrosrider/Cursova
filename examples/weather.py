import urllib.request
import json
import time


class Weather():
    def __init__(self):
        self.location = get_city_id(input('Enter the city you want know the weather (Lviv, UA): \n'))

    def get_daily_weather_in_location(self):
        url = get_daily_url(self.location)
        path = urllib.request.urlopen(url)
        output = path.read().decode('utf-8')
        jdata = json.loads(output)
        path.close()
        return jdata

    def get_weekly_weather_in_location(self):
        url = get_weekly_url(self.location)
        path = urllib.request.urlopen(url)
        output = path.read().decode('utf-8')
        jdata = json.loads(output)
        path.close()
        return jdata

    def temperature(self, data):
        temp = data['main']
        return temp['temp']

    def wind_speed(self, data):
        temp = data['wind']
        return temp['speed']

    def humidity(self, data):
        temp = data['main']
        return temp['humidity']

    def pressure(self, data):
        temp = data['main']
        return temp['pressure']

    def status(self, data):
        temp = data['weather']
        return temp['main']

    def wind_vector(self, data):
        temp = data['wind']
        if temp['deg'] > 45 and temp['deg'] < 135:
            return 'North'
        elif temp['deg'] > 135 and temp['deg'] < 225:
            return 'West'
        elif temp['deg'] > 225 and temp['deg'] < 315:
            return 'South'
        elif temp['deg'] > 315 or temp['deg'] < 45:
            return 'East'

    def visibility(self, data):
        temp = data['id']
        return temp['visibility']

    def daily_forecast(self, data):
        tim = time.time()
        current_time = time.ctime(tim)
        print('----------------------------------------\n', current_time, '\n',
              '{0}{1}{2}'.format('Temperature: ',self.temperature(data), '°C'),'\n',
              '{}'.format('Humidity: '),self.humidity(data),'\n','{}'.format('Pressure: '), self.pressure(data), '\n',
              '{}'.format('Wind speed: '),self.wind_speed(data),'{}'.format('m/s'),'\n', '{}'.format('Wind vector: '),
              self.wind_vector(data),'\n')
        return None

    def weekly_forecast(self, data):
        current_day = ''
        for i in data['list']:
            date = i['dt_txt'].split('-')
            date = '/'.join(date)
            tim = time.strptime(date, "%Y/%m/%d %H:%M:%S")
            current_time = time.strftime("%a", time.localtime(time.mktime(tim)))
            if current_day != current_time:
                print('----------------------------------------\n')
                current_day = current_time
            print(current_time, '\n')
            print(i['dt_txt'],'\n', '{0}{1:+3.0f}{2}'.format('Temperature: ',i['main']['temp'],'°C'),'\n',
                    '{0}{1}'.format('Status: ', i['weather'][0]['description']))
            print('\n')
        return None

def get_city_id(city_id):
    with open('citylist.json', 'r', encoding='utf-8') as f:
        jdata = json.loads(f.read())
    city_id = city_id.split(',')
    for i in jdata:
        if i['name'] == city_id[0] and i['country'] == city_id[1].strip():
            return (i['id'])


def get_daily_url(city_id):
    user_api = 'f2355410d95beeedbbd84dc9cc762fdc'
    unit = 'metric'
    api = 'http://api.openweathermap.org/data/2.5/weather?id='
    full_api_url = api + str(city_id) + '&mode=json&units=' + unit + '&APPID=' + user_api
    return full_api_url


def get_weekly_url(city_id):
    user_api = 'f2355410d95beeedbbd84dc9cc762fdc'
    unit = 'metric'
    api = 'http://api.openweathermap.org/data/2.5/forecast?id='
    full_api_url = api + str(city_id) + '&mode=json&units=' + unit + '&APPID=' + user_api
    return full_api_url
