#
# write a function, `top_two` that takes in a graph and a starting
# node and returns two paths, the first and second shortest paths,
# for all the other nodes in the graph.  You can assume that the 
# graph is connected.
#
import heapq

def top_two(graph, start, n=2):
    # Create the heap and populate it with the starting node. Heap structure:
    # (distance from start node, current node, path from start node to current node)
    heap = [ (0, start, [start]) ]
    final_dist = {}

    # Get the contents of heap entries. The entries are sorted by min distance.
    # Continue getting heap entries until the heap is empty.
    while heap:
        dist, node, path = heapq.heappop(heap)
        
        # Lock down the n shortest distances and paths.
        if node not in final_dist:
            final_dist[node] = []
        if len(final_dist[node]) < n:
            final_dist[node].append((dist, path))
        
        # Look at the neighbors of that node.
        for nbr in graph[node]:
            
            # Skip neighbors already in the path to prevent loops.
            if nbr in path:
                continue
            
            # Skip locked-down nieghbors, if n shortest distances and paths haven't been reached.
            if nbr in final_dist and len(final_dist[nbr]) >= n:
                continue
            
            # Create a new entry with the neighbor and push it to the heap.
            new_dist = dist + graph[node][nbr]
            new_path = path + [nbr]
            new_entry = (new_dist, nbr, new_path)
            heapq.heappush(heap, new_entry)
                
    return final_dist


def test():
    graph = {'a':{'b':3, 'c':4, 'd':8},
             'b':{'a':3, 'c':1, 'd':2},
             'c':{'a':4, 'b':1, 'd':2},
             'd':{'a':8, 'b':2, 'c':2}}
    result = top_two(graph, 'a') # this is a dictionary
    b = result['b'] # this is a list
    b_first = b[0] # this is a list
    assert b_first[0] == 3 # the cost to get to 'b'
    assert b_first[1] == ['a', 'b'] # the path to 'b'
    b_second = b[1] # this is a list
    assert b_second[0] == 5 # the cost to get to 'b'
    assert b_second[1] == ['a', 'c', 'b']

test()
