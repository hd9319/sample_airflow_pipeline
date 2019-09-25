import os
import json

from airflow.operators import PythonOperator, BashOperator, EmailOperator

from common.helpers.generate_logs import generate_logs
from operators.downloader import download_data
from operators.transformer import clean_wheels_data
from operators.validate import validate_data
from operators.uploader import upload_data


# initialize globals
with open('config.json', 'r') as readfile:
	config = json.load(readfile)
	globals().update(config)


if __name__ == '__main__':
	generate_logs(csv_path='data/logs/logs.csv')