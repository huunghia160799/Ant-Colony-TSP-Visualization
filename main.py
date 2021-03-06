import math

from aco import ACO, Graph
from plot import Plotter
import argparse


def distance(city1: dict, city2: dict):
    return math.sqrt((city1['x'] - city2['x']) ** 2 + (city1['y'] - city2['y']) ** 2)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", help="Data file to use", choices=["chn31", "chn144", "att48"], default="chn31")
    args = parser.parse_args()

    cities = []
    points = []
    with open(f'./data/{args.file}.txt') as f:
        for line in f.readlines():
            city = line.split(' ')
            cities.append(dict(index=int(city[0]), x=int(city[1]), y=int(city[2])))
            points.append((int(city[1]), int(city[2])))
    cost_matrix = []
    rank = len(cities)
    for i in range(rank):
        row = []
        for j in range(rank):
            row.append(distance(cities[i], cities[j]))
        cost_matrix.append(row)
    aco = ACO(10, 100, 1.0, 10.0, 0.5, 10, 2, args)
    graph = Graph(cost_matrix, rank)
    aco.add_graph(graph)
    # path, cost = aco.solve(graph)
    # print('cost: {}, path: {}'.format(cost, path))
    plotter = Plotter(aco.solve)
    plotter.plot()
    # plot(points, path)

if __name__ == '__main__':
    main()
