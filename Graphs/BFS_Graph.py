from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u,v):
        self.graph[u].append(v)

    def bfs(self,start):
        visited = []
        queue = [start]
        result = []

        while queue:
            curr = queue.pop(0)
            if curr not in visited:
                visited.append(curr)
            result.append(curr)

            for child in self.graph[curr]:
                if child not in visited:
                    visited.append(child)
                    queue.append(child)
        return result





a = Graph()
a.addEdge(1,2)
a.addEdge(0,1)
a.addEdge(0,2)
a.addEdge(2,0)
a.addEdge(2,3)
a.addEdge(3,3)

print a.graph
print a.bfs(2)