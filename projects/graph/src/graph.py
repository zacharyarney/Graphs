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

    def add_edge(self, v1, v2):
        if not self.vertices[v1] and not self.vertices[v2]:
            raise IndexError('Vertex does not exist.')
        else:
            self.vertices[v1].add(v2)
            self.vertices[v2].add(v1)

    def add_directed_edge(self, v1, v2):
        if not self.vertices[v1] and not self.vertices[v2]:
            print('error: no vertext')
        else:
            self.vertices[v1].add(v2)

    def bft(self, start):
        queue = [start]
        visited = set()
        output = []
        while len(queue) > 0:
            popped = queue.pop(0)
            visited.add(popped)
            output.append(popped)
            for v in self.vertices[popped]:
                if v not in queue and v not in visited:
                    queue.append(v)
        print(f'PATH: {output}')

    def dft(self, start):
        stack = [start]
        visited = set()
        output = []
        while len(stack) > 0:
            popped = stack.pop()
            visited.add(popped)
            output.append(popped)
            for v in self.vertices[popped]:
                if v not in stack and v not in visited:
                    stack.append(v)
        print(f'PATH: {output}')

    def recursive_dft(self, start, target, visited=set(), path=[]):
        visited = set()
        visited.add(start)
        path += [start]
        if start == target:
            return path
        for neighbor in self.vertices[start]:
            if neighbor not in visited:
                new_path = recursive_dft(neighbor, target, visited, path)
                if new_path:
                    return new_path
        return None

    def bfs(self, start, target):
        queue = [start]
        visited = set()
        while len(queue) > 0:
            path = queue.pop(0)  # path = [start]
            v = path[-1]
            if v not in visited:
                if v == target:
                    return path
                visited.add(v)
                for neighbor in self.vertices[v]:
                    new_path = list(path)
                    new_path.append(neighbor)
                    queue.append(new_path)


# [ ]
# {1, 5, 2, 4, 3, 6 }
g = Graph()
g.dft('1')
