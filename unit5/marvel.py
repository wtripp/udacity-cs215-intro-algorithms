import csv

def make_link(G, node1, node2):
    if node1 not in G:
        G[node1] = {}
    (G[node1])[node2] = 1
    return G

def read_graph(filename):
    tsv = csv.reader(open(filename), delimiter='\t')
    G = {}
    for (chr, book) in tsv: make_link(G, book, chr)
    return G

# Read the marvel comics graph
marvelG = read_graph('file.tsv')

def char_weights(G):
	charG = {}
	for book in G:
		if len(book) > 1: # If more than one character
			for chr in G[book]: # Go through each character
				for other_chr in G[book]: # Go through the other characters in that book
					if other_chr == chr: # Skip the character you're looking at
						continue
					if chr not in charG: # Add the other character + weight to the graph
						charG[chr] = {}
						charG[chr][other_chr] = 1
					else:
						if other_chr not in charG[chr]:
							charG[chr][other_chr] = 1
						else:
							charG[chr][other_chr] += 1
	return charG

def highest_weight(G):
	highest = 0
	char1 = ""
	char2 = ""
	for char in G:
		for other_char in G[char]:
			if G[char][other_char] > highest:
				highest = G[char][other_char]
				char1 = char
				char2 = other_char
	return "Highest weight: %s to %s has a weight of %d" % (char1, char2, highest)

charG = char_weights(marvelG)			
print highest_weight(charG)
			
			
			
			
				