'''
Given a Directed Graph with V vertices (Numbered from 0 to V-1) and E edges, Find the number of strongly connected components in the graph.
 

Example 1:

Input:

Output:
3
Explanation:

We can clearly see that there are 3 Strongly
Connected Components in the Graph
Example 2:

Input:

Output:
1
Explanation:
All of the nodes are connected to each other.
So, there's only one SCC.
 

Your Task:
You don't need to read input or print anything. Your task is to complete the function kosaraju() which takes the number of vertices V and adjacency list of the graph of size V as inputs and returns an integer denoting the number of strongly connected components in the given graph.
 

Expected Time Complexity: O(V+E).
Expected Auxiliary Space: O(V+E).
 

Constraints:
1 ≤ V ≤ 5000
0 ≤ E ≤ (V*(V-1))
0 ≤ u, v ≤ V-1
Sum of E over all testcases will not exceed 25*106
'''

class Solution:
    def __init__(self):
        self.stack = []
        
    def dfs(self, node, visited, adj):
        if visited[node]:
            return
        visited[node] = True
        for child in adj[node]:
            self.dfs(child, visited, adj)
        self.stack.append(node)
    
    def reverse(self, V, adj):
        new = [[] for _ in range(V)]
        for i in range(V):
            for j in adj[i]:
                new[j].append(i)
        return new
        
    def revdfs(self, node, visited, new):
        if visited[node]:
            return
        visited[node] = True
        for child in new[node]:
            self.revdfs(child, visited, new)
            
    def kosaraju(self, V, adj):
        visited = [False] * V
        for i in range(V):
            self.dfs(i, visited, adj)
        new = self.reverse(V, adj)
        visited = [False] * V
        ans = 0 
        while self.stack:
            curr = self.stack.pop()
            if not visited[curr]:
                self.revdfs(curr, visited, new)
                ans += 1
        return ans