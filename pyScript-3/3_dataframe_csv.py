import pandas as pd

subway_df = pd.read_csv(r'D:\Github\DAWithPython\pyScript-3\data\nyc_subway_weather.csv')
print(subway_df.describe())