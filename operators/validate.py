import os

import numpy as np
import pandas as pd

"""
Validate quality of data following cleaning.
"""

def validate_data(data, **dtype_assertions):
	for column, dtype in dtype_assertions.items():
		assert data[column].dtype == dtype

def validate_wheels_data(csv_file):
	"""
	Offset                    float64
	HubBore                   float64
	Weight                    float64
	Finish                     object
	SKU                        object
	ManufacturerPartNumber     object
	Price                     float64
	Stock                       int64
	Diameter                  float64
	Width                     float64
	"""
	print('Reading Data.')
	data = pd.read_csv(csv_file)

	print('Validating Data.')
	_ = validate_data(data,
						Price=np.float64, 
						HubBore=np.float64,
						Weight=np.float64,
						Stock=np.int64,
						Diameter=np.float64,
						Width=np.float64,
					)

if __name__ == '__main__':
	_ = validate_wheels_data('clean_wheels.csv')
