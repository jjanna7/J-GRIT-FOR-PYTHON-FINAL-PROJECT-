import requests
import pandas as pd

def scrape_weather():
    """Scrape messy WTTR weather data for Istanbul and clean it into a structured dataset."""

    url= "https://wttr.in/Istanbul?format=j1"
    print("Requesting live weather data from WTTR...")

    try:
         response=requests.get(url,timeout=10)
         response.raise_for_status()
         data= response.json()
    except Exception as e:
         print("\nFailed to fetch weather from WTTR!")
         print("Error:",e)
         return
    
    today=data["weather"][0]
    hourly=today["hourly"][4]

    temp =hourly["tempC"]
    feels_like=hourly["FeelsLikeC"]
    wind_speed=hourly["windspeedKmph"]
    humidity=hourly["humidity"]
    condition=hourly["weatherDesc"][0]["value"]
    precip=hourly["precipMM"]

    print("\n==== RAW SCRAPED DATA (MESSY) ====")
    print("Temperature:" , temp,"°C")
    print("Feels like:" , feels_like,"°C")
    print("Humidity:" , humidity,"%")
    print("Wind Speed:", wind_speed,"km/h")
    print("Precip(mm):" , precip)
    print("Condition:", condition)

    df=pd.DataFrame ({
        "temperature_C":[float(temp)],
        "feels_like_C":[float(feels_like)],
        "humidity_%":[float(humidity)],
        "wind_speed_kmh":[float(wind_speed)],
        "precip_mm":[float(precip)],
        "condition":[condition]
    })

    print("\n==== CLEANED STRUCTURED DATA ====")
    print(df,"\n")

    df.to_csv("data/scraped_weather.csv",index=False)

    print("\nSaved cleaned scraped data -> data/scraped_weather.csv")
    print("Scraping complete.")


if __name__=="__main__":
     scrape_weather()
    