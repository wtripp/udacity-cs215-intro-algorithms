import networks
import random

def partition(L, v):
    smaller = []
    bigger = []
    for val in L:
        if val[1] < v[1]: smaller += [val]
        if val[1] > v[1]: bigger += [val]
    return (smaller, [v], bigger)

def top_k(L, k):
    v = L[random.randrange(len(L))]
    (left, middle, right) = partition(L, v)
    # middle used below (in place of [v]) for clarity
    if len(left) == k:   return left
    if len(left)+1 == k: return left + middle
    if len(left) > k:    return top_k(left, k)
    return left + middle + top_k(right, k - len(left) - len(middle))

def sort_k(k):
	sorted(k, key = lambda x: k[1])

n = 20

k1 = top_k(networks.L1, n)
k2 = top_k(networks.L2, n)
k3 = top_k(networks.L3, n)
k4 = top_k(networks.L4, n)

sort_k(k1)
sort_k(k2)
sort_k(k3)
sort_k(k4)

print "Top 20th centrality in imdb-1:", k1[-1]
print "Top 20th centrality in imdb-2:", k2[-1]
print "Top 20th centrality in imdb-3:", k3[-1]
print "Top 20th centrality in imdb-4:", k4[-1]