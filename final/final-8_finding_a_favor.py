# Finding a Favor v2 
#
# Each edge (u,v) in a social network has a weight p(u,v) that
# represents the probability that u would do a favor for v if asked.
# Note that p(v,u) != p(u,v), in general.
#
# Write a function that finds the right sequence of friends to maximize
# the probability that v1 will do a favor for v2.
# 

#
# Provided are two standard versions of dijkstra's algorithm that were
# discussed in class. One uses a list and another uses a heap.
#
# You should manipulate the input graph, G, so that it works using
# the given implementations.  Based on G, you should decide which
# version (heap or list) you should use.
#

# code for heap can be found in the instructors comments below
from final-8_heap import *
from operator import itemgetter
from math import log, exp

def maximize_probability_of_favor(G, v1, v2):
    
    logG = {}
    nodes = len(G)
    edges = 0
    
    # To find the probability of a path, you need to multiply
    # the probabilities along the shortest path. Multiplying very small numbers
    # leads to underflow errors. So, convert the probs to their
    # logs, and the dijkstra algorithms simply add the logs together
    # to find the probabilities. Because numbers < 1 have negative logs,
    # find the absolute value of the logs.
    for node in G:
        logG[node] = {}
        edges += len(G[node])
        for nbr in G[node]:
            logG[node][nbr] = abs(log(G[node][nbr]))
    
    # If O(n + m * log(n)) exceeds O(n^2), use dijkstra_list.
    # dijkstra_list requires that all nodes are reachable from each other.
    # dijkstra_heap does not.
    if nodes ** 2 < (nodes + edges) * log(nodes):
        d = dijkstra_list(logG, v1)
    else:
        d = dijkstra_heap(logG, v1)
    
    # Construct the path and return the probability of the shortest path.
    # The probability is the negative exponential of the logarithm.
    node = v2
    path = [v2]
    while node != v1:
        node = d[node][1]
        path.insert(0,node)
    prob = exp(-d[v2][0])
    return path, prob

#
# version of dijkstra implemented using a heap
#
# returns a dictionary mapping a node to the distance
# to that node and the parent
#
# Do not modify this code
#
def dijkstra_heap(G, a):
    # Distance to the input node is zero, and it has
    # no parent
    first_entry = (0, a, None)
    heap = [first_entry]
    # location keeps track of items in the heap
    # so that we can update their value later
    location = {first_entry:0}
    dist_so_far = {a:first_entry} 
    final_dist = {}
    while len(dist_so_far) > 0:
        dist, node, parent = heappopmin(heap, location)
        # lock it down!
        final_dist[node] = (dist, parent)
        del dist_so_far[node]
        for x in G[node]:
            if x in final_dist:
                continue
            new_dist = G[node][x] + final_dist[node][0]
            new_entry = (new_dist, x, node)
            if x not in dist_so_far:
                # add to the heap
                insert_heap(heap, new_entry, location)
                dist_so_far[x] = new_entry
            elif new_entry < dist_so_far[x]:
                # update heap
                decrease_val(heap, location, dist_so_far[x], new_entry)
                dist_so_far[x] = new_entry
    return final_dist

#
# version of dijkstra implemented using a list
#
# returns a dictionary mapping a node to the distance
# to that node and the parent
#
# Do not modify this code
#
def dijkstra_list(G, a):
    dist_so_far = {a:(0, None)} #keep track of the parent node
    final_dist = {}
    while len(final_dist) < len(G):
        node, entry = min(dist_so_far.items(), key=itemgetter(1))
        # lock it down!
        final_dist[node] = entry
        del dist_so_far[node]
        for x in G[node]:
            if x in final_dist:
                continue
            new_dist = G[node][x] + final_dist[node][0]
            new_entry = (new_dist, node)
            if x not in dist_so_far:
                dist_so_far[x] = new_entry
            elif new_entry < dist_so_far[x]:
                dist_so_far[x] = new_entry
    return final_dist

##########
#
# Test

def test():
    G = {'a':{'b':.9, 'e':.5},
         'b':{'c':.9},
         'c':{'d':.01},
         'd':{},
         'e':{'f':.5},
         'f':{'d':.5}}
    path, prob = maximize_probability_of_favor(G, 'a', 'd')
    assert path == ['a', 'e', 'f', 'd']
    assert abs(prob - .5 * .5 * .5) < 0.001

G = {'a':{'b':.9, 'e':.5},
     'b':{'c':.9},
     'c':{'d':.01},
     'd':{},
     'e':{'f':.5},
     'f':{'d':.5}}    

print test()