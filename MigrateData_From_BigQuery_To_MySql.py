import os
from google.cloud import bigquery
import pandas as pd
import mysql.connector

# Define variables
gcloud_credentials_path = "PATH/TO/YOUR/FILE/credentials.json"
mysql_host = "your_host"
mysql_user = "your_user"
mysql_password = "your_password"
mysql_database = "your_database"
bigquery_project = "your_project"
bigquery_dataset = "your_dataset"
bigquery_table = "your_table"

# Set the path to your Google Cloud credentials file using an environment variable
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = gcloud_credentials_path

# Connect to your MySQL database
conn = mysql.connector.connect(
    host=mysql_host,
    user=mysql_user,
    password=mysql_password,
    database=mysql_database
)

# BigQuery client
client = bigquery.Client(project=bigquery_project)
query = f"SELECT * FROM `{bigquery_project}.{bigquery_dataset}.{bigquery_table}`"
df = client.query(query).to_dataframe()

# Replace NaN values with None
df = df.astype(object).where(pd.notnull(df), None)

# Function to insert DataFrame into MySQL
def insert_dataframe_to_mysql(df, table_name, conn):
    cols = ",".join([f"`{col}`" for col in df.columns.tolist()])
    placeholders = ", ".join(["%s"] * len(df.columns))
    sql = f"INSERT INTO {table_name} ({cols}) VALUES ({placeholders})"
    data = [tuple(row) for row in df.values]
    
    # Create cursor, execute the statement, and close cursor
    with conn.cursor() as cursor:
        cursor.executemany(sql, data)
        conn.commit()

# Call the function to insert the data
insert_dataframe_to_mysql(df, bigquery_table, conn)

# Close the connection
conn.close()
