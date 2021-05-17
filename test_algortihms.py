import pytest
from numpy import inf
from bellman_ford import *
from dijkstra import *

# ----------------------------------------------------------------------------------------------------------------
from johnsons import JohnsonAlgorithm

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


# ----------------------------------------------------------------------------------------------------------------


@pytest.mark.parametrize("graph,starting_node", [(negative_cycle_graph_1, 'A'), (negative_cycle_graph_2, 'A')])
def test_negative_cycle(graph: WeightedDirectedGraph, starting_node):
    with pytest.raises(Exception) as e:
        BellmanFord(graph, starting_node)
    assert 'Graph contains negative cycle' == str(e.value)


# ----------------------------------------------------------------------------------------------------------------
directed_weighted_graph_1 = WeightedDirectedGraph([
    WeightedEdge('A', 0, 'B'),
    WeightedEdge('B', 1, 'C'),
    WeightedEdge('B', 1, 'D'),
    WeightedEdge('C', -1, 'A'),
    WeightedEdge('C', 2, 'D'),
    WeightedEdge('C', 2, 'E'),
    WeightedEdge('E', -3, 'D'),
])
solution_1 = ({'A': 0, 'B': 0, 'C': 1, 'D': 0, 'E': 3}, {'A': None, 'B': 'A', 'C': 'B', 'D': 'E', 'E': 'C'})
# ----------------------------------------------------------------------------------------------------------------
directed_weighted_graph_2 = WeightedDirectedGraph([
    WeightedEdge('A', 0, 'B'),
    WeightedEdge('B', 1, 'C'),
    WeightedEdge('C', -1, 'A'),
    WeightedEdge('C', 2, 'D'),
    WeightedEdge('C', 2, 'E')
])
solution_2 = ({'A': 0, 'B': 0, 'C': 1, 'D': 3, 'E': 3}, {'A': None, 'B': 'A', 'C': 'B', 'D': 'C', 'E': 'C'})
# ----------------------------------------------------------------------------------------------------------------
directed_weighted_graph_3 = WeightedDirectedGraph([
    WeightedEdge('A', 0, 'B'),
    WeightedEdge('B', 1, 'C'),
    WeightedEdge('B', 1, 'D'),
    WeightedEdge('C', -1, 'A'),
    WeightedEdge('C', 2, 'D'),
    WeightedEdge('C', 2, 'E')
])
solution_3 = ({'A': 0, 'B': 0, 'C': 1, 'D': 1, 'E': 3}, {'A': None, 'B': 'A', 'C': 'B', 'D': 'B', 'E': 'C'})
# ----------------------------------------------------------------------------------------------------------------
directed_weighted_graph_4 = WeightedDirectedGraph([
    WeightedEdge('A', 2, 'B'),
    WeightedEdge('B', 1, 'C'),
    WeightedEdge('B', -4, 'D'),
    WeightedEdge('C', 1, 'A'),
    WeightedEdge('A', 1, 'C')
])
solution_4 = ({'A': 0, 'B': 2, 'C': 1, 'D': -2}, {'A': None, 'B': 'A', 'C': 'A', 'D': 'B'})
# ----------------------------------------------------------------------------------------------------------------
directed_weighted_graph_5 = WeightedDirectedGraph([
    WeightedEdge('A', 2, 'B'),
    WeightedEdge('B', 1, 'C'),
    WeightedEdge('B', 2, 'D'),
    WeightedEdge('A', 1, 'C'),
    WeightedEdge('C', 2, 'E'), WeightedEdge('B', 1, 'E'), WeightedEdge('D', -2, 'E'),
])
solution_5 = ({'A': 0, 'B': 2, 'C': 1, 'D': 4, 'E': 2}, {'A': None, 'B': 'A', 'C': 'A', 'D': 'B', 'E': 'D'})
# ----------------------------------------------------------------------------------------------------------------
directed_weighted_graph_6 = WeightedDirectedGraph(
    [
        WeightedEdge('B', 3, 'D'),
        WeightedEdge('A', 2, 'C')
    ]
)
solution_6 = ({'A': 0, 'B': inf, 'C': 2, 'D': inf}, {'A': None, 'B': None, 'C': 'A', 'D': None})


# ----------------------------------------------------------------------------------------------------------------

@pytest.mark.parametrize("graph,starting_node,correct_solution",
                         [(directed_weighted_graph_1, 'A', solution_1), (directed_weighted_graph_2, 'A', solution_2),
                          (directed_weighted_graph_3, 'A', solution_3), (directed_weighted_graph_4, 'A', solution_4),
                          (directed_weighted_graph_5, 'A', solution_5), (directed_weighted_graph_6, 'A', solution_6)])
def test_non_negative_cycle_BELLMAN_FORD(graph: WeightedDirectedGraph, starting_node, correct_solution):
    (correct_shortest_distance, correct_predecessors) = correct_solution
    (shortest_distances, predecessors) = BellmanFord(graph, starting_node)
    shortest_distance_test = all(result for result in
                                 [correct_shortest_distance[node] == shortest_distances[node] for node in
                                  correct_shortest_distance])
    predecessors_test = all(
        result for result in [correct_predecessors[node] == predecessors[node] for node in correct_predecessors])
    assert shortest_distance_test and predecessors_test


# ----------------------------------------------------------------------------------------------------------------
@pytest.mark.parametrize("graph,starting_node,correct_solution",
                         [(directed_weighted_graph_1, 'A', solution_1), (directed_weighted_graph_2, 'A', solution_2),
                          (directed_weighted_graph_3, 'A', solution_3), (directed_weighted_graph_4, 'A', solution_4),
                          (directed_weighted_graph_5, 'A', solution_5), (directed_weighted_graph_6, 'A', solution_6)])
def test_non_negative_cycle_DIJKSTRA(graph: WeightedDirectedGraph, starting_node, correct_solution):
    (correct_shortest_distance, correct_predecessors) = correct_solution
    (shortest_distances, predecessors) = Dijkstra(graph, starting_node)
    shortest_distance_test = all(result for result in
                                 [correct_shortest_distance[node] == shortest_distances[node] for node in
                                  correct_shortest_distance])
    predecessors_test = all(
        result for result in [correct_predecessors[node] == predecessors[node] for node in correct_predecessors])
    assert shortest_distance_test and predecessors_test


# ----------------------------------------------------------------------------------------------------------------


johnsons_graph_1 = WeightedDirectedGraph(
    [
        WeightedEdge('A', -3, 'B'),
        WeightedEdge('A', 1, 'C'),
        WeightedEdge('A', -3, 'E'),
        WeightedEdge('B', -2, 'D'),
        WeightedEdge('B', 2, 'C'),
        WeightedEdge('C', -4, 'D'),
        WeightedEdge('E', 4, 'D')
    ]
)

johnsons_solution_1 = {'A': {'A': 0, 'B': -3, 'C': -1, 'E': -3, 'D': -5},
                       'D': {'D': 0, 'A': inf, 'B': inf, 'C': inf, 'E': inf},
                       'E': {'E': 0, 'D': 4, 'C': inf, 'B': inf, 'A': inf},
                       'C': {'C': 0, 'D': -4, 'A': inf, 'B': inf, 'E': inf},
                       'B': {'B': 0, 'D': -2, 'C': 2, 'E': inf, 'A': inf}}

johnsons_graph_2 = WeightedDirectedGraph(
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
johnsons_graph_3 = WeightedDirectedGraph(
    [
        WeightedEdge('A', -5, 'B'),
        WeightedEdge('A', 2, 'C'),
        WeightedEdge('A', 6, 'D')
    ]
)

johnsons_solution_3 = {'A': {'A': 0, 'B': -5, 'C': 2, 'D': 6},
                       'B': {'A': inf, 'B': 0, 'C': inf, 'D': inf},
                       'C': {'A': inf, 'B': inf, 'C': 0, 'D': inf},
                       'D': {'A': inf, 'B': inf, 'C': inf, 'D': 0},
                       }

johnsons_graph_4 = WeightedDirectedGraph(
    [
        WeightedEdge('A', -5, 'B'),
        WeightedEdge('A', 2, 'C'),
        WeightedEdge('A', 6, 'D'),
        WeightedEdge('B', -1, 'C'),
        WeightedEdge('B', -2, 'D'),
        WeightedEdge('D', 0, 'C'),
    ]
)

johnsons_solution_4 = {'A': {'A': 0, 'B': -5, 'C': -7, 'D': -7},
                       'B': {'A': inf, 'B': 0, 'C': -2, 'D': -2},
                       'C': {'A': inf, 'B': inf, 'C': 0, 'D': inf},
                       'D': {'A': inf, 'B': inf, 'C': 0, 'D': 0},
                       }


@pytest.mark.parametrize("graph,correct_solution",
                         [(johnsons_graph_1, johnsons_solution_1), (johnsons_graph_3, johnsons_solution_3)
                          , (johnsons_graph_4, johnsons_solution_4)])
def test_johsons(graph: WeightedDirectedGraph, correct_solution):
    result = JohnsonAlgorithm(graph)
    print(result)
    assert result == correct_solution


@pytest.mark.parametrize("graph", [(johnsons_graph_2)])
def test_johnsons_negative_cycle(graph: WeightedDirectedGraph):
    assert 'Graph contains negative cycle' == JohnsonAlgorithm(graph)
