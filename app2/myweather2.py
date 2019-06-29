# app/myweatherpy.py

import os
import requests
import json
import re
import datetime
import tzlocal
import pytz
import time
import csv

from dotenv import load_dotenv
from datetime import datetime
from pytz import timezone


def K_to_C (K) :                     # converting from K to C 
    return ( K- 273.15 )

load_dotenv()

API_KEY = "e4a6cee1403f08b045e56f64111d8ead"  # to obtain API_KEY from env file. 
print("----------------------------------")
print("welcome to the weather app")
city = input("Please input the desired city name")

request_url= f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
response = requests.get(request_url)
#print(type(response))
#print(response.status_code)
#print(response.text)

parsed_response = json.loads(response.text)

city_name = parsed_response["name"] 
temp= parsed_response["main"]["temp"]
temp_C= K_to_C(temp)
temp_max=parsed_response["main"]["temp_max"]
temp_max_C=K_to_C(temp_max)
temp_min=parsed_response["main"]["temp_min"]
temp_min_C=K_to_C(temp_min)
humidity=parsed_response["main"]["humidity"]
pressure = parsed_response["main"]["pressure"]
clouds_status= parsed_response["weather"][0]["description"]

print("----------------------------------")
print("You have chosen :   " + city_name)
print("Temperature : " + str(temp_C) + " C")
print("Max temperature : " + str(temp_max_C) +" C")
print("Min temperature : " + str(temp_min_C) + " C")
print("Humidity : " +str(humidity) + " %" )
print("Pressure : " + str(pressure)+ " kPa")
print("Cloud status : " + clouds_status)
print("----------------------------------")
print("Thank you for using the wather app, visit us again")

#last_refreshed = parsed_response["Meta Data"]["3. Last Refreshed"]
#tsd = parsed_response["Time Series (5min)"]
#latest_close = tsd[latest_day]["4. close"]
#{"coord":{"lon":-0.13,"lat":51.51},
#"weather":[{"id":802,"main":"Clouds","description":"scattered clouds","icon":"03n"}]
#,"base":"stations","main":{"temp":294.9,"pressure":1011,"humidity":69,"temp_min":291.15,"temp_max":298.71}
#,"visibility":10000,"wind":{"speed":8.2,"deg":270},
#"clouds":{"all":40},"dt":1561848629,
#"sys":{"type":1,"id":1417,"message":0.0107,"country":"GB","sunrise":1561779962,"sunset":1561839692}
#,"timezone":3600,
#"id":2643743,"name":"London"
#,"cod":200}