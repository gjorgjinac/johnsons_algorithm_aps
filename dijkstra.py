from collections import defaultdict

from config import MAX_INT
from graph import WeightedDirectedGraph, WeightedEdge
from priority_queue import PriorityNode, MinHeap


def init_min_heap_with_nodes(source_node, graph):
    min_heap = MinHeap()
    min_heap.heap.append(PriorityNode(source_node, 0))

    for index, node in enumerate(list(set(graph.nodes).difference({source_node}))):
        min_heap.heap.append(PriorityNode(node, MAX_INT))
        min_heap.node_position[node] = index + 1

    min_heap.node_position[source_node] = 0
    min_heap.update_priority(source_node, 0)
    min_heap.size = graph.node_count
    return min_heap


def Dijkstra(graph: WeightedDirectedGraph, source_node, verbose=True):
    shortest_distances = defaultdict(lambda: MAX_INT)
    shortest_distances[source_node] = 0
    predecessors = defaultdict(lambda: None)
    adjacency_list = graph.get_adjacency_list()
    min_heap = init_min_heap_with_nodes(source_node, graph)

    while not min_heap.is_empty():
        current_node_name=min_heap.pop_min().name
        for node in adjacency_list[current_node_name].keys():
            new_distance = shortest_distances[current_node_name] + adjacency_list[current_node_name][node]
            if shortest_distances[node] > new_distance:
                shortest_distances[node] = new_distance
                predecessors[node] = current_node_name
                min_heap.update_priority(node, new_distance)
    if verbose:
        for node in sorted(graph.nodes):
            print(f'Node {node}: {str(shortest_distances[node])} through {predecessors[node]}')
    return shortest_distances, predecessors

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
