from requests import *
from pprint import pprint

user_agent = {'User-agent': 'Python Application'}
response = get('https://api.met.no/weatherapi/locationforecast/2.0/compact?lat=58.37814547321612&lon=26.72852054945728', headers = user_agent)

if response.status_code == 200:
    pprint(response.json())
    for item in response.json()['properties']['timeseries']:
        print(item['time'], '-', item['data']['instant']['details']['air_temperature'])
else:
    print('Paring ei onnestunud. Saime vastuseks', response.status_code)