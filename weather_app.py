import requests

print("=" * 60)
print("        REAL-TIME WEATHER APPLICATION")
print("=" * 60)

API_KEY = "YOUR_API_KEY"

city = input("Enter city name: ")

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

try:
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:

        print("\n" + "=" * 60)
        print("                 WEATHER REPORT")
        print("=" * 60)

        print(f"🏙️ City         : {data['name']}")
        print(f"🌍 Country      : {data['sys']['country']}")
        print(f"🌡️ Temperature  : {data['main']['temp']} °C")
        print(f"🤗 Feels Like   : {data['main']['feels_like']} °C")
        print(f"💧 Humidity     : {data['main']['humidity']} %")
        print(f"☁️ Weather      : {data['weather'][0]['description'].title()}")
        print(f"🌬️ Wind Speed   : {data['wind']['speed']} m/s")

        print("=" * 60)
        print("Thank you for using Weather App!")
        print("=" * 60)

    else:
        print("❌ City not found. Please enter a valid city name.")

except Exception as e:
    print("❌ Error:", e)