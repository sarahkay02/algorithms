import csv
import sys
import Queue
import re



def find_neighbors(graph_ADT, user_input):
    # if the state is in the data set
    if (user_input in graph_ADT):
        # no neighbors if values are empty
        if (graph_ADT[user_input] == ['']):
            print user_input, " has no neighbors.\n"

        # if neighbors exist, print them out
        else:
            print user_input, " has the following neighbors: "

            for neighbor in graph_ADT[user_input]:
                print neighbor,             # suppresses newline
            print "\n"                      # for spacing purposes

    else:
        print "Not a valid state. Try again.\n"



def create_graph():
    # open the data file, containing states in the US and their neighbors
    # source: https://docs.python.org/2/library/csv.html
    with open('/Users/skay/Desktop/USStates.csv', 'rb') as csvfile:
        reader = csv.reader(csvfile)

        # skip the first line--these are the data labels
        next(reader)

        # create the graph_ADT dictionary (key: state, values: neighbors)
        G = {}

        # determine which state has the most neighbors
        max_neighbors = []
        neighbor_count = 0

        # read each line and store information in dictionary
        for line in reader:
            key = line[0]                    # state name
            value = line[1].split(", ")      # neighbors

            # populate the graph_ADT dictionary
            G[key] = value

            # determine which state has the most neighbors
            if (len(value) > neighbor_count):
                neighbor_count = len(value)

        for key in G:
            if (len(G[key])== neighbor_count):
                max_neighbors.append(key)

        # print out the state with the most neighbors
        print "State(s) with the most neighbors: ", max_neighbors, "with", neighbor_count, "neighbors\n"


    return G



def search(G, s, t):
    # unbuilt path from Washington to Washington, DC
    path = []

    # create dictionaries to record node predecessors and visited nodes
    pred = {}
    visited = {}

    # create a Queue (FIFO) for Breadth-First Search
    Q = Queue.Queue()

    # for each vertex v in G...
    for v in G:
        pred[v] = None
        visited[v] = False

    Q.put(s)                    # put s on the Queue

    while (not Q.empty()):        # while Q is not empty
        u = Q.get()             # pop from the Queue

        # successfully reached final destination, return full path
        if (u == t):
            path.append(t)

            # build path backwards, from terminal node to start node
            while (pred[u] != None):
                path.append(pred[u])
                u = pred[u]

            return path

        else:
            visited[u] = True

            # for each vertex adjacent to u...
            for v in G[u]:
                # only consider paths to WOMAN states (check using Python regular expressions)
                if ((re.search('^[WOMAN]', v)) or (v == "District of Columbia")):
                    # only consider paths that have not been visited already
                    if (not visited[v]):
                        pred[v] = u
                        Q.put(v)

    # failed search, no path found
    return -1



def user_query(G):
    # ask user for input
    user_input = raw_input("Enter a state ('Exit' to quit): ")

    while (user_input != "Exit"):
        # print out the neighbors of the query state
        find_neighbors(G, user_input)

        # keep asking user for input until they say "Exit"
        user_input = raw_input("Enter a state ('Exit' to quit): ")

    sys.exit()



# create and populate the graph_ADT using a dictionary of lists
G = create_graph()
user_query(G)

# search for a path from Washington to Washington, DC
start = "Washington"
end = "District of Columbia"

path = search(G, start, end)

# search successful--path found
if (path != -1):
    # reverse path, since it was built backwards
    path.reverse()

    print "Yes. To get from", start, "to", end, "march from: "
    for state in range(len(path)-1):
        print path[state], "to",

    print path[state+1]

else:
    print "There is no path from", start, "to", end



"""
SOLUTION:

To get from Washington to District of Columbia march from:
Washington to Oregon to Nevada to Arizona to New Mexico to Oklahoma to Arkansas to Missouri to Nebraska to Wyoming to Montana to North Dakota to Minnesota to Wisconsin to Michigan to Ohio to West Virginia to Maryland to District of Columbia
"""
