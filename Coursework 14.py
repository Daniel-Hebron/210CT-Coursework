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

    def DFS(self,v):
        stack = [] # starting dfs with stack
        visited = []
        stack.append(v)
        while stack != []: #loops through the graph using first item in stack
            u = stack.pop()
            if u not in visited:
                visited.append(u)
                for edge in self.graph[u]: #loop through edge connected to that vertex & add edge to stack
                    stack.append(edge)
                    file = open("DFS.txt", "w")
                    file.write(str(visited))
                    file.close
        return visited

    def BFS(self, v):
        queue = [] #create queue
        visited = []
        queue.insert(0,v)
        while queue != []: #loops through graph using start value
            u = queue.pop()
            if u not in visited:
                visited.append(u) #add vertex to visited
                for edge in self.graph[u]:#loops through edges connected to that verex and put into queue
                    queue.insert(0,edge)
                    file = open("BFS.txt", "w")
                    file.write(str(visited))
                    file.close
        return visited

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

print('Depth First search: ' + str(g.DFS('2')))
print('Breadth First search: ' + str(g.BFS('4')))
