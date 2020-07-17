import csv

filepath = 'Desktop/Coding_Projects/Data_Visualization/sitka_weather_07-2014.csv'
with open(filepath) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)
#This is the first use of the csv module in the Python standard library
#csv stands for comma separated values, a common-ish file type
#csv files are easy for computers to read, but cumbersome for humans
#The code above works by making reader an object associated with the file
#Then next() is called, which returns the next line in the file
#As this is it's first calling, it returns the first line, the headers 
