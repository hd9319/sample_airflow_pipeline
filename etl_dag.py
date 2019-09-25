import os
import json
from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python_operator import PythonOperator

from common.helpers.generate_logs import generate_logs
from operators.downloader import download_wheels_data
from operators.transformer import clean_wheels_data
from operators.validate import validate_wheels_data

# initialize globals
with open('config.json', 'r') as readfile:
	config = json.load(readfile)
	globals().update(config)

# directory
BASE_DIR  = os.path.dirname(__file__)

START_DATE = datetime(2019, 9, 24)
default_args = {
    'owner': 'hd9319',
    'depends_on_past': False,
    'start_date': START_DATE,
    'email': ['henrydang26@gmail.com'],
    'email_on_failure': False,
    'email_son_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=60),
}

# Define DAG
etl = DAG(
        'wheels_etl', default_args=default_args, 
        schedule_interval=timedelta(hours=5))

# Define Operators
download_data = PythonOperator(
    task_id='download_wheels_data',
    python_callable=download_wheels_data,
    op_kwargs={'csv_path': 'data/scrapes/wheel_scrapes.csv'},
    dag=etl,
	start_date=START_DATE,
)

clean_data = PythonOperator(
    task_id='clean_wheels_data',
    python_callable=clean_wheels_data,
    op_kwargs={'csv_path': 'data/scrapes/wheel_scrapes.csv', 
    			'output_file': 'data/output/wheels_cleaned.csv'},
    dag=etl,
    start_date=START_DATE,
)

validate_data = PythonOperator(
	task_id='validate_data',
	python_callable=validate_wheels_data,
	op_kwargs={'csv_file': 'data/output/wheels_cleaned.csv'},
	data=etl,
	start_date=START_DATE,
)

download_data >> clean_data >> validate_data





