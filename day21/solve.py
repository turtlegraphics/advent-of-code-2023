#
# Advent of Code 2023
# Bryan Clair
#
# Day 21
#
import sys
sys.path.append("..")
import aocutils

args = aocutils.parse_args()

inputlines = [x.strip() for x in open(args.file).readlines()]

garden = aocutils.Grid()
garden.scan(inputlines)
for g in garden:
    if garden[g] == 'S':
        start = g
garden[start] = '.'

def nowall(u,v):
    if garden[v] == '#':
        return None
    return 1

part1, part2 = 0,0

dist, prev = garden.dijkstra(start,target=None,distance_function = nowall)

for k in dist:
    if dist[k] % 2 == 0 and dist[k] <= 64:
        part1 += 1

triplestr = []
for i in range(3):
    for l in inputlines:
        if 'S' in l:
            spot = l.find('S')
            l2 = l[:spot] + '.' + l[spot+1:]
            if i == 1:
                triplestr.append(l2 + l + l2)
            else:
                triplestr.append(l2 + l2 + l2)
        else:
            triplestr.append(l + l + l)

garden = aocutils.Grid()
garden.scan(triplestr)

for g in garden:
    if garden[g] == 'S':
        start = g
garden[start] = '.'

dist, prev = garden.dijkstra(start,target=None,distance_function = nowall)

dim = len(inputlines)


centercount = 0
edgecount = 0
cornercount = 0

sx,sy = start

fullsteps = 26501365
steps = fullsteps

for loc,d in dist.items():
    x,y = loc
    # parity if True if the path to (x,y) has
    # the right number of steps mod 2
    parity = (sx - x + sy - y) % 2 == steps % 2
    if d <= steps:
        # print(x,y,d)
        bx, by = x//dim, y//dim
        if bx == 1 and by == 1:
            # center case
            centercount += 1
            if parity:
                part2 += 1
        elif bx == 1 or by == 1:
            # edge case
            edgecount += 1
            blocksteps = (steps - d)//dim
            if parity:
                part2 += (blocksteps // 2) + 1
            else:
                part2 += ((blocksteps + 1) // 2)
            pass
        else:
            # corner case
            cornercount += 1
            blocksteps = (steps - d)//dim
            if parity:
                n = blocksteps // 2
                blocks = (n + 1) * (n + 1)
            else:
                n = (blocksteps + 1) // 2
                blocks = n * (n + 1)
                
            part2 += blocks

print('center',centercount,'edge',edgecount,'corner',cornercount)
print('part1:',part1)
print('part2:',part2)
