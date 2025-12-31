# stats module
import pandas as pd
def clean_weather_data(df):
    """Clean and standardize the weather DataFrame."""
    df=df.copy()

    numeric_cols=["temp", "low", "high", "precip", "feels_like"]
    for col in numeric_cols:
     df[col]=pd.to_numeric(df[col], errors="coerce")

    df["date"]=pd.to_datetime(df["date"], errors="coerce")
    df=df.ffill()
    df=df.bfill()
    
  
    return df

def analyze_weather(df):
    """Return summary statistics."""
    summary = {
        "avg_temp": df["temp"].mean(),
        "max_temp": df["high"].max(),
        "min_temp": df["low"].min(),
        "avg_precip": df["precip"].mean()
    }
    return summary