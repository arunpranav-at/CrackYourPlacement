'''
Find the number of islands using DFS
Last Updated : 26 Jul, 2024
Given a binary 2D matrix, find the number of islands. A group of connected 1s forms an island. For example, the below matrix contains 4 islands.

Example: 

Input: mat[][] = {{1, 1, 0, 0, 0},
                           {0, 1, 0, 0, 1},
                           {1, 0, 0, 1, 1},
                          {0, 0, 0, 0, 0},
                         {1, 0, 1, 0, 0}}
Output: 4

This is a variation of the standard problem: “Counting the number of connected components in an undirected graph”. 

Before we go to the problem, let us understand what is a connected component. A connected component of an undirected graph is a subgraph in which every two vertices are connected to each other by a path(s), and which is connected to no other vertices outside the subgraph. 
For example, the graph shown below has three connected components. 
 

Find the number of islands
 

A graph where all vertices are connected with each other has exactly one connected component, consisting of the whole graph. Such a graph with only one connected component is called a Strongly Connected Graph.
This problem can be easily solved by applying DFS() on each component. In each DFS() call, a component or a sub-graph is visited. We will call DFS on the next un-visited component. The number of calls to DFS() gives the number of connected components. BFS can also be used.

What is an island? 
A group of connected 1s forms an island. For example, the below matrix contains 4 islands

island

Finding the number of islands using an additional Matrix:
The idea is to keep an additional matrix to keep track of the visited nodes in the given matrix, and perform DFS to find the total number of islands

Follow the steps below to solve the problem:

Initialize count = 0 and boolean matrix, visited[][] to false.
For each cell of the input matrix check if the value of the current cell is 1 and is not visited , call for the DFS for all its 8 neighbouring cells.
If the neighbor is safe to visit and is not visited already Call DFS recursively and Increment count by 1
Return count as the final answer.
'''

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        count = 0
        def dfs(i, j):
            if 0<=i<rows and 0<=j<cols:
                if grid[i][j] == "1":
                    grid[i][j] = "$"
                    dfs(i - 1, j)
                    dfs(i + 1, j)
                    dfs(i, j - 1)
                    dfs(i, j + 1)
                    dfs(i + 1, j + 1)
                    dfs(i - 1, j + 1)
                    dfs(i - 1, j - 1)
                    dfs(i + 1, j - 1)
                    
            else:
                return
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    count += 1
                    dfs(i, j)
        return count