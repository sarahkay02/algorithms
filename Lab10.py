import urllib
from edge import *
from graph import *


def dijkstra(G, s):
    # create lists to record shortest paths and vertex predecessors
    # for each vertex v, set the shortest path length to infinity and predecessors to null
    shortest = [float('inf') for vertex in range(G.getSize())]
    pred = [None for vertex in range(G.getSize())]

    # begin with the Start vertex, s
    shortest[s] = 0
    pred[s] = None

    # create an array (mock priority queue)
    Q = []

    # insert each vertex v into Q
    for vertex in range(G.getSize()):
        Q.append(vertex)

    # while Q is not empty, remove from Q the vertex with the shortest value
    while Q:
        u = extract_min(Q, shortest)
        Q.remove(u)

        # for each vertex v adjacent to u, relax
        for v in G.getAdjacent(u):
            relax(G, shortest, pred, u, v)

    return pred



def extract_min(Q, shortest):
    short = Q[0]

    for vertex in Q:
        if shortest[vertex] < shortest[short]:
            short = vertex

    return short



def relax(G, shortest, pred, u, v):
    # update the values in shortest[v] and pred[v] if possible
    edge = G.getEdge(u,v)

    if ((shortest[u] + edge.getWeight()) < shortest[v]):
        shortest[v] = shortest[u] + edge.getWeight()
        pred[v] = u



def shortest_path(G, pred, s, t):
    for i in range(len(pred)):
        print "i: ", i
        print "pred: \n", pred[i]


    path = []
    path_cost = 0

    # build path backwards, from terminal vertex to start vertex
    u = t

    while (pred[u] != s):
        edge = G.getEdge(pred[u], u)
        path.append(edge)
        path_cost = path_cost + edge.getWeight()
        u = pred[u]

    first_edge = G.getEdge(s, u)
    path.append(first_edge)
    path_cost = path_cost + first_edge.getWeight()

    print "There is a path from", s, "to", t
    print "The shortest path has a cost of", path_cost
    print "\nHere it is:"

    path.reverse()

    for edge in path:
        print edge
    print

    return path




# main function for testing
if __name__ == '__main__':
    G = graph()
    G.read_graph('https://cs.brynmawr.edu/Courses/cs330/spring2018/tinyEWD.txt')

    #G = graph()
    #G.read_graph('https://cs.brynmawr.edu/Courses/cs330/spring2018/mediumEWD.txt')

    s = input("\nEnter the source vertex: ")
    t = input("Enter the destination vertex: ")

    pred = dijkstra(G, s)
    shortest_path(G, pred, s, t)
