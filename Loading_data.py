#Loading CSV file
import pandas as pd

# Specify the path to the CSV file
file_path_1= 'raw_data/student_coffee_crisis.csv'

# Read the CSV file
df_1 = pd.read_csv(file_path_1, sep=';', encoding='utf-8', skiprows=1)

# Print the CSV data
print("Data loaded successfully_CSV")
print(df_1.head())
#exel file
file_path_2= 'raw_data/student_coffee_crisis.xlsx'
df_2 = pd.read_excel(file_path_2)
print("Data loaded successfully_excel")
print(df_2.head())

#JSON file
file_path_3= 'raw_data/student_coffee_crisis.json'
df_3 = pd.read_json(file_path_3)
# nested JSON → use json + normalize
import json 
data = json.load(open(file_path_3)) 
df = pd.json_normalize(data)
print("Data loaded successfully_json")
print(df.head())
# Parquet file
file_path_4 = 'raw_data/student_coffee_crisis.parquet'
df_parquet = pd.read_parquet(file_path_4)

print("Data loaded successfully - Parquet")
print(df_parquet.head())
