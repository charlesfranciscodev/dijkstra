import math


class Graph:
    def __init__(self):
        self.nodes = {}  # identifier, routes

    def read_input(self):
        self.start_id = input()
        nb_nodes = int(input())
        for _ in range(nb_nodes):
            identifier = input()
            self.nodes[identifier] = []

        nb_routes = int(input())
        for _ in range(nb_routes):
            identifier1, identifier2, distance = input().split()
            distance = int(distance)
            self.nodes[identifier1].append((identifier2, distance))
            self.nodes[identifier2].append((identifier1, distance))

    def search(self, start_id):
        """Compute the shortest path between start and end using Dijkstra.
        Reference: https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm
        """
        opened = set()
        parents = {}  # identifier: parent_id
        distances = {}  # identifier: distance
        for identifier in self.nodes.keys():
            distances[identifier] = math.inf
            parents[identifier] = None
            opened.add(identifier)
        distances[start_id] = 0

        while (len(opened) != 0):
            min_id = self.minimum(opened, distances)
            opened.remove(min_id)
            for (neighbor_id, distance) in self.nodes[min_id]:
                alt_distance = distances[min_id] + distance
                if (alt_distance < distances[neighbor_id]):
                    distances[neighbor_id] = alt_distance
                    parents[neighbor_id] = min_id
        return parents, distances

    def minimum(self, opened, distances):
        min_id = None
        min_dist = math.inf
        for identifier in opened:
            distance = distances[identifier]
            if (distance < min_dist):
                min_id = identifier
                min_dist = distance
        return min_id

    def solve(self):
        parents, distances = self.search(self.start_id)
        print(parents)
        print(distances)


graph = Graph()
graph.read_input()
graph.solve()
