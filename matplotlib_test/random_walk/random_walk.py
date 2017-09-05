from random import choice

class RandomWalk():
    def __init__(self, num_points=5000):
        self.num_points = num_points

        # 设置x, y坐标，初始都为0
        self.x_label = [0]
        self.y_label = [0]

    def fill_walk(self):
        while len(self.x_label) < self.num_points:
            x_direction = choice([-1, 1])
            x_distance = choice([1, 2, 3, 4])
            x_step = x_direction * x_distance

            y_direction = choice([-1, 1])
            y_distance = choice([1, 2, 3, 4])
            y_step = y_direction * y_distance

            next_x = self.x_label[-1] + x_step
            next_y = self.y_label[-1] + y_step

            self.x_label.append(next_x)
            self.y_label.append(next_y)