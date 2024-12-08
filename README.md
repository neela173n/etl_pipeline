Overview
This project demonstrates how to build an ETL (Extract, Transform, Load) pipeline using open-source tools like Python, SQLite, and Pandas. The pipeline extracts data from a CSV file (Titanic dataset), performs some transformation (e.g., filtering), and then loads the data into an SQLite database.

Tools Used
Python (v3.x)
Pandas - For data processing
SQLite - For storing transformed data
Schedule - For automation
Git - Version control and repository management
Steps to Run the ETL Pipeline
1. Extract: Data Extraction from CSV
First, you need to extract the Titanic dataset from a CSV file.

Command to Download Kaggle Dataset:

Ensure you have the Kaggle API key (kaggle.json) and that it is properly placed under ~/.kaggle/kaggle.json (for Linux/Mac) or C:\Users\<Your Username>\.kaggle\kaggle.json (Windows).



How to Use the Repository
Clone the Repository:

To clone this repository, run the following command in your terminal:

bash
Copy code
git clone https://github.com/<your-username>/etl_pipeline.git
cd etl_pipeline
Install Required Libraries:

To install the necessary libraries, run:

bash
Copy code
pip install -r requirements.txt
Note: If you don't have requirements.txt, you can create it using:

bash
Copy code
pip freeze > requirements.txt
Run the ETL Pipeline:

To run the ETL pipeline, execute the following command:

bash
Copy code
python etl_pipeline.py
Automate the Process:

The pipeline will run every day at 10 AM as scheduled. You can also manually trigger the ETL process by calling run_etl() function in the code.

