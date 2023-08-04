import requests
from datetime import datetime
import smtplib

MY_LAT = 30.339781
MY_LONG = 76.386879


def iss_pos():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()

    data = response.json()

    longitude = float(data["iss_position"]["longitude"])
    latitude = float(data["iss_position"]["latitude"])

    if longitude > MY_LONG - 5 or longitude < MY_LONG + 5 and latitude > MY_LAT - 5 or latitude < MY_LAT + 5:
        return True
    else:
        return False


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()
    if time_now.hour <= sunrise or time_now.hour >= sunset:
        return True


if iss_pos() and is_night():
    my_email = "testerpython65@gmail.com"
    password = "zwigzayryxdncnou"

    connection = smtplib.SMTP("smtp.gmail.com", port=587)
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email
                        , to_addrs="javacoder24@yahoo.com"
                        , msg="Subject:Look Up\n\nThe ISS is above you in the sky.")
    connection.close()
