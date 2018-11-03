
class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.v = val


class Solution:

    def bfs(self, graph, start):
        visited, queue = list(), [start]
        while queue:
            vertex = queue.pop()
            if vertex not in visited:
                visited.append(vertex)
                # new nodes are added to end of queue
                queue = queue.extend((graph[vertex]).remove(visited))
                print queue

        return visited



a =Solution()
graph = {1:[2,3],
         2:[1,4,5],
         3:[1,6,7],
         4:[2,8,9],
         5:[2],
         6:[3],
         7:[3],
         8:[4],
         9:[4]}


print a.bfs(graph,1)