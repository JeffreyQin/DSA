
from collections import defaultdict, deque

# TOPOLOGICAL SORTING ALGORITHM

def topo_sort_util(graph, starting_vertex, visited, stack):

    visited.add(starting_vertex)

    for neighbor in list(graph[starting_vertex].keys()):
        if neighbor not in visited:
            topo_sort_util(graph, neighbor, visited, stack)

    stack.append(starting_vertex)


def topo_sort(directed_graph):

    graph = directed_graph.adj_lst
    V = directed_graph.vertices

    visited = set()
    stack = list()
    result = list()

    for vertex in V:
        if vertex not in visited:
            topo_sort_util(graph, vertex, visited, stack)

    # reverse stack
    while stack:
        result.append(stack.pop())
    
    return result
    

# KAHN'S ALGORITHM FOR TOPOLOGICAL SORTING
# - allows recognition of possibly cyclic graph
# - O(V+E)

def kahn_get_indegree(graph, V):

    indegree = dict()

    for vertex in V:
        indegree[vertex] = 0

    for vertex in V:
        for neighbor in graph[vertex].keys():
            indegree[neighbor] += 1
    
    return indegree


def kahn(directed_graph):

    graph = directed_graph.adj_lst
    not_sorted = directed_graph.vertices

    sorted = list()

    indegree = kahn_get_indegree(graph, not_sorted)

    zero_indegree = deque()

    for vertex in indegree.keys():
        if indegree[vertex] == 0:
            zero_indegree.append(vertex)

    while zero_indegree:
        curr_vertex = zero_indegree.popleft()
        sorted.append(curr_vertex)
        not_sorted.remove(curr_vertex)

        for neighbor in graph[curr_vertex].keys():
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                zero_indegree.append(neighbor)

    if len(not_sorted) > 0:
        return "IMPOSSIBLE, THERE IS A CYCLE"
    else:
        return sorted
