import requests
from datetime import datetime
import smtplib
import time
MY_EMAIL = "hotaruinorinana@gmail.com"
MY_PASSWORD = "*************"
MY_LAT = 25.042423 # Your latitude
MY_LONG = 121.444639 # Your longitude

#Your position is within +5 or -5 degrees of the ISS position.
# If the ISS is close to my current position
def is_over_head():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and  MY_LONG-5 <= iss_longitude <= MY_LONG + 5:
        return True
# and it is currently dark

def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
        "tzid": "Asia/Taipei"
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.now().hour
    if time_now >= sunset or time_now <= sunrise:
        return True

# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
while True:
    time.sleep(60)
    if is_night() and is_over_head():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg= "Subject: LOOK UP \n\n The ISS is above you in the sky"

    )






