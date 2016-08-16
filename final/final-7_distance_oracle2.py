#  
# This is the same problem as "Distance Oracle I" except that instead of
# only having to deal with binary trees, the assignment asks you to
# create labels for all tree graphs.
#
# In the shortest-path oracle described in Andrew Goldberg's
# interview, each node has a label, which is a list of some other
# nodes in the network and their distance to these nodes.  These lists
# have the property that
#
#  (1) for any pair of nodes (x,y) in the network, their lists will
#  have at least one node z in common
#
#  (2) the shortest path from x to y will go through z.
# 
# Given a graph G that is a tree, preprocess the graph to
# create such labels for each node.  Note that the size of the list in
# each label should not be larger than log n for a graph of size n.
#

#
# create_labels takes in a tree and returns a dictionary, mapping each
# node to its label
#
# a label is a dictionary mapping another node and the distance to
# that node
#
from copy import deepcopy

def create_labels(treeG):
    
    # Create a copy to prevent changing size of original graph.
    treeGcopy = deepcopy(treeG)
    labels = {}
    
    while len(treeGcopy) > 0:
        
        # Pick a connected graph and find its center.
        connectedG = deepcopy(find_connected_graph(treeGcopy))
        ctr = center_node(connectedG)
        
        # Find the labels from that center. Merge with existing labels.
        new_labels = get_labels(connectedG, ctr)
        labels = merge_labels(labels, new_labels)
    
        # Remove the center from the graph.
        for nbr in connectedG[ctr]:
            break_link(treeGcopy, ctr, nbr)
        del treeGcopy[ctr]
        
        # Repeat the loop until all nodes have been visited and removed.
        
    return labels

def find_connected_graph(G):
    
    # Pick any root.
    root = G.keys()[0] 
    
    # Use BFS to traverse the graph, starting at that root.
    connectedG = {root: G[root]}
    open_list = [root]
    while len(open_list) > 0:
        node = open_list.pop(0)
        for nbr in G[node]:
            if nbr not in connectedG:
                connectedG[nbr] = G[nbr]
                open_list.append(nbr)

    return connectedG 

def center_node(treeG):
    
    # If only one node in graph, return that node.
    if len(treeG) == 1: return treeG.keys()[0]
    
    while True:
        G = deepcopy(treeG)
        current_len = len(G)
        
        # Delete nodes with only one leaf.
        for node in treeG:
            if len(G[node]) == 1:
                nbr = G[node].iterkeys().next()
                del G[nbr][node]
                del G[node]
                
        # Stop if no nodes were deleted this iteration.
        if current_len == len(G): break
        treeG = G
        
    # If multiple centers, return only one of them.
    return treeG.keys()[0]


def get_labels(G, root):
    # Find the labels from the input root. Take weights into account.
    labels = {root: {root:0}}
    open_list = [root]
    while len(open_list) > 0:
        parent = open_list.pop(0)
        for child in G[parent]:
            if child not in labels:
                wt = G[parent][child]
                labels[child] = {root:wt}
                for ancestor in labels[parent]:
                    labels[child][root] += labels[parent][root]
                open_list.append(child)
    return labels

def merge_labels(L1, L2):
    # Update the first set of labels to include the second set of labels.
    for label in L2:
        if label not in L1:
            L1[label] = L2[label]
        else:
            L1[label].update(L2[label])
    return L1

def break_link(G, node1, node2):
    if node1 not in G:
        print "error: breaking link in a non-existent node"
        return
    if node2 not in G:
        print "error: breaking link in a non-existent node"
        return
    if node2 not in G[node1]:
        print "error: breaking non-existent link"
        return
    if node1 not in G[node2]:
        print "error: breaking non-existent link"
        return
    del G[node1][node2]
    del G[node2][node1]
    return G

#######
# Testing
#


def get_distances(G, labels):
    # labels = {a:{b: distance from a to b,
    #              c: distance from a to c}}
    # create a mapping of all distances for
    # all nodes
    distances = {}
    for start in G:
        # get all the labels for my starting node
        label_node = labels[start]
        s_distances = {}
        for destination in G:
            shortest = float('inf')
            # get all the labels for the destination node
            label_dest = labels[destination]
            # and then merge them together, saving the
            # shortest distance
            for intermediate_node, dist in label_node.iteritems():
                # see if intermediate_node is our destination
                # if it is we can stop - we know that is
                # the shortest path
                if intermediate_node == destination:
                    shortest = dist
                    break
                other_dist = label_dest.get(intermediate_node)
                if other_dist is None:
                    continue
                if other_dist + dist < shortest:
                    shortest = other_dist + dist
            s_distances[destination] = shortest
        distances[start] = s_distances
    return distances

def make_link(G, node1, node2, weight=1):
    if node1 not in G:
        G[node1] = {}
    (G[node1])[node2] = weight
    if node2 not in G:
        G[node2] = {}
    (G[node2])[node1] = weight
    return G

def test():
    edges = [(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (3, 7),
             (4, 8), (4, 9), (5, 10), (5, 11), (6, 12), (6, 13)]
    tree = {}
    for n1, n2 in edges:
        make_link(tree, n1, n2)
    labels = create_labels(tree)
    distances = get_distances(tree, labels)
    assert distances[1][2] == 1
    assert distances[1][4] == 2
    print "test passes"

test()