import math


class Node:
    def __init__(self, identifier):
        self.routes = []  # (id, distance)
        self.identifier = identifier


class Graph:
    def __init__(self):
        self.nodes = {}  # identifier, node

    def read_standard_input(self):
        self.start_id = input()  # start id
        nb_nodes = int(input())
        for _ in range(nb_nodes):
            identifier = input()
            self.nodes[identifier] = Node(identifier)

        nb_routes = int(input())
        for _ in range(nb_routes):
            route = input().split(" ")
            identifier1 = route[0]
            identifier2 = route[1]
            distance = int(route[2])
            self.nodes[identifier1].routes.append((identifier2, distance))
            self.nodes[identifier2].routes.append((identifier1, distance))

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
            for (neighbor_id, distance) in self.nodes[min_id].routes:
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
graph.read_standard_input()
graph.solve()
