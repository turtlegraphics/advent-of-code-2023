#
# Advent of Code 2023
# Bryan Clair
#
# Day 23
#
import sys
sys.path.append("..")
sys.setrecursionlimit(30000)

import networkx as nx

import aocutils

args = aocutils.parse_args()

inputlines = [x.strip() for x in open(args.file).readlines()]

trails = aocutils.Grid()
trails.scan(inputlines)

for t in trails:
    if trails[t] in ['>','v']:
        trails[t] = '.'
        
start = (1,trails.height()-1)
finish = (trails.width()-2,0)

# The following code converts the Grid to a networkx Graph object
# first run dfs to build a Graph where each node is a Grid coordinate
# then go through and eliminate all degree 2 nodes
# keep track of lengths as the 'weight' attribute
# when two paths connect the same two nodes, keep the longer one

def dfs(maze, G, loc):
    """DFS through Grid maze, creating nodes and edges in a Graph G."""
    loc = tuple(loc)
    maze[loc] = 'o'
    G.add_node(loc)
    for n in maze.neighbors(loc):
        if maze[n] == '#':
            continue
        if maze[n] == 'o':
            G.add_edge(loc,tuple(n),weight=1)
        if maze[n] == '.':
            dfs(maze, G, n)

def condense(G):
    """
    Take a Graph G and remove degree 2 nodes, keeping connections.
    Calculates lengths.  When two paths connect the same two nodes,
    it keeps the longer one.
    """
    for node, degree in dict(G.degree()).items():
        if degree == 2:
            nbrs = []
            weight = 0
            for n,v,data in G.edges(node, data=True):
                assert(n==node)
                nbrs.append(v)
                weight += data['weight']
            if G.has_edge(nbrs[0],nbrs[1]):
                # this is not the first path connecting these nodes
                # for this problem, we want the longer of the two
                # possible paths.  definitely watch out for this if
                # you re-use this code
                oldweight = G.get_edge_data(nbrs[0],nbrs[1])['weight']
                weight = max(oldweight,weight)
            G.add_edge(nbrs[0],nbrs[1],weight=weight)
            G.remove_node(node)

def Grid_to_Graph(maze):
    """Convert from a Grid object to a networkx Graph."""
    from copy import deepcopy
    G = nx.Graph()
    dfs(deepcopy(trails), G, start)
    condense(G)
    return G

def path_length(p):
    """why do I need this? because networkx path length function seems to be
    incompatible with its own paths."""
    l = 0
    for e in p:
        l += G.get_edge_data(*e)['weight']
    return l

G = Grid_to_Graph(trails)

print('part 2: showing best so far (total runtime < 3 minutes)')
best = 0
for path in nx.all_simple_edge_paths(G,start,finish):
    l = path_length(path)
    if l > best:
        best = l
        print(best)
    
print('part 2:',best)    

