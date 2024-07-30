'''
Given a Directed Graph with V vertices (Numbered from 0 to V-1) and E edges, check whether it contains any cycle or not.


Example 1:

Input:



Output: 1
Explanation: 3 -> 3 is a cycle

Example 2:

Input:


Output: 0
Explanation: no cycle in the graph

Your task:
You dont need to read input or print anything. Your task is to complete the function isCyclic() which takes the integer V denoting the number of vertices and adjacency list adj as input parameters and returns a boolean value denoting if the given directed graph contains a cycle or not.
In the adjacency list adj, element adj[i][j] represents an edge from i to j.


Expected Time Complexity: O(V + E)
Expected Auxiliary Space: O(V)


Constraints:
1 ≤ V, E ≤ 105

'''

from typing import List

class Solution:
    
    #Function to detect cycle in a directed graph.
    def isCyclic(self, V : int , adj : List[List[int]]) -> bool :
        
        visited = set()
        cycle = set()
        
        def dfs(node):
            if node in cycle:
                return True
            if node in visited:
                return False
            visited.add(node)
            cycle.add(node)
            for child in adj[node]:
                if dfs(child):
                    return True
            cycle.remove(node)
            return False
        
        for i in range(V):
            if i in visited:
                continue
            if dfs(i):
                return True
        return False