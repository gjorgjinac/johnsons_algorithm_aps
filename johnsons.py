from bellman_ford import BellmanFord
from dijkstra import Dijkstra
from graph import WeightedDirectedGraph, WeightedEdge

def JohnsonAlgorithm(graph: WeightedDirectedGraph):
    graph_edges_with_extra_node = graph.edges + [WeightedEdge('new_node', 0, node) for node in graph.nodes]
    graph_with_extra_node = WeightedDirectedGraph(graph_edges_with_extra_node)
    shortest_distances, predecessors = BellmanFord(graph_with_extra_node, 'new_node')
    for edge in graph.edges:
        edge.weight = edge.weight + shortest_distances[edge.head] - shortest_distances[edge.tail]

    for source_node in graph.nodes:
        print('\nShortest Distance with vertex ' + str(source_node) + ' as the source:\n')
        Dijkstra(graph, source_node)




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
JohnsonAlgorithm(johnson_graph2)
