#
# Write a function, `bipartite` that
# takes as input a graph, `G` and tries
# to divide G into two sets where 
# there are no edges between elements of the
# the same set - only between elements in
# different sets.
# If two sets exists, return one of them
# or `None` otherwise
# Assume G is connected
#
import random

def bipartite(G):
    starter = random.choice(G.keys())
    open_list = [starter]
    checked = []

    s1 = [starter]
    s2 = []
    
    while open_list:
        node = open_list[0]
        checked.append(node)
        del open_list[0]
        
        for neighbor in G[node]:
            if (node in s1 and neighbor in s1) or \
               (node in s2 and neighbor in s2):
                return None
            
            if node in s1 and neighbor not in s2:
                s2.append(neighbor)

            elif node in s2 and neighbor not in s1:
                s1.append(neighbor)
            
            if neighbor not in checked:
                if neighbor not in open_list:
                    open_list.append(neighbor)
    
    return set(s1)


########
#
# Test

def make_link(G, node1, node2, weight=1):
    if node1 not in G:
        G[node1] = {}
    (G[node1])[node2] = weight
    if node2 not in G:
        G[node2] = {}
    (G[node2])[node1] = weight
    return G


def test():
    edges = [(1, 2), (2, 3), (1, 4), (2, 5),
             (3, 8), (5, 6)]
    G = {}
    for n1, n2 in edges:
        make_link(G, n1, n2)
    print G
    g1 = bipartite(G)
    #assert (g1 == set([1, 3, 5]) or
            #g1 == set([2, 4, 6, 8]))
    edges = [(1, 2), (1, 3), (2, 3)]
    print G
    G = {}
    for n1, n2 in edges:
        make_link(G, n1, n2)
    g1 = bipartite(G)
    print G
    assert g1 == None

print test()