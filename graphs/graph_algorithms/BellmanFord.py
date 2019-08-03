"""
Bellman Ford algorithm applied to the BasicGraph class

I chose to split the graph class in mixins classes so
that it is much easier to take the algorithms separately from the structure

As of now BellmanFord returns only the minimum distance between source and destination.
I intend to find the path from the distances list "variable = dist" later-on.
"""
from numpy import full
from graphs import inf, get_vertices_index_book
from graphs.graph_algorithms import source_dest_in_graph


class BellmanFord(object):
    def bellman_ford(self, source, destination):
        # Because of how my graph is made and vertices have actual names instead of being numbers.
        # I have to initialize a dictionnary that will give me positions of said vertices in vertices list
        vertices_index_book = get_vertices_index_book(self)

        assert source_dest_in_graph(self, source, destination)

        number_of_vertices = len(self.vertices)
        number_of_edges = len(self.edges)

        # 1. Initialize distance from source to all other vertices to infinite.
        dist = full(number_of_vertices, inf)
        dist[vertices_index_book[source]] = 0

        # 2. Relax all edges for a number of times equal to ((number of vertices) - 1).
        # Let's remind you that the shortest path from source to any other vertex in the graph
        # can have at most ((number of vertices) - 1) edges.
        for i in range(number_of_vertices - 1):

            for edge in self.edges:
                start = vertices_index_book[edge.start]
                end = vertices_index_book[edge.end]
                cost = edge.cost

                if dist[start] != inf and dist[start] + cost < dist[end]:
                    dist[end] = dist[start] + cost

        # 3. check for negative weight cycles.
        # Stap 2 guarantees shortest path if the graph doesn't contain negative cycles.
        # If we get a shorter path then there is a cycle
        for edge in self.edges:
            start = vertices_index_book[edge.start]
            end = vertices_index_book[edge.end]
            cost = edge.cost
            if dist[start] != inf and dist[start] + cost < dist[end]:
                raise ValueError("The graph contains a negative cycle")

        return dist[vertices_index_book[destination]]
