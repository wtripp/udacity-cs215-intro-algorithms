import csv

# Make one-way links.
def make_link(G, node1, node2):
    if node1 not in G:
        G[node1] = {}
    (G[node1])[node2] = 1
    return G

# Read in graph from CSV file.
def read_graph(filename):
    tsv = csv.reader(open(filename), delimiter='\t')
    G = {}
    for (chr, book) in tsv: make_link(G, book, chr)
    return G

# Read in the marvel comics graph.
marvelG = read_graph('file.tsv')

# Apply weights to each character.
def create_char_graph(G):
	charG = {}
	for book in G:
		if len(book) > 1: # If more than one character
			for char in G[book]: # Go through each character
				for other_chr in G[book]: # Go through the other characters in that book
					if other_chr == char: # Skip the character you're looking at
						continue
					if char not in charG: # Add the other character + weight to the graph
						charG[char] = {}
						charG[char][other_chr] = 1
					else:
						if other_chr not in charG[char]:
							charG[char][other_chr] = 1
						else:
							charG[char][other_chr] += 1
	# Apply char weights.
	for char in charG:
		for other_char in charG[char]:
			charG[char][other_char] = 1.0/charG[char][other_char]

	return charG

# Create the character graph.
charG = create_char_graph(marvelG)

# Find the shortest hop path by weight.
def fewest_hops(G, v1, v2):
	distance_from_start = {}
	open_list = [v1]
	distance_from_start[v1] = 0
	while len(open_list) > 0:
		current = open_list[0]
		del open_list[0]
		for neighbor in G[current].keys():
			if neighbor not in distance_from_start:
				distance_from_start[neighbor] = distance_from_start[current] + 1
				if neighbor == v2: return distance_from_start[v2]
				open_list.append(neighbor)
	return False

# For testing purposes.
#charG = {'A': {'C': 3.123, 'B': 15.4245, 'D': 4.978}, 'B': {'A': 15.4245, 'C': 10.2414}, 'C': {'A': 3.123, 'B': 10.2414}, 'D': {'A': 4.978, 'B': 9.506}, 'E': {'F': 0.2}}

# Implement dijkstra, counting the number of hops for each shortest path.
import heapq

def val(triplet): return triplet[0]
def id(triplet): return triplet[1]
def hop(triplet): return triplet[2]


def dijkstra(G,v):
    heap = [ [0, v, 0] ]
    dist_so_far = {v:[0, v, 0]}
    final_dist = {}
    while len(dist_so_far) > 0:
        while True:
            w = heapq.heappop(heap)
            node = id(w)
            dist = val(w)
            hops = hop(w)
            if node != 'REMOVED':
                del dist_so_far[node]
                break

        final_dist[node] = (dist, hops)
        hops += 1
        for x in G[node]:
            if x not in final_dist:
                new_dist = dist + G[node][x]
                new_entry = [new_dist, x, hops]
                if x not in dist_so_far:
                    dist_so_far[x] = new_entry
                    heapq.heappush(heap, new_entry)
                elif new_dist < val(dist_so_far[x]):
                    dist_so_far[x][1] = "REMOVED"
                    dist_so_far[x] = new_entry
                    heapq.heappush(heap, new_entry)
    return final_dist

# Find number of differences between hop counts.
def find_diff(charG, char_list):
	ndiff = 0
	for char in char_list:
		d = dijkstra(charG, char)
		for other_char in d:
			dijkstra_hops = d[other_char][1]
			# Compare fewest # hops to # hops in shortest weighted path.
			if fewest_hops(charG, char, other_char) != dijkstra_hops:
				print "Adding", char, "->", other_char
				ndiff += 1
	return ndiff

char_list = ['SPIDER-MAN/PETER PAR',
			'GREEN GOBLIN/NORMAN ',
			'WOLVERINE/LOGAN ',
			'PROFESSOR X/CHARLES ',
			'CAPTAIN AMERICA']

print "ndiff =", find_diff(charG, char_list)