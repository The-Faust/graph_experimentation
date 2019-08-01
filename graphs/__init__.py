from collections import namedtuple

Edge = namedtuple('Edge', 'start, end, cost')
inf = float('inf')


def make_edge(start, end, cost=1):
    return Edge(start, end, cost)


def generate_vertices(edges_list):
    return set(sum(([edge.start, edge.end] for edge in edges_list), []))


def generate_neighbours(vertices_list, edges_list):
    neighbours = {vertex: set() for vertex in vertices_list}
    for edge in edges_list:
        neighbours[edge.start].add((edge.end, edge.cost))
    return neighbours
