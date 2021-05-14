from typing import List


class WeightedEdge:
    def __init__(self, head, weight, tail):
        self.head = head
        self.tail = tail
        self.weight = weight


class WeightedDirectedGraph:
    def __init__(self, edges: List[WeightedEdge]):
        self.nodes = set([e.head for e in edges] + [e.tail for e in edges])
        self.edges = edges
        self.node_count = len(self.nodes)

    def get_adjacency_matrix(self):
        adjacency_matrix = {n2: {} for n2 in self.nodes}
        for edge in self.edges:
            adjacency_matrix[edge.head][edge.tail] = edge.weight
        return adjacency_matrix

    def print_edges(self):
        [print(f"{e.head}-{e.weight}-{e.tail}") for e in self.edges]
