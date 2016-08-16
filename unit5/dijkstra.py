import heapq

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