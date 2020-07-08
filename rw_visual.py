import matplotlib.pyplot as plt

from random_walk import Random_Walk

rw = Random_Walk(5000)
rw.fill_walk()
plt.scatter(rw.x_values, rw.y_values, s=5)
plt.show()
#This creates a random 'walk' graph as written in the rw class
point_numbers = list(range(rw.num_points))
plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,
edgecolor='none', s=5)
plt.show()
#This first generation uses the Blues colormap tied to the points in the class

plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,
edgecolor='none', s=5)
plt.scatter(0, 0, c='green', edgecolor='none', s=75)
plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolor='none', s=75)
plt.show()
#This one plots the beginning and end of the walk specifically

plt.axes().get_xaxis().set_visible(False)
plt.axes().get_yaxis().set_visible(False)

plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,
edgecolor='none', s=5)
plt.show()
#Because our data doesn't actually mean anything, having axes is pointless
#The chaining of methods like this can become quite common

plt.figure(dpi=128, figsize=(10,6))
plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,
edgecolor='none', s=5)
plt.show()
#We can also easily adjust the size of the display window
