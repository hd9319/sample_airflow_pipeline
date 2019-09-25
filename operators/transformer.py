import os

import pandas as pd

"""
Transforms data as per data requirements.
"""

def clean_wheels_data(csv_path, output_file):
	columns = ['Size', 'Boltpattern', 'Offset', 'HubBore', 'Weight', 'Finish', 'SKU', 'ManufacturerPartNumber', 'Price', 'Stock']
	dtypes = {
		'Price': float,
		'Weight': float,
		'Offset': float,
		'HubBore': float,
		'Stock': int,
		'Diameter': float,
		'Width': float
	}

	print('Cleaning Product Data: Wheels')
	wheels = pd.read_csv(csv_path, names=columns)

	# cleaning stock data
	wheels['Stock'] = wheels['Stock'].str.replace('\n', '')
	out_of_stock = wheels['Stock'] == 'Out of Stock'
	wheels.loc[out_of_stock, 'Stock'] = 0
	wheels.loc[~out_of_stock, 'Stock'] = 1

	# cleaning size
	wheels['Diameter'] = wheels['Size'].str.split('x').str[0]
	wheels['Width'] = wheels['Size'].str.split('x').str[1]

	# cleaning price
	wheels['Price'] = wheels['Price'].str.replace('[\$ ]', '')

	# convert dtypes
	for column, dtype in dtypes.items():
		wheels[column] = wheels[column].astype(dtype)

	# create cleaned file
	wheels.to_csv(output_file, index=False)

if __name__ == '__main__':
	clean_wheels_data('wheels_products.csv', 'clean_wheels.csv')