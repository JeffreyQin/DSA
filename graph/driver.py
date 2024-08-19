from graphs import Directed_Graph, Undirected_Graph, Undirected_Weighted_Graph
from topological_sort import topo_sort, kahn
from dijkstra_heap import dijkstra_heap
from min_dist import dijkstra
from min_dist_negative_weight import bellman_ford
from min_spanning_tree import prim

def test_prim():

    edges = [
        [0,1,4],
        [0,7,8],
        [1,7,11],
        [1,2,8],
        [2,8,2],
        [8,6,6],
        [7,8,7],
        [7,6,1],
        [2,3,7],
        [2,5,4],
        [6,5,2],
        [3,5,14],
        [3,4,9],
        [5,4,10]
    ]

    undirected_weighted_graph = Undirected_Weighted_Graph()
    for edge in edges:
        undirected_weighted_graph.add_edge(edge)

    graph = undirected_weighted_graph.get_graph()
    result = prim(graph, 0)
    print(result)



def test_dijkstra():

    edges = [[1,0,4],[2,1,8],[3,2,7],[4,3,9],[5,2,4],[5,3,14],[5,4,10],[6,5,2],[7,0,8],[7,1,11],[7,6,1],[8,2,2],[8,6,6],[8,7,7]]

    undirected_weighted_graph = Undirected_Weighted_Graph()
    for edge in edges:
        undirected_weighted_graph.add_edge(edge)
    graph = undirected_weighted_graph.get_graph()
    result = dijkstra(graph, 0)
    
    print(result)

def test_topo_sort():

    edges = [[0,1,1],[1,2,1],[3,1,1],[3,2,1]]

    directed_graph = Directed_Graph()
    for edge in edges:
        directed_graph.add_edge(edge)
    result = kahn(directed_graph)
    print(result)


def test_bellman_ford():

    edges = [
        [0, 1, -1],
        [0, 2, 4],
        [1, 2, 3],
        [1, 3, 2],
        [1, 4, 2],
        [3, 2, 5],
        [3, 1, 1],
        [4, 3, -3]
    ]

    directed_graph = Directed_Graph()
    for edge in edges:
        directed_graph.add_edge(edge)
    result = bellman_ford(directed_graph, 0)
    print(result)

if __name__ == "__main__":
    test_bellman_ford()