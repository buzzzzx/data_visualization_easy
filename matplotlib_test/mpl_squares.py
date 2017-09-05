import matplotlib.pyplot as plt

input_nums = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

plt.plot(input_nums, squares, linewidth=5)

# 设置图表标题，标签
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square", fontsize=14)
plt.tick_params(axis='both', labelsize=14)
plt.show()