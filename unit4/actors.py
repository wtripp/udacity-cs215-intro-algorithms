import csv
import random

def make_link(G, node1, node2):
    if node1 not in G:
        G[node1] = {}
    (G[node1])[node2] = 1
    if node2 not in G:
        G[node2] = {}
    (G[node2])[node1] = 1
    return G

def read_graph(filename):
    # Read an undirected graph in CSV format. Each line is an edge
    tsv = csv.reader(open(filename), delimiter='\t')
    G = {}
    t = (("actor: "+actor, movie+" ("+year+")") for (actor,movie,year) in tsv)

    for (actor, movie) in t: make_link(G, actor, movie)

    return G

# Returns an actor's centrality score, where lower is better
def centrality(G, v):
    distance_from_start = {}
    open_list = [v]
    distance_from_start[v] = 0
    while len(open_list) > 0:
        current = open_list[0]
        del open_list[0]
        for neighbor in G[current].keys():
            if neighbor not in distance_from_start:
                distance_from_start[neighbor] = distance_from_start[current] + 1
                open_list.append(neighbor)
    return float(sum(distance_from_start.values()))/len(distance_from_start)


def centrality_scores(G):
    return [(node, centrality(G, node)) for node in G if node[:5] == "actor"]

G1 = read_graph('imdb1.tsv')
G2 = read_graph('imdb2.tsv')
G3 = read_graph('imdb3.tsv')
G4 = read_graph('imdb4.tsv')

L1 = centrality_scores(G1)
L2 = centrality_scores(G2)
L3 = centrality_scores(G3)
L4 = centrality_scores(G4)

with open("networks.py","a") as f:
    f.write("L1 = " + str(L1) + "\n")
    f.write("L2 = " + str(L2) + "\n")
    f.write("L3 = " + str(L3) + "\n")
    f.write("L4 = " + str(L4))
