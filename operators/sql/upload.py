"""
Queries to upload to database.
"""

sql_upload_wheels = """
INSERT INTO dbo.WheelProducts 
	(Size, Boltpattern, Offset, HubBore, Weight, Finish, SKU, ManufacturerPartNumber, Price, Stock, Diameter, Width)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
"""

sql_create_table_wheels = """
CREATE TABLE dbo.WheelProducts (
	Size varchar(255), 
	Boltpattern varchar(255), 
	Offset varchar(255), 
	HubBore varchar(255), 
	Weight float, 
	Finish varchar(255), 
	SKU varchar(255), 
	ManufacturerPartNumber varchar(255), 
	Price float, 
	Stock bit, 
	Diameter float, 
	Width float
)

"""