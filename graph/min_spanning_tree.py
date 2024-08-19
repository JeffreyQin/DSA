
from collections import defaultdict

# PRIM ALGORITHM FOR MINIMUM SPANNING TREE


def find_min_vertex(not_included, costs):
    min_cost = float('inf')
    min_vertex = None

    for vertex in not_included:
        if costs[vertex] < min_cost:
            min_cost = costs[vertex]
            min_vertex = vertex

    return min_vertex


def prim(graph, start):


    not_included = set(graph.keys())

    costs = defaultdict(lambda: float('inf'))
    costs[start] = 0

    mst = dict() # a mapping of each vertex to its associated reaching cost
    mst[start] = 0

    while not_included:
        curr_vertex = find_min_vertex(not_included, costs)
        
        mst[curr_vertex] = costs[curr_vertex]
        not_included.remove(curr_vertex)
        
        for neighbor in graph[curr_vertex].keys():
            if graph[curr_vertex][neighbor] < costs[neighbor]:
                costs[neighbor] = graph[curr_vertex][neighbor]

    return mst