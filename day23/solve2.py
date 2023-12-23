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

def dfs(G, loc):
    loc = tuple(loc)
    trails[loc] = 'o'
    G.add_node(loc)
    for n in trails.neighbors(loc):
        if trails[n] == '#':
            continue
        if trails[n] == 'o':
            G.add_edge(loc,tuple(n),weight=1)
        if trails[n] == '.':
            dfs(G, n)

G = nx.Graph()
dfs(G, start)
for node, degree in dict(G.degree()).items():
    if degree == 2:
        nbrs = []
        weight = 0
        for n,v,data in G.edges(node, data=True):
            assert(n==node)
            nbrs.append(v)
            weight += data['weight']
        if G.has_edge(nbrs[0],nbrs[1]):
            oldweight = G.get_edge_data(nbrs[0],nbrs[1])['weight']
            weight = max(oldweight,weight)
        G.add_edge(nbrs[0],nbrs[1],weight=weight)
        G.remove_node(node)

def path_length(p):
    l = 0
    for e in p:
        l += G.get_edge_data(*e)['weight']
    return l

print('part 2: showing best so far (total runtime < 3 minutes)')

best = 0
for path in nx.all_simple_edge_paths(G,start,finish):
    l = path_length(path)
    if l > best:
        best = l
        print(best)
    
print('part 2:',best)    

