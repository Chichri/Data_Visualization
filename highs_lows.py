import csv
from datetime import datetime
from matplotlib import pyplot as plt

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

    for index, column_header in enumerate(header_row):
        print(index, column_header)
#enumerate() is a handy function that lets you use lists like dictionaries
#It returns the index of each item on the list as well as the items as well

    dates, highs = [], []
    for row in reader:
        current_date = datetime.strptime(row[0], '%Y-%m-%d')
        dates.append(current_date)
        highs.append(int(row[1]))

    print(highs)
#This loops organizes the high temperatues and their dates into lists
#The highs are stored as index[1] in each row, making it an easy specification
#The dates in each row are index[0], and we use module datetime for..some reason
#Also, because we are using the same reader object, it starts of from where we -
#- left it with the next() function, meaning we skip over the headers

fig = plt.figure(dpi=128, figsize = (10,6))
plt.plot(dates, highs, c='red')

plt.title('Daily high tempuratures, July 2014', fontsize=14)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
#All of this is just for graphing the data. Lets try a larger file

#------------------------------------------------------------------------------

filepath = 'Desktop/Coding_Projects/Data_Visualization/sitka_weather_2014.csv'
#Notice that this path isn't just for July's data, its for the whole year
with open(filepath) as f:
    reader = csv.reader(f)
    next(reader)

    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[0], '%Y-%m-%d')
        dates.append(current_date)
        highs.append(int(row[1]))
        lows.append(int(row[3]))
#Also notice now how we're making a list for the lows as well now
fig = plt.figure(dpi=128, figsize = (10,6))
plt.plot(dates, highs, c='red')
plt.plot(dates, lows, c='blue')
#We can plot the lows onto the same graph for more data
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
plt.title('Daily high and low tempuratures, 2014', fontsize=14)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
#This graph will show an expanded version of the earilier temperature graph, -
#complete with the entire years' data, low temps, and shading in between.
#All of this is acomplished by reading data from a csv file 
