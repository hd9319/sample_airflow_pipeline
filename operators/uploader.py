import os

import pyodbc

from sql.upload import sql_upload_wheels

def upload_wheels_data(csv_path, connection_string, col_format=None):
	"""
	Upload data to database.
	"""
	conn = pyodbc.connect(connection_string)
	cursor = conn.cursor()

	try:
		wheels = pd.read_csv(csv_path)
		# default col_format = order defined by file
		col_format = list(wheels.columns)
		print('Updating Wheels Data: %s' % len(wheels))

		# insert query
		insert_rows = [[row[column] for column in col_format] for _, row in wheels.to_dict(orient='index').items()]
		cursor.execute_many(sql_upload_wheels, insert_rows)

		# commit changes and close connection upon completion
		conn.commit()
		conn.close()

	except Exception as e:
		print(e)
		conn.close()

if __name__ == '__main__':
	wheels = pd.read_csv('clean_wheels.csv')
	_ = upload_wheels_data(wheels)