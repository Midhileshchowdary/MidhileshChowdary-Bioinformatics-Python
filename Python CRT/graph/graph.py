class Graph:
    def __init__(self):
        self.graph={}
    def add_edge(self,u,v):
        if u not in self.graph:
            self.graph[u]=[]
        self.graph[u].append(v)
    def display(self):
        for node in self.graph:
            print(node,"->",self.graph[node])
g=Graph()
g.add_edge('a','b')
g.add_edge('b','c')
g.add_edge('c','d')
g.display()