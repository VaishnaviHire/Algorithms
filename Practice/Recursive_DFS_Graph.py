from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u,v):
        self.graph[u].append(v)

    def dfs(self,start, visited = []):
        visited += [start]
        for child in self.graph[start]:
            if child not in visited:
                visited = self.dfs(child,visited)
        return visited

g = Graph()
g.addEdge(1, 2)
g.addEdge(1, 3)
g.addEdge(2, 4)
g.addEdge(2, 5)
# g.addEdge(2, 3)
# g.addEdge(3, 3)

print g.graph
print g.dfs(1)