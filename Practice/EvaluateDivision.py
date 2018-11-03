#
# Equations are given in the format A / B = k, where A and B are variables represented as
#  strings, and k is a real number (floating point number). Given some queries, return the answers.
# If the answer does not exist, return -1.0.
#
# Example:
# Given a / b = 2.0, b / c = 3.0.
# queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? .
# return [6.0, 0.5, -1.0, 1.0, -1.0 ].
#
# The input is: vector<pair<string, string>> equations, vector<double>& values, vector<pair<string, string>> queries ,
#  where equations.size() == values.size(), and the values are positive. This represents the equations.
# Return vector<double>.
#
# According to the example above:
#
# equations = [ ["a", "b"], ["b", "c"] ],
# values = [2.0, 3.0],
# queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ].
# The input is always valid.
# You may assume that evaluating the queries will result in no division by zero and there is no contradiction.
from collections import defaultdict
class Solution(object):
    def isconnected(self,graph,a,b,path=[]):
        if not path:
            a = (a,1)
            path = path + [a]
        else:
            path = path + [a]

        if a[0] == b:
            return path
        if not graph.has_key(a[0]):
            return None

        for i in graph[a[0]]:

            if i not in path:
                n_path = self.isconnected(graph,i,b,path)
                if n_path:
                    return n_path
        return None

    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        result = []
        graph = defaultdict(list)
        for i in range(len(equations)):
            graph[equations[i][0]].append((equations[i][1],values[i]))
            graph[equations[i][1]].append((equations[i][0], 1.0/values[i]))
        print graph

        print self.isconnected(graph, 'b', 'c')
        #
        #
        for i in queries:
            if i[0] not in graph.keys() and i[1]:
                result.append(-1.0)
            else:
                temp = self.isconnected(graph,i[0],i[1])
                # print (graph)
                if temp:
                    # print "here",i[0]
                    val =  1.0
                    for k in temp:
                        if len(k)==2:
                            val *= k[1]
                    result.append(val)

                else:
                    result.append(-1.0)
        return result

a = Solution()
print a.calcEquation( [["a","b"],["b","c"],["bc","cd"]] ,[1.5,2.5,5.0],[["a","c"],["c","b"],["bc","cd"],["cd","bc"]])
