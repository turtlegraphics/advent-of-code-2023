#
# Advent of Code 2023
# Bryan Clair
#
# Day 16
#
import sys
sys.path.append("..")
import aocutils

args = aocutils.parse_args()

inputlines = [x.strip() for x in open(args.file).readlines()]

# import re
# parser = re.compile(r"name:\s*(\w+)\s*val:\s*(\d+)") # or whatever
# name, val = parser.match(line).groups()
# val = int(val)

part1, part2 = 0,0

cave = aocutils.Grid()
energy = aocutils.Grid()
record = aocutils.Grid()

cave.scan(inputlines)
record.scan(inputlines)

E = aocutils.Point(1,0)
W = aocutils.Point(-1,0)
N = aocutils.Point(0,1)
S = aocutils.Point(0,-1)

def beam(loc,dir):
    while True:
        newloc = loc + dir
        try:
            mirror = cave[newloc]
        except KeyError:
            return
        loc = newloc
        if dir in record[loc]:
            # done this before
            return
        record[loc].add(dir)
        energy[loc] = '#'
        if dir.x != 0 and mirror == '|':
            dir = aocutils.Point(0,1)
            beam(loc,aocutils.Point(0,-1))
        elif dir.y != 0 and mirror == '-':
            dir = aocutils.Point(1,0)
            beam(loc,aocutils.Point(-1,0))
        elif dir == E and mirror == '/':
            dir = N
        elif dir == E and mirror == '\\':
            dir = S
        elif dir == W and mirror == '/':
            dir = S
        elif dir == W and mirror == '\\':
            dir = N
        elif dir == N and mirror == '/':
            dir = E
        elif dir == N and mirror == '\\':
            dir = W
        elif dir == S and mirror == '/':
            dir = W
        elif dir == S and mirror == '\\':
            dir = E

(xmin,ymin,xmax,ymax) = cave.bounds()

def fire(loc,dir):
    energy.scan(inputlines)
    for p in record:
        record[p] = set()
        
    beam(loc, dir)
    v = 0
    
    for p in energy:
        if energy[p] == '#':
            v += 1
    return v
    
start = aocutils.Point(xmin-1,ymax)

print('part1:',fire(start,E))

best = 0
for y in range(ymin,ymax+1):
    v = fire(aocutils.Point(xmin-1,y),E)
    if v > best:
        best = v
print('...')
for y in range(ymin,ymax+1):
    v = fire(aocutils.Point(xmax+1,y),W)
    if v > best:
        best = v
print('...')
for x in range(xmin,xmax+1):
    v = fire(aocutils.Point(x,ymin-1),N)
    if v > best:
        best = v
print('...')
for x in range(xmin,xmax+1):
    v = fire(aocutils.Point(x,ymax+1),S)
    if v > best:
        best = v

print('part2:',best)
