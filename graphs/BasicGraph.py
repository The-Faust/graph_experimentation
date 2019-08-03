"""
Simple graph where an edge is a set of 2 vertices with a weight
    for example if point a -> b and the cost of going from a to b is 3 the edge is ("a", "b", 3)
"""
from graphs import make_edge, generate_vertices, generate_neighbours
from graphs.graph_algorithms._Dijkstra import _Dijkstra
from graphs.graph_algorithms._BellmanFord import _BellmanFord
from graphs._GraphUtilities import _GraphUtilities


class BasicGraph(_Dijkstra, _BellmanFord, _GraphUtilities):
    def __init__(self, edges):
        invalid_edges = [edge for edge in edges if len(edge) not in [2, 3]]
        if invalid_edges:
            raise ValueError("Invalid edges submitted: {}".format(invalid_edges))

        self.edges = [make_edge(*edge) for edge in edges]
        self.vertices = generate_vertices(self.edges)
        self.neighbours = generate_neighbours(self.vertices, self.edges)

    def _update_vertices(self):
        self.vertices = generate_vertices(self.edges)

    def _update_neighbours(self):
        self.neighbours = generate_neighbours(self.vertices, self.edges)

    def get_node_pairs(self, node_1, node_2, both_ends=True):
        if both_ends:
            node_pairs = [[node_1, node_2], [node_2, node_1]]
        else:
            node_pairs = [[node_1, node_2]]
        return node_pairs

    def remove_edge(self, node_1, node_2, both_ends=True):
        node_pairs = self.get_node_pairs(node_1, node_2, both_ends)
        edges = self.edges[:]
        for edge in edges:
            if [edge.start, edge.end] in node_pairs:
                self.edges.remove(edge)

        self._update_vertices()
        self._update_neighbours()

    def add_edge(self, node_1, node_2, cost=1, both_ends=True):
        node_pairs = self.get_node_pairs(node_1, node_2, both_ends)
        for edge in self.edges:
            if [edge.start, edge.end] in node_pairs:
                raise ValueError("Edge {} {} already exists".format(node_1, node_2))

        new_edge = (node_1, node_2, cost)
        self.edges.append(make_edge(*new_edge))

        self._update_vertices()
        self._update_neighbours()
