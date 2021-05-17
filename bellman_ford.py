from config import MAX_INT
from graph import WeightedDirectedGraph, WeightedEdge

def BellmanFord(graph: WeightedDirectedGraph, starting_node, verbose=True):
    shortest_distances = {node: MAX_INT for node in graph.nodes}
    shortest_distances[starting_node] = 0
    predecessors = {node: None for node in graph.nodes}

    for i in range(graph.node_count):
        for edge in graph.edges:
            if shortest_distances[edge.head] != MAX_INT and shortest_distances[edge.head] + edge.weight < \
                    shortest_distances[edge.tail]:
                shortest_distances[edge.tail] = shortest_distances[edge.head] + edge.weight
                predecessors[edge.tail] = edge.head
    if verbose:
        print('Bellman Ford')
    for edge in graph.edges:
        if shortest_distances[edge.head] != MAX_INT and shortest_distances[edge.head] + edge.weight < \
                shortest_distances[edge.tail]:
            print('Graph contains negative cycle')
            raise Exception('Graph contains negative cycle')
    if verbose:
        for node in sorted(graph.nodes):
            print(f'Node {node}: {str(shortest_distances[node])} through {predecessors[node]}')
    return shortest_distances, predecessors


if __name__ == '__main__':
    bellman_ford_graph = WeightedDirectedGraph([
        WeightedEdge('S', -1, 'A'),
        WeightedEdge('S', 4, 'B'),
        WeightedEdge('A', 3, 'B'),
        WeightedEdge('A', 2, 'D'),
        WeightedEdge('A', 2, 'C'),
        WeightedEdge('C', 5, 'B'),
        WeightedEdge('C', 1, 'A'),
        WeightedEdge('D', -3, 'C')
    ])

    negative_cycle_graph_1 = WeightedDirectedGraph([
        WeightedEdge('A', 1, 'B'),
        WeightedEdge('B', 0, 'C'),
        WeightedEdge('B', 1, 'D'),
        WeightedEdge('C', -2, 'A')
    ])
    # ----------------------------------------------------------------------------------------------------------------
    negative_cycle_graph_2 = WeightedDirectedGraph([
        WeightedEdge('A', 2, 'B'),
        WeightedEdge('B', 0, 'C'),
        WeightedEdge('B', 1, 'D'),
        WeightedEdge('C', -2, 'A'),
        WeightedEdge('D', -7, 'A'),
    ])

    BellmanFord(negative_cycle_graph_2,'A')