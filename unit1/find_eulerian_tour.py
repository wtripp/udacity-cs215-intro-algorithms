# Find Eulerian Tour
#
# Write a function that takes in a graph
# represented as a list of tuples
# and return a list of nodes that
# you would follow on an Eulerian Tour
#
# For example, if the input graph was
# [(1, 2), (2, 3), (3, 1)]
# A possible Eulerian tour would be [1, 2, 3, 1]
#use_harder_tests = True
import random

def find_eulerian_tour(graph):
    

    # Create a list of all possible nodes. For [(1,2),(2,3),(3,1)], 
    # nodes = {1:[(1,2),(1,3)], 2:[(2,1),(2,3)], 3:[(3,1),(3,2)]}
    nodes = {}
    
    for x,y in graph:
        set_nodes(nodes,x,y)
        set_nodes(nodes,y,x)
    
    print nodes
    # Exclude graphs that have at least one node w/ an odd number of edges
    for node in nodes:
        if len(nodes[node]) % 2 == 1:
            return None

    path = find_path(nodes)
    return path

def set_nodes(nodes,a,b):    
    if not nodes.get(a):
        nodes[a] = [(a,b)]
    else:
        nodes[a].append((a,b))

def find_path(nodes,start=None,path=[],idx=0):    
    if start is None:
        start = random.choice(nodes.keys()) # Choose a random starting node.
                              
    temp_path = [start] # Start a path with the starting node.
    graph_len = get_node_len(nodes) / 2
    for i in range(graph_len):
        if nodes[start]:
            x,y = nodes[start].pop() # Pick a edge connected to a node.
            temp_path.append(y)      # Add the next node to the path.
            nodes[y].remove((y,x))   # Remove the reverse path of node.
            start = y                # Make the next node the new starting node.
    
    insert_idx = idx + 1
    tpath_len = len(temp_path)

    # If you run this function the first time, the temp_path becomes the path.
    if not path:
        path = temp_path
    
    # If the path already exists, add all but the first value of temp_path
    # into the existing path. The first value is a duplicate of what's already
    # in the path.
    else:    
        for i in range(1,tpath_len):
            path.insert(insert_idx, temp_path[i])        
            insert_idx += 1

    # If unvisited nodes, run find_path again until all nodes have been visited.
    for idx,node in enumerate(path):
        if nodes[node]:
            find_path(nodes,node,path,idx)
            break

    return path

# Get length of nodes by counting every tuple in each node list.
def get_node_len(nodes):
    node_len = 0
    for node in nodes:
        node_len += len(nodes[node])
    return node_len

#print find_eulerian_tour([(1,2),(2,3),(3,1)])
#print find_eulerian_tour([(1,2),(2,3),(3,4),(4,5),(5,1),(1,3),(3,5),(5,6),(6,1)])
#print find_eulerian_tour([(0, 1), (1, 5), (1, 7), (4, 5), (4, 8), (1, 6), (3, 7), (5, 9), (2, 4), (0, 4), (2, 5), (3, 6), (8, 9)])
#print "Challenge Problems"
#print "------------------"
#challenge1 = [(0, 1), (1, 2), (2, 0), (2, 3), (3, 4), (4, 2), (4, 5), (5, 6), (6, 4), (6, 7), (7, 8), (8, 6), (8, 9), (9, 10), (10, 8), (10, 11), (11, 12), (12, 10), (12, 13), (13, 14), (14, 15), (15, 16), (16, 14), (16, 17), (17, 18), (18, 16), (18, 19), (19, 20), (20, 18), (20, 21), (21, 22), (22, 20), (22, 23), (23, 24), (24, 22), (24, 25), (25, 26), (26, 24), (26, 27), (27, 28), (28, 26), (28, 29), (29, 30), (30, 28), (30, 31), (31, 32), (32, 30), (32, 33), (33, 34), (34, 32), (34, 35), (35, 36), (36, 34), (36, 37), (37, 38), (38, 36), (38, 39), (39, 40), (40, 38), (40, 41), (41, 42), (42, 40), (42, 43), (43, 44), (44, 42), (44, 45), (45, 46), (46, 44), (46, 47), (47, 48), (48, 46), (48, 49), (49, 50), (50, 48), (50, 51), (51, 52), (52, 50), (52, 53), (53, 54), (54, 52), (54, 55), (55, 56), (56, 54), (56, 57), (57, 58), (58, 56), (58, 59), (59, 60), (60, 58), (60, 61), (61, 62), (62, 60), (62, 63), (63, 64), (64, 62), (64, 65), (65, 66), (66, 64), (66, 67), (67, 68), (68, 66), (68, 69), (69, 70), (70, 68), (70, 71), (71, 72), (72, 70), (72, 73), (73, 74), (74, 72), (74, 75), (75, 76), (76, 74), (76, 77), (77, 78), (78, 76), (78, 79), (79, 80), (80, 78), (80, 81), (81, 82), (82, 80), (82, 83), (83, 84), (84, 82), (84, 85), (85, 86), (86, 84), (86, 87), (87, 88), (88, 86), (88, 89), (89, 90), (90, 88), (90, 91), (91, 92), (92, 90), (92, 93), (93, 94), (94, 92), (94, 95), (95, 96), (96, 94), (96, 97), (97, 98), (98, 96), (98, 99), (99, 100), (100, 98)]
#challenge2 = [(0, 1), (1, 2), (2, 0), (0, 3), (3, 4), (4, 0), (0, 5), (5, 6), (6, 0), (0, 7), (7, 8), (8, 0), (0, 9), (9, 10), (10, 0), (0, 11), (11, 12), (12, 0), (0, 13), (13, 14), (14, 0)]
#challenge3 = [(0, 1), (1, 2), (2, 0), (0, 3), (3, 4), (4, 0)]