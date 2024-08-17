'''
There are n servers numbered from 0 to n - 1 connected by undirected server-to-server connections forming a network where connections[i] = [ai, bi] represents a connection between servers ai and bi. Any server can reach other servers directly or indirectly through the network.

A critical connection is a connection that, if removed, will make some servers unable to reach some other server.

Return all critical connections in the network in any order. 

Example 1:

Input: n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
Output: [[1,3]]
Explanation: [[3,1]] is also accepted.
Example 2:

Input: n = 2, connections = [[0,1]]
Output: [[0,1]] 

Constraints:

2 <= n <= 105
n - 1 <= connections.length <= 105
0 <= ai, bi <= n - 1
ai != bi
There are no repeated connections.
'''
from collections import defaultdict
from typing import List
class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(set)
        for i, j in connections:
            graph[i].add(j)
            graph[j].add(i)
        low = {}
        result = []
        def dfs(node, parent = None):
            if node in low:
                return low[node]
            curr = low[node] = len(low)
            for child in graph[node]:
                if child == parent:
                    continue
                low[node] = min(low[node], dfs(child, node))
            if curr == low[node] and parent is not None:
                result.append([parent, node])
            return low[node]
        dfs(0)
        return result