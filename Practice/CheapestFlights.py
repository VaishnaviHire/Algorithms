from collections import defaultdict


class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, K):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        """
        graph = defaultdict(list)
        k = K

        for i in flights:
            graph[i[0]].append((i[1], i[2]))
        print graph

        dfs_list = []
        curr_len = 0
        stack = [src]
        visited = []
        #
        while stack and visited != graph.keys():
            curr = stack.pop()
            print curr
            if curr == dst:
                dfs_list.append(curr_len)
                stack = [src]
                k = K
                curr_len = 0
            else:
                visited.append(curr)
                for neigh in graph[curr]:
                    if neigh[0] == dst and neigh[0]:
                        curr_len += neigh[1]
                        stack.append(neigh[0])
                        break
                    else:
                        if k >= 0  and neigh[0] not in visited:
                            curr_len += neigh[1]
                            stack.append(neigh[0])
                            k -= 1
                        else:
                            print dfs_list
                            dfs_list.append(-1)
                            # visited.append(neigh[0])
                            stack = [src]
                            k = K
                            curr_len = 0
                            break




        print dfs_list

a = Solution()
a.findCheapestPrice(3,[[0,1,100],[1,2,100],[0,2,500]],0,2,1)