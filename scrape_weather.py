import requests
import pandas as pd

def scrape_weather():
    """Scrape Istanbul weather using WTTR(messy text)."""

    url= "https://wttr.in/Istanbul?format=j1"

    try:
         response=requests.get(url,timeout=10)
         response.raise_for_status()
    except Exception:
         print("Failed to fetch weather from WTTR!")
         return
    data=response.json()

    today=data["weather"][0]
    hourly=today["hourly"][4]

    temp =hourly["tempC"]
    condition=hourly["weatherDesc"][0]["value"]

    print("RAW SCRAPED DATA:")
    print("Temp:" , temp,"°C")
    print("Condition:", condition)

    df=pd.DataFrame({
        "temp":[float(temp)],
        "condition":[condition]
    })

    print("\nCLEANED DATA:")
    print(df)

    df.to_csv("data/scraped_weather.csv",index=False)
    print("\nSaved cleaned scraped data -> data/scraped_weather.csv")


if __name__=="__main__":
     scrape_weather()
    