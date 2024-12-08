import pandas as pd
import sqlite3

# Extract
data = pd.read_csv("train_and_test2.csv")  # Replace with your dataset name

# Transform
data = data.dropna()  # Remove rows with missing values
filtered_data = data[data['Age'] > 18]  # Filter rows where Age > 18

# Load
conn = sqlite3.connect("titanic.db")
filtered_data.to_sql("passengers", conn, if_exists="replace", index=False)
conn.close()

print("ETL process completed successfully!")


#automation code

import time
import schedule

def run_etl():
    # ETL script here (copy your ETL code here)
    print("ETL executed")

schedule.every().day.at("10:00").do(run_etl)

while True:
    schedule.run_pending()
    time.sleep(1)
