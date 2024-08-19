
from collections import defaultdict
import heapq

class Node(object):
    
    def __init__(self, symbol, idx, dist = float('inf')):
        self.symbol = symbol
        self.heap_idx = idx
        self.dist = dist

    def __lt__(self, other):
        return self.dist < other.dist
    

def parent(idx):
    return (idx - 1) // 2

def left_child(idx):
    return 2 * idx + 1

def right_child(idx):
    return 2 * idx + 2

def fix_up(heap, node):

    while node.heap_idx != 0:
        current_idx = node.heap_idx
        if node < heap[parent(current_idx)]:
            # swap idx
            node.heap_idx = parent(current_idx)
            heap[parent(current_idx)].heap_idx = current_idx
            # swap node
            temp = heap[parent(current_idx)]
            heap[parent(current_idx)] = node
            heap[current_idx] = temp
        else:
            break

def fix_down(heap, node):

    while left_child(node.heap_idx) < len(heap):

        current_idx = node.heap_idx
        comparison_idx = left_child(current_idx)
        if right_child(current_idx) < len(heap) and heap[right_child(current_idx)] < heap[left_child(current_idx)]:
            comparison_idx = right_child(current_idx)

        if node > heap[comparison_idx]:
            # swap idx
            node.heap_idx = comparison_idx
            heap[comparison_idx].heap_idx = current_idx
            # swap node
            temp = heap[comparison_idx]
            heap[comparison_idx] = node
            heap[current_idx] = temp
        else:
            break
         

def dijkstra_heap(graph, start):

    result = defaultdict(lambda: -1)

    distances = []
    vertex_to_node = defaultdict(lambda: None)

    # initialize start node
    node = Node(start, len(distances), 0)
    vertex_to_node[start] = node

    distances.append(node)
    fix_up(distances, node)


    while distances:
        next_node = heapq.heappop(distances)
        for neighbor in graph[next_node.symbol].keys():

            concatenated_dist = next_node.dist + graph[next_node.symbol][neighbor]

            # first time encountering vertex
            if vertex_to_node[neighbor] is None: 
                node = Node(neighbor, len(distances), concatenated_dist)
                vertex_to_node[neighbor] = node
                
                distances.append(node)
                fix_up(distances, node)
            # already encountered before
            else:
                if concatenated_dist < vertex_to_node[neighbor].dist:
                    vertex_to_node[neighbor].dist = concatenated_dist
                    fix_up(distances, vertex_to_node[neighbor])
    
        result[next_node.symbol] = next_node.dist

    return result

    