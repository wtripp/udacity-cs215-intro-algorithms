#
# In lecture, we took the bipartite Marvel graph,
# where edges went between characters and the comics
# books they appeared in, and created a weighted graph
# with edges between characters where the weight was the
# number of comic books in which they both appeared.
#
# In this assignment, determine the weights between
# comic book characters by giving the probability
# that a randomly chosen comic book containing one of
# the characters will also contain the other
#

marvel = cPickle.load(open("final-3_smallG.pkl"))
characters = cPickle.load(open("final-3_smallChr.pkl"))

def create_weighted_graph(bipartiteG, characters):
    G = {}
    for char in characters:
        for other_char in characters:
            if char == other_char:
                continue
            char_set = set(bipartiteG[char])
            other_char_set = set(bipartiteG[other_char])
            
            A_and_B = len(char_set.intersection(other_char_set))
            A_or_B = (len(char_set) + len(other_char_set)) - A_and_B
            
            if G.get(char) is None:
                G[char] = {other_char: None}
            
            if A_and_B > 0.0:
                G[char][other_char] = (0.0 + A_and_B) / A_or_B
            else:
                G[char][other_char] = None
            
    return G

######
#
# Test

def test():
    bipartiteG = {'charA':{'comicB':1, 'comicC':1},
                  'charB':{'comicB':1, 'comicD':1},
                  'charC':{'comicD':1},
                  'comicB':{'charA':1, 'charB':1},
                  'comicC':{'charA':1},
                  'comicD': {'charC':1, 'charB':1}}
    G = create_weighted_graph(bipartiteG, ['charA', 'charB', 'charC'])
    # three comics contain charA or charB
    # charA and charB are together in one of them
    assert G['charA']['charB'] == 1.0 / 3
    assert G['charA'].get('charA') == None
    assert G['charA'].get('charC') == None

def test2():
    G = create_weighted_graph(marvel, characters)
    
