'''
Given an adjacency list for a Directed Acyclic Graph (DAG) where adj_list[i] contains a list of all vertices j such that there is a directed edge from vertex i to vertex j, with  V  vertices and E  edges, your task is to find any valid topological sorting of the graph.
In a topological sort, for every directed edge u -> v,  u must come before v in the ordering.

Example 1:

Input:

Output:
1
Explanation:
The output 1 denotes that the order is
valid. So, if you have, implemented
your function correctly, then output
would be 1 for all test cases.
One possible Topological order for the
graph is 3, 2, 1, 0.
Example 2:

Input:

Output:
1
Explanation:
The output 1 denotes that the order is
valid. So, if you have, implemented
your function correctly, then output
would be 1 for all test cases.
One possible Topological order for the
graph is 5, 4, 2, 1, 3, 0.
Your Task:
You don't need to read input or print anything. Your task is to complete the function topoSort()  which takes the integer V denoting the number of vertices and adjacency list as input parameters and returns an array consisting of the vertices in Topological order. As there are multiple Topological orders possible, you may return any of them. If your returned topo sort is correct then the console output will be 1 else 0.

Expected Time Complexity: O(V + E).
Expected Auxiliary Space: O(V).

Constraints:
2 ≤ V ≤ 104
1 ≤ E ≤ (N*(N-1))/2
'''

from collections import deque
class Solution:
    def topoSort(self, V, adj):
        degrees = {i : 0 for i in range(V)}
        for i in range(V):
            for j in adj[i]:
                degrees[j] += 1
        ans = []
        q = deque()
        for i in range(V):
            if degrees[i] == 0:
                q.append(i)
        while q:
            curr = q.popleft()
            ans.append(curr)
            for child in adj[curr]:
                degrees[child] -= 1
                if degrees[child] == 0:
                    q.append(child)
        return ans