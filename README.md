# Migrate Data from BigQuery to MySQL

This repository contains a Python script to migrate data from Google BigQuery to a MySQL database. The script extracts data from a specified BigQuery table and inserts it into a MySQL table. 

## Requirements

- Python 3.x
- `pandas`
- `google-cloud-bigquery`
- `mysql-connector-python`

## Setup

1. **Clone the repository:**

    ```sh
    git clone https://github.com/mecorp96/MigrateData_From_Bigquery_To_Mysql.git
    cd MigrateData_From_Bigquery_To_Mysql
    ```

2. **Install the required packages:**

    ```sh
    pip install pandas google-cloud-bigquery mysql-connector-python
    ```

3. **Set up Google Cloud credentials:**

    - Download your service account key file from Google Cloud Console.
    - Set the path to your service account key file in the script.

4. **Configure your MySQL database:**

    Update the MySQL connection details in the script.

## Usage

1. **Run the script:**

    ```sh
    python migrate_data.py
    ```

## Configuration

All configuration variables (Google Cloud credentials path, MySQL host, user, password, database, and BigQuery project, dataset, and table) are defined at the beginning of the script for easy modification.

## Author

Jonay Sosa

Follow my [Medium](https://medium.com/@jonay.sosag) for more tech content.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
