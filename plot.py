import operator

import matplotlib.pyplot as plt
import matplotlib.animation as anim


class Plotter():
    def __init__(self, gen_func):
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(1, 1, 1)
        self.gen_func = gen_func

    def update(self, data):
        points, path = data
        self.ax.clear()
        x = []
        y = []
        for point in points:
            x.append(point[0])
            y.append(point[1])
        # noinspection PyUnusedLocal
        y = list(map(operator.sub, [max(y) for i in range(len(points))], y))
        self.ax.plot(x, y, 'co')

        for _ in range(1, len(path)):
            i = path[_ - 1]
            j = path[_]
            # noinspection PyUnresolvedReferences
            self.ax.arrow(x[i], y[i], x[j] - x[i], y[j] - y[i],
                          color='r', length_includes_head=True)
        self.ax.set_xlim(0, max(x) * 1.1)
        self.ax.set_ylim(0, max(y) * 1.1)
        # # noinspection PyTypeChecker
        # self.ax.xlim(0, max(x) * 1.1)
        # # noinspection PyTypeChecker
        # self.ax.ylim(0, max(y) * 1.1)

    def plot(self):
        a = anim.FuncAnimation(self.fig, self.update, self.gen_func)
        plt.show()
