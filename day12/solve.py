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

history = {}

@aocutils.memoized
def ways(springs, counts, inblock):
    # print(springs, '(', ibout[inblock], ')',counts)
    if springs == '':
        if (len(counts) == 0) or (len(counts) == 1 and counts[0] == 0):
            # print('got one')
            return 1
        else:
            return 0

    if springs[0] == '.':
        if not inblock:
            return ways(springs[1:], counts, False)
        if inblock and counts[0] == 0:
            return ways(springs[1:], counts[1:], False)
        # inblock and counts[0] > 0
        return 0
            
    if springs[0] == '#':
        if len(counts) == 0:
            return 0
        if counts[0] == 0:
            return 0
        w = ways(springs[1:],
                 tuple([counts[0]-1]) + counts[1:],
                 True)
        return w
    
    assert(springs[0] == '?')
    w1 = ways('#' + springs[1:], counts, inblock)
    w2 = ways('.' + springs[1:], counts, inblock)
    return w1+w2

part1, part2 = 0,0

for line in inputlines:
    springs, counts = line.split()
    counts = [int(x) for x in counts.split(',')]
    part1 += ways(springs, tuple(counts), False)

print('part1:',part1)

l = 0
ls = len(inputlines)
for line in inputlines:
    l += 1
    s, c = line.split()
    springs = s + '?' + s + '?' + s + '?' + s + '?' + s
    counts  = c + ',' + c + ',' + c + ',' + c + ',' + c
    counts = [int(x) for x in counts.split(',')]
    part2 += ways(springs, tuple(counts), False)

print('part2:',part2)
