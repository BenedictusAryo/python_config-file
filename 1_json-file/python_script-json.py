# This is sample python script 
# that take config-file.json as parameter argument
import json

with open('config-file.json') as json_data_file:
    data = json.load(json_data_file)
print(data)