from collections import defaultdict

from config import MAX_INT
from graph import WeightedDirectedGraph, WeightedEdge
from priority_queue import MinPriorityQueue, PriorityNode


def Dijkstra(graph: WeightedDirectedGraph, source_node):
    shortest_distances = defaultdict(lambda: MAX_INT)
    shortest_distances[source_node] = 0
    predecessors = defaultdict(lambda: None)

    adjacency_list = graph.get_adjacency_list()
    min_queue = MinPriorityQueue()
    current_node = PriorityNode(source_node, 0)
    while current_node is not None:
        current_node_name = current_node.name
        for node in graph.nodes:
            if node in adjacency_list[current_node_name].keys() and shortest_distances[node] > (shortest_distances[current_node_name] + adjacency_list[current_node_name][node]):
                new_shortest_distance = shortest_distances[current_node_name] + adjacency_list[current_node_name][node]
                shortest_distances[node] = new_shortest_distance
                predecessors[node] = current_node_name
                min_queue.push(node, new_shortest_distance)
        current_node = min_queue.pop()
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
