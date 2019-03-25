

class _GraphUtilities:

    def print_edges(self):
        print("edges are: ")
        for edge in self.edges:
            print(edge)
        print()

    def print_vertices(self):
        print("vertices are: ")
        for vertex in self.vertices:
            print(vertex)
        print()

    def print_neighbours(self, vertex):
        print(vertex, "neighbours  are: \n",
              self.neighbours[vertex])
        print()
