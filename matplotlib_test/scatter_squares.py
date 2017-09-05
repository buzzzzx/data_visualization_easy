import matplotlib.pyplot as plt

x = list(range(1, 1001))
y = [x**2 for x in range(1, 1001)]

plt.scatter(x, y, c=y, cmap=plt.cm.Blues, edgecolors='none', s=40)
plt.title("Suqare Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square Value", fontsize=14)
plt.tick_params(axis='both', which='major', labelsize=14)

plt.axis([0, 1100, 0, 1100000])
# plt.show()
plt.savefig("squares_plot.png", bbox_inches="tight")