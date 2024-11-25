import requests
import json
from pyspark.sql import SparkSession

# Initialize Spark session
spark = SparkSession.builder.appName("Weather-CSV-to-Parquet").getOrCreate()

# Define API URL (Open-Meteo free weather API for historical data)
API_URL = "https://api.open-meteo.com/v1/forecast?latitude=40.7128&longitude=-74.0060&hourly=temperature_2m"

# Fetch weather data from API
response = requests.get(API_URL)
if response.status_code == 200:
    print("Successfully fetched weather data from API.")
    data = response.json()

    # Extract hourly temperature data
    hourly_data = data.get("hourly", {})
    temperatures = hourly_data.get("temperature_2m", [])
    timestamps = hourly_data.get("time", [])

    # Prepare data for Spark DataFrame
    weather_records = [{"timestamp": ts, "temperature": temp} for ts, temp in zip(timestamps, temperatures)]

    # Create Spark DataFrame
    df = spark.createDataFrame(weather_records)
    print("DataFrame created successfully.")
else:
    print(f"Failed to fetch data from API. Status code: {response.status_code}")
    exit(1)

# Write DataFrame to Parquet
output_path = "/app/data/output_weather.parquet"  # output path (inside the Docker container)
df.write.parquet(output_path, mode="overwrite")

print(f"Weather data written to Parquet at {output_path}")
