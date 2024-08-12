'''
Given an adjacency list of a graph adj of V no. of vertices having 0 based index. Check whether the graph is bipartite or not.

Know more about Bipartite Graph: - https://www.geeksforgeeks.org/what-is-bipartite-graph/

Example 1:

Input: 

Output: 1
Explanation: The given graph can be colored 
in two colors so, it is a bipartite graph.
Example 2:

Input:

Output: 0
Explanation: The given graph cannot be colored 
in two colors such that color of adjacent 
vertices differs. 
 

Your Task:
You don't need to read or print anything. Your task is to complete the function isBipartite() which takes V denoting no. of vertices and adj denoting adjacency list of the graph and returns a boolean value true if the graph is bipartite otherwise returns false.
 

Expected Time Complexity: O(V + E)
Expected Space Complexity: O(V)
'''

from collections import deque
class Solution:
    def isBipartite(self, V, adj):
        color = {}
        for i in range(V):
            if i not in color:
                node = i
                color[node] = 0
                q = deque([node])
                while q:
                    curr = q.popleft()
                    for child in adj[curr]:
                        if child in color:
                            if color[child] == color[curr]:
                                return False
                        else:
                            color[child] = 1 - color[curr]
                            q.append(child)
        return True