import datetime
import json
import urllib.request

def url_builder(lat, lon):
    user_api = "7dcc1f669c9a855a8ff8fd2f07f97d46"
    unit = "metric"
    return  'https://api.openweathermap.org/' + \
            'data/2.5/weather' + \
            '?lat=' + str(lat) + \
            '&lon='+ str(lon) + \
            '&appid=' + user_api + \
            '&units=' + unit

def fetch_data(full_api_url):
    url = urllib.request.urlopen(full_api_url)
    output = url.read().decode('utf-8')
    f = open('data.json', 'w')
    f.write(output)
    f.close
    return json.loads(output)

def time_converter(timestamp):
    return datetime.datetime.fromtimestamp(timestamp).strftime('%d %b %I:%M %p')

lat = 55.147872
lon = -6.675298
json_data = fetch_data(url_builder(lat, lon))

temperature = str(json_data['main']['temp'])
timestamp = time_converter(json_data['dt'])
description = json_data['weather'][0]['description']

# print('data')
# print(json_data)
# print("===============================")
print('Current weather')
print(timestamp + ' : ' + temperature + ' : ' + description)
