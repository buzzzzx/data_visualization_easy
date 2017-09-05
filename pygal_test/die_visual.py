import pygal
from die import Die

die_1 = Die()
die_2 = Die(10)

results = []
for i in range(50000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

frequencies = []
max_size = die_1.num_size + die_2.num_size
for i in range(2, max_size+1):
    frequency = results.count(i)
    frequencies.append(frequency)

# 对结果可视化
hist = pygal.Bar()
hist.title = "Results of rolling a D6 and a D10 50000 times."
hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16']
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add("D6 + D10", frequencies)
hist.render_to_file('dice_visual.svg')