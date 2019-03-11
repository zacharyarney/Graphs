"""
Simple graph implementation
"""


class Graph:
    """
    Represent a graph as a dictionary of vertices mapping labels to edges.
    """

    def __init__(self):
        self.vertices = self.vertices = {
            "1": {"2", "3"},
            "2": {"4", "5", "1"},
            "3": {"6", "7", "1"},
            "4": {"2", "8", "9"},
            "5": {"2", "10", "11"},
            "6": {"3", "12", "13"},
            "7": {"3", "14", "15"},
            "8": {"4"},
            "9": {"4"},
            "10": {"5"},
            "11": {"5"},
            "12": {"6"},
            "13": {"6"},
            "14": {"7"},
            "15": {"8"}
            }

    def add_vertex(self, vertex):
        self.vertices[vertex] = set()

    def add_edge(self, key, value):
        if not self.vertices[key] and not self.vertices[value]:
            raise IndexError('Vertex does not exist.')
        else:
            self.vertices[key].add(value)
            self.vertices[value].add(key)

    def add_directed_edge(self, key, value):
        if not self.vertices[key] and not self.vertices[value]:
            print('error: no vertext')
        else:
            self.vertices[key].add(value)

    def bft(self, start):
        queue = [start]
        visited = set()
        output = []
        while len(queue) > 0:
            for v in self.vertices[queue[0]]:
                if v not in queue and v not in visited:
                    queue.append(v)
            popped = queue.pop(0)
            visited.add(popped)
            output.append(popped)
        print(f'PATH: {output}')


# [ ]
# {1, 5, 2, 4, 3, 6 }
g = Graph()
g.bft('1')
