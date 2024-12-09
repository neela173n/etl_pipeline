# **ETL Pipeline Project: Titanic Dataset**

## **Overview**
This project demonstrates how to build an ETL (Extract, Transform, Load) pipeline using open-source tools like **Python**, **SQLite**, and **Pandas**. The pipeline extracts data from a CSV file (Titanic dataset), performs transformations (e.g., filtering), and then loads the data into an SQLite database.

---

## **Tools Used**
- **Python (v3.x)**: The programming language for implementing the ETL pipeline.
- **Pandas**: For data processing and transformation.
- **SQLite**: For storing the transformed data.
- **Schedule**: For automating the pipeline to run at a specific time.
- **Git**: For version control and repository management.

---

## **Steps to Run the ETL Pipeline**

### **1. Extract: Data Extraction from CSV**

First, you need to extract the Titanic dataset from a CSV file. 

**Command to Download Kaggle Dataset:**

To download the Titanic dataset from Kaggle, ensure that you have the Kaggle API key (`kaggle.json`) properly set up:
- **Linux/Mac**: Place the file under `~/.kaggle/kaggle.json`
- **Windows**: Place it under `C:\Users\.kaggle\kaggle.json`

Use the following command to download the dataset from Kaggle:
```bash
kaggle datasets download -d [dataset-slug]
```

### **2. Transform: Data Transformation**

After extracting the data, the next step is to perform some transformations on the dataset. In this case, we'll filter the dataset to only include passengers older than 18 years.

**Code for Transformation:**

```python
import pandas as pd

# Extract the data from CSV
data = pd.read_csv("train_and_test2.csv")  # Replace with your actual dataset name

# Transformation: Example filtering based on Age > 18
filtered_data = data[data['Age'] > 18]

# Print first few rows to check if transformation works
print(filtered_data.head())  # Check the first few rows of the filtered data
```

### **3. Load: Load Transformed Data into SQLite**

Once the transformation is complete, the next step is to load the transformed data into an SQLite database.

**Code for Loading Data:**

```python
import sqlite3

# Load the transformed data into SQLite database
conn = sqlite3.connect("titanic.db")  # Connect to the SQLite database
filtered_data.to_sql("passengers", conn, if_exists="replace", index=False)  # Load data into table
conn.close()  # Close the connection
```

After running the above code, the `titanic.db` file will be generated. You can download this file and open it in the SQLite browser to ensure that the tables are loaded correctly.

---

## **Run the ETL Pipeline**

To run the ETL pipeline, execute the following command:

```bash
python etl_pipeline.py
```

This will trigger the entire ETL process: extraction, transformation, and loading.

---

## **Automate the Process**

You can schedule the pipeline to run every day at **10 AM** using the `Schedule` module. Alternatively, you can manually trigger the ETL process by calling the `run_etl()` function within the code.

Example of how to automate:
```python
import schedule
import time

# Define a function to run the ETL pipeline
def run_etl():
    # Call the ETL steps (extraction, transformation, and loading)
    pass  # Replace with actual function calls

# Schedule the task to run every day at 10 AM
schedule.every().day.at("10:00").do(run_etl)

# Keep the script running to check for scheduled tasks
while True:
    schedule.run_pending()
    time.sleep(1)
```

---

## **Repository Structure**
```plaintext
.
├── etl_pipeline.py              # Main ETL script to run the pipeline
├── train_and_test2.csv          # Titanic dataset (CSV)
├── titanic.db                   # SQLite database with transformed data
├── README.md                    # This file
└── requirements.txt             # Python dependencies
```

---

## **Conclusion**

This project showcases how to create a simple yet effective ETL pipeline using **Python**, **SQLite**, and **Pandas**. The dataset is extracted, transformed based on a condition (Age > 18), and then loaded into an SQLite database. You can automate this pipeline to run periodically and also trigger it manually as needed.
