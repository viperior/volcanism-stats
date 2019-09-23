import csv

with open('./volerup-noaa.txt', newline = '') as sve_data_file:                                                                                          
    	sve_csv_data = csv.reader(sve_data_file, delimiter='\t')
    	for sve in sve_csv_data:
    		print(sve)
