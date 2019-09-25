import os
import csv

import requests
from bs4 import BeautifulSoup
"""
Download data and store in directory.
"""

ACCEPTABLE_STATUS_CODES = [200]

urls = ['https://www.canadawheels.ca/ruffino-wheels/block/gloss-black-milled-edge', 
		'https://www.canadawheels.ca/ruffino-wheels/boss/gloss-black']

default_headers = {
    'authority': 'www.canadawheels.ca',
    'cache-control': 'max-age=0',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
    'accept': '*/*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9',
    'Referer': 'https://www.canadawheels.ca/',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
    'Origin': 'https://www.canadawheels.ca',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'origin': 'https://www.canadawheels.ca',
    'referer': 'https://www.canadawheels.ca/',
    'x-requested-with': 'XMLHttpRequest',
    'content-length': '0',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
}

def download_data(csv_path, urls=urls):
	print('Downloading Data.')

	data = []

	for url in urls:
		response = send_request(url)
		items = parse(response)
		data += items

	_ = write_rows(csv_path, data)


def send_request(url, headers=default_headers):
	response = requests.get(url, headers=headers)
	if response.status_code in ACCEPTABLE_STATUS_CODES:
		return response
	else:
		return None

def parse(response):
	if response:
		try:
			soup = BeautifulSoup(response.content, 'lxml')
			table = soup.find('div', {'id': 'specs'}).find('tbody')
			table_rows = table.find_all('tr')
			data = [[element.text if element.text != '' else element.href for element in table_row.find_all('td')] 
						for table_row in table_rows]

			return data
		except Exception as e:
			print(e)
			return []
	else:
		return []

def write_rows(csv_file, rows):
	print('Saving Data.')
	with open(csv_file, 'w+', newline='') as outfile:
	    writer = csv.writer(outfile)
	    writer.writerows(rows)

if __name__ == '__main__':
	download_data('wheels_products.csv')


