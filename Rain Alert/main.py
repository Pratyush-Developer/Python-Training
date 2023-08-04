import requests
from twilio.rest import Client

api_key = "b28cbc35605146bba8a200800232607"
CITY = "Patiala"
account_sid = "ACf20dacd10b969a9cf2e69ed463dfd542"
auth_token = "17468fd02dd412f7e96e06ce090863d7"

PARAMETERS = {
    "key": api_key,
    "q": CITY,
    "days": 1,
}

response = requests.get(url="http://api.weatherapi.com/v1/forecast.json", params=PARAMETERS)
response.raise_for_status()
weather_data = response.json()
forecast_dict = weather_data["forecast"]["forecastday"][0]
hour_list = forecast_dict["hour"]
sliced_hour_list = hour_list[0:12]
zero_hour = sliced_hour_list[0]
will_rain = False
condition_codes = []
for hour in sliced_hour_list:
    weather_code = hour["condition"]["code"]
    condition_codes.append(weather_code)
    if weather_code > 1000:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an ☂️",
        from_='+17624754351',
        to='+918360664411'
    )
    print(message.status)
