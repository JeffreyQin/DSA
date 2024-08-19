from collections import defaultdict


# BELLMAN FORD ALGORITHM FOR MINIMUM DISTANCE WITH NEGATIVE WEIGHTS
# O(V*E)

def bellman_ford(directed_graph, start):

    graph = directed_graph.adj_lst
    V = directed_graph.vertices

    distances = defaultdict(lambda: float('inf'))
    distances[start] = 0


    for iteration in range(len(V) - 1):
        for vertex in V:
            if distances[vertex] == float('inf'):
                continue
            for neighbor in graph[vertex].keys():
                concatenated_dist = distances[vertex] + graph[vertex][neighbor]
                if concatenated_dist < distances[neighbor]:
                    distances[neighbor] = concatenated_dist
    
    # check for negative cycle
    for vertex in V:
        if distances[vertex] == float('inf'):
            continue
        for neighbor in graph[vertex].keys():
            concatenated_dist = distances[vertex] + graph[vertex][neighbor]
            if concatenated_dist < distances[neighbor]:
                return "IMPOSSIBLE"
    
    return distances