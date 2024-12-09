Overview This project demonstrates how to build an ETL (Extract, Transform, Load) pipeline using open-source tools like Python, SQLite, and Pandas. The pipeline extracts data from a CSV file (Titanic dataset), performs some transformation (e.g., filtering), and then loads the data into an SQLite database.

Tools Used: Python (v3.x) Pandas - For data processing SQLite - For storing transformed data Schedule - For automation Git - Version control and repository management Steps to Run the ETL Pipeline

Extract: Data Extraction from CSV First, you need to extract the Titanic dataset from a CSV file.
Command to Download Kaggle Dataset:

Ensure you have the Kaggle API key (kaggle.json) and that it is properly placed under ~/.kaggle/kaggle.json (for Linux/Mac) or C:\Users<Your Username>.kaggle\kaggle.json (Windows).

2.Transform: After extracting the data, you will perform transformations on the dataset. In this case, filtering the dataset based on a specific condition (age > 18).

Code for Transformation: import pandas as pd

Extract the data from CSV
data = pd.read_csv("train_and_test2.csv") # Replace with your actual dataset name

Transformation: Example filtering based on Age > 18
filtered_data = data[data['Age'] > 18]

Print first few rows to check if transformation works
print(filtered_data.head()) # Check the first few rows of the filtered data

Load: Load Transformed Data into SQLite After transformation, you load the data into an SQLite database. Code for Loading Data: import sqlite3
Load the transformed data into SQLite database
conn = sqlite3.connect("titanic.db") filtered_data.to_sql("passengers", conn, if_exists="replace", index=False) conn.close()

the titanic.db file should be downloaded as raw file and opened in the sqlite browser to ensure that the tables are loaded effectively into sqlite

Run the ETL Pipeline:

To run the ETL pipeline, execute the following command: python etl_pipeline.py Automate the Process: The pipeline will run every day at 10 AM as scheduled. You can also manually trigger the ETL process by calling run_etl() function in the code.
