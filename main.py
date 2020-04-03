from die import Die
from plotly.graph_objs import Bar, Layout
from plotly import offline

# create die with 'n' numeber of sides
n = int(input("Enter number of sides in die: "))
die = Die(n)

# roll die 'm' number of times and store results in a list
results = []
m = int(input("Enter number of die throw iterations: "))
for roll_num in range(m):
    result = die.roll()
    results.append(result)

#Counting how many times each number is rolled
frequencies = []
for value in range(1, die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

#Visualize the results
x_values = list(range(1, die.num_sides+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config  = {'title': 'Result'}
y_axis_config = {'title': 'Frequency of Result'}
layout = Layout(title='Results of rolling a die of '+str(n)+' sides '+str(m)+' times',
                xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': layout}, filename='index.html')