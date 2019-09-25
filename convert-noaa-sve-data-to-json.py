import csv, json

csv_filename = './volerup-noaa.txt'
output_json_filename = './volerup-noaa.json'

with open(csv_filename, newline = '') as sve_data_file:                                                                                          
  reader = csv.DictReader(sve_data_file, delimiter = '\t')
  
  data_dict = {}
  
  for index, current_dict in enumerate(reader):
    data_dict[index] = current_dict
  
  output_dict = json.loads(json.dumps(data_dict))
  
  with open(output_json_filename, 'w') as output_file:
    json.dump(output_dict, output_file)
