from collections import defaultdict

# DIJKSTRA ALGORITHM FOR MINIMUM DISTANCE FROM START VERTEX

def dijkstra_find_nearest(distances, vertices, checked):

    nearest_dist = float('inf')
    nearest_vertex = None

    for vertex in vertices:
        if vertex not in checked and distances[vertex] < nearest_dist:
            nearest_dist = distances[vertex]
            nearest_vertex = vertex

    return nearest_vertex


def dijkstra(graph, start):

    distances = defaultdict(lambda: float('inf'))
    distances[start] = 0

    V = set(graph.keys())
    checked = set()

    while len(checked) != len(V):

        curr_vertex = dijkstra_find_nearest(distances, V, checked)
        checked.add(curr_vertex)

        for neighbor in graph[curr_vertex].keys():
            concatenated_dist = distances[curr_vertex] + graph[curr_vertex][neighbor]
            if neighbor not in checked and concatenated_dist < distances[neighbor]:
                distances[neighbor] = concatenated_dist
                
    return distances