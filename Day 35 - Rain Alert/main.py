# Note! For the code to work you need to replace all the placeholders with
# Your own details. e.g. account_sid, lat/lon, from/to phone numbers.

"""api.openweathermap.org did not work for me due to 401 Error, although I had a valid API key.
I'm using www.weatherapi.com API instead. Therefore, the implementation will be slightly different."""

import requests
import os
from twilio.rest import Client

OWM_Endpoint = "https://api.weatherapi.com/v1/forecast.json"
api_key = os.environ.get("OWP_API_KEY")
account_sid = os.environ.get("OWP_ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")

weather_params = {
    "key": api_key,
    "q": "Rasht",
    "days": "1",
    "aqi": "no",
    "alerts": "no"

}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()

will_rain = weather_data["forecast"]["forecastday"][0]["day"]["daily_will_it_rain"]
will_snow = weather_data["forecast"]["forecastday"][0]["day"]["daily_will_it_snow"]

if will_rain or will_snow:

    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an ☂️",
        from_="YOUR TWILIO VIRTUAL NUMBER",
        to="YOUR TWILIO VERIFIED REAL NUMBER"
    )
    print(message.status)
