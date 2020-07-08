import matplotlib.pyplot as plt
from random_walk import Random_Walk

rw = Random_Walk(5000)
rw.fill_walk()
plt.plot(rw.x_values, rw.y_values)
plt.show()
