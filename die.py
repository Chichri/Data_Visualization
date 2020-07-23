from random import randint
class Die():
    def __init__(self, num_sides):
        self.num_sides = num_sides

    def roll(self):
        return randint(1, self.num_sides)

    def x_gen(self):
        x_axis = []
        temp = 1
        for i in range(self.num_sides):
            x_axis.append(temp)
            temp += 1
            if temp == self.num_sides:
                break

        return x_axis

    def x_mult_gen(self, start, end):
        x_axis = []
        for i in range(end):
            x_axis.append(start)
            start += 1
            if start == end + 1:
                break

        return x_axis

#This simple class creates a simulated die of customizable sides
#roll() returns a value, the simulated result of rolling the die
#x_gen() creates a list of each possible result for pygal projections
#x_mult_gen()) does the same, but takes two arguments for projections that use-
#- more then one die
#Props to my friend Zach pointing out this extremly obvious functionality
