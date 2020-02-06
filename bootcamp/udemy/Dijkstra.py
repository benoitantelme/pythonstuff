import sys
from queue import PriorityQueue


class Node:
    def __init__(self, name):
        self.name = name
        self.distance = sys.maxsize
        self.visited = False
        self.adjacent = dict()
        self.shortest = []

    def __str__(self):
        return f'Node {self.name}'

    def __repr__(self):
        return self.__str__()

    def __lt__(self, other):
        return self.distance < other.distance

    def __le__(self, other):
        return self.distance <= other.distance

    def __gt__(self, other):
        return self.distance > other.distance

    def __ge__(self, other):
        return self.distance >= other.distance

    def add_edge(self, destination, distance):
        self.adjacent[destination] = distance

    def compare(self, other):
        return self.distance - other.distance

    def update_minimum_distance(self, node, edge_weight):
        if self.distance + edge_weight < node.distance:
            node.distance = self.distance + edge_weight
            node.shortest = self.shortest.copy()
            node.shortest.append(self)


def print_graph(graph):
    for node in graph:
        print(f'Node {node.name} with distance {node.distance} and shortest path {str(node.shortest)}')


def calculate_shortest_path(node):
    node.distance = 0

    added_nodes = {node}
    unsettled_nodes = PriorityQueue()
    unsettled_nodes.put(node, node.distance)

    while not unsettled_nodes.empty():
        current = unsettled_nodes.get()
        added_nodes.remove(current)

        for neighbour, distance in current.adjacent.items():
            if not neighbour.visited:
                current.update_minimum_distance(neighbour, distance)
                if neighbour not in added_nodes:
                    unsettled_nodes.put(neighbour, neighbour.distance)
                    added_nodes.add(neighbour)

        current.visited = True


a = Node('A')
b = Node('B')
c = Node('C')
d = Node('D')
e = Node('E')
f = Node('F')

a.add_edge(b, 10)
a.add_edge(c, 15)

b.add_edge(d, 12)
b.add_edge(f, 15)

c.add_edge(e, 10)

d.add_edge(e, 2)
d.add_edge(f, 1)

f.add_edge(e, 5)

graph = {a, b, c, d, e, f}

print_graph(graph)
calculate_shortest_path(a)
print_graph(graph)
