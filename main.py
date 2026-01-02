from analysis.stats import clean_weather_data, analyze_weather
from analysis.plots import plot_all_weather
from analysis.stats import detect_anomalies
import json
import pandas as pd
import requests

def load_json():
    """load the weather dataset from JSON file."""
    with open("data/raw_weather.json") as file:
        data = json.load(file)
    return data

def load_weather_data():
 print ("API disabled, loading from local JSON file.")
 return load_json()

def fetch_weather_api():
    """Try fetching weather data from an external API."""
    url="https://wttr.in/Istanbul?format=j1"

    try:
        print("Trying to fetch weather from API...")
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        print("API data loaded successfully!")
        return response.json()

    except Exception as e:
        print(f"API failed: {e}")
        return None

def convert_to_dataframe(data):
    """convert the loaded JSON data to a pandas DataFrame."""
    rows = []


    if "weather" in data:
        dailly_list=data["weather"]

        for day in dailly_list:
            rows.append({
                "date": day.get("date"),
                "temp": float(day["avgtempC"]),
                "low": float(day["mintempC"]),
                "high": float(day["maxtempC"]),
                "precip": float(day["hourly"][0]["precipMM"]),
                "weather": day["hourly"][0]["weatherDesc"][0]["value"],
                "feels_like": float(day["hourly"][0]["FeelsLikeC"]),
            })

    elif "dates" in data:
        for entry in data["dates"]:
            rows.append({
                "date": entry.get("date"),
                "temp": entry.get("temp"),
                "low": entry.get("low"),
                "high": entry.get("high"),
                "precip": entry.get("precip"),
                "weather": entry.get("weather"),
                "feels_like": entry.get("feels_like"),
            })
    df = pd.DataFrame(rows)
    df["date"] = pd.to_datetime(df["date"])
    return df 

def main():
    print("Loading weather data...")
    raw_data = load_weather_data()

    print("Converting JSON to DataFrame...")
    df = convert_to_dataframe(raw_data)

    print ("\n====WEATHER DATA====")
    print(df.to_string())

    print("\nCleaning weather data...")
    df = clean_weather_data(df)

    print("\nAnalyzing weather data...")
    stats= analyze_weather(df)
    clean_stats={k:float(v)for k,v in stats.items()}
    print(clean_stats)
    
    print("\nRunning anomaly detection...")
    detect_anomalies(df)
    
    print("\nCreating weather plots...")
    plot_all_weather(df)

    print("\nAnalysis complete. Charts saved in the analysis folder!")

if __name__ == "__main__":
   main()
