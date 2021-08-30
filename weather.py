import requests
import time


def try_again():
    ans = input("\nWould you like to use this program again? yes/no\n:").lower()
    if "yes" in ans:
        get_woeid()
    elif "no" in ans:
        print("Okay, good bye!")
    else:
        print("Please reply with yes or no only!")
        try_again()

def get_woeid(): 
    inpt = input('\nWhere in the world are you?\n')
    a = requests.get(f"https://www.metaweather.com/api/location/search/?query={inpt}")
    city = a.json()
    if len(city) == 0:
        print("Sorry, that city isn't in our database, please try again.")
        get_woeid()
    else:
        try:
            r = requests.get(f'https://www.metaweather.com/api/location/{city[0]["woeid"]}')
        except requests.exceptions.ConnectionError:
            print("Connection Error, please try again later")
            exit()
        d = r.json()
        print(f"\nWeather report for {inpt}\n")
        for forecast in d['consolidated_weather']:
            date = forecast['applicable_date']
            humidity = forecast['humidity']
            temp = int(forecast['the_temp'])
            state = forecast['weather_state_name']
            print(f"{date}\tHumidity: {humidity}\tTemperature: {temp} \tState: {state}")
        time.sleep(2)
        try_again()

get_woeid()