import requests
import pandas as pd
from datetime import datetime

MY_LAT = 25.042423
MY_LNG = 121.444639
parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted":0,
    "tzid":"Asia/Taipei"
}
response = requests.get(url = "https://api.sunrise-sunset.org/json", params = parameters)
response.raise_for_status()
data = response.json()
print(data)
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]
print(sunrise)
print(sunset)
print(pd.DataFrame(data))

time_now = datetime.now()
print(time_now)
print(time_now.hour)






#====================================================================================================
# API documentation
# Ours is a very simple REST api, you only have to do a GET request to https://api.sunrise-sunset.org/json. No need to sign up or get an API Key.
#
# Request parameters
# lat (float): Latitude in decimal degrees. Required.
# lng (float): Longitude in decimal degrees. Required.
# date (string): Date in YYYY-MM-DD format. Also accepts other date formats and even relative date formats. If not present, date defaults to current date. Optional.
# callback (string): Callback function name for JSONP response. Optional.
# formatted (integer): 0 or 1 (1 is default). Time values in response will be expressed following ISO 8601 and day_length will be expressed in seconds. Optional.
# tzid (string): A timezone identifier, like for example: UTC, Africa/Lagos, Asia/Hong_Kong, or Europe/Lisbon. The list of valid identifiers is available in this List of Supported Timezones. If provided, the times in the response will be referenced to the given Time Zone. Optional.