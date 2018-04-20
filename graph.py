import urllib
from edge import *

class graph():
    # constructor
    # creates an empty graph
    def __init__(self):
        # create a graph data structure, using an adjacency list representation
        # use a dictionary, so vertices can be any data type (not just integers)
        self.size = 0;               # will be updated as file is read
        self.adjacency_list = {}

    # methods
    def getSize(self):
        return self.size

    def getList(self):
        return self.adjacency_list

    # given (frm, to), get the full edge
    def getEdge(self, frm, to):
        # make sure the index is valid
        if (frm in self.getList()):
            for edge in self.getEdges(frm):
                if (edge.getTo() == to):
                    return edge

    # given a vertex, return all edges
    def getEdges(self, vertex):
        # make sure the index is valid
        if (vertex in self.getList()):
            return self.getList()[vertex]
        else:
            return -1

    # given a vertex, return all neighbors/adjacent vertices
    def getAdjacent(self, vertex):
        # make sure the index is valid
        if (vertex in self.getList()):
            neighbors = []

            for edge in self.getEdges(vertex):
                # keep track of neighbors/adjacent vertices to v
                neighbors.append(edge.getTo())

        return neighbors

    def addVertex(self, vertex):
        self.getList()[vertex] = []        # each vertex's value is a list of edges

    def addEdge(self, edge):
        self.getList()[edge.getFrm()].append(edge)

    # populate the entire graph, using data from input file
    def read_graph(self, input_file):
        # open the data file, containing edges
        reader = urllib.urlopen(input_file)

        # skip the first two lines (# vertices, # edges)
        self.size = int(reader.readline())        # update the size
        reader.readline()

        # populate the graph with empty lists (the empty Values)
        for i in range(self.getSize()):
            self.addVertex(i)

        # read each line and populate the graph, with the edges as Values
        for line in reader:
            # remove trailing newline, and split on " "
            data = line.strip().split()

            # create new edge
            frm = int(data[0])
            to = int(data[1])
            weight = float(data[2])
            new_edge = edge(frm, to, weight)

            # add edge to graph
            self.addEdge(new_edge)

    def printGraph(self):
        for vertex in self.getList():
            print "vertex: ", vertex
            for edge in self.getEdges(vertex):
                print "edge: ", edge
            print
