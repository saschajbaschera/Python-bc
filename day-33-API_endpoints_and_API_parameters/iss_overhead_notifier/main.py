import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 47.443970
MY_LONG = 8.627090
MY_EMAIL = "dudesaschaa@gmail.com"
MY_PASSWORD = "jwuzdmwdxoxtiabi"


def is_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        return True
# print("Lat")
# print(MY_LAT)
# print(iss_latitude)
# print("long")
# print(MY_LONG)
# print(iss_longitude)


#Your position is within +5 or -5 degrees of the ISS position.


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()
    hour_now = time_now.hour

    if hour_now >= sunset or hour_now <= sunrise:
        return True
#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.


while True:
    if is_overhead() and is_night():
        print("EMAIL SENT")
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs="sash.baschera@gmail.com",
                msg="Subject:ISS overhead notification\n\nLook up!!"
            )
    else:
        print("ISS not in sight")
    time.sleep(60)



