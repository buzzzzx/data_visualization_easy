import matplotlib.pyplot as plt

from random_walk import RandomWalk

while True:
    rw = RandomWalk(50000)
    rw.fill_walk()

    plt.figure(dpi=128, figsize=(10, 6))

    point_num = list(range(rw.num_points))
    plt.scatter(rw.x_label, rw.y_label, c=point_num, cmap=plt.cm.Blues,
                edgecolors='none', s=15)

    plt.scatter(0, 0, c='green', edgecolors='none', s=100)
    plt.scatter(rw.x_label[-1], rw.y_label[-1], c='red', edgecolors='none', s=100)

    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    plt.title("Random Walk", fontsize=24)
    # plt.xlabel("Value", fontsize=14)
    # plt.ylabel("Square Value", fontsize=14)
    # plt.savefig("random_walk.png", bbox_inches="tight")
    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break