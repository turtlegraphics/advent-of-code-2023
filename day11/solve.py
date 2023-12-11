#
# Advent of Code 2023
# Bryan Clair
#
# Day 11
#
import sys
sys.path.append("..")
import aocutils

args = aocutils.parse_args()

inputlines = [x.strip() for x in open(args.file).readlines()]


part1, part2 = 0,0

universe = aocutils.Grid()
universe.scan(inputlines)

galaxies = []
grows = []
gcols = []
for p in universe:
    if universe[p] == '#':
        g = aocutils.Point(p)
        galaxies.append(g)
        gcols.append(g.x)
        grows.append(g.y)
grows = set(grows)
gcols = set(gcols)

def dist(g1,g2,xfactor):
    d = 0
    x0,x1 = min(g1.x,g2.x), max(g1.x,g2.x)
    for x in range(x0+1,x1+1):
        if x in gcols:
            d += 1
        else:
            d += xfactor
    y0,y1 = min(g1.y,g2.y), max(g1.y,g2.y)
    for y in range(y0+1,y1+1):
        if y in grows:
            d += 1
        else:
            d += xfactor
    return d

for i in range(len(galaxies)):
    for j in range(i):
        part1 += dist(galaxies[i],galaxies[j],2)
        part2 += dist(galaxies[i],galaxies[j],1000000)

print('part1:',part1)
print('part2:',part2)
