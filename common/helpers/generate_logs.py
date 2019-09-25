import os
import csv
import random
from datetime import datetime

STATUS_CODES = [200, 200, 200, 300, 400, 500]

def generate_logs(csv_path, row_count=1000):
	data = generate_content(row_count=row_count)
	_ = write_rows(csv_path, data)

def generate_content(row_count):
	print('Generating Content: %s' % row_count)
	date_generated = datetime.now().strftime('%Y-%m-%d:%H:%M')
	ipv4_addresses = generate_ipv4_addresses()
	endpoints = generate_urls()

	rows = []
	for row_idx in range(row_count):
		row = [random.choice(STATUS_CODES), \
				random.choice(ipv4_addresses), \
				random.choice(endpoints)]
		rows.append(row)

	return rows

def write_rows(csv_file, rows):
	print('Writing Logs.')
	with open(csv_file, 'w+', newline='') as outfile:
	    writer = csv.writer(outfile)
	    writer.writerows(rows)

def generate_ipv4_addresses(address_count=400):
	subnet_range = [i for i in range(256)]
	ipv4_addresses = ['.'.join([str(random.choice(subnet_range)) for i in range(4)]) for _ in range(address_count)]

	return ipv4_addresses

def generate_urls(domain='http://www.test-app.com/', url_count=400):
	urls = ['%s%s' % (domain, index) for index in range(url_count)]
	
	return urls

if __name__ == '__main__':
	_ = generate_logs(csv_path='logs.csv')