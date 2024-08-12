'''
The problem is to find the shortest distances between every pair of vertices in a given edge-weighted directed graph. The graph is represented as an adjacency matrix of size n*n. Matrix[i][j] denotes the weight of the edge from i to j. If Matrix[i][j]=-1, it means there is no edge from i to j.
Note : Modify the distances for every pair in-place.

Examples :

Input: matrix = [[0, 25],[-1, 0]]

Output: [[0, 25],[-1, 0]]

Explanation: The shortest distance between every pair is already given(if it exists).
Input: matrix = [[0, 1, 43],[1, 0, 6],[-1, -1, 0]]

Output: [[0, 1, 7],[1, 0, 6],[-1, -1, 0]]

Explanation: We can reach 2 from 0 as 0->1->2 and the cost will be 1+6=7 which is less than 43.
Expected Time Complexity: O(n3)
Expected Space Complexity: O(1)

Constraints:
1 <= n <= 100
-1 <= matrix[ i ][ j ] <= 1000
'''

from collections import defaultdict
import heapq
class Solution:
	def shortest_distance(self, matrix):
		n = len(matrix)
		graph = defaultdict(list)
		for i in range(n):
		    for j in range(n):
		        if i != j and matrix[i][j] != -1:
		            graph[i].append([j, matrix[i][j]])
		def dijkstras(vertex, graph):
		    minheap = [[0, vertex]]
		    shortest = {}
		    while minheap:
		        dist, node = heapq.heappop(minheap)
		        if node in shortest:
		            continue
		        shortest[node] = dist
		        for child, newdist in graph[node]:
		            if child not in shortest:
		                heapq.heappush(minheap, [newdist + dist, child])
		    for i in range(n):
		        if i not in shortest:
		            shortest[i] = -1
		    return shortest
		for i in range(n):
		    shortest = dijkstras(i, graph)
		    for j in range(n):
		        matrix[i][j] = shortest[j]
        return matrix