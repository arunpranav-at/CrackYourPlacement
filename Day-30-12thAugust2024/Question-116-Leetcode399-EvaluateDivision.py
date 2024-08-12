'''
You are given an array of variable pairs equations and an array of real numbers values, where equations[i] = [Ai, Bi] and values[i] represent the equation Ai / Bi = values[i]. Each Ai or Bi is a string that represents a single variable.

You are also given some queries, where queries[j] = [Cj, Dj] represents the jth query where you must find the answer for Cj / Dj = ?.

Return the answers to all queries. If a single answer cannot be determined, return -1.0.

Note: The input is always valid. You may assume that evaluating the queries will not result in division by zero and that there is no contradiction.

Note: The variables that do not occur in the list of equations are undefined, so the answer cannot be determined for them.

Example 1:

Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]
Explanation: 
Given: a / b = 2.0, b / c = 3.0
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? 
return: [6.0, 0.5, -1.0, 1.0, -1.0 ]
note: x is undefined => -1.0
Example 2:

Input: equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
Output: [3.75000,0.40000,5.00000,0.20000]
Example 3:

Input: equations = [["a","b"]], values = [0.5], queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
Output: [0.50000,2.00000,-1.00000,-1.00000]
'''

from collections import defaultdict
from typing import List
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        nodes = set()
        n = len(values)
        for i in range(n):
            graph[equations[i][0]].append([equations[i][1], values[i]])
            graph[equations[i][1]].append([equations[i][0], 1/values[i]])
            nodes.add(equations[i][0])
            nodes.add(equations[i][1])
        def dfs(src, dest, val, visited):
            if src == dest:
                return val
            if src in visited:
                return None
            visited.add(src)
            for child, dist in graph[src]:
                if child not in visited:
                    result = dfs(child, dest, val * dist, visited)
                    if result is not None:
                        return result
            return None
        ans = []
        print(graph)
        for i, j in queries:
            if i in nodes and j in nodes:
                val = dfs(i, j, 1, set())
                if val is None:
                    ans.append(float(-1))
                else:
                    ans.append(val)
            else:
                ans.append(float(-1))
        return ans