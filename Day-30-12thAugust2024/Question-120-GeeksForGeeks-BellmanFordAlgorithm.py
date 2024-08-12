'''
Given a directed weighted graph, the task is to find whether the given graph contains any negative-weight cycle or not.

Note: A negative-weight cycle is a cycle in a graph whose edges sum to a negative value.
'''
from collections import defaultdict
class Graph:
    def __init__(self, vertices) -> None:
        self.vertices = vertices
        self.edges = []
    def addEdges(self, u, v, w) -> None:
        self.edges.append([u, v, w])
    def bellmanFord(self, src) -> None:
        dist = [float('inf')] * self.vertices
        dist[src] = 0
        for i in range(self.vertices - 1):
            for u, v, w in self.edges:
                if dist[u] != float('inf') and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
        for u, v, w in self.edges:
            if dist[u] != float("inf") and dist[u] + w < dist[v]:
                return True
        return False
if __name__ == '__main__':
        g = Graph(6)
        g.addEdges(0, 1, 5)
        g.addEdges(1, 3, 2)
        g.addEdges(1, 2, 1)
        g.addEdges(2, 4, 1)
        g.addEdges(4, 3, -1)
        g.addEdges(3, 5, 2)
        g.addEdges(5, 4, -3)
        if g.bellmanFord(0):
            print("Graph contains negative weight cycle")
        else:
            print("Graph does not contain negative weight cycle")
        
    
        
    