# plots module
import matplotlib.pyplot as plt

def plot_temperature(df):
    """Plot a professional temperature trend graph."""
    df= df.sort_values("date")

    plt.figure(figsize=(11, 5))

    sunset_colors=["#FFD700","#FFA500","#FF4500"]

    for i in range(len(df)-1):
            plt.plot(
                    df["date"].iloc[i:i+2],
                    df["temp"].iloc[i:i+2],
                    color=sunset_colors[i%len(sunset_colors)],
                    linewidth=3
            )
            
                  
    plt.scatter(df["date"], df["temp"], color='#FF7f0e', s=50,)
       
    start=df["date"].min().strftime("%d-%b-%Y")
    end=df["date"].max().strftime("%d-%b-%Y")
    title=f"Temperature Trend in Istanbul  ({start} to {end})"

    plt.title(title, fontsize=15, fontweight='bold')
    plt.xlabel("Date")
    plt.ylabel("Temperature (°C)")
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("analysis/temp_trend.png")
    plt.close()


def plot_precipitation(df):
        """Plot a daily precipitation ."""
        df=df.sort_values("date")

        plt.figure(figsize=(11, 5))
        plt.plot(
            df["date"], 
            df["precip"], 
            color="#5eff0e",
            linewidth=2.5,
            label="Precipitation (mm)"
     )
        plt.title("Daily Precipitation in Istanbul", fontsize=14, fontweight='bold')
        plt.xlabel("Date")
        plt.ylabel("Precipitation (mm)")
        plt.grid(True, linestyle='--', alpha=0.5)
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig("analysis/precipitation.png")
        plt.close()
        plt.xlabel("Date")
        plt.grid(True, linestyle='--', alpha=0.5)
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.close()
        
def plot_high_low(df):
            """Plot high and low temperature ranges."""
            df=df.sort_values("date")

            plt.figure(figsize=(11, 5))
            plt.plot(
                df["date"], 
                df["high"], 
                color="#ff5733",
                linewidth=2.5,
                label="High Temp (°C)"
         )
            plt.plot(
                df["date"], 
                df["low"], 
                color="#33c1ff",
                linewidth=2.5,
                label="Low Temp (°C)"
         )
            plt.title("Daily High and Low Temperatures in Istanbul", fontsize=14, fontweight='bold')
            plt.xlabel("Date")
            plt.ylabel("Temperature (°C)")
            plt.grid(True, linestyle='--', alpha=0.5)
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.savefig("analysis/high_low_temps.png")
            plt.close()


def plot_weather_frequency(df):
                """Bar chart of weather condition frequencies."""
                condition_counts = df["weather"].value_counts()

                plt.figure(figsize=(10, 6))
                condition_counts.plot(
                    kind='bar', 
                    color='#ffa500', 
                    edgecolor='black'
                )
                plt.title("Frequency of Weather Conditions in Istanbul", fontsize=14, fontweight='bold')
                plt.xlabel("Weather Type")
                plt.ylabel("Count")
                plt.grid(axis='y', linestyle='--', alpha=0.4)
                plt.tight_layout()
                plt.savefig("analysis/weather_conditions.png")
                plt.close()

def plot_all_weather(df):
                    """Generate all weather plots."""
                    plot_temperature(df)
                    plot_precipitation(df)
                    plot_high_low(df)
                    plot_weather_frequency(df)