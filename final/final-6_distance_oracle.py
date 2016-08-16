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
# Given a graph G that is a balanced binary tree, preprocess the graph to
# create such labels for each node.  Note that the size of the list in
# each label should not be larger than log n for a graph of size n.
#

#
# create_labels takes in a balanced binary tree and the root element
# and returns a dictionary, mapping each node to its label
#
# a label is a dictionary mapping another node and the distance to
# that node
#

def create_labels(G, root):
    
    # The root node has a distance of 0 from itself.
    labels = {root: {root:0}}
    
    # Use breadth first search to visit nodes in the graph.
    open_list = [root]
    while len(open_list) > 0: 
        parent = open_list.pop(0)
        
        # Look at the children of the node popped off the open list (the parent).
        for child in G[parent]:
            if child not in labels:
                
                # The distance from the parent to the child (the weight).
                dist = G[parent][child]
                
                # The child node has a distance of 0 from itself.
                labels[child] = {child:0}
                
                # Look at the parents of the child node's parents.
                for ancestor in labels[parent]:
                    
                    # Add the parent-child dist to the child node's ancestors.
                    # The child is that much farther away from each ancestor.
                    labels[child][ancestor] = labels[parent][ancestor] + dist
                    
                # Add the child to the open list.
                open_list.append(child)

    return labels

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
    labels = create_labels(tree, 1)
    print labels

test()