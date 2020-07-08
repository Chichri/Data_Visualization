import matplotlib.pyplot as plt

squares = [1, 4, 9, 16, 25]
plt.plot(squares)
plt.show()
#Python has a lot of tools to display data in diffrent ways
#matplotlib is a very useful module for such activities
#the plot() method here attempts to plot the numbers in a meaningful way
#show() displays the graph, which can then be saved or manipulated as you like

plt.plot(squares, linewidth=5)

"""this is going to label the chart and the axes"""
plt.title('Square Numbers', fontsize = 24)
plt.xlabel('Value', fontsize = 14)
plt.ylabel('Square of Vaule', fontsize = 14)

plt.tick_params(axis='both', labelsize = 14)
plt.show()

#this version of the graph not only has a title, but also labeled axes
#tick_params() in particular can take multiple arguments to adjust things
