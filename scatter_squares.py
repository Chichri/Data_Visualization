import matplotlib.pyplot as plt

plt.scatter(2, 4, s = 200)
plt.title('Squares', fontsize = 24)
plt.xlabel('Value', fontsize = 14)
plt.ylabel('Square of Value', fontsize = 14)
plt.tick_params(axis='both', which='major', labelsize=14)

plt.show()
#scattter() makes a scatter graph, using the first two values as x-y coordinates
#Currently, this scatter graph makes a only a single point, (2,4)
#But we can give it more

x_values = [1, 2, 3, 4, 5]
y_values = [1, 4, 9, 16, 25]
plt.scatter(x_values, y_values, s=200)
plt.show()
#Now scatter() plots each pair of values of the two lists in numerical order
#But writting down these kinds of things by hand can be far too time-consuming

plt.axis([0, 1100, 0, 1100000])
x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]
plt.scatter(x_values, y_values, s=5)
plt.show()
#With a range and a for-loop, 1 to a 1000 can be plotted in two lines

plt.scatter(x_values,y_values, c='red', edgecolor='none',s = 40)
plt.show()
#The color and outlines of the points on your scatter graph can also be edited
#Color can also be set with the RGB color model for greater precision

plt.scatter(x_values,y_values, c=y_values, cmap=plt.cm.Blues, edgecolor='none',
s = 40)
plt.show()
#This graph uses a colormap in the visualization of its data
#Colormaps are a series of colors in a gradient that has a start and an end
#pyplot has a couple of built-in ones
#Here we tie the colormap Blues to the y-value of the graph
#Therefore, the graph gets darker and darker as the values rise
