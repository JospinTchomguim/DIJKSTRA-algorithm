# DIJKSTRA's algorithm

In graph theory, Dijkstra's algorithm is used to solve the problem of the shortest
path. It allows, for example, to determine a shortest way to go from o
city to another knowing the road network of a region. More precisely, it calculates
shortest paths from a source to all other vertices in a graph
oriented weighted by positive reals. It can also be used to calculate a shorter
path between a departure vertex and an arrival vertex.
The algorithm takes as input a directed graph weighted by positive real numbers and a
source vertex. It is a question of gradually building a sub-graph in which are
classified the different vertices in ascending order of their minimum distance from the vertex of
departure. The distance corresponds to the sum of the weights of the arcs taken.
Initially, we consider that the distances from each vertex to the starting vertex are
infinite, except for the starting vertex for which the distance is zero. The subgraph of
start is the empty set.
During each iteration, we choose outside the subgraph a vertex of distance
minimum and we add it to the subgraph. Then, we update the distances of the vertices
neighbors of the added one. The update is done as follows: the new vertex distance
neighbor is the minimum between the existing distance and that obtained by adding the weight of
the arc between neighboring vertex and vertex added to the distance from the added vertex.
We continue in this way until the vertices are exhausted (or until the vertex is selected
of arrival).
