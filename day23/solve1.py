#
# Advent of Code 2023
# Bryan Clair
#
# Day 23
#
import sys
sys.path.append("..")
sys.setrecursionlimit(30000)

import aocutils

args = aocutils.parse_args()

inputlines = [x.strip() for x in open(args.file).readlines()]

trails = aocutils.Grid()
trails.scan(inputlines)

def longest(loc,depth=0):
    old = trails[loc]
    trails[loc] = 'o'
    best = 0
    for n in trails.neighbors(loc):
        what = trails[n]
        if what == '#' or what == 'o':
            continue
        if what == 'E':
            # print('\n',trails,'\n',depth,'\n')
            trails[loc] = old
            return 1
        if what == '.':
            val = longest(n,depth+1)
            if val:
                best = max(best, val+1)
            continue
        if what == '>':
            x,y = n
            if x == tuple(loc)[0]-1:
                # can't step onto slope from below
                continue
            trails[n] = 'o'
            val = longest((x+1,y),depth+2)
            if val:
                best = max(best, val+2)
            trails[n] = '>'
            continue
        if what == 'v':
            x,y = n
            if y == tuple(loc)[1]+1:
                # can't step onto slope from below
                continue
            trails[n] = 'o'
            val = longest((x,y-1),depth+2)
            if val:
                best = max(best, val+2)
            trails[n] = 'v'
            continue
    trails[loc] = old
    return best

start = (1,trails.height()-1)
finish = (trails.width()-2,0)

trails[finish] = 'E'

print('part1:',longest(start))
