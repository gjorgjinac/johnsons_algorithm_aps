from collections import defaultdict

from config import MAX_INT
from graph import WeightedDirectedGraph, WeightedEdge
from priority_queue import MinPriorityQueue


class NoNeighboursException(Exception):
    pass


def find_closest_node(distances, visited):
    minimum_distance, closest_node = MAX_INT, None
    for node in distances.keys():
        if minimum_distance > distances[node] and not visited[node]:
            minimum_distance, closest_node = distances[node], node
    return closest_node


def Dijkstra(graph: WeightedDirectedGraph, source_node):
    visited = defaultdict(lambda: False)
    shortest_distances = defaultdict(lambda: MAX_INT)
    shortest_distances[source_node] = 0
    predecessors = defaultdict(lambda: None)

    adjacency_matrix = graph.get_adjacency_matrix()
    min_queue = MinPriorityQueue()

    min_queue.push(source_node, 0)

    for count in range(graph.node_count):
        current_node = min_queue.pop()
        if current_node is None:
            print(
                f'Cannot find paths to all nodes from node {source_node}. Found outgoing edges to nodes: {adjacency_matrix[source_node].keys()}')
            return
        current_node = current_node.name
        visited[current_node] = True
        for node in graph.nodes:
            if not visited[node] and node in adjacency_matrix[current_node].keys():
                if shortest_distances[node] > (shortest_distances[current_node] + adjacency_matrix[current_node][node]):
                    new_shortest_distance = shortest_distances[current_node] + adjacency_matrix[current_node][node]
                    shortest_distances[node] = new_shortest_distance
                    predecessors[node] = current_node
                    min_queue.push(node, new_shortest_distance)
    print(f'Dijkstra from source node {source_node}')
    for node in sorted(graph.nodes):
        print(f'Node {node}: {str(shortest_distances[node])} through {predecessors[node]}')


if __name__ == '__main__':
    dijkstra_graph = WeightedDirectedGraph(
        [
            WeightedEdge('A', 3, 'B'),
            WeightedEdge('A', 2, 'C'),
            WeightedEdge('B', 2, 'E'),
            WeightedEdge('B', 4, 'D'),
            WeightedEdge('C', 2, 'D'),
            WeightedEdge('C', 6, 'B'),
            WeightedEdge('D', 6, 'E'),
            WeightedEdge('D', 3, 'F'),
            WeightedEdge('E', 1, 'F'),
        ]
    )
    Dijkstra(dijkstra_graph, 'A')
