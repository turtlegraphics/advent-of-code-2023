#
# Advent of Code 2023
# Bryan Clair
#
# Day 13
#
import sys
sys.path.append("..")
import aocutils

args = aocutils.parse_args()

def is_mirror(g,i):
    # check for a mirror before row i
    step = 0
    while (i-1-step >=0) and (i+step < len(g)):
        if g[i-1-step] != g[i+step]:
            return False
        step += 1
    return True
    
def find_mirror(g,ignore=0):
    for i in range(1,len(g)):
        if i != ignore and is_mirror(g,i):
            return i
    return 0

def transpose(g):
    gt = []
    for i in range(len(g[0])):
        s = ''.join([c[i] for c in g])
        gt.append(s)
    return(gt)

part1, part2 = 0,0

gridstrs = open(args.file).read().split('\n\n')
hignore = []
vignore = []

for gridstr in gridstrs:
    g = gridstr.split()
    h = find_mirror(g)
    v = find_mirror(transpose(g))
    hignore.append(h)
    vignore.append(v)
    part1 += 100*h + v

def swap(c):
    if c == '.':
        return '#'
    return '.'

for i in range(len(gridstrs)):
    g = gridstrs[i].split()
    for y in range(len(g)):
        oldrow = g[y]
        for x in range(len(oldrow)):
            newrow = oldrow[:x] + swap(oldrow[x]) + oldrow[x+1:]
            g[y] = newrow
            val = 100*find_mirror(g,hignore[i]) + find_mirror(transpose(g),vignore[i])
            if val > 0:
                break
        if val > 0:
            break
        g[y] = oldrow
        
    part2 += val

print('part1:',part1)
print('part2:',part2)
