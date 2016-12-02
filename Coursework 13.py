#Unweighted graph data structure using adjacency list

class Graph:
    def __init__(self):
        self.graph = {} #Creates dictionary

    def Node(self, label):
        self.graph[label] = [] #Inserts nodes into dictionary

    def Edge(self,N,E): #Add edges to each nodes list of edges
        self.graph[N].append(E)
        self.graph[E].append(N)

    def Graph(self): #Loops through dictionary to print all the key,values
        for key,value in self.graph.items():
            print(key,value)

g = Graph()

g.Node('1')
g.Node('2')
g.Node('3')
g.Node('4')
g.Node('5')
g.Edge('1','2')
g.Edge('1', '2')
g.Edge('2', '1')
g.Edge('2', '5')
g.Edge('4', '2')
g.Edge('3', '5')
g.Edge('5', '2')
g.Edge('4', '1')

g.Graph()
