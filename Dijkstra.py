import timeit

import sys

class Graph():

    def __init__(self, vertx):
        self.V = vertx
        self.graph = [[0 for column in range(vertx)]
                      for row in range(vertx)]
        self.source = None

    def printSolution(self, dist):
        print("Source :", self.source)
        print("Distance la plus courte du nœud source à:")
        for node in range(self.V):
            print(f"{node} -> {dist[node]}")

    def minDistance(self, dist, sptSet):
        minDist = sys.maxsize
        minIndex = -1

        for v in range(self.V): 
            if dist[v] < minDist and sptSet[v] == False:
                minDist = dist[v]
                minIndex = v

        return minIndex

    def dijkstra(self, source):
        self.source = source
        dist = [sys.maxsize] * self.V
        dist[source] = 0
        sptSet = [False] * self.V

        for i in range(self.V):
            u = self.minDistance(dist, sptSet)
            sptSet[u] = True

            for v in range(self.V):
                if (self.graph[u][v] > 0 and
                    sptSet[v] == False and
                    dist[v] > dist[u] + self.graph[u][v]):
                    dist[v] = dist[u] + self.graph[u][v]

        self.printSolution(dist)

g = Graph(9)
g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
           [4, 0, 8, 0, 0, 0, 0, 11, 0],
           [0, 8, 0, 7, 0, 4, 0, 0, 2],
           [0, 0, 7, 0, 9, 14, 0, 0, 0],
           [0, 0, 0, 9, 0, 10, 0, 0, 0],
           [0, 0, 4, 14, 10, 0, 2, 0, 0],
           [0, 0, 0, 0, 0, 2, 0, 1, 6],
           [8, 11, 0, 0, 0, 0, 1, 0, 7],
           [0, 0, 2, 0, 0, 0, 6, 7, 0]
           ]

g.dijkstra(0)

# Mesure du temps d'exécution avec timeit
t = timeit.timeit( number=1) 
print("Durée d'exécution : %.5f secondes" % t)

