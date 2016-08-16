import heapq
import csv

def make_link(G, actor, movie, weights):
    if actor not in G:
        G[actor] = {}
    (G[actor])[movie] = weights[movie]
    return G

def read_weights(filename):
    tsv = csv.reader(open(filename), delimiter='\t')
    t = dict((movie+" ("+year+")", weight) for (movie,year,weight) in tsv)
    return t

def read_graph(filename,weights):
    G = {}
    tsv = csv.reader(open(filename), delimiter='\t')
    t = ((actor, movie+" ("+year+")") for (actor,movie,year) in tsv)
    for (actor, movie) in t: make_link(G, actor, movie, weights)
    return G

def val(pair): return pair[0]
def id(pair): return pair[1]

def dijkstra(G,v):
    heap = [ [0, v] ]
    dist_so_far = {v:[0, v]}
    final_dist = {}
    while len(dist_so_far) > 0:
        while True:
            w = heapq.heappop(heap)
            node = id(w)
            dist = val(w)
            if node != 'REMOVED':
                del dist_so_far[node]
                break

        final_dist[node] = dist
        for x in G[node]:
            if x not in final_dist:
                new_dist = dist + G[node][x]
                new_entry = [new_dist, x]
                if x not in dist_so_far:

                    dist_so_far[x] = new_entry
                    heapq.heappush(heap, new_entry)
                elif new_dist < val(dist_so_far[x]):
                    dist_so_far[x][1] = "REMOVED"
                    dist_so_far[x] = new_entry
                    heapq.heappush(heap, new_entry)
    return final_dist

def least_obscure(G,actor,other_actor):
    a1 = set(G[actor])
    a2 = set(G[other_actor])
    
    joint_movies = a1.intersection(a2)

    if not joint_movies:
        return

    least_obscure_movie = min(joint_movies, key=lambda movie: G[actor][movie])
    least_obscure_weight = G[actor][least_obscure_movie]

    return [least_obscure_movie, least_obscure_weight]

def make_link2(G, actor, other_actor, actorG):
    if actor not in G:
        G[actor] = {}

    a1 = set(actorG[actor])
    a2 = set(actorG[other_actor])

    joint_movies = a1.intersection(a2)

    if joint_movies:
        least_obscure_movie = min(joint_movies, key=lambda movie: actorG[actor][movie])
        least_obscure_weight = actorG[actor][least_obscure_movie]
        (G[actor])[other_actor] = [least_obscure_movie, least_obscure_weight]

    return G

weights = read_weights('imdb-weights.tsv')
actorG = read_graph('imdb-1.tsv',weights)
#print least_obscure(G, 'Ryan, Meg', 'Hanks, Tom')

G = {}
for actor in actorG:
    for other_actor in actorG:
        make_link2(G, actor, other_actor, actorG)

print G

