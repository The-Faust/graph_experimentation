from collections import namedtuple

Edge = namedtuple('Edge', 'start, end, cost')
inf = float('inf')


def make_edge(start, end, cost=1):
    return Edge(start, end, cost)
