"""
https://api.telegram.org/bot5211758343:AAGHoBXmvv3sJFF3ersdhUz44u6-iDreoZI/getUpdates
TARGET = -1001704658427
976223233
1900969183
"""
class Config():
	apiId = 15918522
	apiHash = '689382b9f19dbc03d0dd12ce157438dc'
	stringSession = "BQDy5boAqOghneoR56BD7PJRN9rW_ejnZ_5wad1W_-q-UG9hnb5beEi2YtiTWUInp-UCjqTL4obbTXVKbpYvSluBiIMBzMX5ZlI_UmcVEWdjFkkwv9Vv_0pxeMLVQpAORAzNbp9mqPUFRkAS0ALkFLY8lineJeqFhD_qzA_-nqKwQDTKOcSkRoWHV_IWkWRjIBpfN7icFNGiiNzU-f61BUfodr8UYMY8yh-pqfCIZ5mjamgP08km4W_tWlSIH5O-prv3OKD1mU4_e3rpkQ9lS7eEF9MeCQq8PeLR_GdcWnIgTZ8fANE2RFo_FUa6XkkwkcYMzN9wWnmR3p1ZofsaRycNRXl0wQAAAAA6L_wBAA"
	
class Utils():
	def write_json(data):
		import json
		
		json_data = data
		with open("my_json.json", "w") as file:
			json.dump(json_data, file, indent=4)

