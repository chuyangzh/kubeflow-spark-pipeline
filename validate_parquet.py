import pandas as pd

# Path to the Parquet file
parquet_file = "data/output_weather.parquet"

# Load and display the data
df = pd.read_parquet(parquet_file)
print(df.head())
