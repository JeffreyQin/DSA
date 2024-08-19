from collections import defaultdict


class Vertex(object):
    
    def __init__(self, symbol):
        self.symbol = symbol


class Undirected_Graph(object):

    def __init__(self):

        self.adj_list = defaultdict(lambda: set())

    def add_edge(self, edge):

        # edge = [ vertex 1, vertex 2 ]
        self.adj_list[edge[0]].add(edge[1])
        self.adj_list[edge[1]].add(edge[0])



class Undirected_Weighted_Graph(object):

    def __init__(self): 
        
        self.adj_lst = defaultdict(lambda: dict())

    def add_edge(self, edge): 

        # edge = [ vertex 1, vertex 2, weight ]
        self.adj_lst[edge[0]][edge[1]] = edge[2]
        self.adj_lst[edge[1]][edge[0]] = edge[2]

    def get_graph(self):
        
        return self.adj_lst

class Directed_Graph(object):

    def __init__(self):

        self.adj_lst = defaultdict(lambda: dict())
        self.vertices = set()

    def add_edge(self, edge):

        # edge = [ vertex 1, vertex 2, weight ]
        self.adj_lst[edge[0]][edge[1]] = edge[2]
        self.vertices.add(edge[0])
        self.vertices.add(edge[1])
