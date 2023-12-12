#
# Advent of Code 2023
# Bryan Clair
#
# Day 12
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

ibout = {True: 'in block', False:'not in b'}

def ways(springs, counts, inblock, depth):
    # print(' '*depth + springs, '(', ibout[inblock], ')',counts)
    if springs == '':
        if (len(counts) == 0) or (len(counts) == 1 and counts[0] == 0):
            # print('got one')
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

for line in inputlines:
    springs, counts = line.split()
    counts = [int(x) for x in counts.split(',')]
    part1 += ways(springs, counts, inblock=False, depth = 0)

print('part1:',part1)

l = 0
ls = len(inputlines)
for line in inputlines:
    l += 1
    print(round(100*l/ls),'%')
    s, c = line.split()
    springs = s + '?' + s + '?' + s + '?' + s + '?' + s
    counts  = c + ',' + c + ',' + c + ',' + c + ',' + c
    counts = [int(x) for x in counts.split(',')]
    part2 += ways(springs, counts, inblock=False, depth = 0)

print('part2:',part2)
