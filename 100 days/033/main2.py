from logging import exception

import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
# if response.status_code == 404:
#      raise  exception("That resource does not exist.")
# elif response.status_code == 401:
#      raise  exception("You are not authorised to access this data.")
# 有錯誤可以印出來
response.raise_for_status()

data = response.json()
print(data)
longitude = (data["iss_position"]["longitude"])  #經度
latitude = (data["iss_position"]["latitude"])  #緯度
iss_position = (longitude, latitude)
print(iss_position)
print(data["timestamp"])