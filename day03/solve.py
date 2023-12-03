#
# Advent of Code 2023
# Bryan Clair
#
# Day 03
#
import sys
sys.path.append("..")
import aocutils

args = aocutils.parse_args()

inputlines = [x.strip() for x in open(args.file).readlines()]

part1, part2 = 0,0

scheme = aocutils.Grid()
scheme.scan(inputlines)
xmin, ymin, xmax, ymax = scheme.bounds()

def issymbol(c):
    return not( c == '.' or c.isdigit() )

def symbolneighbor(p):
    """Is point p next to a symbol"""
    neighbors = scheme.neighbors(p, diagonal=True)
    for q in neighbors:
        if issymbol(scheme[q]):
            return True
    return False

def gearneighbors(p):
    """Return a list of gears next to p"""
    gears = []
    neighbors = scheme.neighbors(p, diagonal=True)
    for q in neighbors:
        if scheme[q] == '*':
            gears.append(q)
    return gears

gears = {}

def handlegears(n,g):
    for p in set(g):
        try:
            gears[p].append(n)
        except:
            gears[p] = [n]
        
for y in range(ymin, ymax+1):
    innumber = False
    part = False
    thenum = ''
    mygears = []
    for x in range(xmin, xmax+1):
        if scheme[x,y].isdigit():
            if innumber:
                thenum += scheme[x,y]
            else:
                thenum = scheme[x,y]
                innumber = True
            if symbolneighbor((x,y)):
                part = True
            mygears += gearneighbors((x,y))
        else:
            if innumber and part:
                part1 += int(thenum)
                handlegears(int(thenum),mygears)
            innumber = False
            part = False
            thenum = ''
            mygears = []
    if innumber and part:
        part1 += int(thenum)
        handlegears(int(thenum),mygears)

print('part1:',part1)

for g in gears:
    if len(gears[g]) == 2:
        part2 += gears[g][0]*gears[g][1]
        
print('part2:',part2)
