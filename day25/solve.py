#
# Advent of Code 2023
# Bryan Clair
#
# Day --
#
import sys
sys.path.append("..")
import aocutils
import networkx as nx

args = aocutils.parse_args()

inputlines = [x.strip() for x in open(args.file).readlines()]

g = nx.Graph()

for line in inputlines:
    src,dest = line.split(': ')
    dest = dest.split()
    for d in dest:
        g.add_edge(src,d)

eggs = list(g.edges)
cuts = []
pct = len(eggs)
print(pct)
for t,e in enumerate(eggs):
    print(t, file=sys.stderr)
    g.remove_edge(*e)
    if (not nx.is_k_edge_connected(g,3)):
        cuts.append(e)
        print(e)
    g.add_edge(*e)
    if len(cuts) == 3:
        break

for e in cuts:
    g.remove_edge(*e)

comp = nx.connected_components(g)
size = 1
for c in comp:
    size *= len(c)
    
print('part1:',size)

