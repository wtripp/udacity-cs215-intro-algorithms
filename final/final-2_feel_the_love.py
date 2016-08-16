#
# Take a weighted graph representing a social network where the weight
# between two nodes is the "love" between them.  In this "feel the
# love of a path" problem, we want to find the best path from node `i`
# and node `j` where the score for a path is the maximum love of an
# edge on this path. If there is no path from `i` to `j` return
# `None`.  The returned path doesn't need to be simple, ie it can
# contain cycles or repeated vertices.
#
# Devise and implement an algorithm for this problem.
#

def connected_nodes(G, node):
    max_edge = (0, None, None)
    marked = {}
    marked[node] = True
    open_list = [node]
    while open_list:
        node = open_list.pop()
        for neighbor in G[node]:
            if G[node][neighbor] > max_edge[0]:
                max_edge = (G[node][neighbor], node, neighbor)
            
            if neighbor not in marked:
                open_list.append(neighbor)
                marked[neighbor] = True
    return (marked.keys(), max_edge)

def find_path(G, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if not G.has_key(start):
        return None
    for node in G[start]:
        if node not in path:
            newpath = find_path(G, node, end, path)
            if newpath: return newpath
    return None


def feel_the_love(G, i, j):
    nodes, max_edge = connected_nodes(G, i)

    if j not in nodes:
        return None

    A = find_path(G, i, max_edge[1])
    B = find_path(G, max_edge[2], j)

    return A + B

#########
#
# Test

def score_of_path(G, path):
    max_love = -float('inf')
    for n1, n2 in zip(path[:-1], path[1:]):
        love = G[n1][n2]
        if love > max_love:
            max_love = love
    return max_love

def test():
    G = {'a':{'c':1},
         'b':{'c':1},
         'c':{'a':1, 'b':1, 'e':1, 'd':1},
         'e':{'c':1, 'd':2},
         'd':{'e':2, 'c':1},
         'f':{}}
    path = feel_the_love(G, 'a', 'b')
    assert score_of_path(G, path) == 2

    path = feel_the_love(G, 'a', 'f')
    assert path == None

print test()
