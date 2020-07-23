import json
from country_codes import get_country_code
import pygal
from pygal.style import RotateStyle

#Let's make an interactive population map!

filepath = 'Desktop/Coding_Projects/Data_Visualization/population_data.json'
with open(filepath) as f:
    pop_data = json.load(f)
#This will be our population data. But we can't just use it raw like this
cc_populations = {}
#This will be the main dictionary in which country codes and pops are stored
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        pop = int(float(pop_dict['Value']))
#float() converts strings to decimals, int() converts the decimal to an interger
#We do this to avoid any errors down the line when pops are stored inconsitantly
        print('Population in 2010: ' + country_name + ': ' + str(pop))
#We've worked with json in the past, but never with a file as large as this one
#population_data.json is essentially a big list of dicts containing population-
#- data for various countries
#The loop above combs through the whole thing for entries from 2010, then -
#- filters the whole thing for country codes and pop data
        code = get_country_code(country_name)
        if code:
            cc_populations[code] = pop

cc_pops1, cc_pops2, cc_pops3 = {}, {}, {}

for cc, pop in cc_populations.items():
    if pop < 10000000:
        cc_pops1[cc] = pop
    elif pop < 1000000000:
        cc_pops2[cc] = pop
    else:
        cc_pops3[cc] = pop
#This chunk creates 3 'sub' dicts that filters countries by population magnitude
#This will provide some greater contrast on the final projection

wm_style = RotateStyle('#336699')
#This is just a quick instance of a class which we will use with the actual map
#The argument is a RGB hex color format, it provides a base to work of off
wm = pygal.maps.world.World(style=wm_style)
wm.title = 'World Population in 2010'
wm.add('0-10m', cc_pops1)
wm.add('10m-1bn', cc_pops2)
wm.add('>1bn', cc_pops3)

wm.render_to_file('Desktop/Coding_Projects/Data_Visualization/world_population.svg')
#The World() class is essentially a world map that can be modified with methods
#All of our work has now culminated in an interactive world map that displays-
#- country names and populations from 2010 when you hover over them
