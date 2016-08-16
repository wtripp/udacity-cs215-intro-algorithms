

import math

def make_link(G, node1, node2):
	if node1 not in G:
		G[node1] = {}
	(G[node1])[node2] = 1
	if node2 not in G:
		G[node2] = {}
	(G[node2])[node1] = 1
	return G

def num_nodes(G):
	return len(G)

def num_edges(G):
	return sum([len(G[node]) for node in G.keys()])/2

# Make an empty graph
a_ring = {}

n = 5

# Add in the edges
for i in range(n):
	make_link(a_ring, i, (i+1)%n)

print "Ring Network:"
print a_ring
print "How many nodes?", num_nodes(a_ring)
print "How many edges?", num_edges(a_ring)

a_grid = {}
n = 256
side = int(math.sqrt(256))

# Add in the edges
for i in range(side):
	for j in range(side):
		if i < side-1: make_link(a_grid, (i,j), (i+1,j))
		if j < side-1: make_link(a_grid, (i,j), (i,j+1))

print "Grid Network:"
print a_grid
print "How many nodes?", num_nodes(a_grid)
print "How many edges?", num_edges(a_grid)