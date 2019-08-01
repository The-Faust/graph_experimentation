"""
Since this is a rather small project I do not use a test framework,
I'll test most of what I need to test in the main to show how to use the class BasicGraph
"""

from graphs.BasicGraph import BasicGraph


def main():
    graph = BasicGraph([
        ("a", "b", 7), ("a", "c", 9), ("a", "f", 14), ("b", "c", 10),
        ("b", "d", 15), ("c", "d", 11), ("c", "f", 2), ("d", "e", 6),
        ("e", "f", 9)])

    graph.print_edges()
    graph.print_vertices()

    for vertex in graph.vertices:
        graph.print_neighbours(vertex)

    print("Shortest way from point a to e is: ", *graph.dijkstra("a", "e"))


if __name__=="__main__":
    main()
