from random import choice

class Random_Walk():
    def __init__(self, num_points):
        self.num_points = num_points
        #all walks start at 0,0
        self.x_values = [0]
        self.y_values = [0]

    def get_step(self):
        direction = choice([1,-1])
        distance = choice([0, 1, 2, 3, 4, 5])
        step = direction * distance
        return step

    def fill_walk(self):
        while len(self.x_values) < self.num_points:
            x_step = self.get_step()
            y_step = self.get_step()

            if x_step == 0 and y_step == 0:
                continue

            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)
#this class generates a seires of random coordinates called a 'walk'
#This is done mostly by using the choice() function, which return a random -
#-value from the giving list, dictionary, or tuple
#plotting these coordinates produces a random image on a graph
