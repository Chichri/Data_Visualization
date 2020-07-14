import pygal
from die import Die

d6 = Die(6)

results = []
for i in range(100):
    result = d6.roll()
    results.append(result)

print(results)

frequencies = []
for value in range(1, d6.num_sides + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

print(frequencies)
#This code counts the frequecy of the diffrent results in the die roll

def tally(results):
    count = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
    for key in count.keys():
        for result in results:
            if key == result:
                count[key] += 1
    return count
print(tally(results))
#This code does the exact same, but put in a dictionary
#Also, I came up with this from scratch and I like it better then the textbook

hist = pygal.Bar()

hist.title = '100 Die Rolls'
hist.x_labels = d6.x_gen()
hist.x_title = 'Result'
hist.y_title = 'Frequency'

hist.add('d6', frequencies)
hist.render_to_file('Desktop/Coding_Projects/Data_Visualization/die_visual.svg')
#This is the first use of the pygal package
#pygal is another tool for displaying data, mostly charts and stuff
#The code above makes a bar graph displaying the frequency of our roles
#render_to_file() takes the visual data in hist and renders it to a specified -
#-file to be displayed

die_1 = Die(6)
die_2 = Die(6)

results = []
for i in range(100):
    result = die_1.roll() + die_1.roll()
    results.append(result)

frequencies = []
max_result = die_1.num_sides + die_1.num_sides

for value in range(2, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

hist = pygal.Bar()

hist.title = "Results of rolling two die 100 times."
hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6 + D6', frequencies)
hist.render_to_file('Desktop/Coding_Projects/Data_Visualization/die_visual2.svg')
#This graph displays the results of rolling two dice 100 times
#pygal can be quite versitile in displaying various data projections
