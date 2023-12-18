#
# Advent of Code 2023
# Bryan Clair
#
# Day 18
#
import sys
sys.path.append("..")
import aocutils

args = aocutils.parse_args()

inputlines = [x.strip() for x in open(args.file).readlines()]

part1, part2 = 0,0

pool = aocutils.Grid()
pos = aocutils.Point(0,0)
pool[pos] = '#'

dirs = {
    'R': aocutils.Point(1,0),
    'L': aocutils.Point(-1,0),
    'U': aocutils.Point(0,1),
    'D': aocutils.Point(0,-1)
    }

for line in inputlines:
    heading, distance, color = line.split()
    distance = int(distance)
    for d in range(distance):
        pos += dirs[heading]
        pool[pos] = '#'

xmin, ymin, xmax, ymax = pool.bounds()
for y in range(ymin,ymax+1):
    for x in range(xmin,xmax+1):
        try:
            if pool[(x,y)] != '#':
                pool[(x,y)] = '-'
        except KeyError:
            pool[(x,y)] = '-'

inside = aocutils.Point(1,-1)  # look at input for this
assert(pool[inside] == '-')

def wallfinder(u,v):
    assert(pool[u] == '-')
    if pool[v] == '-':
        return 1
    else:
        assert(pool[v] == '#')
        return None
    
dist, prev = pool.dijkstra(inside, distance_function = wallfinder)

for p in dist:
    pool[p] = '#'
print(pool)

for p in pool:
    if pool[p] == '#':
        part1 += 1
        
print('part1:',part1)
print('part2:',part2)
