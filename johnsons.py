from bellman_ford import BellmanFord
from dijkstra import Dijkstra
from graph import WeightedDirectedGraph, WeightedEdge

def JohnsonAlgorithm(graph: WeightedDirectedGraph, verbose=True):
    graph_edges_with_extra_node = graph.edges + [WeightedEdge('new_node', 0, node) for node in graph.nodes]
    graph_with_extra_node = WeightedDirectedGraph(graph_edges_with_extra_node.copy())
    try:
        bf_shortest_distances, predecessors = BellmanFord(graph_with_extra_node, 'new_node', verbose=False)
    except Exception as e:
        return str(e)
    for edge in graph.edges:
        edge.weight = edge.weight + bf_shortest_distances[edge.head] - bf_shortest_distances[edge.tail]
    all_pairs_shortest_distance={}
    for source_node in graph.nodes:
        if verbose:
            print('\nShortest Distance with vertex ' + str(source_node) + ' as the source:\n')
        dijkstra_shortest_distances, predecessors = Dijkstra(graph, source_node, verbose=verbose)
        dijkstra_shortest_distances = {k:(v+bf_shortest_distances[k] - bf_shortest_distances[source_node]) for k,v in dijkstra_shortest_distances.items()}
        all_pairs_shortest_distance[source_node]=dijkstra_shortest_distances
    return all_pairs_shortest_distance





johnson_graph = WeightedDirectedGraph([
    WeightedEdge('A', -5, 'B'),
    WeightedEdge('A', 2, 'C'),
    WeightedEdge('A', 3, 'D'),
    WeightedEdge('B', 4, 'C'),
    WeightedEdge('C', 1, 'D')
])

johnson_graph2 = WeightedDirectedGraph([
    WeightedEdge('1', 8, '2'),
    WeightedEdge('1', 6, '6'),
    WeightedEdge('6', 3, '2'),
    WeightedEdge('2', -1, '3'),
    WeightedEdge('3', -2, '6'),
    WeightedEdge('6',-2,'5'),
    WeightedEdge('5',2, '4'),
    WeightedEdge('3',3,'4')
])

johnsons_graph_1 = WeightedDirectedGraph(
    [
        WeightedEdge('A', -3, 'B'),
        WeightedEdge('A', 1, 'C'),
        WeightedEdge('A', -3, 'E'),
        WeightedEdge('B', -2, 'D'),
        WeightedEdge('B', 2, 'C'),
        WeightedEdge('C', -4, 'D'),
        WeightedEdge('D', -8, 'A'),
        WeightedEdge('E', 4, 'D')
    ]
)
print(JohnsonAlgorithm(johnsons_graph_1, verbose=False))
