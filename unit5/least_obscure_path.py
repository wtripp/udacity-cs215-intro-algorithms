from movie_graph import G
import heapq

def val(triplet): return triplet[0]
def mov(triplet): return triplet[1]
def id(triplet): return triplet[2]

def dijkstra(G,v):
    heap = [ [0, 'NO_MOVIE', v] ]
    dist_so_far = {v: [0, 'NO_MOVIE', v]}
    final_dist = {}
    while len(dist_so_far) > 0:
        while True:
            w = heapq.heappop(heap)
            dist = val(w)
            movie = mov(w)
            node = id(w)
            if node != 'REMOVED':
                del dist_so_far[node]
                break
        final_dist[node] = (movie, dist)

        for x in G[node]:
            if x not in final_dist:
                new_dist = max(dist, float(G[node][x][1]))
                new_movie = G[node][x][0]
                new_entry = [new_dist, new_movie, x]
                if x not in dist_so_far:
                    dist_so_far[x] = new_entry
                    heapq.heappush(heap, new_entry)
                elif new_dist < val(dist_so_far[x]):
                    dist_so_far[x][2] = "REMOVED"
                    dist_so_far[x] = new_entry
                    heapq.heappush(heap, new_entry)
    return final_dist

for node in G:
    del G[node][node]

a = {(u'Boone Junior, Mark', u'Del Toro, Benicio'): None,
          (u'Braine, Richard', u'Coogan, Will'): None,
          (u'Byrne, Michael (I)', u'Quinn, Al (I)'): None,
          (u'Cartwright, Veronica', u'Edelstein, Lisa'): None,
          (u'Curry, Jon (II)', u'Wise, Ray (I)'): None,
          (u'Di Benedetto, John', u'Hallgrey, Johnathan'): None,
          (u'Hochendoner, Jeff', u'Cross, Kendall'): None,
          (u'Izquierdo, Ty', u'Kimball, Donna'): None,
          (u'Jace, Michael', u'Snell, Don'): None,
          (u'James, Charity', u'Tuerpe, Paul'): None,
          (u'Kay, Dominic Scott', u'Cathey, Reg E.'): None,
          (u'McCabe, Richard', u'Washington, Denzel'): None,
          (u'Reid, Kevin (I)', u'Affleck, Rab'): None,
          (u'Reid, R.D.', u'Boston, David (IV)'): None,
          (u'Restivo, Steve', u'Preston, Carrie (I)'): None,
          (u'Rodriguez, Ramon (II)', u'Mulrooney, Kelsey'): None,
          (u'Rooker, Michael (I)', u'Grady, Kevin (I)'): None,
          (u'Ruscoe, Alan', u'Thornton, Cooper'): None,
          (u'Sloan, Tina', u'Dever, James D.'): None,
          (u'Wasserman, Jerry', u'Sizemore, Tom'): None}

def get_obs_scores(G, actors):
    actor_obs = []
    for a1, a2 in actors:
        a1_obs = dijkstra(G, a1)
        current_obs = "Obscurity score for %s: %s" % (a1, a1_obs[a2][1])
        actor_obs.append(current_obs)
    return actor_obs


obs = get_obs_scores(G, a)

for a in obs:
    print a

actors = {(u'Boone Junior, Mark', u'Del Toro, Benicio'): 0.2979,
          (u'Braine, Richard', u'Coogan, Will'): 1.1345,
          (u'Byrne, Michael (I)', u'Quinn, Al (I)'): 0.1736,
          (u'Cartwright, Veronica', u'Edelstein, Lisa'): 0.7161,
          (u'Curry, Jon (II)', u'Wise, Ray (I)'): 0.2872,
          (u'Di Benedetto, John', u'Hallgrey, Johnathan'): 0.8361,
          (u'Hochendoner, Jeff', u'Cross, Kendall'): 0.6228,
          (u'Izquierdo, Ty', u'Kimball, Donna'): 0.2616,
          (u'Jace, Michael', u'Snell, Don'): 0.6758,
          (u'James, Charity', u'Tuerpe, Paul'): 0.5079,
          (u'Kay, Dominic Scott', u'Cathey, Reg E.'): 0.2184,
          (u'McCabe, Richard', u'Washington, Denzel'): 0.4031,
          (u'Reid, Kevin (I)', u'Affleck, Rab'): 0.5147,
          (u'Reid, R.D.', u'Boston, David (IV)'): 0.5768,
          (u'Restivo, Steve', u'Preston, Carrie (I)'): 0.3628,
          (u'Rodriguez, Ramon (II)', u'Mulrooney, Kelsey'): 0.2394,
          (u'Rooker, Michael (I)', u'Grady, Kevin (I)'): 0.3693,
          (u'Ruscoe, Alan', u'Thornton, Cooper'): 0.4072,
          (u'Sloan, Tina', u'Dever, James D.'): 0.5636,
          (u'Wasserman, Jerry', u'Sizemore, Tom'): 0.1999}