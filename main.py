import os
import requests
from twilio.rest import Client

account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")
api_key = os.environ.get("API_KEY")
api_params = {
    'lat':21.932767,
    'lon':86.681493,
    'cnt':4,
    'appid': api_key
}

def get_details():
    api_call = "https://api.openweathermap.org/data/2.5/forecast"
    response = requests.get(api_call, params=api_params)
    response.raise_for_status()
    weather_forecast = response.json()
    will_rain = False
    for day in weather_forecast['list']:
        if day['weather'][0]['id']<700:
            will_rain = True
    if will_rain:
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            from_='+19204826193',
            body="Don't forget to take an umbrella :)",
            to='+919940901332'
        )
        print(message.status)
get_details()
