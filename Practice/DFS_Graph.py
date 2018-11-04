from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u,v):
        self.graph[u].append(v)

    def dfs(self,start):
        visited = [start]
        stack = [start]

        while stack:
            curr = stack.pop()
            print curr
            if curr not in visited:
                visited.append(curr)

            for child in self.graph[curr]:
                if child not in visited:
                    # visited.append(child)
                    stack.append(child)
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