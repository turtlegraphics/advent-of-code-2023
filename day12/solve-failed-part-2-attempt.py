#
# Advent of Code 2023
# Bryan Clair
#
# Day 12
#
import sys
sys.path.append("..")
import aocutils
from aocutils import debug

args = aocutils.parse_args()

inputlines = [x.strip() for x in open(args.file).readlines()]

# import re
# parser = re.compile(r"name:\s*(\w+)\s*val:\s*(\d+)") # or whatever
# name, val = parser.match(line).groups()
# val = int(val)

ibout = {True: 'in block', False:'not in b'}

def ways(springs, counts, inblock, depth):
    debug(' '*depth + springs, '(', ibout[inblock], ')',counts)
    if springs == '':
        if (len(counts) == 0) or (len(counts) == 1 and counts[0] == 0):
            return 1
        else:
            return 0

    if springs[0] == '.':
        if not inblock:
            return ways(springs[1:], counts, inblock = False, depth = depth+1)
        if inblock and counts[0] == 0:
            return ways(springs[1:], counts[1:], inblock = False, depth = depth+1)
        # inblock and counts[0] > 0
        return 0
            
    if springs[0] == '#':
        if len(counts) == 0:
            return 0
        if counts[0] == 0:
            return 0
        counts[0] -= 1
        w = ways(springs[1:], counts, inblock = True, depth = depth+1)
        counts[0] += 1
        return w
    
    assert(springs[0] == '?')
    w1 = ways('#' + springs[1:], counts, inblock, depth)
    w2 = ways('.' + springs[1:], counts, inblock, depth)
    return w1+w2

part1, part2 = 0,0

def findnearmiddle(springs, c):
    middle = len(springs)//2
    f1 = springs.find(c, middle)
    f2 = springs.rfind(c, 0, middle)
    if f1 == -1:
        return f2
    if f2 == -1:
        return f1
    if f1-middle < middle-f2:
        return f1
    return f2
    
def dac(springs, counts):
    debug('dac',springs,counts)
    if len(springs) < 8:
        # just do it the old way
        return ways(springs, counts, inblock=False, depth = 0)
    # find a ? near the middle
    split = findnearmiddle(springs,'?')
    if split == -1:
        # no ? left, do it the old way
        return ways(springs, counts, inblock=False, depth = 0)
    front = springs[:split]
    back = springs[split+1:]
    # assert(front + '?' + back == springs)

    debug('split at',split, front+'!'+back)
    
    # hard way
    space = 0
    for i in range(len(counts)+1):
        w2 = 0
        w1 = dac(front, counts[:i])
        if w1 > 0:
            w2 = dac(back, counts[i:])
            
        debug('  +',w1*w2,'=',w1,'*',w2)
        space += w1*w2
    
    # easy way
    sharp = dac(front + '#' + back, counts)
    return sharp + space

# print('dac result',dac('??????',[1,3,1]))

l = 0
ls = len(inputlines)
for line in inputlines:
    l += 1
    print(round(100*l/ls),'%')
    s, c = line.split()
    springs = s + '?' + s + '?' + s + '?' + s + '?' + s
    counts  = c + ',' + c + ',' + c + ',' + c + ',' + c
    counts = [int(x) for x in counts.split(',')]
    part2 += dac(springs,counts)

print('part2:',part2)
