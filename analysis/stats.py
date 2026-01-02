# stats module
import pandas as pd
import numpy as np
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
   
def detect_anomalies(df):
   """ Detect temperature anomalies using Z-score."""
   temps=df["temp"]
   mean=temps.mean()
   std=temps.std()

   z_scores=(temps-mean)/std
   anomalies=df[np.abs(z_scores)>2]

   print("\n===ANOMALY DETECTION REPORT===")

   if anomalies.empty:
      print("No temperature anomalies detected ")
   else:
      print("Anomalies found:")
      print(anomalies[["date","temp"]])
      
      return anomalies